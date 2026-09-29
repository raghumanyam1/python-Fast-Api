import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="restaurant_management"
)

print("Database connected successfully!")