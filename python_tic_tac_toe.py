game = [[2,0,1],
        [2,0,0],
        [2 ,2,0]]




 





















#horizontal winner

'''def win(current_game):
    for row in game:
        print (row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print ("winner!!!")
win(game)'''


#Vertical winners
'''for col in range(len(game)):
    check= []
    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print ("Winner!")'''


#Error handling example
'''game = [[0, 0, 0], [0, 0, 0], [0, 0, 0],]



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
        print("Something went very wrong") 


game= game_board(game, just_display=True)
game= game_board(game_board , player="x", row=5, column=2)
'''





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
 




























 