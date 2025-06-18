# Admin Guide

The admin panel currently consists of a single endpoint providing statistics.

## `GET /admin/status`

Returns a JSON object with the number of stored conversations and registered users.
This data is collected from the episodic memory JSONL file and the user database
file. Both paths can be customised via environment variables `MEMORY_PATH` and
`USER_DB`.

Example response:
```json
{
  "conversations": 12,
  "users": 3
}
```
