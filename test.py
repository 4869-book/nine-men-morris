from pygame.display import update
from ai_play import *
from eval import numberOfPiecesEval
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
    1,          3,          2,
        1,      2,      2,
            2,  1,  3,
    2,  1,  2,      2,  1,  3,
            3,  3,  1,
        2,      1,      3,
    2,          2,          3,           
    ]

# print(board2)
# new_board = minimax(board2,depth,player,alpha,beta,2,numberOfPiecesEval).board
# print(new_board)

# def move(board,depth,player,alpha,beta,phase,numberOfPiecesEval):
#     st = None
#     end = None
#     dele = None
#     new_board = minimax(board2,depth,player,alpha,beta,phase,numberOfPiecesEval).board
#     for i in range(24):
#         if board[i] == 2 and new_board[i] == 3:
#             st = i
#         if board[i] == 3 and new_board[i] == 2:
#             end = i
#         if board[i] == 1 and new_board[i] == 3:
#             dele = i
#     return st,end,dele
# p1 = board_to_point(board,depth,player,alpha,beta,phase,numberOfPiecesEval)
# print(p1)

#(board_to_point(board2,depth,player,alpha,beta,2,numberOfPiecesEval))

bd = [3, 2, 2, 2, 2, 2, 3, 2, 3, 2, 3, 1, 1, 3, 1, 2, 1, 3, 3, 3, 3, 1, 2, 1]

print(board_to_point(bd,depth,player,alpha,beta,2,numberOfPiecesEval))

