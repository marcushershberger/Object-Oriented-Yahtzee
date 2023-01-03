import csv

def printHighScores():
    with open('scores.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print ("High Scores:")
        for row in csv_reader:
            print (row[0] + "   " + row[1] + " -- " + row[2])
    return

def checkHighScore(_score):
    print ("Game over. Your final score is " + str(_score))
    rows = 1
    with open('scores.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (_score > int(row[2])):
                break
            rows += 1
    if (rows < 11):
        readHighScores(_score, rows)
    return

def readHighScores(_score, _rank):
    data = []
    with open('scores.csv') as read:
        csv_reader = csv.reader(read, delimiter=',')
        for row in csv_reader:
            data.append([row[1], row[2]])
    enterHighScore(_score, _rank, data)

def enterHighScore(_score, _rank, _prev):
    with open('scores.csv', mode='w') as scores:
        score_writer = csv.writer(scores, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rank = 1
        for x in _prev:
            if (rank == _rank):
                name = raw_input("Enter your name:   ")
                score_writer.writerow([str(rank), name, str(_score)])
                score_writer.writerow([str(rank + 1), x[0], x[1]])
                rank += 1
            elif (rank < 11):
                score_writer.writerow([str(rank), x[0], x[1]])
            rank += 1

    return
