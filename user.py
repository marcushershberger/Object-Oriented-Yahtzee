from score import *
from output import *

def printKeys():
    print "(1-5) Hold   (q) ones    (w) twos"
    print "(e) threes   (r) fours   (t) fives"
    print "(y) sixes    (a) 3 match (s) 4 match"
    print "(d) full hs  (f) sm str  (g) lg str"
    print "(h) chance   (j) yahtzee (k) roll"
    print "(z) keys     (x) card    (c) dice"
    print ""
    return

def getInput():
    userInput = raw_input("Enter action:  ")
    while (notValid(userInput)):
        userInput = raw_input("Enter a scoring method, roll, or print keybinds (z):  ")
    return userInput

def notValid(_input):
    validInputs = ["1","2","3","4","5","q","w","e","r","t","y","a","s","d","f","g","h","j","k","z","x","c"]
    return not _input in validInputs

def handleMethod(usrInput, sc, ss, heldV, _dice):
    if (usrInput == "1"):
        heldV[0] = not heldV[0]
        printDice(_dice, heldV)
        return "The hold on die " + usrInput + " was toggled"
    elif (usrInput == "2"):
        heldV[1] = not heldV[1]
        printDice(_dice, heldV)
        return "The hold on die " + usrInput + " was toggled"
    elif (usrInput == "3"):
        heldV[2] = not heldV[2]
        printDice(_dice, heldV)
        return "The hold on die " + usrInput + " was toggled"
    elif (usrInput == "4"):
        heldV[3] = not heldV[3]
        printDice(_dice, heldV)
        return "The hold on die " + usrInput + " was toggled"
    elif (usrInput == "5"):
        heldV[4] = not heldV[4]
        printDice(_dice, heldV)
        return "The hold on die " + usrInput + " was toggled"
    elif (usrInput == "q" and not ss.ones):
        sc.ones = value(_dice, 1)
        ss.ones = True
        ss.scored = True
        return "You scored " + str(sc.ones) + " points this move"
    elif (usrInput == "w" and not ss.twos):
        sc.twos = value(_dice, 2)
        ss.twos = True
        ss.scored = True
        return "You scored " + str(sc.twos) + " points this move"
    elif (usrInput == "e" and not ss.threes):
        sc.threes = value(_dice, 3)
        ss.threes = True
        ss.scored = True
        return "You scored " + str(sc.threes) + " points this move"
    elif (usrInput == "r" and not ss.fours):
        sc.fours = value(_dice, 4)
        ss.fours = True
        ss.scored = True
        return "You scored " + str(sc.fours) + " points this move"
    elif (usrInput == "t" and not sc.fives):
        sc.fives = value(_dice, 5)
        ss.fives = True
        ss.scored = True
        return "You scored " + str(sc.fives) + " points this move"
    elif (usrInput == "y" and not ss.sixes):
        sc.sixes = value(_dice, 6)
        ss.sixes = True
        ss.scored = True
        return "You scored " + str(sc.sixes) + " points this move"
    elif (usrInput == "a" and not ss.threeofakind):
        sc.threeofakind = threeOfAKind(_dice)
        ss.threeofakind = True
        ss.scored = True
        return "You scored " + str(sc.threeofakind) + " points this move"
    elif (usrInput == "s" and not ss.fourofakind):
        sc.fourofakind = fourOfAKind(_dice)
        ss.fourofakind = True
        ss.scored = True
        return "You scored " + str(sc.fourofakind) + " points this move"
    elif (usrInput == "d" and not ss.fullhouse):
        sc.fullhouse = fullHouse(_dice)
        ss.fullhouse = True
        ss.scored = True
        return "You scored " + str(sc.fullhouse) + " points this move"
    elif (usrInput == "f" and not ss.smallstraight):
        sc.smallstraight = smallStraight(_dice)
        ss.smallstraight = True
        ss.scored = True
        return "You scored " + str(sc.smallstraight) + " points this move"
    elif (usrInput == "g" and not ss.largestraight):
        sc.largestraight = largeStraight(_dice)
        ss.largestraight = True
        ss.scored = True
        return "You scored " + str(sc.largestraight) + " points this move"
    elif (usrInput == "h" and not ss.chance):
        sc.chance = chance(_dice)
        ss.chance = True
        ss.scored = True
        return "You scored " + str(sc.chance) + " points this move"
    elif (usrInput == "j" and not ss.yahtzee):
        newPoints = yahtzee(_dice, ss)
        sc.yahtzee = sc.yahtzee + newPoints
        ss.yahtzee = True
        ss.scored = True
        return "You scored " + str(newPoints) + " points this move"
    else:
        return "You have already used that move"
    
    
        