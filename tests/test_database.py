import sqlite3

def check_database():
    conn = sqlite3.connect('/Users/kadaffi/Sergei/TelRan/myproject/mydatabase.db')
    cursor = conn.cursor()
    
    # Проверяем наличие таблицы employees
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employees';")
    table_exists = cursor.fetchone()
    
    if table_exists:
        print("Table 'employees' exists.")
        
        # Проверяем наличие данных в таблице
        cursor.execute("SELECT * FROM employees;")
        rows = cursor.fetchall()
        
        if rows:
            print(f"Found {len(rows)} records in the 'employees' table.")
            for row in rows:
                print(row)
        else:
            print("No records found in the 'employees' table.")
    else:
        print("Table 'employees' does not exist.")
    
    conn.close()

check_database()
