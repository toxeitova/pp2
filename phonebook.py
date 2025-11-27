import psycopg2
import csv

def load_config():
    return {
        "host": "localhost",
        "database": "phonebook",
        "user": "postgres",
        "password": "123"
    }

def connect():
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        return conn
    except Exception as e:
        print("Connection error:", e)

def create_table():
    sql = """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        )
    """
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
    print("Table ready ✔")

# INSERT (MANUAL) -------------------------------------------
def insert_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    sql = """INSERT INTO phonebook(first_name, phone)
             VALUES (%s, %s) RETURNING id;"""

    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                print("Inserted ID:", cur.fetchone()[0])
                conn.commit()
    except Exception as e:
        print("Insert error:", e)

def insert_from_csv():
    filename = "phonebook.csv"  # same folder

    sql = """
        INSERT INTO phonebook(first_name, phone)
        VALUES (%s, %s)
        ON CONFLICT(phone) DO NOTHING;
    """

    try:
        with connect() as conn:
            with conn.cursor() as cur:
                with open(filename, "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        cur.execute(sql, (row["first_name"], row["phone"]))
                conn.commit()
                print("CSV imported ✔")
    except Exception as e:
        print("CSV error:", e)

#update
def update_name():
    phone = input("Phone of user: ")
    new_name = input("New name: ")

    sql = "UPDATE phonebook SET first_name = %s WHERE phone = %s"

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (new_name, phone))
            print("Updated rows:", cur.rowcount)
            conn.commit()

def update_phone():
    name = input("Name of user: ")
    new_phone = input("New phone: ")

    sql = "UPDATE phonebook SET phone = %s WHERE first_name = %s"

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (new_phone, name))
            print("Updated rows:", cur.rowcount)
            conn.commit()

#query
def query_all():
    sql = "SELECT * FROM phonebook ORDER BY id"

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            for r in rows:
                print(r)

def query_by_name():
    pattern = input("Enter name: ")
    sql = "SELECT * FROM phonebook WHERE first_name ILIKE %s"

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (f"%{pattern}%",))
            print(cur.fetchall())

def query_by_phone():
    prefix = input("Enter phone prefix: ")
    sql = "SELECT * FROM phonebook WHERE phone LIKE %s"

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (f"{prefix}%",))
            print(cur.fetchall())

#delete
def delete_by_name():
    name = input("Enter name: ")
    sql = "DELETE FROM phonebook WHERE first_name = %s"

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (name,))
            print("Deleted rows:", cur.rowcount)
            conn.commit()

def delete_by_phone():
    phone = input("Enter phone: ")
    sql = "DELETE FROM phonebook WHERE phone = %s"

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (phone,))
            print("Deleted rows:", cur.rowcount)
            conn.commit()
#menu
def menu():
    create_table()

    while True:
        print("""
--- PHONEBOOK MENU ---
1. Insert user (manual)
2. Insert from CSV
3. Update name
4. Update phone
5. Query all
6. Query by name
7. Query by phone
8. Delete by name
9. Delete by phone
0. Exit
""")

        choice = input("Choose: ")

        if choice == "1": insert_user()
        elif choice == "2": insert_from_csv()
        elif choice == "3": update_name()
        elif choice == "4": update_phone()
        elif choice == "5": query_all()
        elif choice == "6": query_by_name()
        elif choice == "7": query_by_phone()
        elif choice == "8": delete_by_name()
        elif choice == "9": delete_by_phone()
        elif choice == "0": break

menu()
