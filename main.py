import pygame
import sys
from PIL.ImageChops import screen
from pygame.locals import *
from ai_play import board_to_point, minimax
from eval import numberOfPiecesEval, AdvancedHeuristic , moveableEval
from config import *
from logic import *
from ai import *
from aiplayer import*

from pygame.surface import *

import time
import pygame.freetype
import re
import random

waittime = 0

depth = 3
player = 2
alpha = float('-inf')
beta = float('inf')
phase = 1

def draw_board():
    pygame.init()

    # Initializing surface
    surface = pygame.display.set_mode((650, 650))
    pygame.display.set_caption("Nine men's morris")

    # Initialing Color
    color = (255, 0, 0)

    for x in range(len(LINES)):
        pygame.draw.line(surface, WHITE,
                         (LINES[x][0] * SQUARESIZE, SQUARESIZE * LINES[x][1]),
                         (LINES[x][2] * SQUARESIZE, LINES[x][3] * SQUARESIZE), 5)

    for r in range(ROWS):
        for c in range(COLS):
            radius = RADIUS
            color2 = WHITE
            if (int(CURRENTBOARDPOSITION[r][c]) == PLAY1):  # p1 is red
                (color2, radius) = (RED, radius)
            elif (int(CURRENTBOARDPOSITION[r][c]) == PLAY2):  # p2 is blue
                (color2, radius) = (BLUE, radius)
            elif (int(BOARDPOSTION[r][c] == VALID)):
                radius = int(RADIUS / 2)
            else:
                radius = 0

            pygame.draw.circle(surface, color2,
                               (int(c * SQUARESIZE + SQUARESIZE / 2),
                                int(r * SQUARESIZE + SQUARESIZE / 2)), radius)

# phase 1


def mainAutoPhase1():
    global round
    for round in range(9):
        # print("round ", round + 1)
        for i in range(2):  # i = 0 is player 1, i = 1 is player 2
            # print("Player " + str(i+1) + " round")
            draw_board()
            pygame.display.update()
            time.sleep(waittime)
            while (True):

                if i == 0:
                    #cdn = randomPlace()  # using random ai
                    cdn = findBestMove(board, i+1, 1) #using Max's AI

                else:

                    cdn,dele = board_to_point(board,depth,player,alpha,beta,1,numberOfPiecesEval) #using Book's AI
                    

                if placeable(i, cdn):  # only check if placeable
                    break

            placePawn(i + 1, cdn)
            draw_board()
            pygame.display.update()
            time.sleep(waittime)

            if checkMill(i + 1, cdn) :  # after placing, check if a mill is formed
                if i == 0:
                    #autoDelete(2)  # using random ai
                    deletePawn(2, findBestMill(board, 2))
                    draw_board()
                    pygame.display.update()
                    time.sleep(waittime)
                else:
                    if(dele!=None):
                        targetedDelete(1, dele)  # using algorithm
                        draw_board()
                        pygame.display.update()
                        time.sleep(waittime)

    print("This is the end of phase 1")

# phase 2


def mainAutoPhase2():
    global round, phase3EndFlag, phase3StartFlag, player1Phase3Flag
    istie = False
    round += 1
    print("Welcome to Phase 2 of the game!")
    print("You can now move the pawn in the board next to their starting point.")
    print("Same rule applies.")

    while (True):
        round += 1
        print("round " + str(round))

        draw_board()
        pygame.display.update()
        time.sleep(waittime)

        for i in range(2):
            # print("Player " + str(i+1) + " round")
            # if player1Phase3Flag:
            #     player1Phase3Flag = False
            #     continue
            draw_board()
            pygame.display.update()
            time.sleep(waittime)
            # Move
            while (True):
                if i == 0:
                    #st, end = randomMove(i + 1)  # using random ai
                    st, end = findBestMove(board, i+1, 2)
                    print(1)
                    print(board)
                else:

                    # using algorithm
                    st,end,dele = board_to_point(board,depth,player,alpha,beta,2,numberOfPiecesEval)
                    print(st,end,dele)

                    if end == -1 or st == -1 or (end in movablePawn[st] == False):
                        print('FAILSAFE ACTIVE')
                        # FAILSAFE WHEN EITHER IS INVALID
                        st, end = randomMove(i + 1)
                        

                if movable(i + 1, st, end):
                    break

            move(i + 1, st, end)
            draw_board()
            pygame.display.update()
            time.sleep(waittime)

            if checkMill(i + 1, end):
                if i == 0:
                    #autoDelete(2)  # using random ai
                    deletePawn(2, findBestMill(board, 2))
                    draw_board()
                    pygame.display.update()
                    time.sleep(waittime)
                else:
                    if(dele!=None):
                        targetedDelete(1, dele)  # using algorithm
                        draw_board()
                        pygame.display.update()
                        time.sleep(waittime)
            print(flag3phase())
            print(phase3EndFlag)
            if flag3phase():
                if i == 0:
                    mainAutoPhase3(2)
                    break
                else:
                    mainAutoPhase3(1)
                    break
            elif playerPawn[1] == 2 or playerPawn[2] == 2:
                break

        if round > 99:  # END THE GAME WITH TIE
            istie = True
            break
        if playerPawn[1] == 2 or playerPawn[2] == 2:  # END THE GAME
            break
    print("YEET")
    updateCurrentBoardPosition()
    draw_board()
    time.sleep(waittime)
    pygame.display.update()
    print("This game has ended!")
    if istie:
        print("It's a tie")
    else:
        print("Congrats to player ", i + 1)
    print("Round : ", round)
    print("Player 1 left pawn = "+str(playerPawn[1]))
    print("Player 2 left pawn = "+str(playerPawn[2]))


def mainAutoPhase3(player):
    global round
    round += 1
    print("Welcome to Phase 3 of the game!")
    print("You can now move the pawn in the board in any coordinate that's still an empty spot for one move.")
    print("Same rule applies.")
    print("Player " + str(player) + "round")
    draw_board()
    pygame.display.update()
    time.sleep(waittime)
    while (True):
        print('phase3',player)
        if player == 1:
            #st, end = randomJump(player)  # using 
             st, end = findBestMove(board, 1, 3)
             print(player,st,end)
        else:
            # using algorithm
            st,end,dele = board_to_point(board,depth,player,alpha,beta,3,numberOfPiecesEval)
            print(player,st,end,dele)

            # if end == -1:
            #     print('FAILSAFE ACTIVE')
            #     st, end = randomMove(player)  # FAILSAFE
        #if st in board and end in board and board[st] == player and board[end] == 3:
        if jumpable(player,st,end):
            break
    jump(player, st, end)
    draw_board()
    pygame.display.update()
    time.sleep(waittime)
    if checkMill(player, end):
        if player == 1:
            #autoDelete(2)  # using randomness
            deletePawn(2, findBestMill(board, 2))
            draw_board()
            pygame.display.update()
            time.sleep(waittime)
        else:
            if(dele!=None):
                targetedDelete(1, dele)  # using algorithm
                draw_board()
                pygame.display.update()
                time.sleep(waittime)


def main():
    mainAutoPhase1()
    mainAutoPhase2()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
main()
