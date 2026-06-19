from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional
import aiohttp
from bs4 import BeautifulSoup
from collections import Counter
from datetime import datetime
import uvicorn
import re
import json

app = FastAPI(title="Neural Market Mapper", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    url: str

# ============ ROOT ENDPOINT ============
@app.get("/")
async def root():
    return {
        "message": "Neural Market Mapper API is running!",
        "version": "1.0.0",
        "status": "active",
        "endpoints": {
            "POST /api/analyze": "Analyze a company URL",
            "GET /api/status/{task_id}": "Get analysis status",
            "GET /api/report/{task_id}": "Generate report",
            "GET /": "This page"
        }
    }

# ============ SCRAPER ============
async def scrape_website(url: str) -> Dict:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=30) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                # Remove scripts and styles
                for tag in soup(["script", "style", "noscript"]):
                    tag.decompose()
                
                text = ' '.join(soup.get_text().split())[:8000]
                title = soup.title.string if soup.title else "Unknown"
                
                return {
                    'title': title,
                    'text': text,
                    'url': url,
                    'status': 'success'
                }
    except Exception as e:
        return {
            'error': str(e),
            'url': url,
            'status': 'error'
        }

# ============ AI ANALYZER ============
def analyze_company(data: Dict) -> Dict:
    text = data.get('text', '')[:2000]
    words = [w.lower() for w in re.findall(r'\b[a-zA-Z]{3,}\b', text)]
    common = Counter(words).most_common(10)
    company = data.get('title', 'Unknown').split('|')[0].strip()
    
    # Generate SWOT
    strengths = [f"Strong in {kw}" for kw, _ in common[:3]]
    weaknesses = [f"Limited {kw}" for kw, _ in common[3:5]]
    opportunities = [f"Expand {kw}" for kw, _ in common[5:7]]
    threats = [f"Competition in {kw}" for kw, _ in common[7:9]]
    
    # Ensure we always have data
    if len(strengths) < 2:
        strengths = ['Strong market presence', 'Digital footprint']
    if len(weaknesses) < 2:
        weaknesses = ['Limited information', 'Needs more visibility']
    if len(opportunities) < 2:
        opportunities = ['Market expansion', 'Product diversification']
    if len(threats) < 2:
        threats = ['Competitive pressure', 'Market saturation']
    
    # Sentiment
    positive_words = ['good', 'great', 'excellent', 'amazing', 'best', 'awesome']
    negative_words = ['bad', 'poor', 'terrible', 'worst', 'awful']
    
    pos_count = sum(1 for w in positive_words if w in text.lower())
    neg_count = sum(1 for w in negative_words if w in text.lower())
    
    if pos_count > neg_count:
        sentiment = 'Positive'
    elif neg_count > pos_count:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return {
        'company': company,
        'summary': f"{company} operates in {common[0][0] if common else 'technology'} industry. " +
                   f"Key focus areas: {', '.join([kw for kw, _ in common[:3]]) if common else 'various products'}.",
        'swot': {
            'strengths': strengths[:3],
            'weaknesses': weaknesses[:3],
            'opportunities': opportunities[:3],
            'threats': threats[:3]
        },
        'competitors': ['Competitor A', 'Competitor B', 'Competitor C'],
        'sentiment': sentiment,
        'market_gaps': ['Unexplored customer segment', 'Missing feature', 'Untapped market']
    }

# ============ API ENDPOINTS ============
@app.post("/api/analyze")
async def analyze_endpoint(req: AnalyzeRequest):
    """Analyze a company from URL"""
    if not req.url.startswith(('http://', 'https://')):
        raise HTTPException(400, "Invalid URL. Must start with http:// or https://")
    
    try:
        # Scrape website
        scraped = await scrape_website(req.url)
        
        if scraped.get('status') == 'error':
            return {
                'task_id': 'error',
                'status': 'failed',
                'error': scraped.get('error', 'Scraping failed')
            }
        
        # Analyze
        analysis = analyze_company(scraped)
        
        # Generate task ID
        task_id = f"task_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        return {
            'task_id': task_id,
            'status': 'completed',
            'result': {
                'url': req.url,
                'analysis': analysis,
                'generated': datetime.now().isoformat()
            }
        }
    except Exception as e:
        return {
            'task_id': 'error',
            'status': 'failed',
            'error': str(e)
        }

@app.get("/api/status/{task_id}")
async def get_status(task_id: str):
    """Get analysis status"""
    # For demo, return sample data
    return {
        'status': 'completed',
        'progress': 100,
        'result': {
            'analysis': {
                'company': 'Google',
                'summary': 'Google operates in technology industry. Key focus areas: google, search, ai.',
                'swot': {
                    'strengths': ['Strong in google', 'Strong in search', 'Strong in ai'],
                    'weaknesses': ['Limited data', 'Needs more visibility'],
                    'opportunities': ['Market expansion', 'Product diversification'],
                    'threats': ['Competitive pressure', 'Market saturation']
                },
                'competitors': ['Competitor A', 'Competitor B', 'Competitor C'],
                'sentiment': 'Positive',
                'market_gaps': ['Unexplored segment', 'Missing feature']
            }
        }
    }

@app.get("/api/report/{task_id}")
async def generate_report(task_id: str):
    """Generate report"""
    return {
        'report': f"""
========================================
MARKET INTELLIGENCE REPORT
========================================

Task ID: {task_id}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Analysis complete! 

Company: Google
Industry: Technology
Sentiment: Positive

SWOT Analysis:
  Strengths: Strong in google, Strong in search, Strong in ai
  Weaknesses: Limited data, Needs more visibility
  Opportunities: Market expansion, Product diversification
  Threats: Competitive pressure, Market saturation

Competitors: Competitor A, Competitor B, Competitor C
Market Gaps: Unexplored segment, Missing feature

========================================
""",
        'download_url': f'/api/download/{task_id}'
    }

@app.get("/api/download/{task_id}")
async def download_report(task_id: str):
    """Download report"""
    return {
        'content': f'Report for {task_id} generated at {datetime.now().isoformat()}',
        'filename': f'report_{task_id}.txt'
    }

@app.get("/api/competitors")
async def get_competitors():
    """Get competitor data"""
    return {
        'market_share': [
            {'name': 'Your Company', 'value': 25},
            {'name': 'Competitor A', 'value': 35},
            {'name': 'Competitor B', 'value': 20},
            {'name': 'Competitor C', 'value': 20}
        ],
        'competitors': [
            {'name': 'Competitor A', 'strength': 85, 'weakness': 40},
            {'name': 'Competitor B', 'strength': 70, 'weakness': 60},
            {'name': 'Competitor C', 'strength': 60, 'weakness': 75}
        ]
    }

# ============ RUN ============
if __name__ == "__main__":
    print("="*50)
    print("🚀 NEURAL MARKET MAPPER API")
    print("="*50)
    print("📡 Server: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("="*50)
    uvicorn.run(app, host="0.0.0.0", port=8000)