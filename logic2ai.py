import copy

def boardOutput(board):
		
		print(board[0]+"(00)----------------------"+board[1]+"(01)----------------------"+board[2]+"(02)");
		print("|                           |                           |");
		print("|       "+board[3]+"(03)--------------"+board[4]+"(04)--------------"+board[5]+"(05)     |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       |        "+board[6]+"(06)-----"+board[7]+"(07)-----"+board[8]+"(08)       |      |");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print(board[9]+"(09)---"+board[10]+"(10)----"+board[11]+"(11)               "+board[12]+"(12)----"+board[13]+"(13)---"+board[14]+"(14)");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print("|       |        "+board[15]+"(15)-----"+board[16]+"(16)-----"+board[17]+"(18)       |      |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       "+board[18]+"(18)--------------"+board[19]+"(19)--------------"+board[20]+"(20)     |");
		print("|                           |                           |");
		print("|                           |                           |");
		print(board[21]+"(21)----------------------"+board[22]+"(22)----------------------"+board[23]+"(23)");


def pawnInBoard(board,player): #cheak player's pawn in board
    return board.count(player)

def isMill(player, board, pos1, pos2):

	if (board[pos1] == player and board[pos2] == player):
		return True
	return False

def moveableLocation(position):
    movablePawn = [
        [9, 1],
        [4, 0, 2],
        [14, 1],
        [10, 4],
        [7, 1, 3, 5],
        [4, 13],
        [11, 7],
        [4, 6, 8],
        [12, 7],
        [21, 0, 10],
        [18, 3, 9, 11],
        [15, 6, 10],
        [17, 8, 13],
        [20, 5, 12, 14],
        [23, 2, 13],
        [11, 16],
        [19, 15, 17],
        [12, 16],
        [10, 19],
        [22, 16, 18, 20],
        [13, 19],
        [9, 22],
        [19, 21, 23],
        [14, 22]
    ]
    return movablePawn[position]

def checkMillFormation(position, board, player):
    mill =[
        (isMill(player, board, 1, 2) or isMill(player, board, 9, 21)),
        (isMill(player, board, 0, 2) or isMill(player, board, 4, 7)),
        (isMill(player, board, 14, 23) or isMill(player, board, 0, 1)),
        (isMill(player, board, 4, 5) or isMill(player, board, 10, 18)),
        (isMill(player, board, 1, 7) or isMill(player, board, 3, 5)),
        (isMill(player, board, 3, 4) or isMill(player, board, 13, 20)),
        (isMill(player, board, 11, 15) or isMill(player, board, 7, 8)),
        (isMill(player, board, 1, 4) or isMill(player, board, 6, 8)),
        (isMill(player, board, 6, 7) or isMill(player, board, 12, 17)),
        (isMill(player, board, 10, 11) or isMill(player, board, 0, 21)),
        (isMill(player, board, 3, 18) or isMill(player, board, 9, 11)),
        (isMill(player, board, 9, 10) or isMill(player, board, 6, 15)),
        (isMill(player, board, 8, 17) or isMill(player, board, 13, 14)),
        (isMill(player, board, 5, 20) or isMill(player, board, 12, 14)),
        (isMill(player, board, 12, 13) or isMill(player, board, 2, 23)),
        (isMill(player, board, 6, 11) or isMill(player, board, 16, 17)),
        (isMill(player, board, 15, 17) or isMill(player, board, 19, 22)),
        (isMill(player, board, 8, 12) or isMill(player, board, 15, 16)),
        (isMill(player, board, 3, 10) or isMill(player, board, 19, 20)),
        (isMill(player, board, 16, 22) or isMill(player, board, 18, 20)),
        (isMill(player, board, 18, 19) or isMill(player, board, 5, 13)),
        (isMill(player, board, 0, 9) or isMill(player, board, 22, 23)),
        (isMill(player, board, 16, 19) or isMill(player, board, 21, 23)),
        (isMill(player, board, 21, 22) or isMill(player, board, 2, 14)),
    ]
    
    return mill[position]

def isCloseMill(position,board): #check future board mill
    player = board[position]

    if player != 3: #if position is empty
        return checkMillFormation(position, board, player)
    else:
        return False

def removePiece(board_clone, board_list):

	for i in range(len(board_clone)):
		if (board_clone[i] == 2):

			if not isCloseMill(i, board_clone):
				new_board = copy.deepcopy(board_clone)
				new_board[i] = 3
				board_list.append(new_board)
	return board_list

def InvertedBoard(board):
    invertedboard = []
    for i in board:
        if i == 1:
            invertedboard.append(2)
        elif i == 2:
            invertedboard.append(1)
        else:
            invertedboard.append(3)
    return invertedboard

def generateInvertedBoardList(pos_list):
    result = []
    for i in pos_list:
        result.append(InvertedBoard(i))
    return result

def stage1Moves(board): #fill all possibility in phase1 into list
    board_list = []

    for i in range(len(board)):
        # fill empty positions with 3
        if board[i] == 3:
            board_clone = copy.deepcopy(board)
            board_clone[i]=1 

            if isCloseMill(i, board_clone):
                board_list = removePiece(board_clone, board_list)
            else:
                board_list.append(board_clone)
    return board_list

def stage2Moves(board):
    board_list = []
    for i in range(len(board)):
        if board[i] == 1:
            movable_list = moveableLocation(i)

            for pos in movable_list:
                if board[pos] == 3:
                    board_clone = copy.deepcopy(board)
                    board_clone[i] = 3
                    board_clone[pos] = 1

                    if isCloseMill(pos, board_clone):
                        board_list = removePiece(board_clone, board_list)
                    else:
                        board_list.append(board_clone)
    return board_list

def stage3Moves(board):

	board_list = []
	for i in range(len(board)):
		if (board[i] == 1):

			for j in range(len(board)):
				if (board[j] == 3):
					board_clone = copy.deepcopy(board)

					board_clone[i] = 3
					board_clone[j] = 1

					if (isCloseMill(j, board_clone)):
						board_list = removePiece(board_clone, board_list)
					else:
						board_list.append(board_clone)
	return board_list

def stage23Moves(board):
	if (pawnInBoard(board, 1) == 3):
		return stage3Moves(board)
	else:
		return stage2Moves(board)

