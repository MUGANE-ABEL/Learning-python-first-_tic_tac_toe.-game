import itertools
import random
import sqlite3
from colorama import Fore, Back, Style

def win(current_game):
    def all_same(l):
        return l.count(l[0]) == len(l) and l[0] != 0

    # Horizontal winners
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally(|)!")
            return True

    # Diagonal winners
    diags = [current_game[row][col] for col, row in enumerate(reversed(range(len(current_game))))]
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally(/)!")
        return True

    diags = [current_game[ix][ix] for ix in range(len(current_game))]
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally(\\)!")
        return True

    # Vertical winners
    for col in range(len(current_game)):
        check = [row[col] for row in current_game]
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically(|)!")
            return True

    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied, Choose Another!")
            return game_map, False
        
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
        
        if not just_display:
            game_map[row][column] = player
        
        for count, row in enumerate(game_map):
            colored_row = "".join(
                "   " if item == 0 else (Fore.GREEN + ' X ' + Style.RESET_ALL if item == 1 else Fore.MAGENTA + ' O ' + Style.RESET_ALL)
                for item in row
            )
            print(count, colored_row)
        
        return game_map, True
    
    except IndexError as e:
        print("This number seems to be a bit bigger than the rows/ columns specified:\n Please enter a number within that displayed on the margins...ie\n", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong", e)
        return game_map, False

def get_random_move(game_map):
    empty_positions = [(r, c) for r in range(len(game_map)) for c in range(len(game_map[r])) if game_map[r][c] == 0]
    return random.choice(empty_positions) if empty_positions else None

def update_win_count(player_id):
    conn = sqlite3.connect('tic_tac_toe.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE wins
        SET win_count = win_count + 1
        WHERE player_id = ?
    ''', (player_id,))
    conn.commit()
    conn.close()

def get_win_count(player_id):
    conn = sqlite3.connect('tic_tac_toe.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT win_count
        FROM wins
        WHERE player_id = ?
    ''', (player_id,))
    win_count = cursor.fetchone()
    conn.close()
    return win_count[0] if win_count else 0

def setup_database():
    conn = sqlite3.connect('tic_tac_toe.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wins (
            player_id INTEGER PRIMARY KEY,
            win_count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def play_game_with_computer(game_size):
    game = [[0 for _ in range(game_size)] for _ in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        if current_player == 1:  # Human player
            while not played:
                row_choice = int(input("What row do you want to play? (0,1,2): "))
                column_choice = int(input("What column do you want to play? (0,1,2): "))
                game, played = game_board(game, current_player, row_choice, column_choice)
        else:  # Computer player
            move = get_random_move(game)
            if move:
                row_choice, column_choice = move
                game, played = game_board(game, current_player, row_choice, column_choice)
                print(f"Computer played at ({row_choice}, {column_choice})")

        if win(game):
            print(f"Player {current_player} wins!")
            update_win_count(current_player)
            print(f"Player 1 wins: {get_win_count(1)}")
            print(f"Player 2 wins: {get_win_count(2)}")
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
                return True
            elif again.lower() == "n":
                print("Byeeeeeeeeee")
                return False
            else:
                print("Not a valid answer, so... c u l8trrr aligator")
                return False

def play_game_two_player(game_size):
    game = [[0 for _ in range(game_size)] for _ in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            row_choice = int(input("What row do you want to play? (0,1,2): "))
            column_choice = int(input("What column do you want to play? (0,1,2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            print(f"Player {current_player} wins!")
            update_win_count(current_player)
            print(f"Player 1 wins: {get_win_count(1)}")
            print(f"Player 2 wins: {get_win_count(2)}")
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
                return True
            elif again.lower() == "n":
                print("Byeeeeeeeeee")
                return False
            else:
                print("Not a valid answer, so... c u l8trrr aligator")
                return False

def main():
    setup_database()
    play = True
    while play:
        mode = input("This is a game of tic tac toe:\n                              ===== Info:=====\n *One wins by matching all the characters in a row/column/diagonal ie (-)(|)(/)(\\)\n *A game often is often a square matrix\n *Notice that the row numbers are shown on the margins of the game ie, begining at 0\n\n                 ==================#######==================\n\nChoose game mode: 1 for Player vs Computer, 2 for Two Player: ")
        game_size = int(input("What game size would you like? "))
        if mode == '1':
            play = play_game_with_computer(game_size)
        elif mode == '2':
            play = play_game_two_player(game_size)
        else:
            print("Invalid mode selected. Exiting.")
            play = False

if __name__ == "__main__":
    main()
