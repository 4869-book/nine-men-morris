from logic import *

'''
            if player 1
main.py --> add     --> from aiplayer import *
                    (phase 1)
        --> change  --> from    --> cdn = randomPlace()
                    --> to      --> cdn = findBestMove(board, i+1, 1)
                    (phase 2)
                    --> from    --> st, end = randomMove(i + 1)
                    --> to      --> st, end = findBestMove(board, i+1, 2)
                    (phase 3)
                    --> from    --> st, end = randomJump(player)
                    --> to      --> st, end = findBestMove(board, 1, 3)
                    (mill)
                    --> from    --> autoDelete(2)
                    --> to      --> deletePawn(2, findBestMill(board, 2))
'''

# check if player mill in this index


def curMill(board, player, index):
    b = board.copy()
    i = index
    if b[i] == player:
        for j in range(len(millPosition[i])):
            if b[millPosition[i][j][0]] == player and b[millPosition[i][j][1]] == player:
                # if mill return True
                return True

    # if not mill return False
    return False

# Find opposite player or enemy


def oppPlayer(player):
    return 1 if player == 2 else 2

# find set of mill to compare


def findMillSet(board, player):
    b = board.copy()
    millset = []
    for i in range(len(b)):
        if b[i] == player:
            for j in range(len(millPosition[i])):
                if b[i] == b[millPosition[i][j][0]] and b[i] == b[millPosition[i][j][1]]:
                    # if mill, create set to store
                    millunit = [i, millPosition[i][j]
                                [0], millPosition[i][j][1]]
                    # append to main set
                    millset.append(millunit)

    # return result for compare len
    return millset

# evaluate score for alpha beta pruning


def evaluate(board, player, playerMillSet, enemyMillSet):
    b = board.copy()
    # if player move make more mill or value
    if len(findMillSet(b, player)) > len(playerMillSet):
        return 100
    # if enemy move make more mill or value
    if len(findMillSet(b, oppPlayer(player))) > len(enemyMillSet):
        return -100
    # if player move make less mill, it mean move out from mill set and ready to move in again
    if len(findMillSet(b, player)) < len(playerMillSet):
        return 50
    # if enemy move make less mill, it mean move out from mill set and ready to move in again
    if len(findMillSet(b, oppPlayer(player))) < len(enemyMillSet):
        return -50

    return 0


MAX, MIN = 10000, -10000

# Alpha Beta pruning


def alphaBetaPruning(board, player, phase, depth, playerMillSet, enemyMillSet, alpha, beta, isMax):
    b = board.copy()
    # evaluate score
    score = evaluate(board, player, playerMillSet, enemyMillSet)
    # end condition
    endScore = (-100, 100)
    # end way
    if score in endScore or depth == 3:
        return score

    # if player turn
    if isMax:
        best = MIN
        # loop all posible move
        for i in range(len(b)):
            if phase == 1:
                if b[i] == 3:
                    # do action
                    b[i] = player
                    # recursive
                    val = alphaBetaPruning(
                        b, player, phase, depth+1, playerMillSet, enemyMillSet, alpha, beta, not isMax)
                    # undo action
                    b[i] = 3
                    best = max(best, val)
                    alpha = max(alpha, best)
                    # beta break
                    if beta <= alpha:
                        break
            elif phase == 2:
                if b[i] == player:
                    for j in range(len(movablePawn[i])):
                        if b[movablePawn[i][j]] == 3:
                            # do action
                            b[i] = 3
                            b[movablePawn[i][j]] = player
                            # recursive
                            val = alphaBetaPruning(
                                b, player, phase, depth+1, playerMillSet, enemyMillSet, alpha, beta, not isMax)
                            # undo action
                            b[i] = player
                            b[movablePawn[i][j]] = 3

                            best = max(best, val)
                            alpha = max(alpha, best)
                            # beta break
                            if beta <= alpha:
                                break
            else:
                if b[i] == player:
                    for j in range(len(b)):
                        if b[j] == 3:
                            # do action
                            b[i] = 3
                            b[j] = player
                            # recursive
                            val = alphaBetaPruning(
                                b, player, phase, depth+1, playerMillSet, enemyMillSet, alpha, beta, not isMax)
                            # undo action
                            b[i] = player
                            b[j] = 3

                            best = max(best, val)
                            alpha = max(alpha, best)
                            # beta break
                            if beta <= alpha:
                                break

        return best

    # if enemy turn
    else:
        best = MAX
        for i in range(len(b)):
            if phase == 1:
                if b[i] == 3:
                    # do action
                    b[i] = oppPlayer(player)
                    # recursive
                    val = alphaBetaPruning(
                        b, player, phase, depth+1, playerMillSet, enemyMillSet, alpha, beta, not isMax)
                    # undo action
                    b[i] = 3

                    best = min(best, val)
                    beta = min(beta, best)
                    # beta break
                    if beta <= alpha:
                        break
            elif phase == 2:
                if b[i] == oppPlayer(player):
                    for j in range(len(movablePawn[i])):
                        if b[movablePawn[i][j]] == 3:
                            # do action
                            b[i] = 3
                            b[movablePawn[i][j]] = oppPlayer(player)
                            # recursive
                            val = alphaBetaPruning(
                                b, player, phase, depth+1, playerMillSet, enemyMillSet, alpha, beta, not isMax)
                            # undo action
                            b[i] = oppPlayer(player)
                            b[movablePawn[i][j]] = 3

                            best = min(best, val)
                            beta = min(beta, best)
                            # beta break
                            if beta <= alpha:
                                break
            else:
                if b[i] == oppPlayer(player):
                    for j in range(len(b)):
                        if b[j] == 3:
                            # do action
                            b[i] = 3
                            b[j] = oppPlayer(player)
                            # recursive
                            val = alphaBetaPruning(
                                b, player, phase, depth+1, playerMillSet, enemyMillSet, alpha, beta, not isMax)
                            # undo action
                            b[i] = oppPlayer(player)
                            b[j] = 3

                            best = min(best, val)
                            beta = min(beta, best)
                            # beta break
                            if beta <= alpha:
                                break

        return best


