-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  emailVerified BOOLEAN ,
  name TEXT,
  image TEXT,
  created_at INTEGER,
  updated_at INTEGER
);


