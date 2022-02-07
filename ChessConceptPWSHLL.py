import math
from sqlite3 import enable_shared_cache

BLACK = "black"
WHITE = "white"
class empty: #Define the empty squares
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = " "
        
    def isEmpty(self): #A general function to know if the square is empty
        return True
    
    def isKing(self): #A general function to know if the king is in the square
        return False

class queen: #Defines the queens
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.position = self.x, self.y
        self.color = color
        if self.color == BLACK:
            self.symbol = "♕"
        elif self.color == WHITE:
            self.symbol = "♛"

    def getSymbol(self):#Returns the symbol necesary for the graphic representation
        return self.symbol
    
    def move(self,board, x, y): #The function that allows movement
        moving = True
        while moving: #This while is running until the user introduces the valid inputs and a movement is done
            whereToMove = input("Introduce the coordinates of the place you want to move: \n")
            row = (int(whereToMove[-1]))-1
            col = 7 - (ord(whereToMove[0].upper())-65)#These 2 variables take the letter and the column and converts them into valid coordinates
            print(row, col)
            if not(board[row][col].isEmpty()):#If there is a piece already in the square to move
                if board[row][col].color == self.color:#The if checks if the piece in the square can be eaten
                    print("There's already one of your pieces there!\n")
                    continue
            Ydifference = col - y #This variables are meant to know if there was a movement in each axis
            Xdifference = row - x
            canMove=True
           
            if Xdifference != 0 and Ydifference!=0: #If the movement was in both axis
                if abs(Xdifference) != abs(Ydifference):#If the movement is not fully diagonal, it's not a valid movement
                    print("That's not a valid movement")
                    continue
                else: #here it checks if theres pieces on the way between the startig point and the end point
                    if Xdifference > 0: 
                        for i in range(1, Xdifference):
                            print(board[row-i][col-i].symbol)
                            if not(board[row-i][col-i].isEmpty()):
                                canMove = False
                        
                    if Xdifference < 0:
                        for i in range(1, abs(Xdifference)):
                            print(board[row+i][col+i].symbol)
                            if not(board[row+i][col+i].isEmpty()):
                                canMove = False
                                print(board[row+i][col+i])

            
            elif Xdifference != 0 and Ydifference == 0: #If the movement is vertical
                #here it checks if theres pieces on the way between the startig point and the end point
                if Xdifference > 0:
                    for i in range(1,Xdifference):
                        print(board[row-i][col].symbol)
                        if not(board[row-i][col].isEmpty()):
                            canMove = False
                        
                if Xdifference < 0:
                    for i in range(1, abs(Xdifference)):
                        print(board[row+i][col].symbol)
                        if not(board[row+i][col].isEmpty()):
                            canMove = False

            elif Xdifference == 0 and Ydifference != 0: #If the movement is horizontal
                if Ydifference > 0:
                    for i in range(1, Ydifference):
                        print(board[row][col-i].symbol)
                        if not(board[row][col-i].isEmpty()):
                            canMove = False
                        
                if Ydifference < 0:
                    for i in range(1, abs(Ydifference)):
                        print(board[row][col+i].symbol)
                        if not(board[row][col+i].isEmpty()):
                            canMove = False


            if canMove == False:#If there is a piece on the way, this if passes
                print("There is a piece on the way!\n")
                continue

            if board[row][col].isKing(): #If the piece eaten is king, it returns true, which means the game has ended
                board[x][y] = empty(x, y)
                board[row][col] = queen(x, y, self.color)
                return(True)
            else:
                board[x][y] = empty(x, y) #If it was not the king, it returns false and the while continues
                board[row][col] = queen(x, y, self.color)
                return(False)
    
    def isEmpty(self):
        return False

    def isKing(self):
        return False
                    
