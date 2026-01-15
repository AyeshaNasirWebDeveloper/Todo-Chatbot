export default function ChatMessage({ role, content }: any) {
  const isUser = role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-[70%] px-4 py-3 rounded-2xl shadow text-sm ${
          isUser
            ? "bg-blue-600 text-white rounded-br-none"
            : "bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 rounded-bl-none"
        }`}
      >
        {content}
      </div>
    </div>
  );
}
