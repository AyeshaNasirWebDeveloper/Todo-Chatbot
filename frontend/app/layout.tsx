import "./globals.css";
import { Toaster } from "react-hot-toast";

export const metadata = {
  title: "Todo AI Chatbot",
  description: "Premium AI-powered Todo chatbot built with ChatKit & MCP",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="bg-gray-100 dark:bg-gray-900 transition-all">{children}<Toaster position="top-right" /></body>
    </html>
  );
}
