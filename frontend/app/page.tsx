"use client";

import { useState } from "react";
import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";

export default function HomePage() {
  // Messages state
  const [messages, setMessages] = useState([
    {
      id: 1,
      content: "Hello! How can I help you today?",
      role: "bot",
      type: "text"
    }
  ]);

  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <Sidebar />

      {/* Chat window */}
      <div className="flex flex-col flex-1">
        <ChatWindow messages={messages} />
      </div>
    </div>
  );
}
