"use client";

import { useEffect, useState } from "react";

export default function ThemeSwitcher() {
  const [dark, setDark] = useState(false);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark);
  }, [dark]);

  return (
    <button
      className="w-full py-2 bg-gray-300 dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg shadow"
      onClick={() => setDark(!dark)}
    >
      {dark ? "🌞 Light Mode" : "🌙 Dark Mode"}
    </button>
  );
}
