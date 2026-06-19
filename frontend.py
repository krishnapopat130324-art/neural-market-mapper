import os
import json

os.makedirs('frontend/app/analysis/[id]', exist_ok=True)
os.makedirs('frontend/components', exist_ok=True)

# ============ package.json ============
with open('frontend/package.json', 'w') as f:
    json.dump({
        "name": "neural-market-mapper",
        "version": "1.0.0",
        "private": True,
        "scripts": {
            "dev": "next dev",
            "build": "next build",
            "start": "next start"
        },
        "dependencies": {
            "next": "14.0.4",
            "react": "18.2.0",
            "react-dom": "18.2.0",
            "framer-motion": "^10.16.4",
            "react-icons": "^4.11.0"
        },
        "devDependencies": {
            "@types/node": "20.10.4",
            "@types/react": "18.2.45",
            "autoprefixer": "10.4.16",
            "postcss": "8.4.32",
            "tailwindcss": "3.3.6",
            "typescript": "5.3.3"
        }
    }, f, indent=2)

# ============ tailwind.config.js ============
with open('frontend/tailwind.config.js', 'w') as f:
    f.write("""module.exports = {
  content: ['./app/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#6366F1',
        secondary: '#8B5CF6',
        accent: '#EC4899',
        dark: '#0F172A',
        light: '#F8FAFC'
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      }
    },
  },
  plugins: [],
}""")

# ============ globals.css ============
with open('frontend/app/globals.css', 'w') as f:
    f.write("""@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: #0F172A;
  color: #F8FAFC;
}

.glass {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.glass-card {
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.06);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(99, 102, 241, 0.3);
  transform: translateY(-4px);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
}

.gradient-text {
  background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 50%, #EC4899 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.gradient-bg {
  background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 50%, #EC4899 100%);
}

.gradient-border {
  position: relative;
  background: linear-gradient(135deg, #6366F1, #8B5CF6, #EC4899);
  padding: 2px;
  border-radius: 16px;
}

.gradient-border > * {
  background: #0F172A;
  border-radius: 14px;
}

.input-dark {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #F8FAFC;
  transition: all 0.3s ease;
}

.input-dark:focus {
  background: rgba(255, 255, 255, 0.08);
  border-color: #6366F1;
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15);
  outline: none;
}

.input-dark::placeholder {
  color: rgba(255, 255, 255, 0.3);
}

.btn-gradient {
  background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%);
  transition: all 0.3s ease;
}

.btn-gradient:hover {
  transform: scale(1.02);
  box-shadow: 0 10px 40px rgba(99, 102, 241, 0.4);
}

.btn-gradient:active {
  transform: scale(0.98);
}

.glow {
  animation: glow 3s ease-in-out infinite;
}

@keyframes glow {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

.floating {
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

.pulse-ring {
  animation: pulseRing 2s ease-out infinite;
}

@keyframes pulseRing {
  0% { transform: scale(0.95); opacity: 1; }
  100% { transform: scale(1.5); opacity: 0; }
}

.shimmer {
  background: linear-gradient(
    90deg,
    rgba(255,255,255,0.02) 0%,
    rgba(255,255,255,0.08) 50%,
    rgba(255,255,255,0.02) 100%
  );
  background-size: 200% 100%;
  animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #6366F1, #8B5CF6);
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #8B5CF6, #EC4899);
}""")

# ============ layout.tsx ============
with open('frontend/app/layout.tsx', 'w') as f:
    f.write("""import './globals.css'

export const metadata = {
  title: 'Neural Market Mapper - AI Competitive Intelligence',
  description: 'AI-powered market research and competitive analysis platform',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}""")

