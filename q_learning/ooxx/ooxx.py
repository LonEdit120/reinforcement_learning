import random
import circle
import cross
<<<<<<< HEAD
import json
=======
>>>>>>> c589314ec99f4f569920fa4c594261375289a06b

print('\033c')

print('Index helper')
print(' 0 | 1 | 2 ')
print('-----------')
print(' 3 | 4 | 5 ')
print('-----------')
print(' 6 | 7 | 8 ')

<<<<<<< HEAD
jump = 0.3
=======
jump = 0.6
>>>>>>> c589314ec99f4f569920fa4c594261375289a06b
Opre = 0
Ocur = 0
Xpre = 0
Xcur = 0
game = 0
side = True
<<<<<<< HEAD
times = 500000
=======
times = 100000
>>>>>>> c589314ec99f4f569920fa4c594261375289a06b
dangerZone = []

def getValueAtIndex(index, res):
    value = int(res/pow(10,index))%10
    return value

def checkResult(board):
    # print ('Board to be checked : ' + str(board))
    # EVEN
    cnt = 0
    for i in range(9):
        if getValueAtIndex(i, board) != 0:
            cnt += 1
        else:
            game = 0
            break
    # 1 or 2 win
    if cnt == 9:
        return 3
    temp = (getValueAtIndex(0, board) * getValueAtIndex(1, board) * getValueAtIndex(2, board))
    if temp == 1:
        return 1
    elif temp == 8:
        return 2
    temp = (getValueAtIndex(3, board) * getValueAtIndex(4, board) * getValueAtIndex(5, board))
    if temp == 1:
        return 1
    elif temp == 8:
        return 2
    temp = (getValueAtIndex(6, board) * getValueAtIndex(7, board) * getValueAtIndex(8, board))
    if temp == 1:
        return 1
    elif temp == 8:
        return 2
    temp = (getValueAtIndex(0, board) * getValueAtIndex(3, board) * getValueAtIndex(6, board))
    if temp == 1:
        return 1
    elif temp == 8:
        return 2
    temp = (getValueAtIndex(1, board) * getValueAtIndex(4, board) * getValueAtIndex(7, board))
    if temp == 1:
        return 1
    elif temp == 8:
        return 2
    temp = (getValueAtIndex(2, board) * getValueAtIndex(5, board) * getValueAtIndex(8, board))
    if temp == 1:
        return 1
    elif temp == 8:
        return 2
    temp = (getValueAtIndex(0, board) * getValueAtIndex(4, board) * getValueAtIndex(8, board))
    if temp == 1:
        return 1
    elif temp == 8:
        return 2
    temp = (getValueAtIndex(2, board) * getValueAtIndex(4, board) * getValueAtIndex(6, board))
    if temp == 1:
        return 1
    elif temp == 8:
        return 2

    return 0

def place(who, index):
    global game
    tempGame = game + who*pow(10,index)
    return tempGame

def fill(who,index):
    global game
    game = game + who*pow(10,index)

def printGame():
    print('Current Game :')
    global game
    tempList = []
    for i in range(9):
        if getValueAtIndex(i, game) == 0:
            tempList.append(' ')
        elif getValueAtIndex(i, game) == 1:
            tempList.append('1')
        elif getValueAtIndex(i, game) == 2:
            tempList.append('2')
        else:
            tempList.append(' ')
    print (' ' + tempList[0] + ' | ' + tempList[1] + ' | ' + tempList[2])
    print('-----------')
    print (' ' + tempList[3] + ' | ' + tempList[4] + ' | ' + tempList[5])
    print('-----------')
    print (' ' + tempList[6] + ' | ' + tempList[7] + ' | ' + tempList[8])

