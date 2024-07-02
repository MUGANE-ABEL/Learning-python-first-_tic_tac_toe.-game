import itertools

#dymnac game size
'''game_size = int(input("What game size of tic tac toe would you like? "))
game = [[0 for i in range(game_size)] for i in range(game_size)]'''





def win(current_game):

    def all_same(l):
         if l.count(l[0]) == len(l) and l[0] != 0:
              return True
         else:
              return False


    #horizontal winner
    for row in game:
        print (row)
    if all_same(row):
            print (f"Player {row[0]} is the winner horizontally!")
            return True


    #Diagonal winners
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
            print (f"Player {diags[0]} is the winner diagonally(/)!")
            return True
        

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
            print (f"Player {diags[0]} is the winner diagonally(\\)!")
            #to print s forward slash, eg \, one has to type 2 of them since the first
            #one is often used to overlook a rule eg 
            #showing the apostrophy in ('don\'t')
            return True
        
    #Vertical winners
    for col in range(len(game)):
        check= []
        for row in game:
            check.append(row[col])

        if all_same(check):
            print (f"Player {check[0]} is the winner vertically(|)!")
            return True
    
    return False


# With errors handled
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
             print("This position is occupied, Choose Another!")
             return game_map, False
        #print ("   0, 1, 2") this line can be written as: below, to make it more dynamic
        #ie, if the game matrix changes
        print ("   "+ "  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column]= player
        for count, row in enumerate(game_map):        
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("Error: did you input row/column as 0,1,2", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong", e) 
        return game_map, False


play = True
players =[1,2]
while play:
     game_size = int(input("What game size of tic tac toe would you like? "))
     game = [[0 for i in range(game_size)] for i in range(game_size)]
     
     game_won = False
     game, _ = game_board(game, just_display=True)
     player_choice = itertools.cycle(players)
     while not game_won:
          current_player = next(player_choice) 
          print(f"Current Player: {current_player}")    
          played= False

          while not played:   
            row_choice = int(input("what row do you want to play?(0,1,2): "))
            column_choice = int(input("what column do you want to play?(0,1,2): "))
            game, played= game_board(game, current_player , row_choice, column_choice)

          if win(game):
               game_won = True
               again = input("The game is over, would you like to play again? (y/n) ")
               if again.lower() == "y":
                    print("restarting")
               elif again.lower() =="n":
                    print ("Byeeeeeeeeee")
                    play= False
               else:
                    print("Not a valid answer, so... c u l8trrr aligator")
                    play = False

            




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
 




























 