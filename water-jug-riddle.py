import queue

#Node class
class Node:
  def __init__(self, jug_3, jug_5):
    self.state = (jug_3, jug_5)
    self.neighbors = []
  def add_state(self, node):
    self.neighbors.append(node)
  def __eq__(self, other):
    return self.__class__ == other.__class__ and self.state == other.state
  def __lt__(self, other):
    return self.__class__ == other.__class__ and self.state < other.state
  def __gt__(self, other):
    return self.__class__ == other.__class__ and self.state > other.state
  
  def makeState(self):
    # state 1
    filled3 = Node(3, self.state[1])
    filled5 = Node(self.state[0], 5)
    
    # state 2
    empty3 = Node(0, self.state[1])
    empty5 = Node(self.state[0], 0)
    
    # pouring from 3 to 5
    if self.state[1] < 3:
      pourFrom3 = Node(0, self.state[1]+self.state[0]) 
    
    # pouring from 5 to 3
    if self.state[1] + self.state[0] <= 3:
      pourFrom5 = Node(self.state[0]+self.state[1], 0)
    
    neighbors = [filled3, filled5, empty3, empty5, pourFrom3, pourFrom5]
    print("neighbors" + str(neighbors))
    
    
    self.neighbors = neighbors
    
    return neighbors
 
  def goalState(self):
    if self.state[1] == 4:
      return True
  
  def heuristic(self):
    if self.goalState() == True:
      return 0
    else:
      difference = abs(4 - self.state[1] + self.state[0]) 
      if difference == 0:
        return 1
      else:
        return difference
        
  def __str__(self):
    string = ""
    key = ""
    for nodes in self.neighbors:
      key += "- " + nodes + "\n"
    string = "Name: " + str(self.state) + "\n" + "Neighbors:\n" + key
    string += str(len(self.neighbors))
    return string
  def __hash__(self):
    return int(str(self.state[0])+str(self.state[1]))
  
#Graph class 
class Graph:
  def __init__(self, startNode):
    self.graph = {}
    self.startNode = startNode
    
  def add_node(self, node):
    self.graph[node.key] = node
  def add_edge(self, node, node2):
    if node.key in self.graph and node2.key in self.graph:
      if node not in node2.neighbors and node2 not in node.neighbors:
        node.add_neighbor(node2)
        node2.add_neighbor(node)
    else:
      print("One of the nodes you are trying to connect is not there.")
  def __str__(self):
    str = ""
    for nodes in self.graph.values():
      str += nodes.__str__() + "\n"
    return str
  
  def greedySearch(self, startNode):
    
    statesSearched = 0
    visitedNode = [startNode]
    currentNode = queue.PriorityQueue()
    currentNode.put((startNode.heuristic(), startNode))
    
    while not currentNode.empty():
      nodeCoordinate  = currentNode.get()
      cost = nodeCoordinate[0]
      node = nodeCoordinate[1]
      
      # 3L
      print(str(node.state[0]) + " ", end = "")
      # 5L
      print(str(node.state[1]) + " ", end = "")
      
      heuristic = node.heuristic()
      
      if node.goalState() == True:
        return node, statesSearched
      
      node.makeState()
      
      for node in node.neighbors:
        if node not in visitedNode:
          currentNode.put((heuristic, node))
          visitedNode.put(node) 
          statesSearched += 1

  def a_star_search(self, startNode):
    
    statesSearched = 0
    
    visitedNode = [startNode]
    currentNode = queue.PriorityQueue()
    
    # (f (prio val), depth, heuristic, node, path)
    currentNode.put((0, 0, 0, startNode))

    while not currentNode.empty():
      nodeCoordinate  = currentNode.get()
      priorityValue = nodeCoordinate[0]
      depth = nodeCoordinate[1]
      heuristic = nodeCoordinate[2]
    
      print(str(node.state[0]) + " ", end = "")
      print(str(node.state[1]) + " ", end = "")
      
      if node.goalState() == True:
        return node, statesSearched
    
      for neighbor in node.neighbors:
        if neighbor not in visitedNode:
          priorityValue = depth+1+neighbor.heuristic()
          currentNode.put((priorityValue, depth+1, neighbor.heuristic(), neighbor))
          visitedNode.put(neighbor)
          statesSearched += 1

nodeA = Node(0,0)
print(nodeA.neighbors)

graph = Graph(nodeA)

#graph.aStarSearch()
#print()
statesSearched = 0
print("Running Greedy Search...")
print("Number of States Searched: " + str(statesSearched))
print("Solution: ")
print(graph.greedySearch(nodeA))

print("Graph:")
print(graph)
nodeA.makeState()
