"use client";

import { useState } from "react";
import Sidebar from "./Sidebar";
import ChatWindow from "./ChatWindow";
import ChatInput from "./ChatInput";

export default function ChatWidget() {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState<any[]>([
    {
      id: 1,
      content: "Hello! How can I help you today?",
      role: "bot",
    },
  ]);

  return (
    <>
      {/* Floating Button */}
      <button
        onClick={() => setOpen(!open)}
        className="fixed bottom-6 right-6 bg-blue-600 text-white p-4 rounded-full shadow-lg z-50"
      >
        💬
      </button>

      {/* Chat Window */}
      {open && (
        <div className="fixed bottom-20 right-6 w-[380px] h-[520px] bg-white dark:bg-gray-900 shadow-2xl rounded-xl flex overflow-hidden z-50">
          <Sidebar />
          <div className="flex flex-col flex-1">
            <ChatWindow messages={messages} />
            <ChatInput setMessages={setMessages} />
          </div>
        </div>
      )}
    </>
  );
}
