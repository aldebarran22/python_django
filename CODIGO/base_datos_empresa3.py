import sqlite3

con = sqlite3.connect("empresa3.db")
cur = con.cursor()
sql = "select * from productos"
cur.execute(sql)
for t in cur.fetchall():
	print(t)
cur.close()
con.close()