class king: #Defines the kings
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.position = self.x, self.y
        self.color = color
        if self.color == BLACK:
            self.symbol = "♔"
        elif self.color == WHITE:
            self.symbol = "♚"

    def getSymbol(self):
        return self.symbol

    def move(self, board, x, y):
        moving =  True#The same movement as the queen, except with a few more limits
        while moving:
            whereToMove = input("Introduce the coordinates of the place you want to move: \n")
            row = (int(whereToMove[-1]))-1
            col = 7 - (ord(whereToMove[0].upper())-65)
            print(row, col)
            canMove = True
            if (x == 7 and y == 3 ):
                if (row == 7 and col ==0):
                    for i in range(1, 3):
                            if not(board[row][col+i].isEmpty()):
                                print(row, col+i)
                                canMove = False
                    if canMove == True:
                        board[7][0] = empty(7, 0)
                        board[7][3] = empty(7, 3)
                        board[7][1] = king(7, 1, self.color)
                        board[7][2] = rook(7, 2, self.color)
                        return False
                    else:
                        print("There's a piece on the way!")
                        continue
            elif (x == 0 and y == 4):
                if (row == 0 and col ==7):
                    for i in range(1, 3):
                            if not(board[row][col-i].isEmpty()):
                                print(row, col-i)
                                canMove = False
                    if canMove == True:
                        board[0][7] = empty(7, 0)
                        board[0][4] = empty(7, 3)
                        board[0][6] = king(7, 1, self.color)
                        board[0][5] = rook(7, 2, self.color)
                        return False
                    else:
                        print("There's a piece on the way!")
                        continue

            if not(board[row][col].isEmpty()):
                if board[row][col].color == self.color:
                    print("There's already one of your pieces there!\n")
                    continue
            
            Ydifference = col - y
            Xdifference = row - x
            if Xdifference != 0 and Ydifference!=0: #There is no piece on the way check with the king, which only moves one square at a time
                if abs(Xdifference) != abs(Ydifference) or (abs(Xdifference)>1 or abs(Ydifference)>1):
                    print("That's not a valid movement")
                    continue
 
            elif Xdifference != 0 and Ydifference == 0:
                if abs(Xdifference)>1:#If the users try to move the king more that one square, this if passes
                    print("That's not a valid movement")
                    continue

            elif Xdifference == 0 and Ydifference != 0:
                if abs(Ydifference)>1:
                    print("That's not a valid movement")
                    continue

            if board[row][col].isKing():#Checks if the king was eaten
                board[x][y] = empty(x, y)
                board[row][col] = king(x, y, self.color)
                return(True)
            else:
                board[x][y] = empty(x, y)
                board[row][col] = king(x, y, self.color)
                return(False)

    def isEmpty(self):
        return False
    
    def isKing(self):
        return True

class pawn: #Defines the pawns
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.position = self.x, self.y
        self.color = color
        if self.color == BLACK:
            self.symbol = "♙"
        elif self.color == WHITE:
            self.symbol = "♟︎"

    def getSymbol(self):
        return self.symbol

    def move(self, board, x, y):
        moving = True 
        while moving:
            whereToMove = input("Introduce the coordinates of the place you want to move: \n")
            row = (int(whereToMove[-1]))-1
            col = 7 - (ord(whereToMove[0].upper())-65)
            print(row, col)
            if not(board[row][col].isEmpty()):
                if board[row][col].color == self.color:
                    print("There's already one of your pieces there!\n")
                    continue
            Ydifference = col - y
            Xdifference = row - x
            canMove=True
            
            if Xdifference != 0 and Ydifference!=0:
                if abs(Xdifference) != abs(Ydifference) or (abs(Xdifference)>1 or abs(Ydifference)>1) or board[row][col].isEmpty():
                    print("That's not a valid movement") #If the user tries to move diagonaly, it checks that is only one square and only to eat
                    continue
            
            elif Xdifference != 0 and Ydifference == 0: #If the user tries to move verticaly
                if abs(Xdifference)>1 and not(x == 1 or x == 6) :#If the user tries to move more than one square and it's not on a starting postition
                    print("That's not a valid movement")
                    continue

                elif(abs(Xdifference>2)): #If it is on a starting postion, it can only move up to 2 squares
                    print("That's not a valid movement")

                if not(board[row][col].isEmpty()):
                    print("Pawns can only eat diagonally!")
                    continue

                if(abs(Xdifference)==2): #If the user moves 2 squares, it runs a check for pieces on the way
                    if Xdifference > 0:
                        for i in range(1,Xdifference):
                            print(board[row-i][col].symbol)
                            if not(board[row-i][col].isEmpty()):
                                canMove = False
                        
                    elif Xdifference < 0:
                        for i in range(1, abs(Xdifference)):
                            print(board[row+i][col].symbol)
                            if not(board[row+i][col].isEmpty()):
                                canMove = False

                    if canMove == False:
                        print("There is a piece on the way!\n")
                        continue


            elif Xdifference == 0 and Ydifference != 0:
                print("That's not a valid movement")
                continue

            if ((self.color==BLACK and Xdifference<0) or (self.color==WHITE and Xdifference>0)):
                print("Pawns can only move foward!")
                continue

            if board[row][col].isKing():
                board[x][y] = empty(x, y)
                board[row][col] = pawn(x, y, self.color)
                return(True)
            else:
                board[x][y] = empty(x, y)
                board[row][col] = pawn(x, y, self.color)
                return(False)

    def isEmpty(self):
        return False

    def isKing(self):
        return False

