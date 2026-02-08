import { setToken } from "../utils/token";

const API_BASE_URL = 'http://localhost:8000';

export const signup = async (email: string, password: string) => {
  const response = await fetch(`${API_BASE_URL}/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Signup failed');
  }

  return response.json();
};

export const login = async (email: string, password: string) => {
  const response = await fetch(`${API_BASE_URL}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Login failed');
  }

  const data = await response.json();

  setToken(data.access_token);

  localStorage.setItem("token", data.access_token);
  localStorage.setItem("user_name", email);

  // TEMP userId until backend provides it
  localStorage.setItem("userId", "4");

  return data;
};


export const forgotPassword = async (email: string) => {
  const response = await fetch(`${API_BASE_URL}/forgot-password`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Forgot password request failed');
  }

  return response.json();
};