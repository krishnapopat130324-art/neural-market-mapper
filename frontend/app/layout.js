import './globals.css'

export const metadata = {
  title: 'Neural Market Mapper - AI Competitive Intelligence',
  description: 'AI-powered market research and competitive analysis platform',
  keywords: 'market intelligence, competitive analysis, AI, SWOT analysis',
  authors: [{ name: 'Neural Market Mapper' }],
  viewport: 'width=device-width, initial-scale=1',
  themeColor: '#6366F1',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
      </head>
      <body>{children}</body>
    </html>
  )
}