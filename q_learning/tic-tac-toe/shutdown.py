dangerZone = []

def detect(enemy, game):
    global dangerZone
    if enemy == 'O':
        cnt = 0
        index = -1
        if game[0][0] == 'O':
            cnt += 1
        else:
            index = 0
        if game[0][1] == 'O':
            cnt += 1
        else:
            index = 1
        if game[0][2] == 'O':
            cnt += 1
        else:
            index = 2
        if cnt == 2:
            dangerZone.append(index)
        ############################
        cnt = 0
        index = -1
        if game[1][0] == 'O':
            cnt += 1
        else:
            index = 3
        if game[1][1] == 'O':
            cnt += 1
        else:
            index = 4
        if game[1][2] == 'O':
            cnt += 1
        else:
            index = 5
        if cnt == 2:
            dangerZone.append(index)
        ############################
        cnt = 0
        index = -1
        if game[2][0] == 'O':
            cnt += 1
        else:
            index = 6
        if game[2][1] == 'O':
            cnt += 1
        else:
            index = 7
        if game[2][2] == 'O':
            cnt += 1
        else:
            index = 8
        if cnt == 2:
            dangerZone.append(index)
        ############################
        cnt = 0
        index = -1
        if game[0][0] == 'O':
            cnt += 1
        else:
            index = 0
        if game[1][0] == 'O':
            cnt += 1
        else:
            index = 3
        if game[2][0] == 'O':
            cnt += 1
        else:
            index = 6
        if cnt == 2:
            dangerZone.append(index)
        ############################
        cnt = 0
        index = -1
        if game[0][1] == 'O':
            cnt += 1
        else:
            index = 1
        if game[1][1] == 'O':
            cnt += 1
        else:
            index = 4
        if game[2][1] == 'O':
            cnt += 1
        else:
            index = 7
        if cnt == 2:
            dangerZone.append(index)
        ############################
        cnt = 0
        index = -1
        if game[0][2] == 'O':
            cnt += 1
        else:
            index = 2
        if game[1][2] == 'O':
            cnt += 1
        else:
            index = 5
        if game[2][2] == 'O':
            cnt += 1
        else:
            index = 8
        if cnt == 2:
            dangerZone.append(index)
        ############################
        cnt = 0
        index = -1
        if game[0][0] == 'O':
            cnt += 1
        else:
            index = 0
        if game[1][1] == 'O':
            cnt += 1
        else:
            index = 4
        if game[2][2] == 'O':
            cnt += 1
        else:
            index = 8
        if cnt == 2:
            dangerZone.append(index)
        ############################
        cnt = 0
        index = -1
        if game[0][2] == 'O':
            cnt += 1
        else:
            index = 2
        if game[1][1] == 'O':
            cnt += 1
        else:
            index = 4
        if game[2][0] == 'O':
            cnt += 1
        else:
            index = 6
        if cnt == 2:
            dangerZone.append(index)
        ############################
        dangerZone = sorted(dangerZone)
        n = 9
        for temp in dangerZone:
            if temp == n:
                dangerZone.remove(temp)
            n = temp
        return True

def getShutDownPos():
    global dangerZone
    return dangerZone
