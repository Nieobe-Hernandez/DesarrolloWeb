import apiClient from "./tokenService";

const userService = {
  getAllUsers: async () => {
    try {
      const response = await apiClient.get("api/");
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  getUserById: async (id) => {
    try {
      const response = await apiClient.get(`api/${id}/`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  updateUser: async (id, userData) => {
    try {
      const response = await apiClient.put(`api/${id}/`, userData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  deleteUser: async (id) => {
    try {
      const response = await apiClient.delete(`api/${id}/`);
      return response;
    } catch (error) {
      throw error;
    }
  },

  getCurrentUserId: () => {
    const token = localStorage.getItem("accessToken");
    if (!token) return null;
    
    try {
      const payload = token.split(".")[1];
      const decodedPayload = JSON.parse(atob(payload));
      return decodedPayload.user_id;
    } catch (error) {
      console.error("Error decoding token:", error);
      return null;
    }
  }
};

export default userService;