import sqlite3

conn = sqlite3.connect("Carbon.db")
cmd = conn.cursor()

cmd.execute("""
CREATE TABLE IF NOT EXISTS carbonfootprint
(id INTEGER PRIMARY KEY AUTOINCREMENT,
organization TEXT,
energyusage REAL,
waste REAL,
travel REAL
)
""")

conn.commit()
conn.close()
