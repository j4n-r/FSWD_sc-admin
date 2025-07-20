---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .label }
  * [ ] [Jan Rueggeberg]

{: .no_toc }
# Architecture

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Overview

Team Chat is a web-based real-time messaging application designed for academic environments, specifically enabling professors to manage and moderate student group discussions. The application provides a secure, transparent platform where administrators (professors) have full oversight of all communications while students can participate in organized group chats.

The system consists of two main components:
- **Flask Web Application**: Handles user authentication, web interface, database operations, and REST API endpoints
- **Standalone WebSocket Server**: Manages real-time messaging using Rust for performance

The architecture follows a traditional MVC pattern with Flask blueprints for modularity, SQLite for data persistence, and WebSocket connections for real-time communication. Authentication supports both session-based (web) and JWT-based (API) approaches.

## Codemap

### Core Directory Structure

```
app/
├── __init__.py          # App factory, CORS, JWT setup
├── db.py               # Database connection, queries, CLI commands
├── auth/               # Authentication blueprint
│   ├── routes.py       # Login, register, JWT endpoints
│   └── templates/      # Auth-specific templates
├── main/               # Main application blueprint
│   ├── routes.py       # Chat, user, group management
│   └── templates/      # Main application templates
├── api/                # REST API blueprint
│   └── routes.py       # API endpoints for external access
└── templates/
    └── base.html       # Base template with navigation
```

### Key Components

**Flask Blueprints**:
- `auth_bp` (`/auth/*`): Handles user registration, login, logout, and JWT token management
- `main_bp` (`/`): Core application functionality including chat interface, user management, and group creation
- `api_bp` (`/api/*`): REST API endpoints for external integrations

**Database Layer** (`app/db.py`):
- Simple SQLite database with raw SQL queries (no ORM)
- Connection management with Flask's `g` object
- CLI commands for database initialization and management

**Templates**:
- Jinja2 templating with a base template providing consistent navigation
- Responsive design using Tailwind CSS via CDN
- Role-based UI elements (admin vs regular user views)

## Cross-cutting concerns

### Authentication & Authorization

The application implements a dual authentication system:

1. **Session-based Authentication** (Web Interface):
   - Uses Flask sessions with `@login_required` decorator
   - Stores `user_id`, `username`, and `role` in session
   - Automatic user loading via `@auth_bp.before_app_request`

2. **JWT Authentication** (API Access):
   - Access tokens (1 hour expiry) and refresh tokens (30 days)
   - Used by external clients and the WebSocket server
   - Tokens include user identity and additional claims

**Role-based Access Control**:
- `admin`: Full system access, can manage users and groups
- `user`: Standard access to assigned conversations
- `guest`: Limited access, temporary accounts without passwords

### Real-time Messaging Architecture

Real-time messaging is handled by a separate Rust-based WebSocket server that communicates with the Flask application's database:


**Message Types**:
- `IdMessage`: Establishes user connection to specific conversation
- `ChatMessage`: Actual chat content with metadata

### Database Design Philosophy

The application uses **raw SQL queries** instead of an ORM ([design decision](../design-decisions.md#01-how-to-access-the-database)):

**Benefits**:
- Simple, transparent queries
- No learning overhead for additional frameworks
- Direct control over database operations
- Lightweight for the application's complexity level

**Schema**:
- `users`: User accounts with roles
- `conversations`: Group/chat containers
- `conversation_members`: Many-to-many relationship with roles
- `messages`: All chat messages with timestamps

### Error Handling & Logging

- Comprehensive error handling in all routes with database rollbacks
- Flask logging configured for development and production
- Flash messages for user feedback in web interface
- JSON error responses for API endpoints

### Security Considerations

- Password hashing using Werkzeug's security utilities
- CSRF protection considerations (noted as acceptable risk for admin-only forms)
- Input validation and sanitization
- Role-based route protection
- Secure session management

### Development & Deployment

**Development Tools**:
- `run.sh` script for easy development setup
- Flask CLI commands for database management
- Automatic server restart and cleanup handling

**Dependencies**:
- Minimal Flask application with essential extensions
- External WebSocket server for performance
- Tailwind CSS via CDN for styling

---
Most of this was written by [Claude](https://claude.ai/public/artifacts/23cf8788-a935-4aac-82ce-99cd2e7a878e)
