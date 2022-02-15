import time
import random

# print board
def conways(board):
  columnNums = "   "
  for i in range(10):
    columnNums += str(i)+" "
  print(columnNums)
  rowCounter = 0
  colCounter = 0
  rowElems = ""
  for row in board:
    rowElems += str(rowCounter)+"  "
    rowCounter += 1
    for elements in row:
      if elements == 0:
        rowElems += "- "
      elif elements == 1:
        rowElems += "X "
      elif elements == 2:
        rowElems += "O "
    
    print(rowElems)        
    rowElems = ""
print()

# coords for player1 X
player1 = open("player1.in")
file1 = player1.readlines()
file1 = [player1.strip() for player1 in file1]

player1list = []

for elements in file1:
  nums = elements.split()
  for i in range(len(nums)):
    elems = int(nums[i])
    nums[i] = elems
  player1list.append(nums)

player1.close()

# coords for player 2 O
player2 = open("player2.in")
file2 = player2.readlines()
file2 = [player2.strip() for player2 in file2]

player2.close()

player2list = []

# makes file readable
for elements in file2:
  elems = elements.split()
  for i in range(len(elems)):
    nums = int(elems[i])
    elems[i] = nums
  player2list.append(elems)

# initializes board with dead cells
b = []
for r in range(10):
  rows = []
  for c in range(10):
    rows.append(0)
  b.append(rows)

# places the alive cell in board
for elems in player1list:
  row = elems[0] 
  column = elems[1]
  b[row][column] = 1

# places the alive cell in board
for elems in player2list:
  row = elems[0]
  col = elems[1]
  b[row][col] = 2

# counts the neighbors
def count(board, r, c):
  counter = 0
  counter2 = 0 
  # checks if in range first
  if (0 <= r < 9) == True:
    # north
  
    #x check
    if board[r-1][c] == 1:
      counter += 1
    # O check
    if board[r-1][c] == 2:
      counter2 += 1
    # south
    if board[r+1][c] == 1:
      counter += 1
      
    # o check
    if board[r+1][c] == 2:
      counter2 += 1
      
  if (0 <= c < 9) == True:
    # east
    if board[r][c+1] == 1:
      counter += 1
    # o check
    if board[r][c+1] == 2:
      counter2 += 1
    # west
    if board[r][c-1] == 1:
      counter += 1
    # o check
    if board[r][c-1] == 2:
      counter2 += 1
  if (0 <= r < 9) == True and (0 <= c < 9) == True:
    # ne
    if board[r-1][c+1] == 1:
      counter += 1
    # o check 
    if board[r-1][c+1] == 2:
      counter2 += 1
    # se
    if board[r+1][c+1] == 1:
      counter += 1
    # o check
    if board[r+1][c+1] == 2:
      counter2 += 1
    # nw
    if board[r-1][c-1] == 1:
      counter += 1 
    # o check 
    if board[r-1][c-1] == 2:
      counter2 += 1 
    # sw
    if board[r+1][c-1] == 1:
      counter += 1
    # o check 
    if board[r+1][c-1] == 2:
      counter2 += 1
  return [counter, counter2]


# rules: how it stays alive/dies
def function2(board, life, row, col):
  numNeighborsX = 0
  numNeighborsO = 0
  if board[row][col] == 1:
    numNeighborsX = count(board, row, col)[0]
  if board[row][col] == 2:
    numNeighborsO = count(board, row, col)[1]
  if life == 1:
    if numNeighborsX <= 1:
      life = 0
    elif numNeighborsX == 2 or numNeighborsX == 3:
      life = life
    elif numNeighborsX > 3:
      life = 0
  if life == 2:
    if numNeighborsO <= 1:
      life = 0
    elif numNeighborsO == 2 or numNeighborsO == 3:
      life = life
    elif numNeighborsO > 3:
      life = 0
  if life == 0:
    numNeighbors = count(board, row, col)
    if numNeighbors[0] == 3 or numNeighbors[1] == 3:
      if numNeighbors[0] > numNeighbors[1]:
        life = 1
      elif numNeighbors[1] > numNeighbors[0]:
        life = 2
      else:
        life = 1
  return life

# how many alive cells each player has
def aliveCells(board):
  cellCounterX = 0
  cellCounterO = 0
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        cellCounterX += 1
      elif board[i][j] == 2:
        cellCounterO += 1
  return [cellCounterX, cellCounterO]


# GAMEPLAY

# print rules
print("Welcome to Conway's Game of Life. We start with a 10x10 grid of cells, either alive or dead." + "\n\nHere are the rules:")
print("    1) Any live cell with fewer than two live neighbors dies, as if           by underpopulation." + "\n    2) Any live cell with two or three live neighbors lives on to t           he next generation." + "\n    3) Any live cell with more than three live neighbors dies, as i           f by overpopulation." + "\n    4) Any dead cell with exactly three live neighbors becomes a li           ve cell, as if by reproduction.")
print()
enter = input("Press ENTER to continue:")

# choose who goes first
coinFlip = random.randint(1, 2)
turn = 0
if coinFlip == 1:
  turn = 1
elif coinFlip == 2:
  turn = 2

while True:
  # creates new board for showing the next life each time
  newB = []
  for r in range(10):
    rows = []
    for c in range(10):
      rows.append(0)
    newB.append(rows)
    
  '''
  # replicating board
  for elems in player1list:
    row = elems[0] 
    column = elems[1]
    newB[row][column] = 1

  for elems in player2list:
    row = elems[0]
    col = elems[1]
    newB[row][col] = 2
  '''
  
  # newb goes through function 2 (rules)
  for r in range(0, len(b)):
    for c in range(0, len(b[r])):
      newB[r][c] = function2(b, b[r][c], r, c)
  b = newB
  print()
  conways(newB)
  print()
  print("Player O has " + str(aliveCells(b)[1]) + " cells alive.")
  print("Player X has " + str(aliveCells(b)[0]) + " cells alive.")
  print()
  if aliveCells(b)[1] == 0:
    print("Player X won!")
    break
  elif aliveCells(b)[0] == 0:
    print("Player O won!")
    break
  elif aliveCells(b)[0] == 0 and aliveCells(b)[1] == 0:
    print("The game is a tie!")
    break
  
  if turn == 1:
    print("It's Player X's turn.")
    
  elif turn == 2:
    print("It's Player O's turn.")
  
  if turn == 1:
    row = int(input("Please enter the row of the cell you wish to add: "))
    column = int(input("Please enter the column of the cell you wish to add: "))
    newB[row][column] = turn
    delRow = int(input("Please enter the row of the cell you wish to delete: "))
    delCol = int(input("Please enter the column of the cell you wish to delete: "))    
    newB[delRow][delCol] = 0

    b = newB
    conways(b)
    turn = 2
    
  
  elif turn == 2:
    row2 = int(input("Please enter the row of the cell you wish to add: "))
    column2 = int(input("Please enter the column of the cell you wish to add: "))
    newB[row2][column2] = turn
    delRow2 = int(input("Please enter the row of the cell you wish to delete: "))
    delCol2 = int(input("Please enter the column of the cell you wish to delete: ")) 
    newB[delRow2][delCol2] = 0
    b = newB
    conways(b)
    turn = 1
