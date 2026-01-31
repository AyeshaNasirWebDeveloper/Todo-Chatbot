"use client";

import { useState } from "react";

const API_BASE_URL = "http://localhost:8000/api";

export default function ChatInput({ setMessages }: any) {
  const [text, setText] = useState("");

  const sendMessage = async () => {
    if (!text.trim()) return;

    setMessages((prev: any[]) => [
      ...prev,
      { id: Date.now(), content: text, role: "user" },
    ]);

    setText("");

    const res = await fetch(`${API_BASE_URL}/chat/{user_id}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer YOUR_TOKEN_HERE`,
      },
      body: JSON.stringify({ message: text }),
    });

    const data = await res.json();

    setMessages((prev: any[]) => [
      ...prev,
      { id: Date.now() + 1, content: data.response, role: "bot" },
    ]);
  };

  return (
    <div className="p-3 border-t flex gap-2">
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="flex-1 border rounded px-3 py-2"
        placeholder="Ask me anything..."
      />
      <button onClick={sendMessage} className="bg-blue-600 text-white px-4 rounded">
        Send
      </button>
    </div>
  );
}
