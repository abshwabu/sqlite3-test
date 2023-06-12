import sqlite3

db = sqlite3.connect('inventory.db')

cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTIGER,price REAL)")
cur.execute("INSERT INTO store VALUES('book',10,15.50)")
db.commit()
db.close()