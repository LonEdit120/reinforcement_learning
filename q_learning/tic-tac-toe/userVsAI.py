import train
import circle
import cross
import random

train.train(100000)
AIdata = {}
index = 0

print('\033c')
while True:
    train.clearMap()
    user = input('Please choose which side you want to be : \n1. circle\n2. cross\n')
    if user == '1':
        AIdata = cross.getBoard()
        print('\033c')
        print('You just picked Circle ! You should go first\n')
        while True:
            print('\033c')
            game = train.getGame()
            if train.whoWon(game) != 'nobody':
                if train.whoWon(game) == 'even':
                    print ('\nNobody won ! It was an even game !\n')
                else:
                    print ('\n' + train.whoWon(game) + ' is the Winner !\n')
                break
            index = int(input('\nPlease input which index you want to place : \n\n 0 | 1 | 2\n-----------\n 3 | 4 | 5\n-----------\n 6 | 7 | 8\n\n'))
            print('\033c')

            if (index == 0 or index == 1 or index == 2 or index == 3 or index == 4 or index == 5 or index == 6 or index == 7 or index == 8) and game[int(index/3)][index%3] == ' ':
                train.defPlace('O',index,game)
                print ('Placed at [' + str(int(index/3)) + '][' + str(index%3) + ']')
                game = train.getGame()
                if train.whoWon(game) == 'nobody':
                    tempScore = []
                    choose = []
                    for i in range(len(game)):
                        for j in range(len(game[i])):
                            if game[i][j] == ' ':
                                tempGame = game
                                tempGame = train.place('X',3*i+j,game)
                                if circle.checkExist(hash(tempGame)):
                                    tempScore.append(circle.getScore(hash(tempGame)))
                                else:
                                    tempScore.append(0)
                            else:
                                tempScore.append(-100)
                    for i in range(len(tempScore)):
                        if tempScore[i] == max(tempScore):
                            choose.append(i)
                    rand = random.randint(0,len(choose)-1)
                    # print('O placed at ' + str(choose[rand]))
                    train.defPlace('X',choose[rand],game)

            else:
                print ('Placed failure ! Please follow the index input instructions above or check if the box is empty!')

    elif user == '2':
        '''
        AIdata = cross.getBoard()
        print('\033c')
        print('You just picked Cross ! AI would go first\n')
        while True:
            print('\033c')
            game = train.getGame()
            if train.whoWon(game) != 'nobody':
                if train.whoWon(game) == 'even':
                    print ('\nNobody won ! It was an even game !\n')
                else:
                    print ('\n' + train.whoWon(game) + ' is the Winner !\n')
                break

            if train.whoWon(game) == 'nobody':
                tempScore = []
                choose = []
                for i in range(len(game)):
                    for j in range(len(game[i])):
                        if game[i][j] == ' ':
                            tempGame = game
                            tempGame = train.place('X',3*i+j,game)
                            if cross.checkExist(hash(tempGame)):
                                tempScore.append(cross.getScore(hash(tempGame)))
                            else:
                                tempScore.append(0)
                        else:
                            tempScore.append(-100)
                for i in range(len(tempScore)):
                    if tempScore[i] == max(tempScore):
                        choose.append(i)
                rand = random.randint(0,len(choose)-1)
                # print('O placed at ' + str(choose[rand]))
                game = train.defPlace('X',choose[rand],game)

            index = int(input('\nPlease input which index you want to place : \n\n 0 | 1 | 2\n-----------\n 3 | 4 | 5\n-----------\n 6 | 7 | 8\n\n'))
            t = index
            print('\033c')
            if (t == 0 or t == 1 or t == 2 or t == 3 or t == 4 or t == 5 or t == 6 or t == 7 or t == 8):
                train.defPlace('O',t,game)
                print ('Placed at [' + str(int(t/3)) + '][' + str(t%3) + ']')
                game = train.getGame()
                print('?')
            else:
                print ('Placed failure ! Please follow the index input instructions above or check if the box is empty!')
        '''
        print('Cross is current unavailable due to unknown bug')
    else:
        print('\033c')
        print('Input 1 or 2 for circle or cross !!!\n')
