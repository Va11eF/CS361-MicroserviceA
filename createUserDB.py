import sqlite3

# Connect to databse
conn = sqlite3.connect('user.db')

# Create a cursor
curr = conn.cursor()
    
curr.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        friends TEXT
    )
''')

curr.execute('''
    CREATE TABLE IF NOT EXISTS achievements (
        id INTEGER PRIMARY KEY,
        username TEXT,
        title TEXT,
        description TEXT
    )
''')

curr.execute('''
    CREATE TABLE IF NOT EXISTS friend_requests (
        sender TEXT,
        receiver TEXT,
        PRIMARY KEY (sender, receiver)
    )
''')

curr.execute('''
    CREATE TABLE IF NOT EXISTS shared_achievements (
        username TEXT,
        achievement_id INTEGER,
        PRIMARY KEY (username, achievement_id)
    )
''')

conn.commit()
conn.close()
print("Database initialized.")


