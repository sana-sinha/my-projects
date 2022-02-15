import time

def conways(board):
  rowElems = ""
  for row in board:
    for elements in row:
      if elements == False:
        rowElems += "-"
      elif elements == True:
        rowElems += "O"
    print(rowElems)
    rowElems = ""

# ==== function ====
# (1) count the neighbors (up down left right diagonals)
# (2) test the neighbor count
# (3) set to true or False
  # if 0-1 neighbors = DIE
  # if 2-3 neighbors = LIVE (true)
  # if 3+ = DIE
    # if cell = DIE and you have exactly 3 neighbors = RESSURECTION

def count(board, r, c):
  # how many neighbors = true
  counter = 0
  if (0 < r < 29) == True:
    # north
    if board[r-1][c] == True:
      counter += 1
    # south
    if board[r+1][c] == True:
      counter += 1
  if (0 < c < 59) == True:
    # east
    if board[r][c+1] == True:
      counter += 1
    # west
    if board[r][c-1] == True:
      counter += 1
  if (0 < r < 29) == True and (0 < c < 59) == True:
    # ne
    if board[r-1][c+1] == True:
      counter += 1
    # se
    if board[r+1][c+1] == True:
      counter += 1
    # nw
    if board[r-1][c-1] == True:
      counter += 1 
    # sw
    if board[r+1][c-1] == True:
      counter += 1
  return counter

def function2(board, life, row, col):
  numNeighbors = count(board, row, col)
  if life == True:
    if numNeighbors <= 1:
      life = False
    elif numNeighbors == 2 or numNeighbors == 3:
      life = True
    elif numNeighbors > 3:
      life = False
  if life == False:
    if numNeighbors == 3:
      life = True
  return life

# GAMEPLAY

print("Welcome to Conway's Game of Life. We start with a 30x60 grid of cells, either alive or dead. Here are the rules:")
print("\t1) Any live cell with fewer than two live neighbors dies, as if by underpopulation." + "\n\t2) Any live cell with two or three live neighbors lives on to the next generation." + "\n\t3) Any live cell with more than three live neighbors dies, as if by overpopulation." + "\n\t4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.")
print()
enter = input("Press ENTER to continue:")
print()

print("1. B-Heptomino Shuttle" + "\n2. Boat" + "\n3. Random Design" + "\n4. F-Pentomino" + "\n5. Hertz Oscillator" + "\n6. Repeat" + "\n7. Spaceship" + "\n8. Square")
print()
pattern = input("Which pattern would you like to start with? #")
print()
if pattern == "1":
  myBHeptomino = open("b-heptomino-shuttle.in")
  file = myBHeptomino.readlines()
  file = [myBHeptomino.strip() for myBHeptomino in file]
  myBHeptomino.close()
  
elif pattern == "2":
  myBoat = open("boat.in")
  file = myBoat.readlines()
  file = [myBoat.strip() for myBoat in file]
  myBoat.close()
elif pattern == "3":
  myDesign = open("design.in")
  file = myDesign.readlines()
  file = [myDesign.strip() for myDesign in file]
  myDesign.close()
elif pattern == "4":
  myFPentomino = open("f-pentomino.in")
  file = myFPentomino.readlines()
  file = [myFPentomino.strip() for myFPentomino in file]
  myFPentomino.close()
elif pattern == "5":
  myHOscillator = open("hertz-oscillator.in")
  file = myHOscillator.readlines()
  file = [myHOscillator.strip() for myHOscillator in file]
  myHOscillator.close()
elif pattern == "6":
  myRepeat = open("repeat.in")
  file = myRepeat.readlines()
  file = [myRepeat.strip() for myRepeat in file]
  myRepeat.close()
elif pattern == "7":
  mySpaceship = open("spaceship.in")
  file = mySpaceship.readlines()
  file = [mySpaceship.strip() for mySpaceship in file]
  mySpaceship.close()
elif pattern == "8":
  mySquare = open("square.in")
  file = mySquare.readlines()
  file = [mySquare.strip() for mySquare in file]
  mySquare.close()

coordList = []

for elements in file:
  myElements = elements.split()
  for i in range(0, len(myElements)): 
    myElements[i] = int(myElements[i]) 
  coordList.append(myElements)

b = []
for r in range(30):
  rows = []
  for c in range(60):
    rows.append(False)
  b.append(rows)
  
for coords in coordList:
  row = coords[0] 
  column = coords[1]
  b[row][column] = True
conways(b)

start = input("Press ENTER to start:")

while True:

  newB = []
  for r in range(30):
    rows = []
    for c in range(60):
      rows.append(False)
    newB.append(rows)
  
  for r in range(0, len(b)):
    for c in range(0, len(b[r])):
      newB[r][c] = function2(b, b[r][c], r, c)
  conways(newB)
  b = newB
  time.sleep(0.1)
