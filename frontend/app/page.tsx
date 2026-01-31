"use client";

import ChatWidget from "./components/ChatWidget";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-white dark:bg-gray-900">
      {/* WEBSITE CONTENT */}
      <section className="p-10">
        <h1 className="text-4xl font-bold">Welcome to Todo AI 🚀</h1>
        <p className="mt-4 text-gray-600 dark:text-gray-300">
          Manage tasks, chat with AI, and get flight info — all in one place.
        </p>
      </section>

      {/* CHATBOT WIDGET */}
      <ChatWidget />
    </main>
  );
}
