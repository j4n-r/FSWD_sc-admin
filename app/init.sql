CREATE TABLE users (
  id  TEXT PRIMARY KEY NOT NULL, -- UUID as TEXT
  email TEXT UNIQUE NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT,
  role TEXT NOT NULL CHECK(role in ('admin', 'user','guest')),
  name TEXT,
  updated_at NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  created_at  TEXT                    NOT NULL DEFAULT (CURRENT_TIMESTAMP)
);

-- We do not store the message type here because it only chat messages will get saved
-- (maybe attachments but these will  be in another table)
CREATE TABLE IF NOT EXISTS messages (
    id                TEXT    PRIMARY KEY   NOT NULL, -- UUID as TEXT
    sender_id         TEXT    NOT NULL
        REFERENCES users(id),
    conversation_id TEXT NOT NULL
        REFERENCES conversations(id) ON DELETE CASCADE,
    content           TEXT    NOT NULL,
    sent_from_client  TEXT    NOT NULL,  -- ISO8601 string
    sent_from_server  TEXT    NOT NULL   -- ISO8601 string
);

-- Groups, one-to-one DMs and small group-DMs
CREATE TABLE conversations (
    id           TEXT PRIMARY KEY NOT NULL,                -- UUID
    owner_id     TEXT                                       
        REFERENCES users(id) ON DELETE SET NULL,
    name         TEXT NOT NULL,
    description  TEXT,
    created_at   TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP),
    updated_at   TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE conversation_members (
    conversation_id TEXT NOT NULL
        REFERENCES conversations(id) ON DELETE CASCADE,
    user_id         TEXT NOT NULL
        REFERENCES users(id) ON DELETE CASCADE,
    role            TEXT NOT NULL DEFAULT 'member',        -- 'owner'/'admin'/…
    joined_at       TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP),
    PRIMARY KEY (conversation_id, user_id)
);

-- ───────────────────────────────────────────────────────────────────
-- Sample users
-- ───────────────────────────────────────────────────────────────────
-- run sc-admin "flask init-db" to create the admin and test user with hashed password

    -- users = [
    --     {
    --         "id": "624f76c7-7b46-4309-8207-126317477e88",
    --         "email": "admin@admin.com",
    --         "username": "admin",
    --         "password": "admin",
    --         "name": "admin",
    --     },
    --     {
    --         "id": "203170c2-e811-44ba-a24f-a1e57d53b363",
    --         "email": "test@test.com",
    --         "username": "test",
    --         "password": "test",
    --         "name": "test",
    --     },

/* ─────────────────────────────────────────────
   CONVERSATIONS
   ───────────────────────────────────────────── */
INSERT INTO conversations (id, owner_id,name, created_at)
VALUES ('c0000000-0000-0000-0000-00000000d001',
         '624f76c7-7b46-4309-8207-126317477e88',
         'Another Group',
         '2025-04-15 09:15:00');

INSERT INTO conversations
        (id,  owner_id, name,  created_at)
VALUES  ('c0000000-0000-0000-0000-00000000g001',
         '624f76c7-7b46-4309-8207-126317477e88',
         'General', '2025-04-15 09:20:00');

/* ─────────────────────────────────────────────
   CONVERSATION MEMBERS
   ───────────────────────────────────────────── */
INSERT INTO conversation_members
        (conversation_id, user_id,  role,   joined_at) VALUES
  -- DM (two members)
  ('c0000000-0000-0000-0000-00000000d001',
   '624f76c7-7b46-4309-8207-126317477e88', 'owner', '2025-04-15 09:15:00'),
  ('c0000000-0000-0000-0000-00000000d001',
   '203170c2-e811-44ba-a24f-a1e57d53b363', 'member', '2025-04-15 09:15:00'),

  -- Group (owner + member)
  ('c0000000-0000-0000-0000-00000000g001',
   '624f76c7-7b46-4309-8207-126317477e88', 'owner',  '2025-04-15 09:20:00'),
  ('c0000000-0000-0000-0000-00000000g001',
   '203170c2-e811-44ba-a24f-a1e57d53b363', 'member', '2025-04-15 09:22:00');

/* ─────────────────────────────────────────────
   MESSAGES  (column order: id, sender_id, conversation_id, 
              content, sent_from_client, sent_from_server)
   ───────────────────────────────────────────── */
INSERT INTO messages
    (id, sender_id,  conversation_id, 
     content, sent_from_client, sent_from_server)
VALUES
    -- DM: admin → test
    ('m1111111-1111-1111-1111-111111111111',
     '624f76c7-7b46-4309-8207-126317477e88',
     'c0000000-0000-0000-0000-00000000d001',
     'Hi test, welcome aboard!',
     '2025-04-15 09:16:00', '2025-04-15 09:16:01'),

    -- DM: test → admin
    ('m2222222-2222-2222-2222-222222222222',
     '203170c2-e811-44ba-a24f-a1e57d53b363',
     'c0000000-0000-0000-0000-00000000d001',
     'Thanks! Glad to join.',
     '2025-04-15 09:17:10', '2025-04-15 09:17:11'),

    -- Group: admin → General
    ('m3333333-3333-3333-3333-333333333333',
     '624f76c7-7b46-4309-8207-126317477e88',
     'c0000000-0000-0000-0000-00000000g001',
     'Stand-up starts in 5 min.',
     '2025-04-15 09:25:00', '2025-04-15 09:25:02');
