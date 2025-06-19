# Backend API

The backend provides a minimal REST API built with Flask. It exposes the following routes:

## `POST /chat`
Send a message to the assistant and receive a reply.

**Body JSON**:
```json
{
  "message": "<user question>",
  "docs_path": "/optional/path/to/documents"
}
```

If `docs_path` is supplied, files found at the path will be loaded via the RAG loader and appended to the conversation.

**Response**:
```json
{ "reply": "<assistant response>" }
```
The request must include a token obtained from `/auth/login` in the
`Authorization` header.

## `POST /auth/register`
Register a new user. Body JSON must contain `username` and `password` fields.

## `POST /auth/login`
Login with previously registered credentials.

## `GET /admin/status`
Return counts of stored conversations and registered users.
