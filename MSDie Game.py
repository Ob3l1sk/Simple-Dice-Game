#Verison: 1.0.1.5 12/8/2023 2:14pm
from MSDie import *
from graphics import *
from Button import *
from NumberDisplay import *
def main():
    winnings = 0
    guesses = 0
    center = Point(400, 300)
    dice = MSDie(6)
    w = GraphWin("MSDie Game", 800, 600)
    w.setBackground("green")
    label = Text(Point(400, 20), "Click The Button To Roll The Dice")
    label.draw(w)
    winningsDisplay = NumberDisplay(w, winnings, Point(400, 470), 50, "Winnings")
    winningsDisplay.display("blue")
    diceDisplay = NumberDisplay(w,dice.getValue(),Point(120,130), 50, "Dice Rolls")
    diceDisplay.display("blue")
    playerDisplay = NumberDisplay(w,guesses,Point(120, 250),50,"Player Guesses")
    playerDisplay.display("blue")
    subButton = Button(w, center, 300, 50, "Press To Roll!")
    subButton.activate()
    entry = Entry(Point(400, 200), 5)
    entry.setText("")
    entry.draw(w)
    game = True
    print("To play the game type a number 1-6 in the box and press the button.")
    print("If you win you'll win $3.")
    print("But if you lose you'll lose -$1")
    while game:
        message = Text(Point(400, 515), "")
        exitButton = Button(w, Point(400, 550), 100, 40, "Exit")
        exitButton.activate()
        p = w.getMouse()
        if exitButton.clicked(p):
            w.close()
            game = False
        elif subButton.clicked(p):
            dice.roll()
            diceText = Text(Point(400, 250), f"Dice Roll: {dice.getValue()}")
            playerResponse = entry.getText()
            playerChoice = int(playerResponse)
            if playerChoice >= int(7):
                w.close()
                break
            elif playerChoice == dice.getValue():
                winnings += 3
                message.setText("Congrats You Won!")
                guesses += 1
            else:
                winnings -= 1
                message.setText("Incorrect You Lose!")
                guesses += 1 
            winningsDisplay.changeNumber(winnings)
            diceDisplay.changeNumber(dice.getValue())
            playerDisplay.changeNumber(guesses)
            diceText.draw(w)
            message.draw(w)
            w.getMouse()
            message.undraw()
            diceText.undraw()
        else:
            w.close()
            break
main()
