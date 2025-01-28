import axios from 'axios';
import { refreshToken } from './auth'; 

// 創建 Axios 實例
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api', // 替換為你的 API 基礎 URL
  timeout: 10000, 
  headers: {
    'Content-Type': 'application/json',
  },
});

// 請求攔截器
api.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token'); 
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// 回應攔截器
api.interceptors.response.use(
  response => {
    return response;
  },
  async error => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const newToken = await refreshToken(); 
        localStorage.setItem('token', newToken);
        api.defaults.headers.common['Authorization'] = `Bearer ${newToken}`;
        originalRequest.headers['Authorization'] = `Bearer ${newToken}`;
        return api(originalRequest);
      } catch (refreshError) {
        console.error('Token refresh failed:', refreshError);
      }
    }
    return Promise.reject(error);
  }
);

// 定義 fetchMessage 函數
export function fetchMessage() {
  return fetch('https://api.example.com/data')
    .then(response => response.json());
}

export default api;