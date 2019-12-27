from score import *
from user import *
from output import *
from scorecard import Scorecard
from highscores import *
from game import ScoreSet
from random import randint


sc = Scorecard()
rounds = ScoreSet()
dice = [1,1,1,1,1]
held = [False,False,False,False,False]
holds = ["1","2","3","4","5"]

def useInput(_input):
    if (_input == "k"):
        print "Rolls:  " + (str(rounds.rolls  + 1))
        if rounds.rolls == 3:
            print "You cannot roll again this turn"
            return
        rollDice()
        rounds.rolls = rounds.rolls + 1
    elif (_input == "z"):
        printKeys()
    elif (_input == "x"):
        sc.printCard(rounds)
    elif (_input == "c"):
        printDice(dice, held)
    else:
        print (handleMethod(_input, sc, rounds, held, dice))
    return

def rollDice():
    for i in range(5):
        if not held[i]:
            dice[i] = roll()
    printDice(dice, held)
            
def roll():
    return randint(1,6)


printKeys()

while rounds.movesLeft:
    rounds.rolls = 0
    rounds.scored = False
    held = [False,False,False,False,False]
    sc.updateTotals()
    sc.printCard(rounds)
    useInput("k")
    while not rounds.scored:
        useInput(getInput())
    rounds.checkAvailability()
                
checkHighScore(str(sc.total))  
printHighScores()