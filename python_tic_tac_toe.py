import itertools


game = [[1,0,2],
        [1,2,0],
        [2,2,1]]




def win(current_game):
    #horizontal winner
    for row in game:
        print (row)
    if row.count(row[0]) == len(row) and row[0] != 0:
            print (f"Player {row[0]} is the winner horizontally!")


    #Diagonal winners
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            print (f"Player {diags[0]} is the winner diagonally(/)!")
        

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            print (f"Player {diags[0]} is the winner diagonally(\\)!")
            #to print s forward slash, eg \, one has to type 2 of them since the first
            #one is often used to overlook a rule eg 
            #showing the apostrophy in ('don\'t')
        
    #Vertical winners
    for col in range(len(game)):
        check= []
        for row in game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print (f"Player {check[0]} is the winner vertically!")


# With errors handled
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print ("   0, 1, 2")
        if not just_display:
            game_map[row][column]= player
        for count, row in enumerate(game_map):        
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: did you input row/column as 0,1,2", e)
    except Exception as e:
        print("Something went very wrong", e) 


play = True
players =[1,2]
while play:
     game = [[0,0,0],
             [0,0,0],
             [0,0,0]]
     
     game_won = False
     game= game_board(game, just_display=True)
     player_choice = itertools.cycle(players)
     while not game_won:
          current_player = next(player_choice) 
          print(f"Current Player: {current_player}")       
          row_choice = int(input("what row do you want to play?(0,1,2): "))
          column_choice = int(input("what column do you want to play?(0,1,2): "))
          game= game_board(game, current_player , row_choice, column_choice) 




#game= game_board(game, just_display=True)
#game= game_board(game_board, player=1, row=3, column=1)




























'''game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(player=0, row=0, column=0, just_display=False):
    print ("   0  1  2")
    if not just_display:
        game[row][column]= player
    for count, row in enumerate(game):
        print(count, row )

game_board(just_display=True)
game_board(1,2,1)
#game[0][1] = 1
#game_board()'''


### Exercise test to see wherther you can,
#by hand calculation,
#predict what running the following codes
#is going to output {it is a test of understanding of indexes and slices}
'''x = 1
def test(): 
    x = 2
test()
print(x) 


x = 1
def test(): 
    global x 
    x = 2 
test() 
print(x)


x = [1] 
def test():
    x = [2]
test()
print(x) 

x = [1] 
def test(): 
    global x 
    x = [2]
test() 
print(x) 

x = [1] 
def test(): 
    x[0] = 2 
test() 
print(x)'''
 




























 