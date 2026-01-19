import React from 'react';
import Header from './Header';
import Sidebar from './Sidebar';
import ThemeSwitcher from '../../../app/ThemeSwitcher';

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="flex h-screen bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100 transition-colors duration-200">
      <Sidebar />
      <div className="flex flex-col flex-1">
        <Header />
        <main className="flex-1 overflow-y-auto p-4">
          {children}
        </main>
      </div>
      <div className="fixed bottom-4 right-4">
        <ThemeSwitcher />
      </div>
    </div>
  );
};

export default Layout;

// Placeholder components for now
const Sidebar: React.FC = () => {
  return (
    <aside className="w-64 bg-white dark:bg-gray-800 shadow-md p-4 flex flex-col justify-between">
      <h2 className="text-2xl font-bold text-blue-600 dark:text-blue-400">Travel Assistant</h2>
      <nav>
        <ul className="space-y-2 mt-4">
          <li><a href="#" className="block px-3 py-2 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700">Flights</a></li>
          <li><a href="#" className="block px-3 py-2 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700">Todos</a></li>
          <li><a href="#" className="block px-3 py-2 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700">Settings</a></li>
        </ul>
      </nav>
      <div className="mt-auto">
        <p className="text-sm text-gray-500 dark:text-gray-400">© 2026 Travel Assistant</p>
      </div>
    </aside>
  );
};

const Header: React.FC = () => {
  return (
    <header className="bg-white dark:bg-gray-800 shadow-sm p-4 flex items-center justify-between">
      <h1 className="text-xl font-semibold">Chat Window</h1>
      {/* Future: User profile/settings */}
    </header>
  );
};
