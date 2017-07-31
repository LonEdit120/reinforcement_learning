import circle
import cross
import random

jump = 0.2
game = ((' ',' ',' '),(' ',' ',' '),(' ',' ',' '))

def clearMap():
    global game
    game = ((' ',' ',' '),(' ',' ',' '),(' ',' ',' '))

def showMap(game):
    for temp in game:
        print (temp)

def whoWon(game):
    cnt = 0
    for i in range(3):
        cnt = 0
        for check in game[i]:
            if check == 'O':
                cnt += 1
        if cnt == 3:
            return 'O'
    for i in range(3):
        cnt = 0
        for temp in game:
            if temp[i] == 'O':
                cnt += 1
        if cnt == 3:
            return 'O'
    if game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        return 'O'
    if game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
        return 'O'
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    cnt = 0
    for i in range(3):
        cnt = 0
        for check in game[i]:
            if check == 'X':
                cnt += 1
        if cnt == 3:
            return 'X'
    for i in range(3):
        cnt = 0
        for temp in game:
            if temp[i] == 'X':
                cnt += 1
        if cnt == 3:
            return 'X'
    if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        return 'X'
    if game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':
        return 'X'
    cnt = 0
    for a in game:
        for b in a:
            if b != ' ':
                cnt += 1
    if cnt == 9:
        return 'even'
    return 'nobody'

def place(who, loc, game):
    gameList=[]
    for i in game:
        gameList.append(list(i))

    gameList[int(loc/3)][loc-int(loc/3)*3] = who
    temp = tuple(tuple(x) for x in gameList)
    return temp

def defPlace(who, loc, temp):
    global game
    game = place(who, loc, temp)

def getGame():
    print('Current Game :\n')
    global game
    for i in range(len(game)):
        print (' ' + game[i][0] + ' | ' + game[i][1] + ' | ' + game[i][2])
        if i != 2:
            print('-----------')
    return game

def train(trainTimes):
    OpreKey = 0
    OcurKey = 0
    XpreKey = 0
    XcurKey = 0
    global game
    game = ((' ',' ',' '),(' ',' ',' '),(' ',' ',' '))

    while trainTimes != 0:
        if trainTimes % 5000 == 0:
            print('Remaining train times : ' + str(trainTimes))
        # Initialize
        trainTimes -= 1
        turn = -1
        OpreKey = hash(game)
        while True:
            turn *= -1
            tempScore = []
            choose = []
            if turn == 1: # CIRCLE
                # print('circle')
                for i in range(len(game)):
                    for j in range(len(game[i])):
                        if game[i][j] == ' ':
                            tempGame = game
                            tempGame = place('O',3*i+j,game)
                            if circle.checkExist(hash(tempGame)):
                                tempScore.append(circle.getScore(hash(tempGame)))
                            else:
                                tempScore.append(0)
                        else:
                            tempScore.append(-100)
                # JUMP Selection
                if random.random() > jump:
                    for i in range(len(tempScore)):
                        if tempScore[i] == max(tempScore):
                            choose.append(i)
                    rand = random.randint(0,len(choose)-1)
                    # print('O placed at ' + str(choose[rand]))
                    game = place('O',choose[rand],game)
                else:
                    for i in range(len(tempScore)):
                        if tempScore[i] >= 0:
                            choose.append(i)
                    rand = random.randint(0,len(choose)-1)
                    # print('O placed at ' + str(choose[rand]))
                    game = place('O',choose[rand],game)

                if whoWon(game) == 'O':
                    circle.update(whoWon(game),OpreKey,OcurKey)
                    cross.update(whoWon(game),XpreKey,XcurKey)
                    # print ('Winner : O')
                    # print('============================================================================')
                    # circle.getBoard()
                    # cross.getBoard()
                    break
                elif whoWon(game) == 'even':
                    circle.update('even',OpreKey,OcurKey)
                    cross.update('even',OpreKey,OcurKey)
                    # print('Even !')
                    break
                OcurKey = hash(game)
                # showMap(game)
                circle.update(whoWon(game),OpreKey,OcurKey)
                OpreKey = OcurKey
                # print('-----------------------------------------------')

    ###############################################################################################
            else: #CROSS
                if XpreKey == 0:
                    XpreKey = OcurKey
                # print('Cross')
                for i in range(len(game)):
                    for j in range(len(game[i])):
                        if game[i][j] == ' ':
                            tempGame = game
                            tempGame = place('X',3*i+j,game)
                            if cross.checkExist(hash(tempGame)):
                                tempScore.append(cross.getScore(hash(tempGame)))
                            else:
                                tempScore.append(0)
                        else:
                            tempScore.append(-100)

                # JUMP Selection
                if random.random() > jump:
                    for i in range(len(tempScore)):
                        if tempScore[i] == max(tempScore):
                            choose.append(i)
                    rand = random.randint(0,len(choose)-1)
                    # print('X placed at ' + str(choose[rand]))
                    game = place('X',choose[rand],game)
                else:
                    for i in range(len(tempScore)):
                        if tempScore[i] >= 0:
                            choose.append(i)
                    rand = random.randint(0,len(choose)-1)
                    # print('X placed at ' + str(choose[rand]))
                    game = place('X',choose[rand],game)

                if whoWon(game) == 'X':
                    circle.update(whoWon(game),OpreKey,OcurKey)
                    cross.update(whoWon(game),XpreKey,XcurKey)
                    # print ('Winner : X')
                    # print('============================================================================')
                    # circle.getBoard()
                    # cross.getBoard()
                    break
                else:
                    cnt = 0
                    for a in game:
                        for b in a:
                            if b != ' ':
                                cnt += 1
                    if cnt == 9:
                        circle.update('even',OpreKey,OcurKey)
                        cross.update('even',OpreKey,OcurKey)
                        # print('Even !')
                        break
                XcurKey = hash(game)
                # showMap(game)
                cross.update(whoWon(game),XpreKey,XcurKey)
                XpreKey = XcurKey
                # print('----------------------------------------------------------------------------------------------')
        game = ((' ',' ',' '),(' ',' ',' '),(' ',' ',' '))
    circle.toFile()
    cross.toFile()
