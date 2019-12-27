class Scorecard:
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    bonus = 0
    ttotal = 0
    chance = 0
    threeofakind = 0
    fourofakind = 0
    fullhouse = 0
    smallstraight = 0
    largestraight = 0
    yahtzee = 0
    ybonus = 0
    ltotal = 0
    total = 0
    
    def updateTotals(self):
        self.bonus = 35 if (self.ones + self.twos + self.threes + self.fours + self.fives + self.sixes >= 63) else 0
        self.ttotal = self.ones + self.twos + self.threes + self.fours + self.fives + self.sixes + self.bonus
        self.ltotal = self.chance + self.threeofakind + self.fourofakind + self.fullhouse + self.smallstraight + self.largestraight + self.yahtzee + self.ybonus
        self.total = self.ttotal + self.ltotal
    
    def printCard(self, ss):
        print (ind(ss.ones)) + (" Ones        " + str(self.ones))
        print (ind(ss.twos)) + (" Twos        " + str(self.twos))
        print (ind(ss.threes)) + (" Threes      " + str(self.threes))
        print (ind(ss.fours)) + (" Fours       " + str(self.fours))
        print (ind(ss.fives)) + (" Fives       " + str(self.fives))
        print (ind(ss.sixes)) + (" Sixes       " + str(self.sixes))
        print ("  Bonus       " + str(self.bonus))
        print ("  Top Total   " + str(self.ttotal))
        print ("------------------------")
        print (ind(ss.threeofakind)) + (" 3 of a Kind " + str(self.threeofakind))
        print (ind(ss.fourofakind)) + (" 4 of a Kind " + str(self.fourofakind))
        print (ind(ss.fullhouse)) + (" Full House  " + str(self.fullhouse))
        print (ind(ss.smallstraight)) + (" Sm Straight " + str(self.smallstraight))
        print (ind(ss.largestraight)) + (" Lg Straight " + str(self.largestraight))
        print (ind(ss.chance)) + (" Chance      " + str(self.chance))
        print (ind(ss.yahtzee)) + (" Yahtzee     " + str(self.yahtzee))
        print ("  Bonus       " + str(self.ybonus))
        print ("  Lower Total " + str(self.ltotal))
        print (">   TOTAL     " + str(self.total))
        print ""
        return
    
def ind(_ss):
    return " " if _ss else "|"
