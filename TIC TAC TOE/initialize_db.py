import sqlite3

def initialize_db():
    conn = sqlite3.connect('tic_tac_toe.db')
    cursor = conn.cursor()
    
    # Create table to store win counts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wins (
            player_id INTEGER PRIMARY KEY,
            win_count INTEGER
        )
    ''')
    
    # Initialize win counts for both players if not already present
    for player_id in [1, 2]:
        cursor.execute('''
            INSERT OR IGNORE INTO wins (player_id, win_count) VALUES (?, ?)
        ''', (player_id, 0))
    
    conn.commit()
    conn.close()

initialize_db()
