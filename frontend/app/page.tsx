"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import ChatWidget from "./components/ChatWidget";

export default function HomePage() {
  const [userName, setUserName] = useState<string | null>(null);

  useEffect(() => {
  const loadUser = () => {
    setUserName(localStorage.getItem("user_name"));
  };

  loadUser();
  window.addEventListener("storage", loadUser);

  return () => window.removeEventListener("storage", loadUser);
}, []);

  const logout = () => {
    localStorage.clear();
    window.location.reload();
  };
  return (
    <main className="min-h-screen bg-white dark:bg-gray-900">
      {/* WEBSITE CONTENT */}
      {/* HEADER */}
      <header className="w-full bg-white/80 backdrop-blur shadow sticky top-0 z-50 transition">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <h1 className="text-3xl font-extrabold text-indigo-700 animate-fadeIn">
            TaskBloom ✨
          </h1>

          <div className="flex gap-4 items-center">
            {userName ? (
              <>
                <p className="font-medium text-gray-700 animate-slideIn">
                  👋 {userName}
                </p>

                <button
                  onClick={logout}
                  className="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 transition"
                >
                  Logout
                </button>
              </>
            ) : (
              <>
                <Link
                  href="/login"
                  className="hover:text-indigo-700 font-medium"
                >
                  Login
                </Link>
                <Link
                  href="/signup"
                  className="px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700"
                >
                  Sign Up
                </Link>
              </>
            )}
          </div>
        </div>
      </header>

      {/* HERO WITH FULL BANNER */}
      <section className="text-center py-24 bg-gradient-to-br from-indigo-50 to-purple-50">
        <h2 className="text-5xl font-extrabold text-gray-800 animate-fadeIn">
          Organize your life beautifully
        </h2>

        <p className="text-gray-600 mt-4 text-lg">
          Manage tasks with AI assistance
        </p>

        <Link
          href="/tasks"
          className="inline-block mt-8 px-8 py-4 bg-indigo-600 text-white rounded-xl shadow-lg hover:scale-105 transition"
        >
          Open My Tasks
        </Link>
      </section>

      {/* FOOTER */}
      <footer className="bg-indigo-700 text-white py-10 ">
        <p className="text-center text-gray-200 mt-10">
          Ayesha Nasir ❤️ © 2026 TaskBloom — All Rights Reserved.
        </p>
      </footer>

      {/* ANIMATIONS */}
      <style>
        {`
          .animate-fadeIn {
    animation: fadeIn 0.7s ease-in-out;
  }

  .animate-slideIn {
    animation: slideIn 0.6s ease-in-out;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes slideIn {
    from { opacity: 0; transform: translateX(20px); }
    to { opacity: 1; transform: translateX(0); }
  }
        `}
      </style>

      {/* CHATBOT WIDGET */}
      <ChatWidget />
    </main>
  );
}