# ============ page.tsx (Homepage - Professional Dark Theme) ============
with open('frontend/app/page.tsx', 'w') as f:
    f.write("""'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { motion, AnimatePresence } from 'framer-motion'
import { 
  FiSearch, FiArrowRight, FiTrendingUp, FiBarChart2, 
  FiShield, FiZap, FiCpu, FiGlobe, FiUsers, FiTarget,
  FiStar, FiChevronRight, FiActivity, FiDatabase
} from 'react-icons/fi'

export default function Home() {
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const [isFocused, setIsFocused] = useState(false)
  const router = useRouter()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!url) return
    setLoading(true)
    try {
      const res = await fetch('http://localhost:8000/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      })
      const data = await res.json()
      if (data.task_id) {
        router.push(`/analysis/${data.task_id}`)
      }
    } catch (error) {
      alert('Error analyzing company')
    } finally {
      setLoading(false)
    }
  }

  const features = [
    { icon: FiCpu, title: 'AI-Powered Analysis', desc: 'Advanced machine learning for deep insights' },
    { icon: FiGlobe, title: 'Market Intelligence', desc: 'Real-time competitive landscape mapping' },
    { icon: FiBarChart2, title: 'SWOT Analytics', desc: 'Comprehensive strengths & weaknesses analysis' },
    { icon: FiTarget, title: 'Opportunity Detection', desc: 'Identify market gaps and growth areas' },
  ]

  return (
    <div className="min-h-screen bg-dark relative overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -top-40 -right-40 w-96 h-96 bg-gradient-conic from-primary via-secondary to-accent rounded-full blur-3xl opacity-20 glow"></div>
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-gradient-conic from-accent via-secondary to-primary rounded-full blur-3xl opacity-20 glow" style={{ animationDelay: '1.5s' }}></div>
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-gradient-radial from-primary/5 to-transparent rounded-full blur-3xl"></div>
      </div>

      {/* Navbar */}
      <nav className="relative z-10 glass border-b border-white/5">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-20">
            <motion.div 
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              className="flex items-center gap-3"
            >
              <div className="w-12 h-12 gradient-bg rounded-2xl flex items-center justify-center shadow-lg shadow-primary/25">
                <span className="text-white font-black text-xl">NM</span>
              </div>
              <div>
                <span className="font-bold text-xl text-white">Neural<span className="gradient-text">Mapper</span></span>
                <span className="ml-2 text-xs px-2 py-0.5 bg-primary/20 text-primary rounded-full">AI</span>
              </div>
            </motion.div>
            <motion.div 
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              className="flex items-center gap-6"
            >
              <button className="text-gray-400 hover:text-white transition text-sm font-medium">Features</button>
              <button className="text-gray-400 hover:text-white transition text-sm font-medium">Pricing</button>
              <button className="text-gray-400 hover:text-white transition text-sm font-medium">Docs</button>
              <button className="px-5 py-2.5 gradient-bg text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-primary/30 transition-all">
                Get Started
              </button>
            </motion.div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 lg:py-32">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-8">
              <span className="w-2 h-2 bg-primary rounded-full animate-pulse"></span>
              <span className="text-sm font-medium text-primary">AI-Powered Intelligence</span>
              <FiChevronRight className="text-primary text-sm" />
            </div>
            
            <h1 className="text-6xl lg:text-7xl font-black leading-[1.1] mb-6">
              Unlock
              <br />
              <span className="gradient-text">Market Insights</span>
              <br />
              in Seconds
            </h1>
            
            <p className="text-xl text-gray-400 mb-10 leading-relaxed max-w-lg">
              Enter any company URL and get instant AI-powered competitive analysis,
              SWOT insights, and market intelligence reports.
            </p>

            {/* Search Form */}
            <form onSubmit={handleSubmit} className="relative">
              <div className={`relative group transition-all duration-300 ${isFocused ? 'scale-[1.02]' : ''}`}>
                <div className="absolute inset-0 gradient-bg rounded-2xl blur-xl opacity-20 group-hover:opacity-40 transition-opacity"></div>
                <div className="relative glass border border-white/10 rounded-2xl overflow-hidden">
                  <FiSearch className="absolute left-5 top-1/2 -translate-y-1/2 text-gray-400 text-xl" />
                  <input
                    type="url"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    onFocus={() => setIsFocused(true)}
                    onBlur={() => setIsFocused(false)}
                    placeholder="Enter company URL (e.g., https://google.com)"
                    className="w-full bg-transparent pl-14 pr-36 py-4 text-white placeholder-gray-500 outline-none"
                    required
                  />
                  <button
                    type="submit"
                    disabled={loading}
                    className="absolute right-2 top-1/2 -translate-y-1/2 btn-gradient px-6 py-2.5 rounded-xl text-white font-semibold flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {loading ? (
                      <>
                        <span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></span>
                        Analyzing
                      </>
                    ) : (
                      <>
                        Analyze
                        <FiArrowRight />
                      </>
                    )}
                  </button>
                </div>
              </div>
            </form>

            {/* Stats */}
            <div className="flex items-center gap-8 mt-8">
              <div className="flex items-center gap-2">
                <FiActivity className="text-primary" />
                <span className="text-sm text-gray-400">Real-time analysis</span>
              </div>
              <div className="w-px h-6 bg-white/10"></div>
              <div className="flex items-center gap-2">
                <FiDatabase className="text-secondary" />
                <span className="text-sm text-gray-400">Enterprise grade</span>
              </div>
              <div className="w-px h-6 bg-white/10"></div>
              <div className="flex items-center gap-2">
                <FiStar className="text-accent" />
                <span className="text-sm text-gray-400">100% free</span>
              </div>
            </div>
          </motion.div>

          {/* Right Side - 3D Card */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="relative"
          >
            <div className="absolute inset-0 gradient-bg rounded-3xl blur-2xl opacity-20 floating"></div>
            <div className="relative glass-card rounded-3xl p-8">
              <div className="flex items-center justify-between mb-6">
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 gradient-bg rounded-xl flex items-center justify-center">
                    <span className="text-white text-xl">📊</span>
                  </div>
                  <div>
                    <p className="font-semibold text-white">SWOT Analysis</p>
                    <p className="text-sm text-gray-400">Google Inc.</p>
                  </div>
                </div>
                <span className="px-3 py-1 bg-green-500/20 text-green-400 text-xs font-semibold rounded-full">
                  Live
                </span>
              </div>

              <div className="space-y-4">
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span className="text-gray-400">Analysis Progress</span>
                    <span className="text-white font-semibold">85%</span>
                  </div>
                  <div className="w-full h-2 bg-white/5 rounded-full overflow-hidden">
                    <motion.div 
                      initial={{ width: 0 }}
                      animate={{ width: '85%' }}
                      transition={{ duration: 1.5 }}
                      className="h-full gradient-bg rounded-full"
                    ></motion.div>
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-3">
                  {[
                    { label: 'Strengths', value: '12', color: 'green' },
                    { label: 'Weaknesses', value: '5', color: 'red' },
                    { label: 'Opportunities', value: '8', color: 'blue' },
                    { label: 'Threats', value: '4', color: 'orange' },
                  ].map((item) => (
                    <div key={item.label} className={`p-3 rounded-xl bg-${item.color}-500/10 border border-${item.color}-500/20`}>
                      <p className={`text-${item.color}-400 text-xs font-medium`}>{item.label}</p>
                      <p className={`text-${item.color}-400 text-xl font-bold`}>{item.value}</p>
                    </div>
                  ))}
                </div>

                <div className="pt-4 border-t border-white/5">
                  <div className="flex items-center justify-between text-sm">
                    <span className="text-gray-400">Market Position</span>
                    <span className="text-white font-semibold">#1 in Search</span>
                  </div>
                  <div className="flex items-center justify-between text-sm mt-2">
                    <span className="text-gray-400">Sentiment</span>
                    <span className="text-green-400 font-semibold">Positive</span>
                  </div>
                </div>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Features Grid */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-24"
        >
          {features.map((feature, index) => (
            <motion.div
              key={index}
              whileHover={{ y: -8 }}
              className="glass-card rounded-2xl p-6 cursor-pointer"
            >
              <div className="w-12 h-12 gradient-bg rounded-xl flex items-center justify-center mb-4 shadow-lg shadow-primary/20">
                <feature.icon className="text-white text-xl" />
              </div>
              <h3 className="text-white font-semibold text-lg mb-1">{feature.title}</h3>
              <p className="text-gray-400 text-sm">{feature.desc}</p>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </div>
  )
}
""")

