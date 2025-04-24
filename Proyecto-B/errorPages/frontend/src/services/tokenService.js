import axios from "axios";

const API_URL = "http://127.0.0.1:8000/users/";

// Función para obtener nuevo accessToken usando refreshToken
const refreshAccessToken = async () => {
  try {
    const refreshToken = localStorage.getItem("refreshToken");
    if (!refreshToken) {
      throw new Error("No refresh token available");
    }

    const response = await axios.post(`${API_URL}token/refresh`, {
      refresh: refreshToken
    });

    if (response.data.access) {
      localStorage.setItem("accessToken", response.data.access);
      return response.data.access;
    }
  } catch (error) {
    console.error("Error refreshing token:", error);
    // Si hay un error al refrescar, desloguear al usuario
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    window.location.href = "/login";
    throw new Error("Session expired. Please login again.");
  }
};

// Crear una instancia de axios con interceptores
const apiClient = axios.create({
  baseURL: API_URL
});

// Interceptor para añadir token a las peticiones
apiClient.interceptors.request.use(
  async (config) => {
    let token = localStorage.getItem("accessToken");
    if (token) {
      config.headers["Authorization"] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor para manejar errores de autenticación
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    
    // Si el error es 401 y no hemos intentado refrescar el token ya
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      try {
        // Obtener nuevo token
        const newToken = await refreshAccessToken();
        
        // Actualizar header con nuevo token
        originalRequest.headers["Authorization"] = `Bearer ${newToken}`;
        
        // Reintentar la petición original
        return apiClient(originalRequest);
      } catch (refreshError) {
        return Promise.reject(refreshError);
      }
    }
    
    return Promise.reject(error);
  }
);

export default apiClient;