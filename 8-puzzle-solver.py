import time
import queue

#Node class
class Node:
  
  # Initialization method creates board and neighbor list
  def __init__(self, board):
    self.board = board
    self.neighbors = []
  
  # Equal to method
  def __eq__(self, other):
    return self.__class__ == other.__class__ and self.board == other.board
   
  # Less than method
  def __lt__(self, other):
    return self.__class__ == other.__class__ and self.board < other.board
  
  # Greater than method
  def __gt__(self, other):
    return self.__class__ == other.__class__ and self.board > other.board

  # String method prints board
  def __str__(self):
    row1 = ""
    ret = ""
    for row in self.board:
      for element in row:
        row1 += element + " " 
      ret += row1 + "\n"
      row1 = ""
    return ret
  
  # Hash method totals the ASCII values for elements in board
  def __hash__(self):
    total = ''
    for row in self.board:
      for space in row:
        if space != ' ':
          total += space
        else:
          total += '0'
    return int(total)

  # Changes the coordinates of the tiles
  def makeState(self):

    # Find empty space
    emptyRow = 0
    emptyColumn = 0
    moves = []
    
    for rows in range(0, 3):
      for columns in range(0, 3):
        if self.board[rows][columns] == " ":
          emptyRow = rows
          emptyColumn = columns
          break
      
    # Find possible moves
    # North
    if emptyRow-1 >= 0:
      moves.append((emptyRow-1, emptyColumn))
    # South
    if emptyRow+1 <= 2:
      moves.append((emptyRow+1, emptyColumn))
    # East
    if emptyColumn+1 <= 2:
      moves.append((emptyRow, emptyColumn+1))
    # West
    if emptyColumn-1 >= 0:
      moves.append((emptyRow, emptyColumn-1))
    
    for moveRow, moveCol in moves:
      # Duplicate board
      newBoard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
      for rows in range(0, 3):
        for columns in range(0, 3):
          newBoard[rows][columns] = self.board[rows][columns]
      
      # Switches coordinates
      newBoard[emptyRow][emptyColumn] = self.board[moveRow][moveCol]
      newBoard[moveRow][moveCol] = " "
    
      # Append to self.neighbors
      myNode = Node(newBoard)
      
      self.neighbors.append(myNode)
      

  # Goal method checks if puzzle has been solved
  def goalState(self):
    if self.board == [
      ['1', '2', '3'],
      ['4', '5', '6'],
      ['7', '8', ' '],
    ]:
      return True
    else:
      return False
  
  # Heuristic method sums manhattan distances of each tile from its correct positions
  def heuristic(self):
    totalDistance = 0
    correctBoard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]
    correctCoords = {'1':(0,0), '2':(0,1), '3':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '7':(2,0), '8':(2,1), ' ':(2,2)}
    for rows in range(0, 3):
      for columns in range(0, 3):
        currentCoords = (rows, columns)
        currentTile = self.board[rows][columns]
        xDistance = abs(rows-correctCoords[currentTile][0])
        yDistance = abs(columns-correctCoords[currentTile][1])
        totalDistance += xDistance+yDistance
    return totalDistance

#Graph class 
class Graph:
  def __init__(self, startNode):
    self.startNode = startNode
  
  # A* Search
  def a_star_search(self, startNode):
    
    statesSearched = 0
    path = [startNode]
    visitedNode = [startNode]
    currentNode = queue.PriorityQueue()
    currentNode.put((0, 0, startNode, path))
    while not currentNode.empty():
      nodeCoordinate  = currentNode.get()
      priorityValue = nodeCoordinate[0]
      depth = nodeCoordinate[1]
      node = nodeCoordinate[2]
      path = nodeCoordinate[3]

      if node.goalState() == True:
        return path, statesSearched
      
      node.makeState()
      
      for neighbor in node.neighbors:
        if neighbor not in visitedNode:
          heuristic2 = neighbor.heuristic()
          priorityValue = depth+1+heuristic2
          currentNode.put((priorityValue, depth+1, neighbor, path+[neighbor]))
          visitedNode.append(neighbor)
          statesSearched += 1
  
  # BFS 
  def bfs(self, start):
    statesSearched = 0
    path = [start]
    visitedNode = [start]
    currentNode = [(start, path)]
    while len(currentNode) > 0:
      nodeCoordinate = currentNode.pop(0)
      node = nodeCoordinate[0]
      path = nodeCoordinate[1]

  
      if node.goalState() == True:
        return path, statesSearched
      
      node.makeState()

      for neighbor in node.neighbors:
        if neighbor not in visitedNode:
          currentNode.append((neighbor, path+[neighbor]))
          visitedNode.append(neighbor)
          statesSearched += 1

b = [
      ['5', '3', '4'],
      [' ', '2', '8'],
      ['1', '6', '7'],
    ]
    
start_board = [
  ['3', '6', '8'],
  ['1', ' ', '4'],
  ['7', '2', '5'],
]


node = Node(start_board)
graph = Graph(node)

print("Testing A*")
start = time.time()
aStar = graph.a_star_search(node)
end = time.time()

aStarTime = abs(end-start)

for b in aStar[0]:
  print(b)

print("States searched: " + str(aStar[1]))
print("Length of path: " + str(len(aStar[0])))
print("Time: " + str(aStarTime))

print()

print("Testing BFS")
start2 = time.time()
bfs = graph.bfs(node)
end2 = time.time()

bfsTime = abs(end2-start2)

for b in bfs[0]:
  print(b)
  
print("States searched: " + str(bfs[1]))
print("Length of path: " + str(len(bfs[0])))
print("Time: " + str(bfsTime))

