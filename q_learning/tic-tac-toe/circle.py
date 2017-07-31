discount = 0.9
learnRate = 0.1
scoreBoard = []
preKey = 0
curKey = 0
newScore = 0
def setCurKey(key):
    curKey = key

def setPreKey(key):
    preKey = key

def checkExist(key):
    if not scoreBoard:
        return True
    else:
        for temp in scoreBoard:
            if temp["key"] == key:
                return True
            else:
                return False

def getScore(key):
    if key not in scoreBoard:
        return 0
    else:
        for temp in scoreBoard:
            if temp["key"] == key:
                return temp["score"]

def update(winner,preKey,curKey):
    # print('Os preKey : ' + str(preKey))
    # print('Os curKey : ' + str(curKey))

    exist = False
    for i in range(len(scoreBoard)):
        if scoreBoard[i]["key"] == curKey:
            curScore = scoreBoard[i]["score"]
            exist = True
            break
    if (not exist):
        curScore = 0
        scoreBoard.append({"key":curKey,"score":0})

    exist = False
    for j in range(len(scoreBoard)):
        if scoreBoard[j]["key"] == preKey:
            preScore = scoreBoard[j]["score"]
            exist = True
            break
    if (not exist):
        scoreBoard.append({"key":preKey,"score":0})
        preScore = 0
        #print('bugged : O preKey ' + str(preKey) + ' not found===========')

    if winner == 'X':
        scoreBoard[j]["score"] = preScore + learnRate * ((-1) - curScore)
    if winner == 'O':
        scoreBoard[j]["score"] = preScore + learnRate * ((1) - curScore)
    if winner == 'even':
        scoreBoard[j]["score"] = preScore + learnRate * ((0.3) - curScore)
    if curScore > preScore:
        scoreBoard[j]["score"] = preScore + learnRate * (0 + discount * curScore - preScore)

    # print('Os scoreBoard :')
    # for temp in scoreBoard:
    #     print(temp)

def getBoard():
    print('Os scoreBoard :')
    for temp in scoreBoard:
        print(temp)

def toFile():
    with open('circleTrainData.txt','w+') as f:
        f.write('          KEY                                SCORE\n')
        for temp in scoreBoard:
            f.write('{0:20d}                  '.format(temp['key']) + str(temp['score'])+'\n')
    print('Circle train data successfully imported to circleTrainData.txt !')
