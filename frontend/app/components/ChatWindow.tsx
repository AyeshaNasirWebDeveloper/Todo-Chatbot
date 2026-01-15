"use client";

import { useState } from "react";
import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";

export default function ChatWindow() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hello! I’m your Todo AI Assistant. How can I help you today? 😊" },
  ]);

  const sendMessage = async (text: string) => {
    const newMsg = { role: "user", content: text };
    setMessages((prev) => [...prev, newMsg]);

    const res = await fetch("http://localhost:8000/api/ayesha/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    const data = await res.json();

    const botReply = { role: "assistant", content: data.response };
    setMessages((prev) => [...prev, botReply]);
  };

  return (
    <div className="flex flex-col h-full">

      <div className="px-6 py-4 border-b bg-white dark:bg-gray-800 shadow">
        <h2 className="text-xl font-semibold text-gray-800 dark:text-white">
          Todo AI Assistant
        </h2>
      </div>

      <div className="flex-1 overflow-y-auto p-6 space-y-4 bg-gray-50 dark:bg-gray-900">
        {messages.map((msg, index) => (
          <ChatMessage key={index} role={msg.role} content={msg.content} />
        ))}
      </div>

      <ChatInput onSend={sendMessage} />
    </div>
  );
}
