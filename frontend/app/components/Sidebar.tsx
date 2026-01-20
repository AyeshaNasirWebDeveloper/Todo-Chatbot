"use client";

import { useState } from "react";
import ThemeSwitcher from "./ThemeSwitcher";

export default function Sidebar() {
  const [activeTab, setActiveTab] = useState("chat");

  return (
    <div className="w-64 bg-white dark:bg-gray-800 shadow-xl p-6 flex flex-col justify-between">
      <div>
        <h1 className="text-2xl font-bold text-gray-800 dark:text-white mb-6">
          Todo <span className="text-blue-600">AI</span>
        </h1>

        <div className="space-y-3">
          <button
            className={`w-full px-3 py-2 text-left rounded-lg transition ${
              activeTab === "chat"
                ? "bg-blue-600 text-white shadow"
                : "text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700"
            }`}
            onClick={() => setActiveTab("chat")}
          >
            💬 Chat
          </button>

          <button
            className={`w-full px-3 py-2 text-left rounded-lg transition ${
              activeTab === "tasks"
                ? "bg-blue-600 text-white shadow"
                : "text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700"
            }`}
          >
            ✅ Tasks
          </button>
        </div>
      </div>

      <div className="mt-10">
        <ThemeSwitcher />
      </div>
    </div>
  );
}