def findBestMove(board, player, phase):
    b = board.copy()
    # compare value
    bestVal = -1000
    # target move or place
    bestMove = -1
    # target destination
    bestDest = -1

    # set to compare player and enemy
    playerMillSet = findMillSet(b, player)
    enemyMillSet = findMillSet(b, oppPlayer(player))
    for i in range(len(b)):
        # phase 1
        if phase == 1:
            if b[i] == 3:
                # do action
                b[i] = player
                # recursive score
                val = alphaBetaPruning(
                    b, player, phase, 0, playerMillSet, enemyMillSet, MIN, MAX, False)
                # undo action
                b[i] = 3
                if val > bestVal:
                    bestVal = val
                    bestMove = i
                # change by random to avoid loop (same move)
                # if val == bestVal:
                #     if random.randint(0, 2) == 1:
                #         bestVal = val
                #         bestMove = i
        # phase 2
        elif phase == 2:
            if b[i] == player:
                for j in range(len(movablePawn[i])):
                    if b[movablePawn[i][j]] == 3:
                        # do action
                        b[i] = 3
                        b[movablePawn[i][j]] = player
                        # recursive score
                        val = alphaBetaPruning(
                            b, player, phase, 0, playerMillSet, enemyMillSet, MIN, MAX, False)
                        # undo action
                        b[i] = player
                        b[movablePawn[i][j]] = 3

                        if val > bestVal:
                            bestVal = val
                            bestMove = i
                            bestDest = movablePawn[i][j]
                        # change by random to avoid loop (same move)
                        # if val == bestVal:
                        #     if random.randint(0, 2) == 1:
                        #         bestVal = val
                        #         bestMove = i
                        #         bestDest = movablePawn[i][j]
        # phase 3
        else:
            if b[i] == player:
                for j in range(len(b)):
                    if b[j] == 3:
                        # do action
                        b[i] = 3
                        b[j] = player
                        # recursive score
                        val = alphaBetaPruning(
                            b, player, phase, 0, playerMillSet, enemyMillSet, MIN, MAX, False)
                        # undo action
                        b[i] = player
                        b[j] = 3

                        if val > bestVal:
                            bestVal = val
                            bestMove = i
                            bestDest = j
                        # change by random to avoid loop (same move)
                        if val == bestVal:
                            if random.randint(0, 2) == 1:
                                bestVal = val
                                bestMove = i
                                bestDest = j

    # final result of each phase
    if phase == 1:
        return bestMove
    elif phase == 2:
        return bestMove, bestDest
    else:
        return bestMove, bestDest

# find score to consider mill index


def findMillScore(board, targetPlayer):
    b = board.copy()
    score = 0
    for i in range(len(b)):
        if b[i] == targetPlayer:
            if b[i] == b[millPosition[i][0][0]] and b[i] == b[millPosition[i][0][1]]:
                score += 10
            if b[i] == b[millPosition[i][1][0]] and b[i] == b[millPosition[i][1][1]]:
                score += 10
            if b[i] == b[millPosition[i][0][0]] or b[i] == b[millPosition[i][0][1]]:
                score += 5
            if b[i] == b[millPosition[i][1][0]] or b[i] == b[millPosition[i][1][1]]:
                score += 5

    return score

# find index to mill


def findBestMill(board, targetPlayer):
    b = board.copy()

    bestTargetMillScore = findMillScore(b, targetPlayer)
    target = -1

    for i in range(len(b)):
        if b[i] == targetPlayer:
            b[i] = 3
            curScore = findMillScore(b, targetPlayer)
            b[i] = targetPlayer

            if curScore < bestTargetMillScore:
                bestTargetMillScore = curScore
                target = i

            # change by random to avoid loop (same move)
            if curScore == bestTargetMillScore:
                if random.randint(0, 2) == 1:
                    bestTargetMillScore = curScore
                    target = i

    return target