class rook: #Defines the rooks
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.position = self.x, self.y
        self.color = color
        if self.color == BLACK:
            self.symbol = "♖"
        elif self.color == WHITE:
            self.symbol = "♜"
    def getSymbol(self):
        return self.symbol

    def move(self,board, x, y):
        moving = True
        while moving:
            whereToMove = input("Introduce the coordinates of the place you want to move: \n")
            row = (int(whereToMove[-1]))-1
            col = 7 - (ord(whereToMove[0].upper())-65)
            print(row, col)
            if not(board[row][col].isEmpty()):
                if board[row][col].color == self.color:
                    print("There's already one of your pieces there!\n")
                    continue
            Ydifference = col - y
            Xdifference = row - x
            canMove=True
           
            if Xdifference != 0 and Ydifference!=0: #If the user tries to move diagonaly, it won't allow it
                print("That's not a valid movement")
                continue

            elif Xdifference != 0 and Ydifference == 0:#If the user tries to move verticaly or horzontaly, it runs a check
                if Xdifference > 0:
                    for i in range(1,Xdifference):
                        print(board[row-i][col].symbol)
                        if not(board[row-i][col].isEmpty()):
                            canMove = False
                        
                if Xdifference < 0:
                    for i in range(1, abs(Xdifference)):
                        print(board[row+i][col].symbol)
                        if not(board[row+i][col].isEmpty()):
                            canMove = False

            elif Xdifference == 0 and Ydifference != 0:
                if Ydifference > 0:
                    for i in range(1, Ydifference):
                        print(board[row][col-i].symbol)
                        if not(board[row][col-i].isEmpty()):
                            canMove = False
                        
                if Ydifference < 0:
                    for i in range(1, abs(Ydifference)):
                        print(board[row][col+i].symbol)
                        if not(board[row][col+i].isEmpty()):
                            canMove = False


            if canMove == False:
                print("There is a piece on the way!\n")
                continue

            if board[row][col].isKing():
                board[x][y] = empty(x, y)
                board[row][col] = rook(x, y, self.color)
                return(True)
            else:
                board[x][y] = empty(x, y)
                board[row][col] = rook(x, y, self.color)
                return(False)

    def isEmpty(self):
        return False

    def isKing(self):
        return False

class bishop:#Defines de Bishops
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.position = self.x, self.y
        self.color = color
        if self.color == BLACK:
            self.symbol = "♗"
        elif self.color == WHITE:
            self.symbol = "♝"
    def getSymbol(self):
        return self.symbol

    def move(self,board, x, y):
        moving = True
        while moving:
            whereToMove = input("Introduce the coordinates of the place you want to move: \n")
            row = (int(whereToMove[-1]))-1
            col = 7 - (ord(whereToMove[0].upper())-65)
            print(row, col)
            if not(board[row][col].isEmpty()):
                if board[row][col].color == self.color:
                    print("There's already one of your pieces there!\n")
                    continue
            Ydifference = col - y
            Xdifference = row - x
            canMove=True
           
            if Xdifference != 0 and Ydifference!=0: #If the user tries to move diagonaly, it runs a check
                if abs(Xdifference) != abs(Ydifference):
                    print("That's not a valid movement")
                    continue
                else:
                    if Xdifference > 0:
                        for i in range(1, Xdifference):
                            print(board[row-i][col-i].symbol)
                            if not(board[row-i][col-i].isEmpty()):
                                canMove = False
                        
                    if Xdifference < 0:
                        for i in range(1, abs(Xdifference)):
                            print(board[row+i][col+i].symbol)
                            if not(board[row+i][col+i].isEmpty()):
                                canMove = False
                                print(board[row+i][col+i])

            
            elif Xdifference != 0 and Ydifference == 0: #If the user tries to move verticaly or horizontaly, it won't allow it
                print("That's not a valid movement!")
                continue

            elif Xdifference == 0 and Ydifference != 0:
                print("That's not a valid movement!")
                continue


            if canMove == False:
                print("There is a piece on the way!\n")
                continue

            if board[row][col].isKing():
                board[x][y] = empty(x, y)
                board[row][col] = bishop(x, y, self.color)
                return(True)
            else:
                board[x][y] = empty(x, y)
                board[row][col] = bishop(x, y, self.color)
                return(False)
    
    def isEmpty(self):
        return False

    def isKing(self):
        return False

