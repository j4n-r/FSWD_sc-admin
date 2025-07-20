---
title: Data Model
parent: Technical Docs
nav_order: 2
---

{: .label }
Jan Rueggebeg

{: .no_toc }
# Data model

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Database model
Simple and self exploratory data model. \
We got `users`, who are "assigned" to `conversations` through the `conversation_members` table. And one `messages` table for all messages which were sent in conversations by users.

![data-model-chartdb](https://github.com/user-attachments/assets/82ca4feb-b3b0-4020-a0c6-3eb092886693)

## WebSocket messages
The messages that are sent are different then the ones that are saved in the database.

### Identification message
The IdMessage gets send every time a user enters a chat. The ws server will add the user and the connection to the connection pool.
```json
{
   "message_type":"IdMessage",
   "sender_id":"624f76c7-7b46-4309-8207-126317477e88",
   "conv_id":"c0000000-0000-0000-0000-00000000d001",
   "timestamp":"2025-06-22T16:38:23.964Z"
}
```

### Chat message
This is the actual message that gets send over the wire.
```json
{
   "message_type":"ChatMessage",
   "payload":{
      "content":"Hiiii, any blockers today?",
      "display_name":"admin"
   },
   "meta":{
      "conversation_id":"c0000000-0000-0000-0000-00000000d001",
      "sender_id":"624f76c7-7b46-4309-8207-126317477e88",
      "timestamp":"2025-06-22T16:38:58.548Z"
   }
}
```
