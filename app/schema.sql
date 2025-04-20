-- DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id  PRIMARY KEY NOT NULL, -- UUID as TEXT
  email TEXT UNIQUE NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  emailVerified BOOLEAN ,
  name TEXT,
  image TEXT,
  updated_at NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  created_at  TEXT                    NOT NULL DEFAULT (CURRENT_TIMESTAMP)
);
