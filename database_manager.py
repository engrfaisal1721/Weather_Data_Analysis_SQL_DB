


import sqlite3
import os
import datetime


BASE_DIR = os.getcwd()
data_dir = os.path.join(BASE_DIR, "data")
os.makedirs(data_dir, exist_ok=True)
database_path = os.path.join(data_dir, "weather.db")


def create_table():
    conn = sqlite3.connect(database_path)  
    cur = conn.cursor()                    

    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity REAL,
            weather TEXT,
            description TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()  
    conn.close()   


def insert_weather(data):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()
    cur.execute("""
        INSERT INTO weather (city,temperature,humidity,weather,description,timestamp)
        VALUES (?,?,?,?,?,?)
    """, (data["city"], data["temperature"], data["humidity"], data["weather"], data["description"], timestamp))
    conn.commit()
    conn.close()


def update_weather(city, new_temp):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("""
        UPDATE weather
        SET temperature=?
        WHERE city=?
    """, (new_temp, city))
    conn.commit()
    conn.close()


def delete_weather(city):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM weather WHERE city=?", (city,))
    conn.commit()
    conn.close()


def query_all():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM weather")
    rows = cur.fetchall()
    conn.close()
    return rows