import api from './api';

export const login = async (email, password) => {
  try {
    const response = await api.post('/token/', {
      email,
      password,
    });
    localStorage.setItem('token', response.data.access);
    return response.data;
  } catch (error) {
    console.error('Login failed:', error);
    throw error;
  }
};

export const refreshToken = async () => {
  try {
    const response = await api.post('/token/refresh/', {
      refresh: localStorage.getItem('refreshToken'), 
    });
    return response.data.access;
  } catch (error) {
    console.error('Token refresh failed:', error);
    throw error;
  }
};