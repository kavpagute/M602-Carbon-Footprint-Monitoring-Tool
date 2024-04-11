import sqlite3

conn = sqlite3.connect("Carbon.db")
cmd = conn.cursor()

cmd.execute("""
insert into carbonfootprint(organization,
energyusage,
waste,
travel) VALUES("GOOGLE",440.23,244.44,1002.11)
""")

conn.commit()
conn.close()
