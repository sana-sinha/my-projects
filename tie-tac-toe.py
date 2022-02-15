import random
import time

class TreeNode:
  
  def __init__(self, board, player):
    self.board = board
    self.player = player
    self.children = []
    self.score = 0
    self.bestChild = None
  
  def add_children(self, node):
    self.children.append(node)
  
  def print_board(self):
    string = ""
    print("  0 1 2")
    counter = -1
    for rows in self.board:
      counter += 1
      string += str(counter)+" "
      for elems in rows:
        string += elems+" "
      print(string)
      string = ""
 
  def check_win(self):
    # check each row for a winner
    if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != '-':
      return self.board[0][0], True
    elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != '-' :
      return self.board[1][0], True
    elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != '-':
      return self.board[2][0], True
    # check each column for a winner
    if self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != '-':
      return self.board[0][0], True
    elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != '-':
      return self.board[0][1], True
    elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != '-':
      return self.board[0][2], True
    # check each diagonal for a winner
    if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-':
      return self.board[0][0], True
    if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '-':
      return self.board[0][2], True
    return "None", False
 
  def check_tie(self):
    winOrLose = self.check_win()
    if winOrLose[1] == False: #No win
      for rows in self.board:
        for elems in rows:
          if elems == "-":
            return False
      return True
  
  def set_best_child(self):
    if self.check_win()[1] == True:
      #print("line 77")
      if self.check_win()[0] == "X":
        #print("line 79")
        self.score = -10
        self.bestChild = None
        return
      elif self.check_win()[0] == "O":
        #print("line 84")
        self.score = 10 
        self.bestChild = None
        return
    
    elif self.check_tie() == True:
      #print("line 90")
      self.score = 0
      self.bestChild = None
      return 
    '''
    elif self.check_win()[1] == False:
      print("line 96")
      self.score = 0
      self.bestChild = None
      return
    '''
    for children in self.children:
      #print("SETTING BEST CHILD FOR EVERY CHILDREN")
      children.set_best_child()
    
    # minimax algorithm
    chosenChild = None
    if self.player == "O":
      best = -1000
      for child in self.children:
        if child.score > best:
          #print("choosing best child!")
          chosenChild = child
          best = child.score
    elif self.player == "X":
      best = 1000
      for child2 in self.children:
        if child2.score < best:
         # print("choosing best child 2!")
          chosenChild = child2
          best = child2.score
    
    self.bestChild = chosenChild
    self.score = best
  def randomAI(self, ogBoard):
    # allows computer to place their piece in a random available position
    while True:
      rPosition = random.randint(0, len(ogBoard)-1)
      ePosition = random.randint(0, len(ogBoard)-1)  
      if ogBoard[rPosition][ePosition] == "-":
        return rPosition, ePosition

turn = ""


class Tree:
  
  instructions = input("Welcome to the Tic Tac Toe AI Game, where you can play Tic Tac Toe against a random AI. You will be Player X and the computer will be Player O. Press ENTER to start.")
    
  def __init__(self, rootNode):
    self.root = rootNode
    self.ai = ""
    self.user = ""
    self.build_tree(self.root)
    self.root.set_best_child()
    
  def dBoard(self, ogBoard):
    # allows to print a new board after each move
    newBoard = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    for rows in range(0, len(ogBoard)):
      for elems in range(0, len(ogBoard[rows])):
        newBoard[rows][elems] = ogBoard[rows][elems]
    return newBoard
    
  
  def build_tree(self, root):

    childPlayer = ""
    # if game over
    if root.check_win()[1] == True:
      return 
    # switch players each row of tree
    if root.player == "X":
      childPlayer = "O"
    else:
      childPlayer = "X"
    # for all 9 spots on board, if there is a space
    for rows in range(0, len(root.board)):
      for cols in range(0, len(root.board[rows])):
        if root.board[rows][cols] == "-":
          # duplicate root board, dupe board is the other player
          newRoot = self.dBoard(root.board)
          newRoot[rows][cols] = root.player
          childTree = TreeNode(newRoot, childPlayer)
          root.add_children(childTree)
    for children in root.children:
      self.build_tree(children)
  
  def complexAI(self):
    # allows computer to place their piece in a strategic  position
    self.build_tree(self.root)


  def gamePlay(self):
    start = self.root
    start.print_board()
  
    while True: 
      # goes down tree from root --> terminal b
      print("It is now your turn.")
      row = int(input("Which row would you like to place your " + start.player + "? ")) #TODO: to reflect the changes in player use start.player
      column = int(input("Which column would you like to place your " + start.player + "? "))

      for children in start.children:
        if children.board[row][column] == start.player:
          #print("child found!")
          #print(children.board)
          ##error here
          start = children

          if start.check_win()[1] == True and start.check_win()[0] == "X":
            print("The winner is X!")
            break
          break
          
      start.print_board()

        # AI start 
      if start.check_tie() == False:
        print("It is now the computer's turn.")
        time.sleep(1)

        start = start.bestChild
        start.print_board()
        start.player
      if start.check_win()[1] == True:
        print("The winner is " + start.check_win()[0] + "!")
        break
      elif start.check_tie() == True:
        print("There is a tie. No winner.")
        break
  
myBoard = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

player = "X"
player2 = "O"

tree = TreeNode(myBoard, player)
treeC = Tree(tree)

print()
treeC.gamePlay()
