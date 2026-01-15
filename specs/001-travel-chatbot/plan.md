# Implementation Plan: AI-Powered Travel Assistant (Todo-Chat) – Phase III Hackathon

**Branch**: `001-travel-chatbot` | **Date**: 2026-01-14 | **Spec**: [specs/001-travel-chatbot/spec.md](specs/001-travel-chatbot/spec.md)
**Input**: Feature specification from `/specs/001-travel-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Extend Phase II's Flight UI and Todo app into a premium AI Chatbot assistant by integrating OpenAI ChatKit (powered by a Gemini API key) with a FastAPI backend and MCP tools. This will deliver a fully functional, modern, and context-aware chatbot while maintaining a clean architecture, modular code, and deployment readiness for the hackathon.

## Technical Context

**Language/Version**: Python (for FastAPI backend), JavaScript/TypeScript (for Next.js frontend)
**Primary Dependencies**:
  - Frontend: Next.js, TailwindCSS, OpenAI ChatKit SDK
  - Backend: FastAPI, SQLModel, MCP SDK, Uvicorn, Pydantic
**Storage**: PostgreSQL (Neon)
**Testing**: Unit tests, Integration tests, Manual testing (as per project constitution)
**Target Platform**: Web application (Frontend deployed on Vercel, Backend on Railway/Render)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: UI and API response times optimized for a smooth user experience; chatbot responds correctly to 95%+ of user queries.
**Constraints**: No external LLMs allowed except ChatKit running via Gemini key; adherence to hackathon timeline; modular code structure; architecture must support future expansion (Phase IV readiness).
**Scale/Scope**: Hackathon project, demonstrating 10+ realistic conversation flows.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **I. User-Centric Design**: The plan prioritizes intuitive UI, smooth transitions, and a modern ChatKit interface for effective user-AI communication.
- [X] **II. Functional Correctness**: The plan details robust implementation for chatbot logic, MCP tool integration, and comprehensive system testing to ensure specified functionality.
- [X] **III. Modularity & Maintainability**: The plan explicitly aims for clean architecture, modular code (routes, components, utils separated), and future expansion readiness.
- [X] **IV. Performance Optimization**: The plan includes UI polish, animations, and smooth transitions, with performance goals for responsive AI and API interactions.
- [X] **V. Security by Design**: The plan addresses environment variable configuration for API keys and input validation within the backend, aligning with secure data handling.

## Project Structure

### Documentation (this feature)

```text
specs/001-travel-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (generated if needed by /sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/           # SQLModel definitions (Task, Conversation, Message)
│   ├── services/         # Business logic, e.g., database interactions
│   ├── api/              # FastAPI endpoints (tasks, chat)
│   └── mcp_tools/        # MCP tool definitions (add_task, list_tasks, etc.)
└── tests/                # Backend unit and integration tests

frontend/
├── src/
│   ├── components/       # Reusable UI components (ChatWindow, ChatInput, ThemeSwitcher)
│   ├── pages/            # Next.js pages (Flight UI, Todo List, integrated Chat)
│   ├── services/         # Frontend API calls, ChatKit integration
│   └── utils/            # Utility functions
└── tests/                # Frontend unit and e2e tests
```

**Structure Decision**: The project will utilize a monorepo-like structure with distinct `backend/` and `frontend/` directories at the repository root, as outlined in Option 2 of the template. This aligns with the Next.js and FastAPI frameworks and promotes clear separation of concerns, modularity, and maintainability.

## Implementation Phases

### Phase 1: Project Setup (Day 1)
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

### Phase 2: Backend – FastAPI + MCP Server (Days 2–4)
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

### Phase 3: OpenAI Agent & GPT Logic (Days 5–6)
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

### Phase 4: Frontend – Premium ChatKit UI (Days 7–8)
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

### Phase 5: Integration & Testing (Days 9–10)
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

### Phase 6: Deployment & Demo (Days 11–12)
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

## Milestones & Deliverables:
- Day 2–4: Backend + MCP tools + DB models completed
- Day 5–6: Agent logic tested and functional
- Day 7–8: Frontend Premium UI implemented
- Day 9–10: Full integration & testing completed
- Day 11–12: Deployment, demo recording, README finalization

## Success Metrics:
- Chatbot responds correctly to 95%+ of user queries
- Task operations confirmed in database and frontend
- UI responsive, modern, and visually appealing
- Deployed project accessible via public URLs
- Judges can evaluate system in under 5 minutes

## Notes:
- Phase II backend continuity ensures full marks are retained
- Focus on **Premium UI + ChatKit integration** to maximize Phase III evaluation
- Keep all commits well-documented for judges review

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |
