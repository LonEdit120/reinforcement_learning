import random

reward = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
action = [-1,1]

discount = 0.9
learnRate = 0.1
jump = 0.05
trainTimes = 100

steps = []

scoreBoard= [[0 for x in range(len(reward))] for y  in range(len(reward))]
for i in range(len(scoreBoard)):
    if i != len(scoreBoard)-1:
        scoreBoard[i][len(reward)-1] = 1
    else:
        for j in range(len(scoreBoard[i])):
            scoreBoard[i][j] = 1

def update(curScore, biggerScore, nextLocation):
    if nextLocation == len(reward) - 1:
        newScore = curScore + learnRate * (1 - curScore)
    else:
        newScore = curScore + learnRate * (0 + discount*biggerScore - curScore)
    return newScore

for i in range(trainTimes):
    step = 0
    loc = 0
    score = 0
    pre = 0
    #rand = random.randint(0,3)
    while(loc != len(reward)-1):

        step += 1
        #pre = loc
        score = scoreBoard[pre][loc]
        if loc == 0:
            if step == 1:
                pre = loc
                loc += 1
            else:
                rightScore = scoreBoard[loc][loc+1]
                if rightScore > score:
                    scoreBoard[pre][loc] = update(scoreBoard[pre][loc], rightScore, loc+1)
                pre = loc
                loc += 1
        else:
            leftScore  = scoreBoard[loc][loc-1]
            rightScore = scoreBoard[loc][loc+1]

            if random.random() > jump:

                if leftScore > rightScore:
                    if leftScore > score:
                        scoreBoard[pre][loc] = update(scoreBoard[pre][loc], leftScore, loc-1)
                    pre = loc
                    loc -= 1

                elif rightScore > leftScore:
                    if rightScore > score:
                        scoreBoard[pre][loc] = update(scoreBoard[pre][loc], rightScore, loc+1)
                    pre = loc
                    loc += 1

                else:
                    rand = action[random.randint(0,1)]
                    nextScore = scoreBoard[loc][loc+rand]
                    if nextScore > score:
                        scoreBoard[pre][loc] = update(scoreBoard[pre][loc], nextScore, loc+rand)
                    pre = loc
                    loc += rand

            else:

                if leftScore < rightScore:
                    if leftScore > score:
                        scoreBoard[pre][loc] = update(scoreBoard[pre][loc], leftScore, loc-1)
                    pre = loc
                    loc -= 1

                elif rightScore < leftScore:
                    if rightScore > score:
                        scoreBoard[pre][loc] = update(scoreBoard[pre][loc], rightScore, loc+1)
                    pre = loc
                    loc += 1

                else:
                    rand = action[random.randint(0,1)]
                    nextScore = scoreBoard[loc][loc+rand]
                    if nextScore > score:
                        scoreBoard[pre][loc] = update(scoreBoard[pre][loc], nextScore, loc+rand)
                    pre = loc
                    loc += rand
    steps.append(step)
    print ('Round ' + "{:0>2d}".format(i) + ', step : ' + str(step))
print ('At Round : ' + str(steps.index(min(steps))) + ', we found the best solution ' + str(min(steps)) +' steps.')

print ('Total State length : ' + str(len(reward)))

#for temp in scoreBoard:
#    print (temp)
