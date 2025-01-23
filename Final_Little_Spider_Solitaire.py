'''
Name:Nitai Mahat

This program plays a version of Little Spider Solitaire. In this version
the foundation piles starting with two red aces and two black kings
are created when the game begins. The eight tableau piles are in
one horizontal line. At any time, cards can be moved from the
tableau to the foundation piles or to another tableau, as long as
it is a valid move. One point is earned for every valid move to
a foundation pile.

'''

from board import *
from button import *
from deck import *
from card import *
import time

GAME_WINDOW_WIDTH = 750
GAME_WINDOW_HEIGHT = 500

def displayDirections():
    """
    Gives the directions for Little Spider Solitaire. To continue the game,
    the "Click to Begin" button must be clicked.

    """
    win = GraphWin("Directions", 700, 600)
    win.setBackground("white")
    string = ("Welcome to Little Spider Solitaire\n\n"
                "The objective is to get all cards\n"
                "into the foundation piles which are built\n"
                "sequentially from cards of the same suit.\n\n"
                "The top card in any tableau can be moved\n"
                "either to a foundation pile, to another\n"
                "tableau if its rank is one above or\n"
                "below the tableau's current top card, or\n"
                "moved to an empty tableau.\n\n"
                "No more moves? Click the stock pile to get\n"
                "eight more cards.\n\n"
                "Good luck!")
    directions = Text(Point(win.getWidth()/ 2, win.getHeight()/2), string)
    directions.setSize(16)
    directions.draw(win)
    startButton = Button(Point(350, 525), 120, 40, "Click to Begin")
    startButton.draw(win)
    startButton.activate()
    click = win.getMouse()
    while not startButton.isClicked(click):
        click = win.getMouse()
    win.close()

def setUpGame():
    '''
    Creates the window with a start button, the tableaus, the stock pile, the
    foundation, and the label for scoring an Aces Up solitaire game. When the
    start button is clicked one card is dealt to each tableau and the button
    is renamed Quit.
    
    Returns:
        the window where the game will be played, the board managing the cards,
        the button now labeled Quit, and the scoring label.
    '''
    win = GraphWin('Little Spider Solitaire', GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT)
    win.setBackground('lightgreen')
    
    gameBoard = LittleSpiderBoard(win)
    
    button = Button(Point(675, 50), 80, 40, "Start")
    button.draw(win)
    button.activate()
    
    scoreLabel = Text(Point(70, 450), "Score: 0")
    scoreLabel.setSize(16)
    scoreLabel.draw(win)
    
    click = win.getMouse()
    while not button.isClicked(click):
        click = win.getMouse()
    
    button.setLabel("Quit")
    
    gameBoard.dealFromStock(win)
    return win, gameBoard, button, scoreLabel


def playGame(window, gameBoard, button, scoreLabel):
    """
    Plays the Little Spider Solitaire game enforcing the rules.

    Params:
        window (GraphWin): the window where the game is played.
        gameBoard (LittleSpiderBoard): the board managing the cards.
        button (Button): the button to click to end the game.
        scoreLabel (Text): the label showing the game score as the game progresses.

    Returns:
        score (int): the score earned by the player determined by the number of
        cards moved to the foundation piles.
        winScreen (Bool): returns True when player Wins.
    """
    gameRunning = True
    score = 0
    selectedCard = None

    while gameRunning:
        click = window.getMouse()

    
        if gameBoard.isPointInTableauCard(click):
            if selectedCard is None:
                selectedCard = gameBoard.getCardAtPoint(click)
            else:
                targetCard = gameBoard.getCardAtPoint(click)
                cardRank = selectedCard.getRank()
                targetRank = targetCard.getRank()

                if selectedCard.isRed() and cardRank == targetRank + 1 or cardRank == targetRank  -1 or (cardRank == 1 and targetRank == 13) or(cardRank == 13 and targetRank == 1):
                    gameBoard.moveCardToAnotherTableauPile(selectedCard, click, window)
                elif not selectedCard.isRed() and cardRank == targetRank + 1:
                    gameBoard.moveCardToAnotherTableauPile(selectedCard, click, window)

                selectedCard = None
                
        elif gameBoard.isPointInEmptyTableau(click):
            if selectedCard:  
                gameBoard.moveCardToAnotherTableauPile(selectedCard, click, window)
                selectedCard = None
      
        elif gameBoard.isPointInFoundationCard(click):
            if selectedCard:
                foundationCard = gameBoard.getCardAtPoint(click)
                cardSuit = selectedCard.getSuit()
                foundationSuit = foundationCard.getSuit()
                cardRank = selectedCard.getRank()
                foundationRank = foundationCard.getRank()

                if selectedCard.isRed() and foundationSuit == cardSuit and cardRank == foundationRank + 1:
                    gameBoard.moveCardToFoundationPile(selectedCard, click, window)
                    score += 1
                    scoreLabel.setText(f"Score: {score}")
                elif not selectedCard.isRed() and foundationSuit == cardSuit and cardRank == foundationRank - 1:
                    gameBoard.moveCardToFoundationPile(selectedCard, click, window)
                    score += 1
                    scoreLabel.setText(f"Score: {score}")

                selectedCard = None

     
        elif gameBoard.isPointInStockCard(click):
            if not gameBoard.isStockEmpty():
                gameBoard.dealFromStock(window)

      
        elif button.isClicked(click):
            gameRunning = False

     
        if gameBoard.isWin():
            winScreen = True
            gameRunning = False
        else:
            winScreen = False


    window.close()

  
    return score,winScreen



def endGameWindow(score,winScreen):
    """
    Displays a pop-up window with the final score and a message based on the player's performance.

    Params:
        score (int): The final score achieved by the player.
    """
    win = GraphWin("Game Over", 300, 200)
    win.setBackground("lightblue")
    
    if winScreen:
        message = "Amazing! You Win!"
    elif score < 10:
        message = "Were you even trying?"
    elif score < 20:
        message = "You can do better!"
    elif score < 40:
        message = "Great job! almost there!"
    else:
        message = "Amazing! You're a pro!"


    scoreText = Text(Point(150, 80), f"Your Final Score: {score}")
    scoreText.setSize(12)
    scoreText.draw(win)

    messageText = Text(Point(150, 120), message)
    messageText.setSize(12)
    messageText.setStyle("bold")
    messageText.draw(win)

    
    quitButton = Button(Point(150, 160), 100, 40, "Quit")
    quitButton.draw(win)
    quitButton.activate()
    click = win.getMouse()

    if quitButton.isClicked(click):
        win.close()
        exit(-1)
   
def main():

    displayDirections()


    window, gameBoard, button, scoreLabel = setUpGame()


    score,winScreen = playGame(window, gameBoard, button, scoreLabel)

 
    endGameWindow(score,winScreen)
    
if __name__ == '__main__':
    main()
