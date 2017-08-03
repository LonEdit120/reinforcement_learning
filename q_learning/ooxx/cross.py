<<<<<<< HEAD
import json

=======
>>>>>>> c589314ec99f4f569920fa4c594261375289a06b
discount = 0.9
learnRate = 0.1
scores = {}

def update(winner,pre,cur):

    if cur not in scores:
        curScore = 0
        scores[cur] = 0
    else:
        curScore = scores[cur]

    if pre not in scores:
        preScore = 0
        scores[pre] = 0
    else:
        preScore = scores[pre]

    if winner == 1:
        scores[cur] = preScore + learnRate * ((-1) - curScore)
    if winner == 2 or winner == 3:
        scores[cur] = preScore + learnRate * ((1) - curScore)
<<<<<<< HEAD
    curScore = scores[cur]
=======
>>>>>>> c589314ec99f4f569920fa4c594261375289a06b
    if curScore > preScore:
        scores[pre] = preScore + learnRate * (0 + discount * curScore - preScore)

def checkExist(board):
    if not scores:
        return True
    else:
        if board not in scores:
            return True
        else:
            return False

def getScore(board):
    if board not in scores:
        scores[board] = 0
    return scores[board]

<<<<<<< HEAD
=======
def toFile():
    with open('crossTrainData.txt','w+') as f:
        f.write('          KEY                                SCORE\n')
        for temp in scores:
            f.write('{0:20d}                  '.format(temp) + str(scores[temp]) + '\n')
    print('Cross data successfully imported to crossTrainData.txt !')

>>>>>>> c589314ec99f4f569920fa4c594261375289a06b
def getBoard():
    global scores
    #print('Xs scoreBoard :')
    #for temp in scores:
    #    print('Key : ' + str(temp) + ' Score : ' + str(scores[temp]))
    return scores
<<<<<<< HEAD

def toJSON():
    global scores
    with open ('cross.json','w+') as f:
        json.dump(scores, f)

def getJSON():
    global scores
    with open('cross.json') as f:
        scores = json.load(f)
=======
>>>>>>> c589314ec99f4f569920fa4c594261375289a06b
