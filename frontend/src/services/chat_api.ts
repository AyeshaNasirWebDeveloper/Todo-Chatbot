import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000'; // Ensure this matches your backend URL

interface ChatMessage {
  message: string;
}

interface ChatResponse {
  response: string;
}

export const sendMessage = async (
  userId: number,
  message: string,
  token: string // Assuming JWT token for authentication
): Promise<ChatResponse> => {
  try {
    const response = await axios.post<ChatResponse>(
      `${API_BASE_URL}/api/v1/users/${userId}/chat`,
      { message },
      {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      }
    );
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error('Error sending message:', error.response?.data || error.message);
      throw new Error(error.response?.data?.detail || 'Failed to send message');
    } else {
      console.error('Unexpected error:', error);
      throw new Error('An unexpected error occurred');
    }
  }
};
