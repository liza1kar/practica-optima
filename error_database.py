import sqlite3

def save_errors(errors):
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS errors (id INTEGER PRIMARY KEY AUTOINCREMENT, error_message TEXT)"
    )

    for error in errors:
        cursor.execute("INSERT INTO errors (error_message) VALUES (?)", (error,))
    
    conn.commit()
    conn.close()