import sqlite3

def reset_counters():
    conn = sqlite3.connect('tic_tac_toe.db')
    cursor = conn.cursor()
    
    # Reset win count for both players
    cursor.execute('''
        UPDATE wins
        SET win_count = 0
    ''')
    
    conn.commit()
    conn.close()
    print("Win counters have been reset.")

reset_counters()
