---
id: PHR-0007
title: Create AI Travel Assistant Implementation Plan
stage: plan
date: 2026-01-14
surface: agent
model: claude-sonnet-4-5-20251101
feature: 001-travel-chatbot
branch: none
user: Ayesha Nasir
command: /sp.plan
labels: ["plan", "implementation", "travel-chatbot", "hackathon"]
links:
  spec: specs/001-travel-chatbot/spec.md
  plan: specs/001-travel-chatbot/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-travel-chatbot/plan.md
  - specs/001-travel-chatbot/data-model.md
  - specs/001-travel-chatbot/contracts/chatbot_api.yaml
tests:
  - none
---

## Prompt

```text
AI-Powered Travel Assistant (Todo-Chat) – Phase III Hackathon

Objective:
- Extend Phase II Flight UI + Todo app into a Premium AI Chatbot assistant
- Integrate OpenAI ChatKit (Gemini API key) with backend FastAPI + MCP tools
- Deliver a fully functional, modern, and context-aware chatbot
- Maintain clean architecture, modular code, and deployment readiness

---

Phase 1: Project Setup (Day 1)
- Create new Phase III project folder: todo-chat
- Copy Phase II backend + DB + auth files
- Initialize frontend folder structure for Premium ChatKit UI
- Setup GitHub repository and branch strategy
- Configure environment variables:
  - NEXT_PUBLIC_OPENAI_DOMAIN_KEY
  - Backend URL
- Install required dependencies:
  - Frontend: Next.js, TailwindCSS, ChatKit SDK
  - Backend: FastAPI, SQLModel, MCP SDK, Uvicorn, Pydantic

---

Phase 2: Backend – FastAPI + MCP Server (Days 2–4)
- Define database models (Task, Conversation, Message) using SQLModel
- Implement CRUD endpoints for tasks:
  - Add, List, Update, Delete, Complete
- Setup MCP server:
  - Define tools: add_task, list_tasks, update_task, delete_task, complete_task
  - Ensure stateless tool design with DB persistence
- Create `/api/{user_id}/chat` endpoint:
  - Receives user message
  - Fetches conversation history
  - Passes messages to OpenAI Agent (ChatKit via Gemini)
  - Records tool calls and responses in DB
- Error handling and validation:
  - Task not found
  - Invalid inputs
  - Conversation continuity

---

Phase 3: OpenAI Agent & GPT Logic (Days 5–6)
- Configure OpenAI Agents SDK with ChatKit + Gemini key
- Implement Agent behavior:
  - Parse natural language commands
  - Call appropriate MCP tools
  - Maintain conversational context
  - Respond with confirmations
- Testing Agent:
  - Verify proper handling of task creation, updates, deletion, completion
  - Mock flight-related queries and ensure coherent responses
- Log all tool calls for auditability

---

Phase 4: Frontend – Premium ChatKit UI (Days 7–8)
- Implement layout:
  - Sidebar, Chat Window, Chat Input, Header, ThemeSwitcher
- Connect frontend to backend `/api/{user_id}/chat`
- Display messages in chat bubbles with user/bot avatars
- Implement conversation scroll, dark/light mode, mobile responsiveness
- Integrate tool call feedback (show confirmation messages in chat)
- UI polish:
  - Animations for messages
  - Smooth transitions for sending/receiving messages
  - Consistent color scheme with Phase II branding

---

Phase 5: Integration & Testing (Days 9–10)
- Full system test:
  - Chatbot + MCP tool interactions
  - Task management flows
  - Flight-related query flows
- UI test:
  - Mobile, tablet, desktop responsiveness
  - Dark/light mode toggle
- Edge cases:
  - Empty messages
  - Invalid task IDs
  - API failures
- Deployment readiness:
  - Verify environment variables
  - Remove debug logs
  - Prepare production builds

---

Phase 6: Deployment & Demo (Days 11–12)
- Deploy frontend: Vercel
- Deploy backend: Railway / Render
- Verify CORS & domain allowlist for ChatKit
- Record demo video:
  - 10+ conversation examples
  - Task creation, update, delete, completion
  - Flight-related queries
- Prepare README:
  - Features
  - Tech stack
  - Setup instructions
  - Screenshots & deployment links
- Final review & submission

---

Milestones & Deliverables:
- Day 2–4: Backend + MCP tools + DB models completed
- Day 5–6: Agent logic tested and functional
- Day 7–8: Frontend Premium UI implemented
- Day 9–10: Full integration & testing completed
- Day 11–12: Deployment, demo recording, README finalization

---

Success Metrics:
- Chatbot responds correctly to 95%+ of user queries
- Task operations confirmed in database and frontend
- UI responsive, modern, and visually appealing
- Deployed project accessible via public URLs
- Judges can evaluate system in under 5 minutes

---

Notes:
- Phase II backend continuity ensures full marks are retained
- Focus on **Premium UI + ChatKit integration** to maximize Phase III evaluation
- Keep all commits well-documented for judges review
```

## Response snapshot

The implementation plan for the AI-Powered Travel Assistant (Phase III Hackathon) has been generated and saved to `specs/001-travel-chatbot/plan.md`. Data model and API contracts have also been created.

## Outcome

- ✅ Impact: A detailed implementation plan for Phase III of the AI Travel Assistant was generated, integrating user-provided phases with technical context, constitution checks, data model, and API contracts.
- 🧪 Tests: none
- 📁 Files: `specs/001-travel-chatbot/plan.md`, `specs/001-travel-chatbot/data-model.md`, `specs/001-travel-chatbot/contracts/chatbot_api.yaml` were created.
- 🔁 Next prompts: Next steps could involve generating tasks using `/sp.tasks` or starting implementation based on the plan.
- 🧠 Reflection: The process successfully integrated a comprehensive user-provided plan into the structured plan template, validating against the constitution and generating initial design artifacts. The `setup-plan.ps1` and `update-agent-context.ps1` scripts had issues with feature directory detection in a non-git repo, which required manual path handling for plan, data model, and contracts.

## Evaluation notes (flywheel)

- Failure modes observed: The `setup-plan.ps1` and `update-agent-context.ps1` scripts did not correctly identify the feature directory in a non-git repository, leading to incorrect file paths being generated by the setup script and incorrect context parsing by the update script. This required manual override of file paths for writing the plan and related artifacts.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Improve the `setup-plan.ps1` and `update-agent-context.ps1` scripts to robustly handle non-git repositories and ensure correct feature directory identification, potentially by accepting explicit feature number and short name parameters.
