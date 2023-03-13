import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="mdrive"
    )
    return connection

def get_transactions():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    cursor.close()
    connection.close()
    return transactions

def add_transaction(description, amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO transactions (description, amount) VALUES (%s, %s)", (description, amount))
    connection.commit()
    cursor.close()
    connection.close()
