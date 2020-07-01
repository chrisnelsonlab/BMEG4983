# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:36:18 2020

@author: nelsonc
"""

""" Position 0-63
    0 0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0


By column
    0  1  2  3  4  5  6  7  
    8  9  10 11 12 13 14 15
    16 17 18 19 20 21 22 23
    24 25 26 27 28 29 30 31
    32 33 34 35 36 37 38 39
    40 41 42 43 44 45 46 47
    48 49 50 51 52 53 54 55
    56 57 57 59 60 61 62 63
    
"""
def printasciiboard(board):
    #Prints the current board in ascii format. Mainly for debug
    print(len(board))
    for i in range(0,len(board)):
        linetoprint = " "
        for j in range (0,len(board)):
            linetoprint = linetoprint+" "+str(board[i][j])
        print(linetoprint)
        
def checkattack(board,row,column):
    #This function checks for a given position, if the placed queen would be 
    #under attack for a neighbor.
    #Checks horizontal and then diaganally. No need to check vertical. Only one
    #queen per vertical is placed.
    
    #Check horizontal
    tempvalue = sum(board[row][:])
    if(tempvalue>0):

        return False            
    #Check diaganally once
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if(board[i][j]==1):  
                if(abs(i-row)==abs(j-column)):
                        return False
    return True



def placequeen(board,column, wins, losses):
    #Recursive function. Trys to place a queen and then calls itself 
    #to place an additional queen. Backs up when it hits a dead end.
    #Countin: Round 0 first placement, Round 1 second placement, etc

    if(sum(sum(board,[])) ==len(board)):
        printasciiboard(board)   #uncomment to print all winning arrangements
        wins = wins+1
    else:
        losses = losses +1

    for row in range(0,len(board)):
        #Position_attempt = [row][column]
        #print("Row: " +str(row)+"  Column "+str(column))
        
        if (checkattack(board,row,column)):
            board[row][column] = 1
            board,wins,losses = placequeen(board,column+1,wins,losses)
            board[row][column] = 0

    return board,wins,losses


#Solves for an n x n board. n must be equal. 
    
cols = 8
rows = 8

#make an empty 2D board
board = [[0 for i in range(cols)] for j in range(rows)]

#Print the empty board
printasciiboard(board)

#Count wins and losses
wins = 0
losses = 0

#Begin recursive algorithm
board, wins, losses = placequeen(board,0,wins,losses)
print("wins:"+str(wins))
print("losses:"+str(losses))
  
        
