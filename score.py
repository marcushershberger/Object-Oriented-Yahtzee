def value(_dice, _value):
    total = 0
    for x in _dice:
        if (x == _value):
            total = total + _value
    return total

def fullHouse(_dice):
    counts = [0,0,0,0,0,0]
    for x in _dice:
        counts[x-1] = counts[x-1] + 1
    return 25 if (2 in counts and 3 in counts) else 0

def smallStraight(_dice):
    return 30 if ((hasVal(_dice, 3) and hasVal(_dice, 4)) and ((hasVal(_dice, 1) and hasVal(_dice, 2)) or (hasVal(_dice, 2) and hasVal(_dice, 5)) or (hasVal(_dice, 5) and hasVal(_dice, 6)))) else 0

def largeStraight(_dice):
    return 40 if (hasVal(_dice, 2) and hasVal(_dice, 3) and hasVal(_dice, 4) and hasVal(_dice, 5) and (diceSum(_dice) == 15 or diceSum(_dice) == 20)) else 0

def chance(_dice):
    return diceSum(_dice)

def yahtzee(_dice, _ss):
    return (scoreYahtzee(_ss)) if (_dice[0] == _dice[1] and _dice[1] == _dice[2] and _dice[2] == _dice[3] and _dice[3] == _dice[4]) else 0

def threeOfAKind(_dice):
    counts = [0,0,0,0,0,0]
    for x in _dice:
        counts[x-1] = counts[x-1] + 1
    return (diceSum(_dice)) if (3 in counts or 4 in counts or 5 in counts) else 0

def fourOfAKind(_dice):
    counts = [0,0,0,0,0,0]
    for x in _dice:
        counts[x-1] = counts[x-1] + 1
    return (diceSum(_dice)) if (4 in counts or 5 in counts) else 0

def diceSum(_dice):
    return _dice[0] + _dice[1] + _dice[2] + _dice[3] + _dice[4]

def scoreYahtzee(ss):
    if ss.yahtzees < 1:
        return 50
    else:
        return 100

def hasVal(dice, val):
    for x in dice:
        if x == val:
            return True
    return False