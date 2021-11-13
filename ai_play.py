from logic2ai import*
import copy
states_reached = 0

class evaluator():
    def __init__(self):
        self.evaluator = 0
        self.board = []

def minimax(board ,depth ,player, alpha, beta,phase ,eval):

    finalEvaluation = evaluator()

    global states_reached
    states_reached += 1

    if depth != 0:
        currentEvaluation = evaluator()

        if player == 1:
            if phase == 1:
                possible_configs = stage1Moves(board)
            else:
                possible_configs = stage23Moves(board)
    
        else:
            if phase == 1:
                possible_configs = generateInvertedBoardList(stage1Moves(InvertedBoard(board)))
            else:
                possible_configs = generateInvertedBoardList(stage23Moves(InvertedBoard(board)))

        for move in possible_configs:
            if player == 1:

                currentEvaluation = minimax(move, depth - 1, 2, alpha, beta, phase, eval)

                if currentEvaluation.evaluator > alpha:
                    alpha = currentEvaluation.evaluator
                    finalEvaluation.board = move

            else:

                currentEvaluation = minimax(move, depth - 1, 1, alpha, beta, phase, eval)
               
                if currentEvaluation.evaluator < beta:
                    beta = currentEvaluation.evaluator
                    finalEvaluation.board = move

        if player == 1:
            
            finalEvaluation.evaluator = alpha
        
        else:
            finalEvaluation.evaluator = beta

    else:
        if player == 1:
            
            finalEvaluation.evaluator = eval(board, phase)
        else:
            finalEvaluation.evaluator = eval(InvertedBoard(board), phase)
    
    return finalEvaluation

def board_to_point(board, depth ,player ,alpha, beta, phase, eval):
    place = None
    dele = None
    st = None
    end = None
    if phase == 1:
        newboard = minimax(board, depth ,player ,alpha, beta, phase, eval).board
        for i in range(len(board)):
            if board[i] == 3 and newboard[i] == 2 :
                place = i

            if board[i] ==1 and newboard[i]==3:
                dele = i
        return place, dele
    else:
        new_board = minimax(board,depth,player,alpha,beta,phase,eval).board
        for i in range(24):
            if board[i] == 2 and new_board[i] == 3:
                st = i
            if board[i] == 3 and new_board[i] == 2:
                end = i
            if board[i] == 1 and new_board[i] == 3:
                dele = i
        return st,end,dele
    
    