import sqlite3

conn = sqlite3.connect("fx_rates.db")
cursor = conn.cursor()

query = "SELECT * FROM observations"

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

query = "SELECT * FROM series"

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the database connection
conn.close()
