import random
import circle
import cross
import ooxx

ooxx.train()

while True:
    print('Hi, you are circle')
    side = True
    Xpre = 0
    game = ooxx.getGame()
    scores = {}
    winBlock = []
    badBlock = []
    dontSkip = True
    dangerZone = []
    while ooxx.checkResult(game) == 0:
        if side:
            ooxx.printGame()
            index = int(input('Please input where you want to place : '))
            ooxx.fill(1,index)
            side = not side
        else:
            game = ooxx.getGame()
            if Xpre == 0:
                Xpre = game
            else:
                Xpre = Xcur
            for i in range(9):# SEEK VICTORY
                if ooxx.getValueAtIndex(i, game) == 0:
                    if ooxx.checkResult(ooxx.place(2,i)) == 2:
                        dontSkip = False
                        winBlock.append(i)

            if dontSkip:
                ooxx.shutdown(1)
                if not dangerZone:# SAFE (empty)
                    danger = False
                    tempScore = []
                    for i in range(9):
                        if ooxx.getValueAtIndex(i, game) == 0:
                            cross.update(ooxx.checkResult(ooxx.place(2,i)), Xpre, ooxx.place(2,i))
                            tempScore.append(cross.getScore(ooxx.place(2,i)))
                        else:
                            tempScore.append(-200)
                    tempIndex = []
                    for i in range(len(tempScore)):
                        if tempScore[i] == max(tempScore):
                            tempIndex.append(i)
                    temp = len(tempIndex)-1
                    # print ('WTF?' + str(temp))
                    # print(tempScore)
                    rand = random.randint(0,temp)
                    ooxx.fill(2,tempIndex[rand])
                else:             # DANGER
                    danger = True
                    for temp in dangerZone:
                        cross.update(3,Xpre,ooxx.place(2,temp))
                    scores = cross.getBoard()
                    # printScores()
                    temp = len(dangerZone)-1
                    rand = random.randint(0,temp)
                    ooxx.fill(2,dangerZone[rand])
            else:
                # VICTORY MOVE
                for i in range(9):
                    if ooxx.getValueAtIndex(i, game) == 0:
                        if ooxx.checkResult(ooxx.place(2,i)) != 2:
                            badBlock.append(i)
                # print ('WinBlocks:')
                # print(winBlock)
                # print ('BadBlocks:')
                # print(badBlock)

                for temp in winBlock:
                    cross.update(2, Xpre, ooxx.place(2,temp))
                scores = cross.getBoard()
                # printScores()
                for temp in badBlock:
                    cross.update(1, Xpre, ooxx.place(2,temp))
                scores = cross.getBoard()
                # printScores()
                break
            if ooxx.checkResult(game) == 3:
                cross.update(3, Xpre, game)
                break
            Xcur = game

            side = not side
    if (ooxx.checkResult(game)) == 1:
        print('O won !')
    elif (ooxx.checkResult(game)) == 2:
        print('X won !')
    elif (ooxx.checkResult(game)) == 3:
        print('Even !')
    ooxx.clearGame()
