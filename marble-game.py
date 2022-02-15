import random
import time

class TreeNode:
  
  def __init__(self, numMarbles, ai):
    self.marbleChildren = []
    self.numMarbles = numMarbles
    self.ai = ai
    self.score = 0
    self.bestChild = None
  
  def add_marbleChildren(self, child):
    self.marbleChildren.append(child)
    
  def __str__(self):
    return str(numMarbles)
    
  def set_best_child(self):
    if self.numMarbles == 0:
      if self.ai == True:
        self.score = -10
        self.bestChild = None
        return
      else:
        self.score = 10 
        self.bestChild = None
        return
    
    for children in self.marbleChildren:
      children.set_best_child()
    
    chosenChild = None
    
    if self.ai == True:
      score = 1000
      for children in self.marbleChildren:
        if children.score < score:
          chosenChild = children
          score = children.score
    else:
      score = -1000
      for children2 in self.marbleChildren:
        if children2.score > score:
          chosenChild = children2
          score = children2.score
    
    self.bestChild = chosenChild
    self.score = score
    

# 
class Tree:
  
  def __init__(self, rootNode):
    self.rootNode = rootNode
    self.build_tree(self.rootNode)
    rootNode.set_best_child()
    
  def build_tree(self, rootNode):
    
    # base case: if 0: return 0
    # recursive case: if > 0: go through all possible states (root-1, root-2, root-3)
      # keep track of all possible states in list
      # if a child can become negative (ex. 2-3), don't add that as a possible state (only >= 0)
    
    if rootNode.numMarbles == 0:
      return 
    
    elif rootNode.numMarbles > 0:
      
      marbleStates = []
      if rootNode.numMarbles-3 >= 0:
        marbleStates.append(rootNode.numMarbles-3)
      if rootNode.numMarbles-2 >= 0:
        marbleStates.append(rootNode.numMarbles-2)
      if rootNode.numMarbles-1 >= 0:
        marbleStates.append(rootNode.numMarbles-1)
      
      isAI = not self.rootNode
      
      for state in marbleStates:
        newChild = TreeNode(state, isAI)
        rootNode.add_marbleChildren(newChild)
        
        if newChild.numMarbles > 0:
          self.build_tree(newChild)
          
  def game_play(self):
    start = self.rootNode
    
    player1 = True
    
    while start.numMarbles > 0:
      
      print()
      print("Number of Marbles Remaining: " + str(start.numMarbles))

      if player1 == True:
        print()
        print("It's Player's turn!")
        pickMarbles = input("How many marbles whould you like to pick up? ")
        start.numMarbles -= int(pickMarbles)
        
        for child in start.marbleChildren:
          if child.numMarbles == start.numMarbles:
            start = child
        
        player1 = False
        
      elif player1 == False:
        print()
        print("It's AI's turn!")
        time.sleep(1)
        print()
        print("AI has picked up " + str(start.numMarbles-start.bestChild.numMarbles) + " marbles.")
        start.numMarbles -= int(start.bestChild.numMarbles)
        start = start.bestChild
        player1 = True

      if start.numMarbles == 0:
        print()
        if player1 == True:
          print("Game Over! The AI has won!")
        elif player1 == False:
          print("Game Over! Player has won!")

instructions = input("Welcome to the Marble Game! In this game, you have a pile of n marbles and the computer and you must take turns picking up marbles. During your turn, you can pick up 1, 2, or 3 marbles. A player wins if the opponent doesn't have marbles to pick up. You can start with upto 20 marbles. \nPress ENTER to play: ")
print()
marbleInput = input("How many marbles do you want to start with? ")
howManyMarbles = int(marbleInput)
marbleRoot = TreeNode(howManyMarbles, False)
marbleTree = Tree(marbleRoot)
marbleTree.game_play()
