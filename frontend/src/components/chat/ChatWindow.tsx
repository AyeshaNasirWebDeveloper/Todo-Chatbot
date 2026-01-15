import React, { useRef, useEffect } from 'react';
import MessageBubble from './MessageBubble';

interface Message {
  id: number;
  content: string;
  role: 'user' | 'bot';
  type?: 'text' | 'tool_feedback'; // Add message type
  toolOutput?: any; // To display tool specific output if needed
}

interface ChatWindowProps {
  messages: Message[];
}

const ChatWindow: React.FC<ChatWindowProps> = ({ messages }) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
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
