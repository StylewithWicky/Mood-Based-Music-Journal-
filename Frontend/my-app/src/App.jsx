import React, { useState, useEffect } from 'react'
import LoginForm from './pages/LoginForm'
import MoodForm from './pages/MoodForm'

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  useEffect(() => {
    const token = localStorage.getItem('token')
    setIsAuthenticated(!!token)
  }, [])

  const handleLogout = () => {
    localStorage.removeItem('token')
    setIsAuthenticated(false)
  }

  return (
    <div>
      {isAuthenticated ? (
        <>
          
          <MoodForm />
        </>
      ) : (
        <LoginForm onLogin={() => setIsAuthenticated(true)} />
      )}
    </div>
  )
}

export default App
