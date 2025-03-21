import { useState, useEffect } from 'react'
import axios from 'axios'
import { BrowserRouter as Router, Route, Routes, useLocation, useNavigate } from 'react-router-dom'
import Login from './components/Login'
import Navbar from './components/Navbar'
import AboutUs from './pages/AboutUs'
import NotFound from './pages/404'
import { AnimatePresence } from 'framer-motion'
import './App.css'
import "bootstrap/dist/css/bootstrap.min.css"

const AnimatedRoutes = () => {
  const location = useLocation()
  return (
    <AnimatePresence mode='wait'>
      <Routes location={location
      } key={location.pathname}>
        <Route path="/login" element={<Login />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/" element={<Home />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </AnimatePresence>
  )
}

const Home = () => {
  const [data, setData] = useState([])
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(true)
  const sesion = localStorage.getItem('accessToken');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/users/api/')
      .then(response => {
        setData(response.data)
        setLoading(false)
      })
      .catch((error) => {
        setError(error)
        setLoading(false)
      })
  }, [])

  if (loading) {
    return <div>Loading...</div>
  }

  if (error) {
    return <div>Error: {error.message}</div>
  }

  return (
    <div>
      <h1>Home</h1>
      <h2>Usuario: {sesion}</h2>
      <ul>
        {data.map(user => (
          <li key={user.id}>{JSON.stringify(user)}</li>
        ))}
      </ul>
    </div>
  )

}

export default function App() {
  return (
    <Router>
      <Navbar />
      <div className='container mt-4'>
        <div className='row'>
          <div className='col'>
            <AnimatedRoutes />
          </div>
        </div>
      </div>
    </Router>
  )
}