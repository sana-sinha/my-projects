class Node:
  def __init__(self, key):
    self.key = key
    self.neighbors = {}
  def add_neighbor(self, node, weight):
    self.neighbors[node.key] = weight
    
  def __str__(self):
    string = ""
    key = ""
    for nodes in self.neighbors:
      key += "- " + nodes + "\n"
    string = "name: " + self.key + "\n" + "neighbors:\n" + key
    return string

node = Node("New York")
node2 = Node("San Francisco")
node3 = Node("Washington D.C.")
node4 = Node("Seattle")
node5 = Node("Los Angeles")
node6 = Node("Boston")


node6.add_neighbor(node3, 2)
node6.add_neighbor(node, 1)
node.add_neighbor(node2, 6)
node3.add_neighbor(node4, 7)
node4.add_neighbor(node2, 3)
node2.add_neighbor(node5, 1)


class Graph:
  def __init__(self):
    self.graph = {}
  def add_node(self, node):
    self.graph[node.key] = node
  
  def add_edge(self, node, node2, time):
    if node.key in self.graph and node2.key in self.graph:
      if node not in node2.neighbors and node2 not in node.neighbors:
        node.add_neighbor(node2, time)
        node2.add_neighbor(node, time)
    else:
      print("One of the nodes you are trying to connect is not there.")
  def __str__(self):
    str = ""
    for nodes in self.graph.values():
      str += nodes.__str__() + "\n"
    return str
  
  
  def manual_search(self, start, end):
    hours = 0
    while start != end:
      
      print("\nYou are in " + start.key + ". Here are the available flights and their travel times.")
      
      for n in start.neighbors:
        print("City: " + n + " | Time: " + str(start.neighbors[n]) + " | Key: " + n)
      
      place = input("\nType in the key of the place you would like to go: ")
      
      hours += start.neighbors[place]
      
      start = self.graph[place]
    if start == end:
      print("\nYou made it to " + end.key + "! It took you " + str(hours) + " hours.")

airport = Graph()
airport.add_node(node)
airport.add_node(node2)
airport.add_node(node3)
airport.add_node(node4)
airport.add_node(node5)
airport.add_node(node6)

airport.add_edge(node6, node3, 2)
airport.add_edge(node6, node, 1)
airport.add_edge(node, node2, 6)
airport.add_edge(node3, node4, 7)
airport.add_edge(node4, node2, 3)
airport.add_edge(node2, node5, 1)

airport.manual_search(node6, node5)
