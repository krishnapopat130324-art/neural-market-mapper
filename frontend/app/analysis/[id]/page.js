'use client'

import { useEffect, useState } from 'react'
import { useParams } from 'next/navigation'
import Link from 'next/link'

export default function AnalysisPage() {
  const { id } = useParams()
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)
  const [retryCount, setRetryCount] = useState(0)

  useEffect(() => {
    const fetchResult = async () => {
      try {
        const res = await fetch(`http://localhost:8000/api/status/${id}`)
        const data = await res.json()
        
        if (data.status === 'completed') {
          setResult(data)
          setLoading(false)
        } else if (data.status === 'processing') {
          setTimeout(() => {
            setRetryCount(prev => prev + 1)
          }, 2000)
        } else {
          setError(true)
          setLoading(false)
        }
      } catch (error) {
        if (retryCount < 5) {
          setTimeout(() => {
            setRetryCount(prev => prev + 1)
          }, 2000)
        } else {
          setError(true)
          setLoading(false)
        }
      }
    }
    
    fetchResult()
  }, [id, retryCount])

  if (loading) {
    return (
      <div style={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #FAF6F0 0%, #F5EDE3 30%, #EDE4D6 60%, #E8DDCF 100%)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
      }}>
        <div style={{ textAlign: 'center' }}>
          <div style={{
            width: '80px',
            height: '80px',
            margin: '0 auto 24px',
            borderRadius: '50%',
            border: '3px solid rgba(139, 111, 76, 0.1)',
            borderTop: '3px solid #8B6F4C',
            animation: 'spin 1s linear infinite'
          }}></div>
          <style>{`
            @keyframes spin {
              0% { transform: rotate(0deg); }
              100% { transform: rotate(360deg); }
            }
          `}</style>
          <h2 style={{ color: '#3D2B1F', fontSize: '24px', fontWeight: 700 }}>Analyzing Company</h2>
          <p style={{ color: '#8B7355', marginTop: '8px' }}>Gathering market intelligence...</p>
          <p style={{ color: '#8B7355', fontSize: '13px', marginTop: '4px' }}>Attempt {retryCount + 1}</p>
        </div>
      </div>
    )
  }

  if (error || !result?.result?.analysis) {
    return (
      <div style={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #FAF6F0 0%, #F5EDE3 30%, #EDE4D6 60%, #E8DDCF 100%)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '24px'
      }}>
        <div style={{ textAlign: 'center', maxWidth: '400px' }}>
          <div style={{ fontSize: '64px', marginBottom: '16px' }}>🔍</div>
          <h2 style={{ color: '#3D2B1F', fontSize: '24px', fontWeight: 700, marginBottom: '8px' }}>Analysis Not Found</h2>
          <p style={{ color: '#8B7355', marginBottom: '24px' }}>The analysis you're looking for doesn't exist.</p>
          <Link href="/" style={{
            display: 'inline-block',
            padding: '12px 32px',
            borderRadius: '10px',
            background: 'linear-gradient(135deg, #8B6F4C, #A8876A)',
            color: 'white',
            fontWeight: 600,
            textDecoration: 'none',
            transition: 'all 0.3s ease'
          }} onMouseEnter={e => { e.target.style.boxShadow = '0 8px 30px rgba(139, 111, 76, 0.3)'; e.target.style.transform = 'scale(1.02)' }} onMouseLeave={e => { e.target.style.boxShadow = 'none'; e.target.style.transform = 'scale(1)' }}>
            ← Start New Analysis
          </Link>
        </div>
      </div>
    )
  }

  const a = result.result.analysis

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #FAF6F0 0%, #F5EDE3 30%, #EDE4D6 60%, #E8DDCF 100%)',
      fontFamily: "'Inter', -apple-system, sans-serif",
      padding: '24px',
      position: 'relative',
      overflow: 'hidden'
    }}>
      {/* Decorative Background */}
      <div style={{
        position: 'absolute',
        top: '-20%',
        right: '-10%',
        width: '500px',
        height: '500px',
        background: 'radial-gradient(circle, rgba(193, 162, 138, 0.06) 0%, transparent 70%)',
        borderRadius: '50%'
      }}></div>
      <div style={{
        position: 'absolute',
        bottom: '-20%',
        left: '-10%',
        width: '500px',
        height: '500px',
        background: 'radial-gradient(circle, rgba(160, 130, 110, 0.04) 0%, transparent 70%)',
        borderRadius: '50%'
      }}></div>

      {/* Navbar */}
      <nav style={{
        position: 'relative',
        zIndex: 10,
        maxWidth: '1200px',
        margin: '0 auto',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '16px 24px',
        borderRadius: '14px',
        background: 'rgba(255, 252, 248, 0.7)',
        backdropFilter: 'blur(20px)',
        border: '1px solid rgba(139, 111, 76, 0.06)',
        marginBottom: '32px'
      }}>
        <Link href="/" style={{ display: 'flex', alignItems: 'center', gap: '12px', textDecoration: 'none' }}>
          <div style={{
            width: '40px',
            height: '40px',
            borderRadius: '10px',
            background: 'linear-gradient(135deg, #8B6F4C, #B8977A)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontWeight: 900,
            fontSize: '18px',
            color: 'white'
          }}>NM</div>
          <span style={{ fontWeight: 700, fontSize: '18px', color: '#3D2B1F' }}>Neural<span style={{ background: 'linear-gradient(135deg, #8B6F4C, #B8977A)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>Mapper</span></span>
        </Link>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <Link href="/" style={{
            padding: '10px 24px',
            borderRadius: '10px',
            background: 'linear-gradient(135deg, #8B6F4C, #A8876A)',
            color: 'white',
            fontWeight: 600,
            fontSize: '14px',
            textDecoration: 'none',
            transition: 'all 0.3s ease'
          }} onMouseEnter={e => { e.target.style.boxShadow = '0 8px 30px rgba(139, 111, 76, 0.3)'; e.target.style.transform = 'scale(1.02)' }} onMouseLeave={e => { e.target.style.boxShadow = 'none'; e.target.style.transform = 'scale(1)' }}>
            + New Analysis
          </Link>
        </div>
      </nav>

      {/* Main Content */}
      <div style={{ position: 'relative', zIndex: 10, maxWidth: '1200px', margin: '0 auto' }}>
        {/* Header */}
        <div style={{
          padding: '32px',
          borderRadius: '16px',
          background: 'rgba(255, 252, 248, 0.6)',
          backdropFilter: 'blur(20px)',
          border: '1px solid rgba(139, 111, 76, 0.06)',
          marginBottom: '24px'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '16px' }}>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flexWrap: 'wrap' }}>
                <h1 style={{ color: '#3D2B1F', fontSize: '32px', fontWeight: 800 }}>{a.company || 'Company Analysis'}</h1>
                <span style={{
                  padding: '4px 16px',
                  borderRadius: '20px',
                  background: a.sentiment === 'Positive' ? 'rgba(52, 211, 153, 0.08)' : 'rgba(251, 191, 36, 0.08)',
                  color: a.sentiment === 'Positive' ? '#059669' : '#D97706',
                  fontSize: '13px',
                  fontWeight: 600,
                  border: `1px solid ${a.sentiment === 'Positive' ? 'rgba(52, 211, 153, 0.1)' : 'rgba(251, 191, 36, 0.1)'}`
                }}>{a.sentiment || 'Neutral'} Sentiment</span>
              </div>
              <p style={{ color: '#8B7355', fontSize: '16px', maxWidth: '600px', marginTop: '8px' }}>{a.summary}</p>
            </div>
            
            <div style={{ display: 'flex', gap: '12px' }}>
              <button
                onClick={async () => {
                  const res = await fetch(`http://localhost:8000/api/report/${id}`)
                  const data = await res.json()
                  alert(data.report)
                }}
                style={{
                  padding: '12px 24px',
                  borderRadius: '10px',
                  border: 'none',
                  background: '#8B7355',
                  color: 'white',
                  fontWeight: 600,
                  fontSize: '14px',
                  cursor: 'pointer',
                  transition: 'all 0.3s ease',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px'
                }}
              >
                📝 Text Report
              </button>
              
              <button
                onClick={() => {
                  window.open(`http://localhost:8000/api/download-pdf/${id}`, '_blank')
                }}
                style={{
                  padding: '12px 28px',
                  borderRadius: '10px',
                  border: 'none',
                  background: 'linear-gradient(135deg, #8B6F4C, #A8876A)',
                  color: 'white',
                  fontWeight: 600,
                  fontSize: '14px',
                  cursor: 'pointer',
                  transition: 'all 0.3s ease',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  boxShadow: '0 4px 15px rgba(139, 111, 76, 0.2)'
                }}
                onMouseEnter={e => { e.target.style.boxShadow = '0 8px 30px rgba(139, 111, 76, 0.3)'; e.target.style.transform = 'scale(1.02)' }}
                onMouseLeave={e => { e.target.style.boxShadow = '0 4px 15px rgba(139, 111, 76, 0.2)'; e.target.style.transform = 'scale(1)' }}
              >
                📄 Download PDF
              </button>
            </div>
          </div>
        </div>

        {/* SWOT Grid */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: '20px',
          marginBottom: '24px'
        }}>
          {[
            { title: 'Strengths', icon: '✅', color: '#059669', data: a.swot?.strengths },
            { title: 'Weaknesses', icon: '❌', color: '#DC2626', data: a.swot?.weaknesses },
            { title: 'Opportunities', icon: '🚀', color: '#2563EB', data: a.swot?.opportunities },
            { title: 'Threats', icon: '⚠️', color: '#D97706', data: a.swot?.threats }
          ].map((item, index) => (
            <div key={index} style={{
              padding: '24px',
              borderRadius: '14px',
              background: 'rgba(255, 252, 248, 0.5)',
              backdropFilter: 'blur(10px)',
              border: '1px solid rgba(139, 111, 76, 0.06)',
              borderLeft: `4px solid ${item.color}`
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '12px' }}>
                <span style={{ fontSize: '20px' }}>{item.icon}</span>
                <h3 style={{ color: item.color, fontSize: '18px', fontWeight: 700 }}>{item.title}</h3>
                <span style={{ marginLeft: 'auto', color: '#8B7355', fontSize: '14px' }}>{item.data?.length || 0}</span>
              </div>
              <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                {item.data?.map((s, i) => (
                  <li key={i} style={{
                    padding: '6px 0',
                    color: '#4A3728',
                    fontSize: '14px',
                    borderBottom: i < item.data.length - 1 ? '1px solid rgba(139, 111, 76, 0.04)' : 'none',
                    display: 'flex',
                    alignItems: 'flex-start',
                    gap: '8px'
                  }}>
                    <span style={{ color: item.color }}>▸</span>
                    <span>{s}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Competitors & Market Gaps */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: '20px'
        }}>
          <div style={{
            padding: '24px',
            borderRadius: '14px',
            background: 'rgba(255, 252, 248, 0.5)',
            backdropFilter: 'blur(10px)',
            border: '1px solid rgba(139, 111, 76, 0.06)'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '16px' }}>
              <span style={{ fontSize: '20px' }}>👥</span>
              <h3 style={{ color: '#3D2B1F', fontSize: '18px', fontWeight: 700 }}>Competitors</h3>
            </div>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
              {a.competitors?.map((c, i) => (
                <span key={i} style={{
                  padding: '6px 16px',
                  borderRadius: '20px',
                  background: 'rgba(139, 111, 76, 0.06)',
                  color: '#5C4033',
                  fontSize: '13px',
                  border: '1px solid rgba(139, 111, 76, 0.06)'
                }}>{c}</span>
              ))}
            </div>
          </div>

          <div style={{
            padding: '24px',
            borderRadius: '14px',
            background: 'rgba(255, 252, 248, 0.5)',
            backdropFilter: 'blur(10px)',
            border: '1px solid rgba(139, 111, 76, 0.06)'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '16px' }}>
              <span style={{ fontSize: '20px' }}>🎯</span>
              <h3 style={{ color: '#3D2B1F', fontSize: '18px', fontWeight: 700 }}>Market Gaps</h3>
            </div>
            <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
              {a.market_gaps?.map((g, i) => (
                <li key={i} style={{
                  padding: '6px 0',
                  color: '#4A3728',
                  fontSize: '14px',
                  borderBottom: i < a.market_gaps.length - 1 ? '1px solid rgba(139, 111, 76, 0.04)' : 'none',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px'
                }}>
                  <span style={{ fontSize: '16px' }}>💡</span>
                  <span>{g}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Footer */}
        <div style={{
          marginTop: '24px',
          padding: '20px 24px',
          borderRadius: '14px',
          background: 'rgba(255, 252, 248, 0.4)',
          backdropFilter: 'blur(10px)',
          border: '1px solid rgba(139, 111, 76, 0.04)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '12px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '16px', fontSize: '13px', color: '#8B7355' }}>
            <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#059669', display: 'inline-block' }}></span>
              Live Analysis
            </span>
            <span>|</span>
            <span>{new Date().toLocaleDateString()}</span>
            <span>|</span>
            <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>⚡ AI Generated</span>
          </div>
          
          <button
            onClick={() => {
              window.open(`http://localhost:8000/api/download-pdf/${id}`, '_blank')
            }}
            style={{
              padding: '10px 24px',
              borderRadius: '10px',
              border: 'none',
              background: 'linear-gradient(135deg, #8B6F4C, #A8876A)',
              color: 'white',
              fontWeight: 600,
              fontSize: '14px',
              cursor: 'pointer',
              transition: 'all 0.3s ease',
              display: 'flex',
              alignItems: 'center',
              gap: '8px'
            }}
          >
            📄 Export PDF Report
          </button>
        </div>
      </div>
    </div>
  )
}