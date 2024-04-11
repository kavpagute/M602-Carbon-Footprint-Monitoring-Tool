import sqlite3

conn = sqlite3.connect("Carbon.db")
cmd = conn.cursor()

cmd.execute("""
SELECT * FROM carbonfootprint
""")
print(cmd.fetchall())
conn.close()

