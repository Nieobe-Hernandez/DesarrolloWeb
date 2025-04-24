import { useState, useEffect } from "react";
import axios from "axios";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  useLocation,
} from "react-router-dom";
import Login from "./components/Login";
import Recuperar from "./components/Recuperar";
import ResetPassword from "./components/ResetPassword";
import Navbar from "./components/Navbar";
import UserDataTable from "./components/UserDataTable";
import CustomUserForm from "./components/NewUser";
import AboutUs from "./pages/AboutUs";
import NotFound from "./pages/404";
import { motion, AnimatePresence } from "framer-motion";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";
import "react-toastify/dist/ReactToastify.css";

const AnimatedRoutes = () => {
  const location = useLocation();
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<CustomUserForm />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/" element={<Home />} />
        <Route path="/recuperar" element={<Recuperar />} />
        <Route path="/reset-password/:token" element={<ResetPassword />} />
        <Route path="*" element={<NotFound />} />{" "}
      </Routes>
    </AnimatePresence>
  );
};

function Home() {
  const[sesion, setSesion] = useState(false);

  useEffect(() => {
    const item = localStorage.getItem('accessToken');
    setSesion(item !== null) // Si el item existe
  }, [])

  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0, transition: { duration: 0.5 } }}
        exit={{ opacity: 0, y: -50, transition: { duration: 0.5 } }}
        className="page"
      >
        {sesion ? (
          <div>
            <h1 className="mb-5">Bienvenido usuario logueado</h1>
            <div className="p-1 mw-100">
              <UserDataTable />
            </div>
          </div>
        ) : (
          <h4>Por favor inicia sesión para ver más información</h4>
        )}
      </motion.div>
    </div>
  );
}

function App() {
  const [sesion, setSesion] = useState(false);

  const checkSession = () => {
    const item = localStorage.getItem("accessToken");
    setSesion(item !== null);
  };

  useEffect(() => {
    checkSession();
    
    window.addEventListener('storage', checkSession);
    window.addEventListener('sessionChange', checkSession);
    
    return () => {
      window.removeEventListener('storage', checkSession);
      window.removeEventListener('sessionChange', checkSession);
    };
  }, []);

  return (
    <Router>
      <Navbar sesion={sesion} setSesion={setSesion} />
      <div className="container mt-4">
        <div className="row">
          <div className="col">
            <AnimatedRoutes />
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;