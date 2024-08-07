import sqlite3

def create_connection():
    connection = sqlite3.connect('home_food.db')
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        cpf TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')
    
    connection.commit()
    connection.close()

def insert_user(username, email, phone, cpf, password):
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('''INSERT INTO users (username, email, phone, cpf, password) 
                      VALUES (?, ?, ?, ?, ?)''', (username, email, phone, cpf, password))
    
    connection.commit()
    connection.close()

def get_user(email, password):
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()
    
    connection.close()
    return user

create_table()
