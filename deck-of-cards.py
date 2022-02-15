import random

class Card:

  def __init__(self, value, suit):
    self.value = value
    self.suit = suit
  def __str__(self):
    return str(self.value) + " of " + str(self.suit)

class Deck: 
  
  def __init__(self):
    self.deck = []
    cardSuits = ["clubs", "spades", "hearts", "diamonds"]
    for elements in cardSuits:
      for i in range(1, 14):
        myCards = Card(i, elements)
        self.deck.append(myCards)
  def __str__(self):
    string = ""
    for elems in self.deck:
      string += str(elems) + "\n"
    return string
  def draw_card(self):
    if len(self.deck) > 0:
      first = self.deck[0]
      self.deck.remove(first)
      return first
    else:
      print("No cards to draw.")
  def shuffle(self):
    newDeck = []
    while len(self.deck) > 0:
      randOrder = random.randint(0, len(self.deck)-1)
      card = self.deck[randOrder]
      self.deck.remove(card)
      newDeck.append(card)
    self.deck = newDeck

myDeck = Deck()
print(myDeck)
myDeck.shuffle()
print()
print(myDeck)
print()
print(myDeck.draw_card())
print(myDeck.draw_card())
print(myDeck.draw_card())