# ============ analysis/[id]/page.tsx (Results - Professional Dark) ============
with open('frontend/app/analysis/[id]/page.tsx', 'w') as f:
    f.write("""'use client'

import { useEffect, useState } from 'react'
import { useParams } from 'next/navigation'
import Link from 'next/link'
import { motion } from 'framer-motion'
import {
  FiArrowLeft, FiDownload, FiRefreshCw, FiShare2,
  FiTrendingUp, FiAlertCircle, FiCheckCircle, FiXCircle,
  FiZap, FiBarChart2, FiUsers, FiTarget, FiShield,
  FiStar, FiActivity, FiGlobe, FiCpu
} from 'react-icons/fi'

interface AnalysisResult {
  result?: {
    analysis?: {
      company?: string
      summary?: string
      swot?: {
        strengths?: string[]
        weaknesses?: string[]
        opportunities?: string[]
        threats?: string[]
      }
      competitors?: string[]
      sentiment?: string
      market_gaps?: string[]
    }
  }
}

export default function AnalysisPage() {
  const { id } = useParams()
  const [result, setResult] = useState<AnalysisResult | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)

  useEffect(() => {
    const fetchResult = async () => {
      try {
        const res = await fetch(`http://localhost:8000/api/status/${id}`)
        const data = await res.json()
        if (data.status === 'completed') {
          setResult(data)
          setLoading(false)
        } else {
          setTimeout(fetchResult, 2000)
        }
      } catch (error) {
        setError(true)
        setLoading(false)
      }
    }
    fetchResult()
  }, [id])

  if (loading) {
    return (
      <div className="min-h-screen bg-dark flex items-center justify-center">
        <div className="text-center">
          <div className="relative w-24 h-24 mx-auto mb-6">
            <div className="absolute inset-0 rounded-full border-2 border-primary/20"></div>
            <div className="absolute inset-0 rounded-full border-2 border-primary border-t-transparent animate-spin"></div>
            <div className="absolute inset-2 rounded-full border-2 border-secondary/20"></div>
            <div className="absolute inset-2 rounded-full border-2 border-secondary border-b-transparent animate-spin" style={{ animationDirection: 'reverse', animationDuration: '1.5s' }}></div>
          </div>
          <h2 className="text-2xl font-bold text-white">Analyzing Company</h2>
          <p className="text-gray-400 mt-2">Gathering market intelligence...</p>
        </div>
      </div>
    )
  }

  if (error || !result?.result?.analysis) {
    return (
      <div className="min-h-screen bg-dark flex items-center justify-center p-4">
        <div className="text-center max-w-md">
          <div className="text-6xl mb-6">🔍</div>
          <h2 className="text-2xl font-bold text-white mb-2">Analysis Not Found</h2>
          <p className="text-gray-400 mb-6">The analysis you're looking for doesn't exist.</p>
          <Link href="/" className="inline-flex items-center gap-2 px-6 py-3 gradient-bg text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-primary/30 transition">
            <FiArrowLeft /> Start New Analysis
          </Link>
        </div>
      </div>
    )
  }

  const a = result.result.analysis
  const sentimentColors = {
    Positive: 'text-green-400 bg-green-500/20 border-green-500/30',
    Negative: 'text-red-400 bg-red-500/20 border-red-500/30',
    Neutral: 'text-yellow-400 bg-yellow-500/20 border-yellow-500/30'
  }

  return (
    <div className="min-h-screen bg-dark relative overflow-hidden">
      {/* Background Effects */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -top-40 -right-40 w-96 h-96 bg-gradient-conic from-primary via-secondary to-accent rounded-full blur-3xl opacity-10 glow"></div>
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-gradient-conic from-accent via-secondary to-primary rounded-full blur-3xl opacity-10 glow" style={{ animationDelay: '1.5s' }}></div>
      </div>

      {/* Navbar */}
      <nav className="relative z-10 glass border-b border-white/5">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-20">
            <Link href="/" className="flex items-center gap-3">
              <div className="w-12 h-12 gradient-bg rounded-2xl flex items-center justify-center shadow-lg shadow-primary/25">
                <span className="text-white font-black text-xl">NM</span>
              </div>
              <span className="font-bold text-xl text-white">Neural<span className="gradient-text">Mapper</span></span>
            </Link>
            <div className="flex items-center gap-3">
              <button className="p-2.5 hover:bg-white/5 rounded-xl transition text-gray-400 hover:text-white">
                <FiShare2 className="text-xl" />
              </button>
              <button onClick={() => window.location.reload()} className="p-2.5 hover:bg-white/5 rounded-xl transition text-gray-400 hover:text-white">
                <FiRefreshCw className="text-xl" />
              </button>
              <Link href="/" className="px-5 py-2.5 gradient-bg text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-primary/30 transition">
                New Analysis
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header Card */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="glass-card rounded-3xl p-8 mb-8"
        >
          <div className="flex flex-wrap items-start justify-between gap-4">
            <div>
              <div className="flex items-center gap-3 mb-2 flex-wrap">
                <h1 className="text-4xl font-black text-white">{a.company || 'Company Analysis'}</h1>
                <span className={`px-4 py-1 rounded-full text-sm font-semibold border ${sentimentColors[a.sentiment || 'Neutral']}`}>
                  {a.sentiment || 'Neutral'} Sentiment
                </span>
              </div>
              <p className="text-lg text-gray-400 max-w-2xl">{a.summary}</p>
            </div>
            <button
              onClick={async () => {
                const res = await fetch(`http://localhost:8000/api/report/${id}`)
                const data = await res.json()
                alert(data.report)
              }}
              className="btn-gradient px-6 py-3 rounded-xl text-white font-semibold flex items-center gap-2 hover:shadow-lg hover:shadow-primary/30 transition"
            >
              <FiDownload /> Download Report
            </button>
          </div>
        </motion.div>

        {/* SWOT Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          {[
            { title: 'Strengths', icon: FiCheckCircle, color: 'green', data: a.swot?.strengths },
            { title: 'Weaknesses', icon: FiXCircle, color: 'red', data: a.swot?.weaknesses },
            { title: 'Opportunities', icon: FiTrendingUp, color: 'blue', data: a.swot?.opportunities },
            { title: 'Threats', icon: FiAlertCircle, color: 'orange', data: a.swot?.threats },
          ].map((item, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              className={`glass-card rounded-2xl p-6 border-l-4 border-${item.color}-500`}
            >
              <div className="flex items-center gap-3 mb-4">
                <div className={`w-10 h-10 bg-${item.color}-500/20 rounded-xl flex items-center justify-center`}>
                  <item.icon className={`text-${item.color}-400 text-xl`} />
                </div>
                <h3 className={`text-lg font-bold text-${item.color}-400`}>{item.title}</h3>
                <span className={`ml-auto text-sm text-${item.color}-400/60`}>{item.data?.length || 0}</span>
              </div>
              <ul className="space-y-2">
                {item.data?.map((s: string, i: number) => (
                  <li key={i} className="flex items-start gap-2 text-gray-300">
                    <span className={`text-${item.color}-400 mt-1`}>▸</span>
                    <span className="text-sm">{s}</span>
                  </li>
                ))}
              </ul>
            </motion.div>
          ))}
        </div>

        {/* Competitors & Market Gaps */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="glass-card rounded-2xl p-6"
          >
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-purple-500/20 rounded-xl flex items-center justify-center">
                <FiUsers className="text-purple-400 text-xl" />
              </div>
              <h3 className="text-lg font-bold text-white">Competitors</h3>
            </div>
            <div className="flex flex-wrap gap-2">
              {a.competitors?.map((c: string, i: number) => (
                <span key={i} className="px-4 py-2 bg-white/5 rounded-xl text-sm font-medium text-gray-300 border border-white/5 hover:border-primary/30 transition">
                  {c}
                </span>
              ))}
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className="glass-card rounded-2xl p-6"
          >
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-green-500/20 rounded-xl flex items-center justify-center">
                <FiTarget className="text-green-400 text-xl" />
              </div>
              <h3 className="text-lg font-bold text-white">Market Gaps</h3>
            </div>
            <ul className="space-y-2">
              {a.market_gaps?.map((g: string, i: number) => (
                <li key={i} className="flex items-start gap-2 text-gray-300">
                  <span className="text-green-400 mt-1">💡</span>
                  <span className="text-sm">{g}</span>
                </li>
              ))}
            </ul>
          </motion.div>
        </div>

        {/* Footer Actions */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.6 }}
          className="mt-8 flex flex-wrap gap-4 justify-between items-center p-6 glass-card rounded-2xl"
        >
          <div className="flex items-center gap-4 text-sm text-gray-400">
            <span className="flex items-center gap-1">
              <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
              Live Analysis
            </span>
            <span className="w-px h-4 bg-white/10"></span>
            <span>{new Date().toLocaleDateString()}</span>
            <span className="w-px h-4 bg-white/10"></span>
            <span className="flex items-center gap-1">
              <FiZap className="text-primary" />
              AI Generated
            </span>
          </div>
          <div className="flex gap-3">
            <button
              onClick={async () => {
                const res = await fetch(`http://localhost:8000/api/report/${id}`)
                const data = await res.json()
                alert(data.report)
              }}
              className="px-6 py-3 gradient-bg text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-primary/30 transition flex items-center gap-2"
            >
              <FiDownload /> Export Report
            </button>
          </div>
        </motion.div>
      </div>
    </div>
  )
}
""")

print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ✨ NEURAL MARKET MAPPER - PROFESSIONAL DESIGN COMPLETE     ║
║                                                               ║
║   🎨 Design Features:                                        ║
║   • Dark theme with glass-morphism                          ║
║   • Gradient animations & glow effects                      ║
║   • Professional typography & spacing                       ║
║   • Smooth transitions & hover effects                      ║
║   • Modern card design with blur backgrounds                ║
║   • Animated gradient backgrounds                           ║
║   • Interactive UI with loading states                      ║
║                                                               ║
║   🚀 Run: cd frontend && npm install && npm run dev        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
""")