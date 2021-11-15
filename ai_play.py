from logic2ai import*
import copy
states_reached = 0

class evaluator():
    def __init__(self):
        self.evaluator = 0 #คะแนน   
        self.board = [] #บอร์ด

def minimax(board ,depth ,isPlayer1, alpha, beta,phase ,eval): 

    finalEvaluation = evaluator()

    global states_reached
    states_reached += 1

    if depth != 0:
        currentEvaluation = evaluator()

        if isPlayer1:
            #stage1Moves และ stage23Moves ใช้เพื่อเก็บลิสต์ของการเดินทั้งหมดที่สามารถเดินได้
            if phase == 1:
                possible_configs = stage1Moves(board) 
            else:
                possible_configs = stage23Moves(board)
    
        else:
            #InvertedBoard คือ สลับหมากในบอร์ดจาก 1 เป็น 2 และ 2 เป็น 1 เพื่อที่จะสามารถใช้ฟังก์ชันเดียวกันได้ในการคำนวนของอีกฝั่ง
            if phase == 1:
                possible_configs = generateInvertedBoardList(stage1Moves(InvertedBoard(board)))
            else:
                possible_configs = generateInvertedBoardList(stage23Moves(InvertedBoard(board)))

        for move in possible_configs: #loop board ทั้งหมดใน possible_configs
            if isPlayer1:

                currentEvaluation = minimax(move, depth - 1, False, alpha, beta, phase, eval) #recursive

                if currentEvaluation.evaluator > alpha: #ถ้าคะแนนของบอร์ดปัจจุบัน มากกว่า alpha(alphaเริ่มต้น = -inf)
                    alpha = currentEvaluation.evaluator #alpha = คะแนนของทางเดินนั้น
                    finalEvaluation.board = move  #อัพเดตบอร์ดตัวที่มีคะเเนนมากกว่า

            else:

                currentEvaluation = minimax(move, depth - 1, True, alpha, beta, phase, eval)
               
                if currentEvaluation.evaluator < beta: #ถ้าคะแนนของบอร์ดปัจจุบัน มากกว่า beta(betaเริ่มต้น = inf)
                    beta = currentEvaluation.evaluator #beta = คะแนนของทางเดินนั้น
                    finalEvaluation.board = move  #อัพเดตบอร์ดตัวที่มีคะเเนนมากกว่า

        if isPlayer1:
            
            finalEvaluation.evaluator = alpha #อัพเดตคะเเนน
        
        else:
            finalEvaluation.evaluator = beta #อัพเดตคะเเนน

    else:
        if isPlayer1:
            
            finalEvaluation.evaluator = eval(board, phase) #เก็บคะเเนนของบอร์ด
        else:
            finalEvaluation.evaluator = eval(InvertedBoard(board), phase) #เก็บคะเเนนของบอร์ด
    
    return finalEvaluation

def board_to_point(board, depth ,isPlayer1 ,alpha, beta, phase, eval):
    place = None
    dele = None
    st = None
    end = None
    if not isPlayer1:
        if phase == 1:
            newboard = minimax(board, depth ,isPlayer1 ,alpha, beta, phase, eval).board
            for i in range(len(board)):
                if board[i] == 3 and newboard[i] == 2 :
                    place = i

                if board[i] ==1 and newboard[i]==3:
                    dele = i
            return place, dele
        else:
            new_board = minimax(board,depth,isPlayer1,alpha,beta,phase,eval).board
            for i in range(24):
                if board[i] == 2 and new_board[i] == 3:
                    st = i
                if board[i] == 3 and new_board[i] == 2:
                    end = i
                if board[i] == 1 and new_board[i] == 3:
                    dele = i
            return st,end,dele
    
    