import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="new_database",
        user="postgres",
        password="Anala20070124" 
    )

# === INSERT FROM CONSOLE ===
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    print("Added!")

# === INSERT FROM CSV ===
def insert_from_csv(path):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                with open(path, 'r') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip the header row if it exists
                    for row in reader:
                        if len(row) == 2:  # Ensure the row has two columns
                            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0].strip(), row[1].strip()))
                        else:
                            print(f"Skipping invalid row: {row} (Expected 2 columns)")
                conn.commit()
        print("CSV import successful!")
    except FileNotFoundError:
        print(f"Error: CSV file not found at path: {path}")
    except Exception as e:
        print(f"An error occurred during CSV import: {e}")

# === UPDATE ===
def update_user(name, new_phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    print("Updated!")

# === QUERY ===
def query_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            for row in cur.fetchall():
                print(row)

def query_by_name(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
            print(cur.fetchall())

# === DELETE ===
def delete_user(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    print("Deleted!")


def menu():
    while True:
        print("\n1. Insert (console)")
        print("2. Insert (CSV)")
        print("3. Update user")
        print("4. View all")
        print("5. Querying data by name")
        print("6. Delete user")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("Enter CSV path: "))
        elif choice == '3':
            update_user(input("Name to update: "), input("New phone: "))
        elif choice == '4':
            query_all()
        elif choice == '5':
            query_by_name(input("Name: "))
        elif choice == '6':
            delete_user(input("Name to delete: "))
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
