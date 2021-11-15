from logic import *
from logic2ai import *

board1 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]


def numberOfPiecesEval(board, phase):
    player1Pawn = pawnInBoard(board, 1)
    player2Pawn = pawnInBoard(board, 2)

    if phase == 1:
        eval = 100*(player1Pawn - player2Pawn)
    else:
        eval = 200 * (player1Pawn - player2Pawn)

    return eval


def moveableEval(board, phase):
    eval = 0

    player1Pawn = pawnInBoard(board, 1)
    player2Pawn = pawnInBoard(board, 2)

    player2Moveable = 0

    if phase == 1:
        eval = (100*(player1Pawn - player2Pawn)) - (50 * player2Moveable)

    return eval


def AdvancedHeuristic(board, phase):

    evaluation = 0

    player1Pawn = pawnInBoard(board, 1)
    player2Pawn = pawnInBoard(board, 2)

    numPossibleMillsPlayer1 = getPossibleMillCount(board, 1)
    numPossibleMillsPlayer2 = getPossibleMillCount(board, 2)

    moveablePiecesPlayer1 = 0
    moveablePiecesPlayer2 = 0

    if phase != 1:
        movablePiecesBlack = len(stage23Moves(board))

    potentialMillsPlayer1 = getPiecesInPotentialMillFormation(board, "1")
    potentialMillsPlayer2 = getPiecesInPotentialMillFormation(board, "2")

    if phase != 1:
        if (player1Pawn < 4):
            evaluation += 100 * numPossibleMillsPlayer1
            evaluation += 200 * potentialMillsPlayer2
        else:
            evaluation += 200 * numPossibleMillsPlayer1
            evaluation += 100 * potentialMillsPlayer2
        evaluation -= 25 * movablePiecesBlack
        evaluation += 50 * (player1Pawn - player2Pawn)
    else:
        if player1Pawn < 4:
            evaluation += 100 * numPossibleMillsPlayer1
            evaluation += 200 * potentialMillsPlayer2
        else:
            evaluation += 200 * numPossibleMillsPlayer1
            evaluation += 100 * potentialMillsPlayer2
        evaluation -= 25 * moveablePiecesPlayer2
        evaluation += 50 * (player1Pawn - player2Pawn)

    return evaluation
