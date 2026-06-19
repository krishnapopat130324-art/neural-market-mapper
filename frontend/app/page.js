'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function Home() {
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const router = useRouter()

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!url) {
      setError('Please enter a URL')
      return
    }
    
    setLoading(true)
    setError('')
    
    try {
      const res = await fetch('http://localhost:8000/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      })
      
      const data = await res.json()
      console.log('Response:', data)
      
      if (data.status === 'failed') {
        setError(data.error || 'Analysis failed. Please try again.')
        setLoading(false)
        return
      }
      
      if (data.task_id) {
        router.push(`/analysis/${data.task_id}`)
      } else {
        setError('No task ID received. Please try again.')
        setLoading(false)
      }
      
    } catch (error) {
      console.error('Error:', error)
      setError('Failed to connect to server. Make sure backend is running.')
      setLoading(false)
    }
  }

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #FAF6F0 0%, #F5EDE3 30%, #EDE4D6 60%, #E8DDCF 100%)',
      fontFamily: "'Inter', -apple-system, sans-serif",
      position: 'relative',
      overflow: 'hidden'
    }}>
      {/* Decorative Background Elements */}
      <div style={{
        position: 'absolute',
        top: '-30%',
        right: '-20%',
        width: '800px',
        height: '800px',
        background: 'radial-gradient(circle, rgba(193, 162, 138, 0.08) 0%, transparent 70%)',
        borderRadius: '50%'
      }}></div>
      <div style={{
        position: 'absolute',
        bottom: '-30%',
        left: '-20%',
        width: '600px',
        height: '600px',
        background: 'radial-gradient(circle, rgba(160, 130, 110, 0.06) 0%, transparent 70%)',
        borderRadius: '50%'
      }}></div>
      <div style={{
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: '1000px',
        height: '1000px',
        background: 'radial-gradient(circle, rgba(180, 150, 125, 0.04) 0%, transparent 70%)',
        borderRadius: '50%'
      }}></div>

      <style>{`
        @keyframes float {
          0%, 100% { transform: translate(0, 0) scale(1); }
          50% { transform: translate(20px, -20px) scale(1.05); }
        }
        @keyframes shimmer {
          0% { background-position: -200% center; }
          100% { background-position: 200% center; }
        }
        @keyframes pulse {
          0%, 100% { opacity: 0.6; }
          50% { opacity: 1; }
        }
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
        .gradient-text-brown {
          background: linear-gradient(135deg, #8B6F4C 0%, #A8876A 30%, #C4A88A 60%, #8B6F4C 100%);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-size: 200% auto;
          animation: shimmer 4s linear infinite;
        }
        .glass-card-brown {
          background: rgba(255, 252, 248, 0.7);
          backdrop-filter: blur(20px);
          -webkit-backdrop-filter: blur(20px);
          border: 1px solid rgba(180, 150, 125, 0.15);
          box-shadow: 0 4px 30px rgba(140, 110, 90, 0.06);
        }
        .glass-card-brown:hover {
          background: rgba(255, 252, 248, 0.85);
          border-color: rgba(180, 150, 125, 0.25);
          transform: translateY(-4px);
          box-shadow: 0 20px 60px rgba(140, 110, 90, 0.1);
          transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .input-brown:focus {
          border-color: #A8876A;
          box-shadow: 0 0 0 4px rgba(168, 135, 106, 0.1), 0 0 30px rgba(168, 135, 106, 0.05);
        }
        .btn-brown {
          background: linear-gradient(135deg, #8B6F4C 0%, #A8876A 50%, #B8977A 100%);
          background-size: 200% auto;
          transition: all 0.3s ease;
        }
        .btn-brown:hover {
          transform: scale(1.02);
          box-shadow: 0 10px 40px rgba(139, 111, 76, 0.3);
        }
        .btn-brown:active {
          transform: scale(0.98);
        }
      `}</style>

      {/* Navbar */}
      <nav style={{
        position: 'relative',
        zIndex: 10,
        padding: '0 2rem',
        height: '72px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        borderBottom: '1px solid rgba(139, 111, 76, 0.08)',
        background: 'rgba(255, 252, 248, 0.85)',
        backdropFilter: 'blur(20px)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{
            width: '42px',
            height: '42px',
            borderRadius: '10px',
            background: 'linear-gradient(135deg, #8B6F4C, #B8977A)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontWeight: 900,
            fontSize: '18px',
            color: 'white',
            boxShadow: '0 4px 20px rgba(139, 111, 76, 0.25)'
          }}>NM</div>
          <div>
            <span style={{ fontWeight: 700, fontSize: '20px', color: '#3D2B1F' }}>Neural</span>
            <span style={{ fontWeight: 700, fontSize: '20px', background: 'linear-gradient(135deg, #8B6F4C, #B8977A)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>Mapper</span>
            <span style={{
              marginLeft: '8px',
              fontSize: '10px',
              padding: '2px 10px',
              borderRadius: '20px',
              background: 'rgba(139, 111, 76, 0.1)',
              color: '#8B6F4C',
              fontWeight: 600
            }}>AI</span>
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '32px' }}>
          <a href="#" style={{ color: '#8B7355', textDecoration: 'none', fontSize: '14px', fontWeight: 500, transition: 'color 0.3s' }} onMouseEnter={e => e.target.style.color = '#5C4033'} onMouseLeave={e => e.target.style.color = '#8B7355'}>Features</a>
          <a href="#" style={{ color: '#8B7355', textDecoration: 'none', fontSize: '14px', fontWeight: 500, transition: 'color 0.3s' }} onMouseEnter={e => e.target.style.color = '#5C4033'} onMouseLeave={e => e.target.style.color = '#8B7355'}>Pricing</a>
          <a href="#" style={{ color: '#8B7355', textDecoration: 'none', fontSize: '14px', fontWeight: 500, transition: 'color 0.3s' }} onMouseEnter={e => e.target.style.color = '#5C4033'} onMouseLeave={e => e.target.style.color = '#8B7355'}>Docs</a>
          <button style={{
            padding: '8px 22px',
            borderRadius: '10px',
            border: 'none',
            fontWeight: 600,
            fontSize: '14px',
            color: 'white',
            cursor: 'pointer',
            background: 'linear-gradient(135deg, #8B6F4C, #A8876A)',
            transition: 'all 0.3s ease'
          }} onMouseEnter={e => { e.target.style.boxShadow = '0 8px 25px rgba(139, 111, 76, 0.3)'; e.target.style.transform = 'scale(1.02)' }} onMouseLeave={e => { e.target.style.boxShadow = 'none'; e.target.style.transform = 'scale(1)' }}>Get Started</button>
        </div>
      </nav>

      {/* Hero Section */}
      <div style={{
        position: 'relative',
        zIndex: 10,
        maxWidth: '1200px',
        margin: '0 auto',
        padding: '60px 24px 80px',
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: '60px',
        alignItems: 'center'
      }}>
        {/* Left Content */}
        <div>
          <div style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '8px',
            padding: '6px 16px 6px 10px',
            borderRadius: '50px',
            background: 'rgba(139, 111, 76, 0.06)',
            border: '1px solid rgba(139, 111, 76, 0.1)',
            marginBottom: '32px'
          }}>
            <span style={{
              width: '8px',
              height: '8px',
              borderRadius: '50%',
              background: '#8B6F4C',
              display: 'inline-block',
              animation: 'pulse 2s ease-in-out infinite'
            }}></span>
            <span style={{ fontSize: '13px', fontWeight: 500, color: '#8B6F4C' }}>AI-Powered Intelligence</span>
          </div>

          <h1 style={{
            fontSize: '60px',
            fontWeight: 900,
            lineHeight: 1.1,
            color: '#3D2B1F',
            marginBottom: '20px'
          }}>
            Unlock
            <br />
            <span className="gradient-text-brown">Market Insights</span>
            <br />
            in Seconds
          </h1>

          <p style={{
            fontSize: '18px',
            color: '#8B7355',
            lineHeight: 1.8,
            maxWidth: '480px',
            marginBottom: '36px'
          }}>
            Enter any company URL and get instant AI-powered competitive analysis,
            SWOT insights, and market intelligence reports.
          </p>

          {/* Search Form */}
          <form onSubmit={handleSubmit} style={{ position: 'relative' }}>
            {error && (
              <div style={{
                padding: '10px 14px',
                borderRadius: '8px',
                background: 'rgba(220, 38, 38, 0.08)',
                color: '#DC2626',
                fontSize: '13px',
                marginBottom: '12px',
                border: '1px solid rgba(220, 38, 38, 0.15)'
              }}>
                {error}
              </div>
            )}
            <div style={{
              position: 'relative',
              background: 'rgba(255, 252, 248, 0.8)',
              borderRadius: '14px',
              border: '1px solid rgba(139, 111, 76, 0.12)',
              overflow: 'hidden',
              transition: 'all 0.3s ease',
              boxShadow: '0 4px 20px rgba(139, 111, 76, 0.04)'
            }}>
              <span style={{
                position: 'absolute',
                left: '18px',
                top: '50%',
                transform: 'translateY(-50%)',
                fontSize: '20px',
                color: '#8B7355'
              }}>🔍</span>
              <input
                type="url"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Enter company URL (e.g., https://google.com)"
                style={{
                  width: '100%',
                  padding: '16px 20px 16px 56px',
                  background: 'transparent',
                  border: 'none',
                  color: '#3D2B1F',
                  fontSize: '15px',
                  outline: 'none'
                }}
                required
              />
              <button
                type="submit"
                disabled={loading}
                style={{
                  position: 'absolute',
                  right: '8px',
                  top: '50%',
                  transform: 'translateY(-50%)',
                  padding: '10px 26px',
                  borderRadius: '10px',
                  border: 'none',
                  fontWeight: 600,
                  fontSize: '14px',
                  color: 'white',
                  cursor: loading ? 'not-allowed' : 'pointer',
                  opacity: loading ? 0.7 : 1,
                  background: loading ? '#8B7355' : 'linear-gradient(135deg, #8B6F4C, #A8876A)',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  transition: 'all 0.3s ease'
                }}
              >
                {loading ? (
                  <>
                    <span style={{
                      width: '16px',
                      height: '16px',
                      border: '2px solid rgba(255,255,255,0.3)',
                      borderTop: '2px solid white',
                      borderRadius: '50%',
                      display: 'inline-block',
                      animation: 'spin 0.8s linear infinite'
                    }}></span>
                    Analyzing
                  </>
                ) : (
                  <>Analyze →</>
                )}
              </button>
            </div>
          </form>

          {/* Trust Badges */}
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '24px',
            marginTop: '28px'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ fontSize: '18px' }}>⚡</span>
              <span style={{ fontSize: '13px', color: '#8B7355' }}>Real-time analysis</span>
            </div>
            <div style={{ width: '1px', height: '20px', background: 'rgba(139, 111, 76, 0.15)' }}></div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ fontSize: '18px' }}>💎</span>
              <span style={{ fontSize: '13px', color: '#8B7355' }}>Enterprise grade</span>
            </div>
            <div style={{ width: '1px', height: '20px', background: 'rgba(139, 111, 76, 0.15)' }}></div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ fontSize: '18px' }}>⭐</span>
              <span style={{ fontSize: '13px', color: '#8B7355' }}>100% free</span>
            </div>
          </div>
        </div>

        {/* Right Side - Premium Card */}
        <div style={{ position: 'relative' }}>
          <div style={{
            position: 'absolute',
            inset: '-20px',
            background: 'linear-gradient(135deg, rgba(139, 111, 76, 0.06), rgba(184, 151, 122, 0.04))',
            borderRadius: '28px',
            filter: 'blur(40px)'
          }}></div>
          
          <div style={{
            position: 'relative',
            background: 'rgba(255, 252, 248, 0.8)',
            backdropFilter: 'blur(20px)',
            borderRadius: '20px',
            padding: '32px',
            border: '1px solid rgba(139, 111, 76, 0.08)',
            boxShadow: '0 20px 60px rgba(139, 111, 76, 0.06)'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '24px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                <div style={{
                  width: '48px',
                  height: '48px',
                  borderRadius: '12px',
                  background: 'linear-gradient(135deg, #8B6F4C, #B8977A)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '24px'
                }}>📊</div>
                <div>
                  <div style={{ fontWeight: 600, color: '#3D2B1F', fontSize: '16px' }}>SWOT Analysis</div>
                  <div style={{ color: '#8B7355', fontSize: '13px' }}>Google Inc.</div>
                </div>
              </div>
              <span style={{
                padding: '4px 14px',
                borderRadius: '20px',
                background: 'rgba(52, 211, 153, 0.08)',
                color: '#059669',
                fontSize: '12px',
                fontWeight: 600
              }}>● Live</span>
            </div>

            <div style={{ marginBottom: '20px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px', marginBottom: '6px' }}>
                <span style={{ color: '#8B7355' }}>Analysis Progress</span>
                <span style={{ color: '#3D2B1F', fontWeight: 600 }}>85%</span>
              </div>
              <div style={{
                width: '100%',
                height: '6px',
                borderRadius: '10px',
                background: 'rgba(139, 111, 76, 0.08)',
                overflow: 'hidden'
              }}>
                <div style={{
                  width: '85%',
                  height: '100%',
                  borderRadius: '10px',
                  background: 'linear-gradient(90deg, #8B6F4C, #B8977A)'
                }}></div>
              </div>
            </div>

            <div style={{
              display: 'grid',
              gridTemplateColumns: '1fr 1fr',
              gap: '12px',
              marginBottom: '20px'
            }}>
              {[
                { label: 'Strengths', value: '12', color: '#059669' },
                { label: 'Weaknesses', value: '5', color: '#DC2626' },
                { label: 'Opportunities', value: '8', color: '#2563EB' },
                { label: 'Threats', value: '4', color: '#D97706' }
              ].map((item) => (
                <div key={item.label} style={{
                  padding: '14px',
                  borderRadius: '10px',
                  background: 'rgba(139, 111, 76, 0.04)',
                  border: '1px solid rgba(139, 111, 76, 0.06)'
                }}>
                  <div style={{ fontSize: '11px', color: item.color, fontWeight: 500 }}>{item.label}</div>
                  <div style={{ fontSize: '22px', fontWeight: 700, color: '#3D2B1F' }}>{item.value}</div>
                </div>
              ))}
            </div>

            <div style={{ paddingTop: '16px', borderTop: '1px solid rgba(139, 111, 76, 0.06)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px' }}>
                <span style={{ color: '#8B7355' }}>Market Position</span>
                <span style={{ color: '#3D2B1F', fontWeight: 600 }}>#1 in Search</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px', marginTop: '6px' }}>
                <span style={{ color: '#8B7355' }}>Sentiment</span>
                <span style={{ color: '#059669', fontWeight: 600 }}>Positive</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div style={{
        position: 'relative',
        zIndex: 10,
        maxWidth: '1200px',
        margin: '0 auto',
        padding: '0 24px 80px',
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        gap: '20px'
      }}>
        {[
          { icon: '🧠', title: 'AI-Powered Analysis', desc: 'Advanced machine learning for deep insights' },
          { icon: '🌍', title: 'Market Intelligence', desc: 'Real-time competitive landscape mapping' },
          { icon: '📊', title: 'SWOT Analytics', desc: 'Comprehensive strengths & weaknesses analysis' },
          { icon: '🎯', title: 'Opportunity Detection', desc: 'Identify market gaps and growth areas' }
        ].map((feature, i) => (
          <div key={i} style={{
            padding: '24px',
            borderRadius: '14px',
            background: 'rgba(255, 252, 248, 0.6)',
            backdropFilter: 'blur(10px)',
            border: '1px solid rgba(139, 111, 76, 0.06)',
            transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
            cursor: 'pointer'
          }} onMouseEnter={e => { e.target.style.background = 'rgba(255, 252, 248, 0.85)'; e.target.style.borderColor = 'rgba(139, 111, 76, 0.15)'; e.target.style.transform = 'translateY(-4px)'; e.target.style.boxShadow = '0 12px 40px rgba(139, 111, 76, 0.06)' }} onMouseLeave={e => { e.target.style.background = 'rgba(255, 252, 248, 0.6)'; e.target.style.borderColor = 'rgba(139, 111, 76, 0.06)'; e.target.style.transform = 'translateY(0)'; e.target.style.boxShadow = 'none' }}>
            <div style={{
              fontSize: '32px',
              marginBottom: '12px'
            }}>{feature.icon}</div>
            <div style={{ fontWeight: 600, color: '#3D2B1F', fontSize: '16px', marginBottom: '4px' }}>{feature.title}</div>
            <div style={{ color: '#8B7355', fontSize: '14px', lineHeight: 1.5 }}>{feature.desc}</div>
          </div>
        ))}
      </div>
    </div>
  )
}