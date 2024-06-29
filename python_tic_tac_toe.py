game = [[1,1,1],[0,2,0],[2,2,0]]

horizontally
vertically
diagonally



def zuku():
    print ("   0, 1, 2")
    for count, line in enumerate(game):
        print(count, line)

zuku()





















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
 




























 