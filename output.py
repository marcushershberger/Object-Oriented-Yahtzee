one = " ------- \n|       |\n|   o   |\n|       |\n ------- "
two = " ------- \n| o     |\n|       |\n|     o |\n ------- "
three = " ------- \n| o     |\n|   o   |\n|     o |\n ------- "
four = " ------- \n| o   o |\n|       |\n| o   o |\n ------- "
five = " ------- \n| o   o |\n|   o   |\n| o   o |\n ------- "
six = " ------- \n| o   o |\n| o   o |\n| o   o |\n ------- "
held = " HELD"

dicePatterns = [one,two,three,four,five,six]

def printDice(_dice, heldVals):
    val = 0
    for x in _dice:
        print dicePatterns[x-1] + (held if heldVals[val] else "")
        val = val + 1
    print ""
    return