def shutdown(enemy):
    global dangerZone
    global game
    dangerZone = []
    for i in range(9):
        if getValueAtIndex(i, game) == 0:
            if checkResult(place(enemy,i)) == enemy:
                dangerZone.append(i)
    dangerZone = sorted(dangerZone)
    pre = 9
    for cur in dangerZone:
        if cur == pre:
            dangerZone.remove(cur)
        pre = cur
    # print('Danger detected from ' + str(enemy) + ' at :')
    # print(dangerZone)

def printScores():
    global scores
    for temp in scores:
        tempList = []
        for i in range(9):
            if getValueAtIndex(i, temp) == 0:
                tempList.append(' ')
            elif getValueAtIndex(i, temp) == 1:
                tempList.append('1')
            elif getValueAtIndex(i, temp) == 2:
                tempList.append('2')
        print (' ' + tempList[0] + ' | ' + tempList[1] + ' | ' + tempList[2])
        print('-----------')
        print (' ' + tempList[3] + ' | ' + tempList[4] + ' | ' + tempList[5])
        print('-----------')
        print (' ' + tempList[6] + ' | ' + tempList[7] + ' | ' + tempList[8])
        print ('Score : ' + str(scores[temp]) + '\n===============================================================================')

def getGame():
    global game
    return game

def clearGame():
    global game
    game = 0

def train():
    global jump
    global Opre
    global Ocur
    global Xpre
    global Xcur
    global game
    global side
    global times
    scores = {}
    winBlock = []
    badBlock = []
    # game = 120022100

<<<<<<< HEAD
    circle.getJSON()
    cross.getJSON()
    percent = int(times/100)
    fulltime = times
    while times != 0:
        if times % 5000 == 0:
            circle.toJSON()
            cross.toJSON()
            jump = jump - 0.015
        finished = int(((fulltime - times)/percent)/2)
        unfinished = 50 - finished
        finbar = ''
        for i in range(finished):
            finbar = finbar + '#'
        unfinbar = ''
        for i in range(unfinished):
            unfinbar = unfinbar + '-'
        print('\033c')
        print('Training progress : [' + finbar + unfinbar + '] ( ' + str(finished*2) + '% )')
=======

    while times != 0:
        if times % 5000 == 0:
            print('Remaining train times : ' + str(times))
            jump = jump - 0.03
