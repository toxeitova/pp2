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
    print("Table ready")

def search_by_pattern():
    pattern = input("Enter pattern (name/phone part): ")
    sql = """
        SELECT * FROM phonebook
        WHERE first_name ILIKE %s OR phone LIKE %s
        ORDER BY id
    """
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (f"%{pattern}%", f"%{pattern}%"))
            rows = cur.fetchall()
            print("Search results:")
            for r in rows:
                print(r)


def upsert_user():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()

    with connect() as conn:
        with conn.cursor() as cur:
            # check if exists
            cur.execute("SELECT id FROM phonebook WHERE first_name = %s", (name,))
            result = cur.fetchone()

            if result:
                cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s",
                            (phone, name))
                print("User existed → phone updated")
            else:
                cur.execute("INSERT INTO phonebook(first_name, phone) VALUES (%s, %s)",
                            (name, phone))
                print("New user inserted")

            conn.commit()


def insert_many_users():
    print("Enter users (name, phone). Empty line to stop.")
    invalid = []

    with connect() as conn:
        with conn.cursor() as cur:

            while True:
                line = input("> ").strip()
                if line == "":
                    break

                try:
                    name, phone = [x.strip() for x in line.split(",")]
                except:
                    print("Format: name, phone")
                    continue

                # validate phone only digits
                if not phone.isdigit():
                    invalid.append((name, phone))
                    continue

                try:
                    cur.execute("INSERT INTO phonebook(first_name, phone) VALUES (%s, %s)",
                                (name, phone))
                except psycopg2.errors.UniqueViolation:
                    conn.rollback()
                    print(f"{name} already exists → skipped")
                    continue

                conn.commit()

    if invalid:
        print("Invalid phone numbers:")
        for x in invalid:
            print(x)
    else:
        print("All inserted successfully!")


def pagination():
    try:
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
    except:
        print("Limit and offset must be numbers")
        return

    sql = """
        SELECT * FROM phonebook
        ORDER BY id
        LIMIT %s OFFSET %s
    """

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (limit, offset))
            rows = cur.fetchall()
            print("Page results:")
            for r in rows:
                print(r)


def insert_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    sql = "INSERT INTO phonebook(first_name, phone) VALUES (%s, %s) RETURNING id"

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (name, phone))
            print("Inserted ID:", cur.fetchone()[0])
            conn.commit()


def insert_from_csv():
    filename = "phonebook.csv"
    sql = """
        INSERT INTO phonebook(first_name, phone)
        VALUES (%s, %s)
        ON CONFLICT(phone) DO NOTHING;
    """
    with connect() as conn:
        with conn.cursor() as cur:
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cur.execute(sql, (row["first_name"], row["phone"]))
            conn.commit()
    print("CSV imported")


def update_name():
    phone = input("Phone of user: ")
    new_name = input("New name: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s",
                        (new_name, phone))
            conn.commit()
            print("Updated rows:", cur.rowcount)


def update_phone():
    name = input("Name of user: ")
    new_phone = input("New phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s",
                        (new_phone, name))
            conn.commit()
            print("Updated rows:", cur.rowcount)


def query_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook ORDER BY id")
            for r in cur.fetchall():
                print(r)


def query_by_name():
    pattern = input("Enter name: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s",
                        (f"%{pattern}%",))
            print(cur.fetchall())


def query_by_phone():
    prefix = input("Enter phone prefix: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s",
                        (f"{prefix}%",))
            print(cur.fetchall())


def delete_by_name():
    name = input("Enter name: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
            conn.commit()
            print("Deleted rows:", cur.rowcount)


def delete_by_phone():
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
            conn.commit()
            print("Deleted rows:", cur.rowcount)


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
10. Search by pattern
11. Upsert user (insert or update) 
12. Insert many users with validation 
13. Pagination 
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
        elif choice == "10": search_by_pattern()
        elif choice == "11": upsert_user()
        elif choice == "12": insert_many_users()
        elif choice == "13": pagination()
        elif choice == "0": break

menu()

