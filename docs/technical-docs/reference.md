---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
Jan Rueggebeg
{: .no_toc }

# Reference documentation

{: .attention }
> This page collects internal functions, routes with their functions, and APIs. 

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Home & Navigation

### `home()`

**Route:** `/`\
**Methods:** `GET`\
**Purpose:** Redirect authenticated users to their conversations list. Serves as the main entry point.\
**Sample output:**\
Redirects to `/conversations`

---

## Chat Management

### `chat(id)`

**Route:** `/chat/<string:id>`\
**Methods:** `GET`\
**Purpose:** Display individual chat conversation with all messages. Establishes WebSocket connection for real-time messaging.\
**Sample output:**\
Chat interface showing conversation history with message list and WebSocket connection details.

---

### `conversations()`

**Route:** `/conversations`\
**Methods:** `GET`\
**Purpose:** List all conversations accessible to the current user. Admins see all conversations, regular users see only their own.\
**Sample output:**\
Table/list view of conversations with names, descriptions, and access links.

---

### `conversation(id)`

**Route:** `/conversations/<string:id>`\
**Methods:** `GET`\
**Purpose:** Display detailed view of a specific conversation including member list and roles.\
**Sample output:**\
Conversation details page showing members, their roles (owner/member), and conversation metadata.

---

## Group Management

### `create_conversation()`

**Route:** `/groups/create`\
**Methods:** `GET` `POST`\
**Purpose:** Create new group conversations. GET displays the creation form, POST processes the form submission and creates the group.\
**Sample output:**\
**GET:** Group creation form with user selection checkboxes\
**POST:** Redirects to groups list with success/error flash message

---

### `groups()`

**Route:** `/groups`\
**Methods:** `GET`\
**Purpose:** Display all group conversations. Admin-only view for managing groups.\
**Sample output:**\
Administrative view of all groups with management options.

---

## User Management

### `users()`

**Route:** `/users`\
**Methods:** `GET`\
**Purpose:** Display all users in the system (excluding current user). Admin-only functionality for user management.\
**Sample output:**\
Table view of all users with their details and management options.

---

## Authentication Requirements

**Login Required:** All routes require user authentication via `@login_required` decorator.

**Admin Required:** The following routes require admin role via `@role_required("admin")` decorator:
- `/groups/create`
- `/users`
- `/groups`

## Database Schema References

**Tables Used:**
- `conversations` - Stores group/conversation metadata
- `messages` - Stores individual chat messages
- `users` - User account information
- `conversation_members` - Many-to-many relationship between users and conversations

## WebSocket Integration

The chat functionality integrates with a WebSocket server for real-time messaging. WebSocket URL is configurable via `WS_URL` environment variable (defaults to `ws://0.0.0.0:8080`).

## Session Management

Routes utilize Flask session management for:
- `user_id` - Current user identification
- `role` - User role (admin/regular user)

## Authentication & Token Management

### `register()`

**Route:** `/register`\
**Methods:** `GET` `POST`\
**Purpose:** User registration with email, username, and password. Creates new user account with 'user' role.\
**Sample output:**\
**GET:** Registration form\
**POST:** Success redirect to login or error flash message

---

### `login()`

**Route:** `/login`\
**Methods:** `GET` `POST`\
**Purpose:** Session-based user authentication. Validates credentials and establishes user session.\
**Sample output:**\
**GET:** Login form\
**POST:** Redirect to home page on success or error message on failure

---

### `guest()`

**Route:** `/guest`\
**Methods:** `GET` `POST`\
**Purpose:** Guest user registration without password. Creates temporary guest account with limited privileges.\
**Sample output:**\
**GET:** Guest registration form\
**POST:** Automatic login and redirect to home page

---

### `logout()`

**Route:** `/logout`\
**Methods:** `GET`\
**Purpose:** Clear user session and redirect to login page.\
**Sample output:**\
Redirect to `/auth/login`

---

### `token()`

**Route:** `/token`\
**Methods:** `GET` `POST` `OPTIONS`\
**Purpose:** JWT token generation for API authentication. Returns access and refresh tokens.\
**Sample output:**

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

---

### `refresh()`

**Route:** `/refresh`\
**Methods:** `POST`\
**Headers:** `Authorization: Bearer <your_refresh_token>`\
**Purpose:** Generate new access token using valid refresh token.\
**Sample output:**

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

