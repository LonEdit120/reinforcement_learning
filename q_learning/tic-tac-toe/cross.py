discount = 0.9
learnRate = 0.1
scores = {}

def checkExist(key):
    if not scores:
        return True
    else:
        if key not in scores:
            return True
        else:
            return False

def getScore(key):
    if key not in scores:
        return 0
    else:
        return scores[key]

def update(winner,preKey,curKey):

    if curKey not in scores:
        curScore = 0
        scores[curKey] = 0
    else:
        curScore = scores[curKey]

    if preKey not in scores:
        preScore = 0
        scores[preKey] = 0
    else:
        preScore = scores[preKey]

    if winner == 'O':
        scores[preKey] = preScore + learnRate * ((-1) - curScore)
    if winner == 'X':
        scores[preKey] = preScore + learnRate * ((1) - curScore)
    if winner == 'even':
        scores[preKey] = preScore + learnRate * ((0.3) - curScore)
    if curScore > preScore:
        scores[preKey] = preScore + learnRate * (0 + discount * curScore - preScore)

def getBoard():
    global scores
    print('Xs scoreBoard :')
    for temp in scores:
        print('Key : ' + str(temp) + ' Score : ' + str(scores[temp]))
    return scores


def toFile():
    with open('crossTrainData.txt','w+') as f:
        f.write('          KEY                                SCORE\n')
        for temp in scores:
            f.write('{0:20d}                  '.format(temp) + str(scores[temp]) + '\n')
    print('Cross data successfully imported to crossTrainData.txt !')
