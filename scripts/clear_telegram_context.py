#!/usr/bin/env python3
"""Clear Telegram context: delete the active Telegram session + its messages
so the next user message starts a fresh context (memory + skills persist).
Keeps session_model_usage rows (cost ledger integrity)."""
import os, sqlite3

DB = os.path.expanduser("~/AppData/Local/hermes/state.db")
CHAT = "8862780676"

db = sqlite3.connect(DB)
cur = db.cursor()
rows = cur.execute(
    "SELECT id, message_count FROM sessions WHERE source='telegram' AND chat_id=? ORDER BY last_activity_at DESC",
    (CHAT,)).fetchall()
for sid, mc in rows:
    cur.execute("DELETE FROM messages WHERE session_id=?", (sid,))
    cur.execute("DELETE FROM sessions WHERE id=?", (sid,))
    print("cleared session", sid, "(", mc, "messages )")
try:
    cur.execute("INSERT INTO messages_fts(messages_fts) VALUES('rebuild')")
except Exception as e:
    print("fts rebuild note:", e)
db.commit()
db.close()
print("telegram context cleared")
