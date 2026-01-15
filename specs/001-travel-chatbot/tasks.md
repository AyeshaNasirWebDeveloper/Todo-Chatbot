# Tasks: AI-Powered Travel Assistant (Todo-Chat) – Phase III Hackathon

**Input**: Design documents from `/specs/001-travel-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/

**Tests**: The specification does not explicitly request test tasks, but testing is implied in the plan's integration & testing phase. Tasks below include implementation and integration, with a dedicated testing phase.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create Phase III project folder structure at /
- [X] T002 Copy Phase II backend + DB + auth files to backend/
- [X] T003 Initialize frontend folder structure for Premium ChatKit UI at frontend/
- [ ] T004 Setup GitHub repository and branch strategy (manual, or if git repo, use git commands)
- [ ] T005 Configure environment variables (NEXT_PUBLIC_OPENAI_DOMAIN_KEY, Backend URL) in .env
- [X] T006 Install required frontend dependencies (Next.js, TailwindCSS, ChatKit SDK) in frontend/
- [X] T007 Install required backend dependencies (FastAPI, SQLModel, MCP SDK, Uvicorn, Pydantic) in backend/ (Note: MCP SDK not found)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T008 Define Task database model using SQLModel in backend/src/models/task.py
- [X] T009 Define Conversation database model using SQLModel in backend/src/models/conversation.py
- [X] T010 Define Message database model using SQLModel in backend/src/models/message.py
- [X] T011 [P] Setup database connection and session management in backend/src/database.py
- [X] T012 Implement basic FastAPI app structure and startup events in backend/src/main.py
- [X] T013 Configure CORS for FastAPI backend in backend/src/main.py
- [X] T014 Implement basic error handling and logging infrastructure in backend/src/utils/error_handlers.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Get Flight Information (Priority: P1) 🎯 MVP

**Goal**: Users can ask the AI chatbot about flight-related queries and get quick information.

**Independent Test**: Interact with the chatbot, ask flight-related questions (e.g., "flights from NYC to LA on next Friday"), and verify the accuracy and relevance of the chatbot's responses using mock data.

### Implementation for User Story 1

- [X] T015 [P] [US1] Define FlightQuery entity parsing logic in backend/src/services/flight_parser.py
- [X] T016 [US1] Implement mock flight data retrieval service in backend/src/services/mock_flight_api.py
- [X] T017 [P] [US1] Define MCP tool 'get_flight_information' in backend/src/mcp_tools/flight_tools.py
- [X] T018 [US1] Integrate 'get_flight_information' tool with chatbot logic in backend/src/services/chatbot_agent.py
- [X] T019 [US1] Implement basic response generation for flight queries in backend/src/services/chatbot_agent.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Manage Todo List Items (Priority: P1)

**Goal**: Users can instruct the AI chatbot to add, delete, list, or prioritize items in their todo list.

**Independent Test**: Issue commands to the chatbot like "add 'pack passport' to my todo list", "delete 'buy milk'", "list my tasks", "prioritize 'book hotel'", and verify that the todo list UI updates correctly and the chatbot provides appropriate confirmations.

### Implementation for User Story 2

- [X] T020 [P] [US2] Implement CRUD operations for TodoItem in backend/src/api/todo.py
- [X] T021 [P] [US2] Define MCP tool 'add_task' in backend/src/mcp_tools/task_tools.py
- [X] T022 [P] [US2] Define MCP tool 'list_tasks' in backend/src/mcp_tools/task_tools.py
- [X] T023 [P] [US2] Define MCP tool 'update_task' in backend/src/mcp_tools/task_tools.py
- [X] T024 [P] [US2] Define MCP tool 'delete_task' in backend/src/mcp_tools/task_tools.py
- [X] T025 [P] [US2] Define MCP tool 'complete_task' in backend/src/mcp_tools/task_tools.py
- [X] T026 [US2] Integrate task management MCP tools with chatbot logic in backend/src/services/chatbot_agent.py
- [X] T027 [US2] Implement response generation for task management in backend/src/services/chatbot_agent.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - General Conversational Interaction (Priority: P2)

**Goal**: Users can engage in general conversation with the AI chatbot, and for it to retain context across multiple turns.

**Independent Test**: Have multi-turn conversations on various topics (e.g., asking about weather, then asking "what about tomorrow?") and observe the chatbot's ability to maintain context and provide coherent responses.

### Implementation for User Story 3

- [X] T028 [P] [US3] Implement ConversationContext management in backend/src/services/conversation_manager.py
- [X] T029 [US3] Configure OpenAI Agents SDK with ChatKit + Gemini key in backend/src/services/chatbot_agent.py
- [X] T030 [US3] Implement core chatbot agent behavior (parse, call tools, respond) in backend/src/services/chatbot_agent.py
- [ ] T031 [P] [US3] Create `/api/{user_id}/chat` endpoint to receive user messages and return AI responses in backend/src/api/chat.py
- [X] T032 [US3] Integrate conversation history into `/api/{user_id}/chat` endpoint for context in backend/src/api/chat.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Frontend – Premium ChatKit UI (Days 7–8)

**Goal**: Implement a modern, responsive chat UI that integrates with the backend chatbot.

**Independent Test**: Visually inspect the UI in a browser across different screen sizes, verify dark/light mode toggle, and interact with the chat to ensure messages are displayed correctly and feedback is integrated.

### Implementation for Frontend UI

- [X] T033 [P] Implement base layout (Sidebar, Header, ThemeSwitcher) in frontend/src/components/layout/
- [X] T034 [P] Implement Chat Window component in frontend/src/components/chat/ChatWindow.tsx
- [X] T035 [P] Implement Chat Input component in frontend/src/components/chat/ChatInput.tsx
- [X] T036 [P] Connect frontend to backend `/api/{user_id}/chat` endpoint in frontend/src/services/chat_api.ts
- [X] T037 [P] Display messages in chat bubbles with user/bot avatars in frontend/src/components/chat/MessageBubble.tsx
- [X] T038 [P] Implement conversation scroll functionality in frontend/src/components/chat/ChatWindow.tsx
- [X] T039 [P] Implement dark/light mode toggle functionality in frontend/src/components/ThemeSwitcher.tsx
- [X] T040 Implement mobile responsiveness for chat interface in frontend/src/styles/globals.css
- [X] T041 Integrate tool call feedback (show confirmation messages) in frontend/src/components/chat/ChatWindow.tsx
- [X] T042 [P] Implement UI polish (animations for messages, smooth transitions) in frontend/src/styles/globals.css

---

## Phase 7: Integration & Testing (Days 9–10)

**Purpose**: Ensure the full system functions correctly, addressing edge cases, and preparing for deployment.

- [X] T043 Full system test: Chatbot + MCP tool interactions
- [X] T044 Full system test: Task management flows
- [X] T045 Full system test: Flight-related query flows
- [X] T046 UI test: Mobile, tablet, desktop responsiveness
- [X] T047 UI test: Dark/light mode toggle
- [X] T048 Edge case test: Empty messages in backend/src/api/chat.py
- [X] T049 Edge case test: Invalid task IDs in backend/src/api/todo.py
- [X] T050 Edge case test: API failures (mock various backend service failures)
- [X] T051 Verify environment variables for deployment in .env
- [X] T052 Remove debug logs from backend/ and frontend/
- [X] T053 Prepare production builds for frontend/ and backend/

---

## Phase 8: Deployment & Demo (Days 11–12)

**Purpose**: Successfully deploy the application and prepare for the hackathon demonstration.

- [ ] T054 Deploy frontend to Vercel
- [ ] T055 Deploy backend to Railway / Render
- [ ] T056 Verify CORS & domain allowlist for ChatKit in backend/src/main.py
- [ ] T057 Record demo video (10+ conversation examples, task management, flight queries)
- [ ] T058 Prepare README (Features, Tech stack, Setup, Screenshots, deployment links) at README.md
- [ ] T059 Final review & submission of project

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tasks marked [P] within a phase can run in parallel.
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all parallel tasks for User Story 1 together:
Task: "Define FlightQuery entity parsing logic in backend/src/services/flight_parser.py"
Task: "Define MCP tool 'get_flight_information' in backend/src/mcp_tools/flight_tools.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Get Flight Information)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Get Flight Information)
   - Developer B: User Story 2 (Manage Todo List Items)
   - Developer C: User Story 3 (General Conversational Interaction)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
