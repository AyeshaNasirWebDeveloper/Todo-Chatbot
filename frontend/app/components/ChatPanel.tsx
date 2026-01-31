export default function ChatPanel({ onClose }: any) {
  return (
    <div className="fixed bottom-24 right-6 w-96 h-[500px] bg-white dark:bg-gray-900 rounded-xl shadow-xl flex flex-col">
      <div className="p-3 border-b flex justify-between">
        <span>Todo AI</span>
        <button onClick={onClose}>✖</button>
      </div>

      {/* reuse ChatWindow + ChatInput here */}
    </div>
  );
}
