"use client";

import React, { useRef, useEffect } from "react";
import MessageBubble from "./MessageBubble";

interface Message {
  id: number;
  content: string;
  role: "user" | "bot";
  type?: "text" | "tool_feedback";
  toolOutput?: any;
}

interface ChatWindowProps {
  messages?: Message[]; // <-- make optional
}

const ChatWindow: React.FC<ChatWindowProps> = ({ messages = [] }) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="flex-1 p-4 overflow-y-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-inner">
      <div className="flex flex-col space-y-2">
        {messages.map((message) => (
          <MessageBubble key={message.id} message={message} />
        ))}
        <div ref={messagesEndRef} />
      </div>
    </div>
  );
};

export default ChatWindow;
