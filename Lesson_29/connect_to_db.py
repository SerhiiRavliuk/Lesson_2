
import time
import psycopg2

def connect_db():
    for _ in range(5):
        try:
            conn = psycopg2.connect(
                dbname='my_test_db',
                user='serhiiravliuk',
                password='kabosina2517',
                host='postgres',
                port='5432'
            )
            return conn
        except psycopg2.OperationalError:
            time.sleep(2)
    raise Exception("Не вдалося підключитися до бази даних після кількох спроб.")



def create_table(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
        """)
        conn.commit()

def insert_item(conn, name):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
        conn.commit()

def update_item(conn, item_id, new_name):
    with conn.cursor() as cursor:
        cursor.execute("UPDATE items SET name = %s WHERE id = %s", (new_name, item_id))
        conn.commit()

def delete_item(conn, item_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
        conn.commit()

def select_items(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM items;")
        return cursor.fetchall()
