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
  const response = await fetch(`http://localhost:8000/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    throw new Error("Login failed");
  }

  const data = await response.json();

  console.log("Login successful:", data);

  // STORE VALUES
  localStorage.setItem("token", data.access_token);
  localStorage.setItem("userId", String(data.user.id));

  console.log("Saved token:", localStorage.getItem("token"));
  console.log("Saved userId:", localStorage.getItem("userId"));

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