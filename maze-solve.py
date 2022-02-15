import maze as mz
import queue

maze = ""
maze += "+---+---+---+\n"  
maze += "|           |\n" # row0
maze += "+   +---+   +\n"
maze += "|     * |   |\n" # row1
maze += "+---+   +   +\n"
maze += "| X         |\n" # row2
maze += "+---+---+---+\n"
      # col0 col1 col2

# row has 14 characters (including new line) so maze width is 14
maze = mz.Maze(maze, 14)

class Node:
  def __init__(self, key):
    self.key = key
    self.neighbors = {}
  def add_neighbor(self, node, weight):
    self.neighbors[node] = weight
  def __str__(self):
    string = ""
    key = ""
    for nodes in self.neighbors:
      key += "- " + nodes + "\n"
    string = "Name: " + self.key + "\n" + "Neighbors:\n" + key
    return string
  def __lt__(self, other):
    return self.__class__ == other.__class__ and self.key < other.key
    
class Graph:
  def __init__(self):
    self.graph = {}
  def add_node(self, node):
    self.graph[node.key] = node
  def add_edge(self, node, node2, weight):
    if node.key in self.graph and node2.key in self.graph:
      if node not in node2.neighbors and node2 not in node.neighbors:
        node.add_neighbor(node2, weight)
        node2.add_neighbor(node, weight)
    else:
      print("One of the nodes you are trying to connect is not there.")
  def __str__(self):
    str = ""
    for nodes in self.graph.values():
      str += nodes.__str__() + "\n"
    return str
  
  def get_path_cost(self, path):
    cost = 0
    for i in range(0, len(path)-1):
      node = self.graph[path[i]] 
      next_node = self.graph[path[i+1]]
      weight = node.neighbors[next_node]
      cost += weight
    return cost
  
  def get_bfs_path(self, start_node, end_node):
    visitedNode = [start_node]
    currentNode = [(0, start_node, [start_node.key])]
    while len(currentNode) > 0:
      currentPop = currentNode.pop(0)
      weight = currentPop[0]
      node = currentPop[1]
      path = currentPop[2]
      print(node.key)
      if node == end_node:
        print("Found goal state!")
        return path
      for neighbor in node.neighbors:
        if neighbor not in visitedNode:
          currentNode.append((node.neighbors[neighbor], neighbor, path+[neighbor.key]))
          visitedNode.append(neighbor)
          
          
  def get_dfs_path(self, start_node, end_node):
    visitedNode = [start_node]
    currentNode = [(0, start_node, [start_node.key])]
    while len(currentNode) > 0:
      currentPop = currentNode.pop()
      weight = currentPop[0]
      node = currentPop[1]
      path = currentPop[2]
      print(node.key)
      if node == end_node:
        print("Found goal state!")
        return path
      for neighbor in node.neighbors:
        if neighbor not in visitedNode:
          currentNode.append((node.neighbors[neighbor], neighbor, path+[neighbor.key]))
          visitedNode.append(neighbor)

  def get_ucs_path(self, start_node, end_node):
    visitedNode = [start_node]
    currentNode = queue.PriorityQueue()
    currentNode.put((0, start_node, [start_node.key]))
    while not currentNode.empty():
      currentPop = currentNode.get()
      weight = currentPop[0] 
      node = currentPop[1]
      path = currentPop[2]
      print(node.key + " with the weight of " + str(weight))
      if node == end_node:
        print("Found goal state!")
        return path
      for neighbor in node.neighbors:
        # node.neighbors[neighbor] is a NODE not a number (weight)
        neighborWeight = node.neighbors[neighbor]
        if neighbor not in visitedNode:
          currentNode.put((neighborWeight, neighbor, path+[neighbor.key]))
          visitedNode.append(neighbor)
  
  def get_dls_path(self, rootNode, endNode, depthLimit):
    visitedNode = [rootNode]
    visitableNode = [(rootNode, 0, [rootNode.key])]
    while len(visitableNode) != 0:
      node, depth, path = visitableNode.pop()
      print(node.key)
      if depth > depthLimit:
        break
      if node == endNode:
        return path
      for n in node.neighbors:
        if n not in visitedNode and depth+1 <= depthLimit:
          visitedNode.append(n)
          visitableNode.append((n, depth+1, path+[n.key]))
  def get_ids_path(self, rootNode, endNode, maxDepth):
    depth = 0
    while depth <= maxDepth:
      print(depth)
      dlsCall2 = self.get_dls_path(rootNode, endNode, depth)
      depth += 1
      if dlsCall2 != None:
        return dlsCall2
  
graph = Graph()

node_0A = Node("(0,0)")
node_0B = Node("(0,1)")
node_0C = Node("(0,2)")
node_1A = Node("(1,0)")
node_1B = Node("(1,1)")
node_1C = Node("(1,2)")
node_2A = Node("(2,0)")
node_2B = Node("(2,1)")
node_2C = Node("(2,2)")

graph.add_node(node_0A)
graph.add_node(node_0B)
graph.add_node(node_0C)
graph.add_node(node_1A)
graph.add_node(node_1B)
graph.add_node(node_1C)
graph.add_node(node_2A)
graph.add_node(node_2B)
graph.add_node(node_2C)

# node 1, node 2, cost
graph.add_edge(node_0A, node_1A, 1) 
graph.add_edge(node_0A, node_0B, 1)
graph.add_edge(node_0B, node_0C, 1)
graph.add_edge(node_0C, node_1C, 1)
graph.add_edge(node_1A, node_1B, 10)
graph.add_edge(node_1B, node_2B, 10)
graph.add_edge(node_1C, node_2C, 1)
graph.add_edge(node_2A, node_2B, -10)
graph.add_edge(node_2C, node_2B, 1)



print("BFS Path")
bfsCall = graph.get_bfs_path(node_0A, node_2A)
maze.print_path(bfsCall)
print("Path Cost: " + str(graph.get_path_cost(bfsCall)))


print()
print("DFS Path")
dfsCall = graph.get_dfs_path(node_0A, node_2A)
maze.print_path(dfsCall)
print("Path Cost: " + str(graph.get_path_cost(bfsCall)))


print()
print("UCS Path")
ucsCall = graph.get_ucs_path(node_0A, node_2A)
maze.print_path(ucsCall)
print("Path Cost: " + str(graph.get_path_cost(bfsCall)))


print("DLS Path")
dlsCall = graph.get_dls_path(node_0A, node_2A, 4)
maze.print_path(dlsCall)
print("Path Cost: " + str(graph.get_path_cost(bfsCall)))


print()
print("IDS Path")
idsCall = graph.get_ids_path(node_0A, node_2A, 4)
maze.print_path(idsCall)
print("Path Cost: " + str(graph.get_path_cost(bfsCall)))