---

### `check()`

**Route:** `/check`\
**Methods:** `GET`\
**Purpose:** Verify JWT token validity and return authentication status.\
**Sample output:**

```json
{
  "authenticated": true,
  "message": "User is authenticated",
  "user": "624f76c7-7b46-4309-8207-126317477e88"
}
```

---

## API Endpoints

### `getUserConversations(user_id)`

**Route:** `/user/<string:user_id>/conversations`\
**Methods:** `GET`\
**Purpose:** Retrieve all conversations for a specific user. JWT authentication required.\
**Sample output:**

```json
{
  "conversations": [
    {
      "conversation_id": "c0000000-0000-0000-0000-00000000d001",
      "created_at": "2025-04-15 09:15:00",
      "description": null,
      "id": "c0000000-0000-0000-0000-00000000d001",
      "joined_at": "2025-04-15 09:15:00",
      "name": "Another Group",
      "owner_id": "624f76c7-7b46-4309-8207-126317477e88",
      "role": "owner",
      "updated_at": "2025-06-22 17:22:55",
      "user_id": "624f76c7-7b46-4309-8207-126317477e88"
    },
    {
      "conversation_id": "c0000000-0000-0000-0000-00000000g001",
      "created_at": "2025-04-15 09:20:00",
      "description": null,
      "id": "c0000000-0000-0000-0000-00000000g001",
      "joined_at": "2025-04-15 09:20:00",
      "name": "General",
      "owner_id": "624f76c7-7b46-4309-8207-126317477e88",
      "role": "owner",
      "updated_at": "2025-06-22 17:22:55",
      "user_id": "624f76c7-7b46-4309-8207-126317477e88"
    }
  ]
}
```

---

### `getMessages(conv_id)`

**Route:** `/conversation/<string:conv_id>/messages`\
**Methods:** `GET`\
**Purpose:** Fetch all messages from a specific conversation. JWT authentication required.\
**Sample output:**

```json
{
  "messages": [
    {
      "content": "Hi test, welcome aboard!",
      "conversation_id": "c0000000-0000-0000-0000-00000000d001",
      "id": "m1111111-1111-1111-1111-111111111111",
      "sender_id": "624f76c7-7b46-4309-8207-126317477e88",
      "sent_from_client": "2025-04-15 09:16:00",
      "sent_from_server": "2025-04-15 09:16:01"
    },
    {
      "content": "Thanks! Glad to join.",
      "conversation_id": "c0000000-0000-0000-0000-00000000d001",
      "id": "m2222222-2222-2222-2222-222222222222",
      "sender_id": "203170c2-e811-44ba-a24f-a1e57d53b363",
      "sent_from_client": "2025-04-15 09:17:10",
      "sent_from_server": "2025-04-15 09:17:11"
    }
  ]
}
```

---

### `getConversation(conv_id)`

**Route:** `/conversation/<string:conv_id>`\
**Methods:** `GET`\
**Purpose:** Get detailed information about a specific conversation. JWT authentication required.\
**Sample output:**

```json
{
  "messages": {
    "created_at": "2025-04-15 09:15:00",
    "description": null,
    "id": "c0000000-0000-0000-0000-00000000d001",
    "name": "Another Group",
    "owner_id": "624f76c7-7b46-4309-8207-126317477e88",
    "updated_at": "2025-06-22 17:22:55"
  }
}
```

---

## Authentication Methods

**Session-Based Authentication:**\
- Web routes use Flask sessions with `@login_required` decorator
- Session stores: `user_id`, `username`, `role`

**JWT Authentication:**\
- API routes use JWT tokens with `@jwt_required()` decorator
- Tokens include user identity and additional claims
- Access tokens expire, refresh tokens allow renewal

## User Roles

- **admin** - Full system access, can manage users and groups
- **user** - Standard user with conversation access
- **guest** - Limited access, temporary accounts

## Error Handling

All routes include comprehensive error handling with appropriate HTTP status codes, flash messages for web forms, and JSON responses for API endpoints. Database transactions include rollback on failures.

---

*Written by [Claude](https://claude.ai/public/artifacts/1b2cf0bc-5edc-48ef-8ce9-7b2437d7e708)*
