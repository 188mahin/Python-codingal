import math as m
import random as r
import pygame as p
SCREEN_WIDTH=1000
SCREEN_HEIGHT=800
PLAYER_X=470
PLAYER_Y=480
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27
p.init()
screen=p.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
p.display.set_caption("Space invader")
icon=p.image.load(r"/Users/mahin/Python codingal/lesson 29/UFOpython.png")
p.display.set_icon(icon)
playerimg=p.image.load(r"/Users/mahin/Python codingal/lesson 29/plyerpython.png")
playerX=PLAYER_X
playerY=PLAYER_Y
playerX_change=0

enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
enemyNum=6
for i in range(enemyNum):
    enemyimg.append(p.image.load(r"/Users/mahin/Python codingal/lesson 29/enemypython.png"))
    enemyX.append(r.randint(0,SCREEN_WIDTH-64))
    enemyY.append(r.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
bulletimg=p.image.load(r"/Users/mahin/Python codingal/lesson 29/bulletpython.png")
bulletX=0
bulletY=PLAYER_Y
bulletX_change=0
bulletY_change=BULLET_SPEED_Y
bullet_state="ready"
score=0
font=p.font.Font("Times New Roman",32)
textX=10
textY=10
gameText=p.font.Font("Times New Roman",64)
def showScore(x,y):
    score=font.render("Score:"+str(score),True,(255,255,255))
    screen.blit(score,(x,y))
def gameOverText():
    gametext=gameText.render("Game Over",True,(255,255,255))
    screen.blit(score,(400,500))