class knight:#Defines de Knights
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.position = self.x, self.y
        self.color = color
        if self.color == BLACK:
            self.symbol = "♘"
        elif self.color == WHITE:
            self.symbol = "♞"

    def getSymbol(self):
        return self.symbol
    
    def move(self,board, x, y):
        moving = True
        while moving:
            whereToMove = input("Introduce the coordinates of the place you want to move: \n")
            row = (int(whereToMove[-1]))-1
            col = 7 - (ord(whereToMove[0].upper())-65)
            print(row, col)
            if not(board[row][col].isEmpty()):
                if board[row][col].color == self.color:
                    print("There's already one of your pieces there!\n")
                    continue
            Ydifference = col - y
            Xdifference = row - x
            
            if (Xdifference == 0 or Ydifference == 0 or abs(Xdifference)>2 or abs(Ydifference) > 2 or (abs(Xdifference) == 2 and abs(Ydifference) != 1) or(abs(Ydifference)==2 and abs(Xdifference) !=1)):
                print("That's not a valid movement")
                continue

            if board[row][col].isKing():
                board[x][y] = empty(x, y)
                board[row][col] = knight(x, y, self.color)
                return(True)
            else:
                board[x][y] = empty(x, y)
                board[row][col] = knight(x, y, self.color)
                return(False)

    def isEmpty(self):
        return False
    
    def isKing(self):
        return False

def makeBoard(rows=8):#This function assigns creates a board out of lists and assigns the empty class to all squares
    grid = [] 
    count = 1
    for i in range(rows):
        grid.append([]) 
        for n in range(rows):
            space = empty(n, i)
            grid[i].append(space)
            count+=1
        count+=1
    return grid

def piecesStartPosition(board):#This functions sets up all starting pieces

    board[0][0] = rook(0, 0, BLACK)
    board[0][1] = knight(1, 0, BLACK)
    board[0][2] = bishop(2, 0, BLACK)
    board[0][3] = queen(3, 0, BLACK)
    board[0][4] = king(4, 0, BLACK)
    board[0][5] = bishop(5, 0, BLACK)
    board[0][6] = knight(6, 0, BLACK)
    board[0][7] = rook(7, 0, BLACK)
    board[7][0] = rook(0, 7, WHITE)
    board[7][1] = knight(1, 0, WHITE)
    board[7][2] = bishop(2, 0, WHITE)
    board[7][4] = queen(3, 0, WHITE)
    board[7][3] = king(4, 0, WHITE)
    board[7][5] = bishop(5, 0, WHITE)
    board[7][6] = knight(6, 0, WHITE)
    board[7][7] = rook(7, 0, WHITE)
    for i in range(8):
        board[1][i] = pawn(i, 0, BLACK)
        board[6][i] = pawn(i, 6, WHITE)

def printBoard(board):#This function takes the graphic representation of every class and prints it
    graphBoard = []
    counter = 1
    for i in range(8):
        graphBoard.append([]) 
        for n in range(8):
            pieceSymbol= board[i][n].symbol
            graphBoard[i].append(pieceSymbol)
    for row in range(len(graphBoard)):
        print("{}{}".format(counter, graphBoard[row]))
        counter+=1
    print("   H    G    F    E    D    C    B    A")
        
        
board = makeBoard()
piecesStartPosition(board)

game = True
turnCounter = 1
print("Welcome to my chess game, please start playing\nPlease Introduce the coordinates in the format (Letter)(Number)\n")
while game:#This while runs until the game is over
    printBoard(board)
    if turnCounter%2==0:
        print("Black Turn\n")
        turn=BLACK
    else: 
        print("White Turn\n")
        turn=WHITE

    pieceToMove = input("Introduce the coordinates of the piece you want to move:\n")
    letters = {"A", "B", "C", "D", "E", "F", "G", "H"}
    numbers = {"1", "2", "3", "4", "5", "6", "7", "8"}

    checkmate = False 

    if len(pieceToMove)<=0 or len(pieceToMove)>2 or not(pieceToMove[-1] in numbers) or not(pieceToMove[0].upper() in letters):#Checks if the user input is a valid input
        print("Please introduce a valid input\n")
        continue

    row = (int(pieceToMove[-1]))-1
    col = 7 - (ord(pieceToMove[0].upper())-65)#Takes the letter and converts it into ascii code and the converts into a usabel column
    if board[row][col].isEmpty():
        print("There is no piece in this square\n")
    elif board[row][col].color != turn:
        print("This piece is not yours\n")
    else:
        print(row, col)
        checkmate = board[row][col].move(board, row, col)
        turnCounter+=1
    if checkmate == True:#If the class function returns that there has been a checkate, the game ends
        print("\nThe king has fallen, the game is over\nCredits to: Edgar Zaragoza\nGithub: https://github.com/MeDicenEdgar\n")
        break