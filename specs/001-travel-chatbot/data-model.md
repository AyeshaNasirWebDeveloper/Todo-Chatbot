# Data Model: AI-Powered Travel Assistant (Todo-Chat) – Phase III Hackathon

## Entities

### FlightQuery
Represents a user's intent to find flight information.
- **Attributes:**
    - `origin`: string (e.g., "New York", "NYC")
    - `destination`: string (e.g., "London", "LHR")
    - `departureDate`: date (e.g., "2026-03-15")
    - `returnDate`: date (optional)
    - `airline`: string (optional, e.g., "United", "UA")
    - `passengers`: integer (optional, default 1)
- **Relationships:** None specified (independent entity for chatbot parsing)

### TodoItem
Represents a single task in the user's todo list.
- **Attributes:**
    - `id`: UUID (unique identifier)
    - `description`: string (the task itself, e.g., "pack passport")
    - `status`: string (e.g., "pending", "in_progress", "completed")
    - `priority`: string (optional, e.g., "high", "medium", "low")
    - `userId`: UUID (foreign key, links to user who owns the task)
- **Relationships:** Belongs to a User.

### ConversationContext
Stores the history and relevant information of an ongoing chat session to enable context-aware responses.
- **Attributes:**
    - `sessionId`: UUID (unique identifier for the conversation)
    - `userId`: UUID (foreign key, links to the user participating)
    - `history`: array of objects (each object represents a message with `role` and `content`)
    - `lastActivity`: datetime (timestamp of the last message)
- **Relationships:** Belongs to a User, contains Messages.