>>>>>>> c589314ec99f4f569920fa4c594261375289a06b

        game = 0
        times -= 1
        Ocur = game
        Xpre = 0
        # Initialize
        dontSkip = True
        winBlock = []
        badBlock = []

        while True:
            # Initialize
            danger = False
            if side:
                Opre = Ocur
                for i in range(9):# SEEK VICTORY
                    if getValueAtIndex(i, game) == 0:
                        if checkResult(place(1,i)) == 1:
                            dontSkip = False
                            winBlock.append(i)

                if dontSkip:
                    shutdown(2)
                    if not dangerZone:# SAFE (empty)
                        danger = False
                        tempScore = []
                        # print(game)
                        for i in range(9):
                            if getValueAtIndex(i, game) == 0:
                                circle.update(checkResult(place(1,i)), Opre, place(1,i))
                                tempScore.append(circle.getScore(place(1,i)))
                            else:
                                tempScore.append(-100)
                        tempIndex = []
                        if random.random() > jump or max(tempScore) == 0:
                            for i in range(len(tempScore)):
                                if tempScore[i] == max(tempScore):
                                    tempIndex.append(i)
                        else:
                            # print('jumped !')
                            # printGame()
                            for i in range(len(tempScore)):
                                #print(tempScore[i])
                                if (tempScore[i] != max(tempScore)) and tempScore[i] >= 0:
                                    tempIndex.append(i)
                            if len(tempIndex) == 0:
                                tempIndex.append(tempScore.index(max(tempScore)))
                        temp = len(tempIndex)-1
                        # print ('WTF?' + str(temp))
                        # print(tempScore)
                        rand = random.randint(0,temp)
                        fill(1,tempIndex[rand])
                    else:             # DANGER

                        danger = True
                        for temp in dangerZone:
                            circle.update(3,Opre,place(1,temp))
                        scores = circle.getBoard()
                        # printScores()
                        temp = len(dangerZone)-1
                        rand = random.randint(0,temp)
                        fill(1,dangerZone[rand])
                else:

                    # VICTORY MOVE
                    for i in range(9):
                        if getValueAtIndex(i, game) == 0:
                            if checkResult(place(1,i)) != 1:
                                badBlock.append(i)
                    # print ('WinBlocks:')
                    # print(winBlock)
                    # print ('BadBlocks:')
                    # print(badBlock)

                    for temp in winBlock:
                        circle.update(1, Opre, place(1,temp))
                    scores = circle.getBoard()
                    # printScores()
                    for temp in badBlock:
                        circle.update(2, Opre, place(1,temp))
                    scores = circle.getBoard()
                    # printScores()
                    game = 0
                    break
                if checkResult(game) == 3:
                    circle.update(3, Opre, game)
                    game = 0
                    break
                Ocur = game
                side = not side
                # printGame()
                # print('------------------')
            ####################################################################################
            else:
                if Xpre == 0:
                    Xpre = Ocur
                else:
                    Xpre = Xcur
                for i in range(9):# SEEK VICTORY
                    if getValueAtIndex(i, game) == 0:
                        if checkResult(place(2,i)) == 2:
                            dontSkip = False
                            winBlock.append(i)

                if dontSkip:
                    shutdown(1)
                    if not dangerZone:# SAFE (empty)
                        danger = False
                        tempScore = []
                        for i in range(9):
                            if getValueAtIndex(i, game) == 0:
                                cross.update(checkResult(place(2,i)), Xpre, place(2,i))
                                tempScore.append(cross.getScore(place(2,i)))
                            else:
                                tempScore.append(-200)
                        tempIndex = []
                        if random.random() > jump or max(tempScore) == 0:
                            for i in range(len(tempScore)):
                                if tempScore[i] == max(tempScore):
                                    tempIndex.append(i)
                        else:
                            # print('jumped !')
                            # printGame()
                            for i in range(len(tempScore)):
                                #print(tempScore[i])
                                if (tempScore[i] != max(tempScore)) and tempScore[i] >= 0:
                                    tempIndex.append(i)
                            if len(tempIndex) == 0:
                                tempIndex.append(tempScore.index(max(tempScore)))
                        temp = len(tempIndex)-1
                        # print ('WTF?' + str(temp))
                        # print(tempScore)
                        rand = random.randint(0,temp)
                        fill(2,tempIndex[rand])
                    else:             # DANGER
                        danger = True
                        for temp in dangerZone:
                            cross.update(3,Xpre,place(2,temp))
                        scores = cross.getBoard()
                        # printScores()
                        temp = len(dangerZone)-1
                        rand = random.randint(0,temp)
                        fill(2,dangerZone[rand])
                else:
                    # VICTORY MOVE
                    for i in range(9):
                        if getValueAtIndex(i, game) == 0:
                            if checkResult(place(2,i)) != 2:
                                badBlock.append(i)
                    # print ('WinBlocks:')
                    # print(winBlock)
                    # print ('BadBlocks:')
                    # print(badBlock)

                    for temp in winBlock:
                        cross.update(2, Xpre, place(2,temp))
                    scores = cross.getBoard()
                    # printScores()
                    for temp in badBlock:
                        cross.update(1, Xpre, place(2,temp))
                    scores = cross.getBoard()
                    # printScores()
                    game = 0
                    break
                if checkResult(game) == 3:
                    cross.update(3, Xpre, game)
                    game = 0
                    break
                Xcur = game

                side = not side
                # print('--------------------------------------------------')
<<<<<<< HEAD
    print('\033c')
    print('Training progress : [##################################################] ( 100% )')

    circle.toJSON()
    cross.toJSON()
=======

    circle.toFile()
    cross.toFile()
>>>>>>> c589314ec99f4f569920fa4c594261375289a06b
