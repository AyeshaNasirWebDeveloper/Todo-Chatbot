"use client";

import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { getToken, removeToken } from "../utils/token";
import { TaskPublic } from "../services/taskService";
import { getTasks, createTask, updateTask, deleteTask } from "../services/taskService";

const TaskBloomPage: React.FC = () => {
  const router = useRouter();
  const [tasks, setTasks] = useState<TaskPublic[]>([]);
  const [newTask, setNewTask] = useState({
    title: "",
    description: "",
  });
  const [editingTask, setEditingTask] = useState<TaskPublic | null>(null);

  useEffect(() => {
    const token = getToken();
    if (!token) {
      router.push("/login");
      return;
    }
    fetchTasks();
  }, [router]);

  const fetchTasks = async () => {
    try {
      const fetchedTasks = await getTasks();
      setTasks(fetchedTasks);
    } catch (error) {
      console.error("Failed to fetch tasks:", error);
      removeToken();
      router.push("/login");
    }
  };

  const handleCreateTask = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTask.title) {
      alert("Task title required");
      return;
    }

    try {
      await createTask(newTask);
      setNewTask({ title: "", description: "" });
      fetchTasks();
    } catch (error) {
      console.error(error);
      alert("Failed to create task");
    }
  };

  const handleUpdateTask = async (task: TaskPublic) => {
    try {
      await updateTask(task.id, {
        title: task.title,
        description: task.description,
        completed: task.completed,
      });
      setEditingTask(null);
      fetchTasks();
    } catch (error) {
      alert("Update failed");
    }
  };

  const handleDeleteTask = async (id: number) => {
    if (!confirm("Delete this task?")) return;
    await deleteTask(id);
    fetchTasks();
  };

  const handleLogout = () => {
    removeToken();
    router.push("/login");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 to-purple-50 p-6 md:p-12">
      <div className="max-w-5xl mx-auto bg-white shadow-2xl rounded-3xl p-8">

        {/* Header */}
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-extrabold text-indigo-700">
            TaskBloom ✨
          </h1>

          <button
            onClick={handleLogout}
            className="px-5 py-2 bg-red-500 text-white rounded-xl hover:bg-red-600 transition"
          >
            Logout
          </button>
        </div>

        {/* Add Task */}
        <form onSubmit={handleCreateTask} className="grid md:grid-cols-3 gap-4 mb-8">
          <input
            type="text"
            placeholder="Task title"
            className="p-4 border rounded-2xl"
            value={newTask.title}
            onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
          />

          <input
            type="text"
            placeholder="Description"
            className="p-4 border rounded-2xl"
            value={newTask.description}
            onChange={(e) =>
              setNewTask({ ...newTask, description: e.target.value })
            }
          />

          <button className="bg-indigo-600 text-white rounded-2xl font-semibold">
            Add Task
          </button>
        </form>

        {/* Edit Modal */}
        {editingTask && (
          <div className="fixed inset-0 bg-black/40 flex items-center justify-center">
            <div className="bg-white rounded-3xl p-6 w-full max-w-md">
              <h3 className="text-xl font-bold mb-4">Edit Task</h3>

              <input
                className="w-full p-3 border rounded-xl mb-3"
                value={editingTask.title}
                onChange={(e) =>
                  setEditingTask({ ...editingTask, title: e.target.value })
                }
              />

              <textarea
                className="w-full p-3 border rounded-xl mb-3"
                value={editingTask.description || ""}
                onChange={(e) =>
                  setEditingTask({
                    ...editingTask,
                    description: e.target.value,
                  })
                }
              />

              <div className="flex justify-end gap-3">
                <button onClick={() => setEditingTask(null)}>Cancel</button>
                <button
                  onClick={() => handleUpdateTask(editingTask)}
                  className="bg-indigo-600 text-white px-4 py-2 rounded-xl"
                >
                  Save
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Task List */}
        <div className="grid md:grid-cols-2 gap-6">
          {tasks.map((task) => (
            <div
              key={task.id}
              className="p-6 border rounded-3xl shadow hover:shadow-xl transition"
            >
              <h4 className="text-lg font-bold text-indigo-700">
                {task.title}
              </h4>

              <p className="text-gray-600 mt-2">{task.description}</p>

              <div className="flex justify-end gap-3 mt-4">
                <button
                  onClick={() => setEditingTask(task)}
                  className="px-4 py-2 bg-yellow-200 rounded-xl"
                >
                  Edit
                </button>

                <button
                  onClick={() => handleDeleteTask(task.id)}
                  className="px-4 py-2 bg-red-200 rounded-xl"
                >
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default TaskBloomPage;
