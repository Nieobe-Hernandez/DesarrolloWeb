import axios from "axios";

const API_URL = "http://127.0.0.1:8000/users/token/";

export const login = async (email, password) => {
  try {
    const response = await axios.post(API_URL, { email, password });
    if (response.data.access) {
      // Guardar tokens en localStorage
      localStorage.setItem("accessToken", response.data.access);
      localStorage.setItem("refreshToken", response.data.refresh);

      window.dispatchEvent(new Event('sessionChange'));
    }
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const logout = () => {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("refreshToken");
  window.dispatchEvent(new Event('sessionChange'));
  window.location.reload();
};

export const isAuthenticated = () => {
  return localStorage.getItem("accessToken") !== null;
};

export default {
  login,
  logout,
  isAuthenticated
};