from pygame.display import update
from ai_play import *
from eval import numberOfPiecesEval
from logic import jumpable, movable
depth = 3
player = 2
alpha = float('-inf')
beta = float('inf')
phase = 1

board = [
    1,          2,          2,
        1,      2,      3,
            3,  3,  3,
    3,  3,  3,      3,  3,  1,
            3,  3,  3,
        3,      3,      3,
    3,          3,          1,           
    ]

board2 = [
    1,          3,          3,
        1,      1,      1,
            3,  3,  3,
    3,  3,  3,      3,  1,  2,
            2,  2,  3,
        2,      1,      1,
    1,          3,          1,           
    ]

board3 = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
print(minimax(board3,depth,False,alpha,beta,3,numberOfPiecesEval).board)
# print(board_to_point(board3,depth,False,alpha,beta,1,numberOfPiecesEval))