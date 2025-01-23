'''


The Card class represents one standard poker card from a poker deck. Each Card has an image, rank, and suit.
The card stores its position in a graphics window. It can be drawn and undrawn, moved a distance
in the x or y directions, and determine if a point is within the boundaries of the card.


'''
from graphics2 import *
import time

class Card: 

    
    def __init__(self,fileName):
        '''
            Initializes a Card object.
    
            Params:
                fileName (str): The file name of the card image, including its rank and suit.
        '''
        self.image = Image(Point(0,0),fileName)
        slashFind = fileName.rfind('/')
        dotFind = fileName.rfind('.')
        self.rank = int(fileName[slashFind+1:dotFind-1])
        self.suit = fileName[dotFind-1]
    
    def getRank(self):
        
        '''
            Returns the rank of the card.
    
            Returns:
                int: The rank of the card.
        '''
        return self.rank
    
    def getSuit(self):
        
        '''
            Returns the suit of the card.
    
            Returns:
                str: The suit of the card (e.g., 'h' for hearts, 'd' for diamonds).
        '''
        return self.suit
    
    def getImage(self):
        
        '''
            Returns the image object of the card.
    
            Returns:
                Image: The image object representing the card.
        '''
        return self.image
    
    def draw(self,window):
        
        '''
            Draws the card's image on the given window.
    
            Params:
                window (GraphWin): The window where the card should be drawn.
        '''
        self.image.draw(window)
    
    def undraw(self):
        
        '''
            Removes the card's image from the window.
        '''
        self.image.undraw()
        
    def isRed(self):
        
        '''
            Checks if the card is red.
    
            Returns:
                bool: True if the card is a heart ('h') or diamond ('d'), otherwise False.
        '''
        if self.suit in ['d','h']:
            return True
        else:
            return False
        
    def move(self,dx, dy):
        
        '''
            Moves the card by the given x and y amounts.
    
            Params:
                dx (float): The amount to move the card in the x-direction.
                dy (float): The amount to move the card in the y-direction.
        '''
        self.image.move(dx,dy)
   
    def containsPoint(self,point):
        
        '''
            Checks if a given point is within the card's boundaries.
    
            Params:
                point (Point): The point to check.
    
            Returns:
                bool: True if the point is inside the card, otherwise False.
        '''
        width = self.image.getWidth()
        height = self.image.getHeight()
        center = self.image.getCenter()
        cardLeft = center.x - width / 2
        cardRight = center.x + width / 2
        cardTop = center.y - height / 2
        cardBottom = center.y + height / 2

        return cardTop <= point.y <= cardBottom and cardLeft <= point.x <= cardRight
        
    
    def __eq__(self, cardToCompare):
        '''
        Allows users of the Card class to compare two cards using ==
        
        Params:
            cardToCompare (Card): the Card to check for equality with this Card
        
        Returns:
            True if the two cards have the same rank and suit. Otherwise, False
        '''
        return self.suit == cardToCompare.suit and self.rank == cardToCompare.rank
    
        
            
    def __str__(self):
        
        '''
            Returns a string representation of the card.
    
            Returns:
                str: A string showing the card's suit, rank, and the center of its image.
        '''
        return f'suit = {self.suit}, rank = {self.rank}, center = {self.image.getCenter()}'

def main():  
    window = GraphWin("Card Class Testing", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    if (isinstance(card.getRank(), int)):
        print('Rank stored as an int')
    else:
        print('Rank was not stored as an int. Fix it!')
    print(card.getSuit())
    print(card.getImage())
    print(card.isRed())
    
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click only on the card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click only on the card should move it 200 pixels right and 100 pixels down
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 100)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Spades card
    fileName = 'cards/2s.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
    print(card2.isRed())
    
    # move card2 to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        
        