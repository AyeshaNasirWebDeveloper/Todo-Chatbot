import React from 'react';
import { FaUser, FaRobot } from 'react-icons/fa';

interface Message {
  id: number;
  content: string;
  role: 'user' | 'bot';
  type?: 'text' | 'tool_feedback';
  toolOutput?: any;
}

interface MessageBubbleProps {
  message: Message;
}

const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const isUser = message.role === 'user';
  const bubbleClasses = isUser
    ? 'bg-blue-500 text-white self-end rounded-br-none'
    : 'bg-gray-300 text-gray-900 dark:bg-gray-700 dark:text-gray-100 self-start rounded-bl-none';
  const avatarClasses = isUser
    ? 'ml-2 bg-blue-700 text-white'
    : 'mr-2 bg-gray-500 text-white';

  return (
    <div className={`flex items-end ${isUser ? 'justify-end' : 'justify-start'}`}>
      {!isUser && (
        <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${avatarClasses}`}>
          <FaRobot size={18} />
        </div>
      )}
      <div className={`p-3 rounded-lg max-w-xs md:max-w-md ${bubbleClasses}`}>
        {message.content}
        {message.type === 'tool_feedback' && message.toolOutput && (
          <pre className="mt-2 p-2 bg-gray-200 dark:bg-gray-600 rounded text-xs overflow-x-auto">
            {JSON.stringify(message.toolOutput, null, 2)}
          </pre>
        )}
      </div>
      {isUser && (
        <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${avatarClasses}`}>
          <FaUser size={18} />
        </div>
      )}
    </div>
  );
};

export default MessageBubble;
