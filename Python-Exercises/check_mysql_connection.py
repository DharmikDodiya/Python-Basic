import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
)

print("Connected:", conn.is_connected())
conn.close()
