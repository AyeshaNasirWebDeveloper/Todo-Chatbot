"use client";

import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";

export default function HomePage() {
  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <Sidebar />

      {/* Chat window */}
      <div className="flex flex-col flex-1">
        <ChatWindow />
      </div>
    </div>
  );
}
