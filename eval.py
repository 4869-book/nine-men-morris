from logic import *
from logic2ai import *

#ให้คะแนนโดยการนับจำนวนหมากทั้งหมดของแต่ละฝั่ง
def numberOfPiecesEval(board, phase):
    player1Pawn = pawnInBoard(board, 1)
    player2Pawn = pawnInBoard(board, 2)

    if phase == 1:
        eval = 100*(player1Pawn - player2Pawn)
    else:
        eval = 200 * (player1Pawn - player2Pawn)

    return eval

