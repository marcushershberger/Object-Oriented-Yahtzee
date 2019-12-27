class ScoreSet:
    scored = False
    rolls = 0
    yahtzees = 0
    ones = False
    twos = False
    threes = False
    fours = False
    fives = False
    sixes = False
    chance = False
    threeofakind = False
    fourofakind = False
    fullhouse = False
    smallstraight = False
    largestraight = False
    yahtzee = False
    ybonus = False
    movesLeft = True
    
    def checkAvailability(self):
        self.movesLeft = not (self.ones and self.twos and self.threes and self.fours and self.fives and self.sixes and self.chance and self.threeofakind and self.fourofakind and self.fullhouse and self.smallstraight and self.largestraight and self.yahtzee)