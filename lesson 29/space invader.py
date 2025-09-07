import math as m
import random as r
import pygame as p
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_X=370
PLAYER_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27

p.init()
screen=p.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background=p.image.load(r"/Users/mahin/Python codingal/lesson 29/bgGame.png")
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
score_=0
font=p.font.Font("freesansbold.ttf",32)
textX=10
textY=10
gameText=p.font.Font("freesansbold.ttf",64)
def showScore(x,y):
    score=font.render("Score:"+str(score_),True,(255,255,255))
    screen.blit(score,(x,y))
def gameOverText():
    gametext=gameText.render("Game Over",True,(255,255,255))
    screen.blit(gametext,(400,500))
def player(x,y):
    screen.blit(playerimg,(x,y))
def Enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=m.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    return distance<COLLISION_DISTANCE
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in p.event.get():
        if event.type==p.QUIT:
            running=False
        if event.type==p.KEYDOWN:
            if event.key==p.K_LEFT:
                playerX_change=-5
            if event.key==p.K_RIGHT:
                playerX_change=5
            if event.key==p.K_SPACE and bullet_state=="ready":
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
        if event.type==p.KEYUP and event.key in [p.K_LEFT,p.K_RIGHT]:
            playerX_change=0
    playerX+=playerX_change
    playerX=max(0,min(PLAYER_X,SCREEN_WIDTH-64))
    for i in range(enemyNum):
        if enemyY[i]>340:
            for j in range(enemyNum):
                enemyY[j]=2000
            gameOverText()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0 or enemyX[i]>=SCREEN_WIDTH-64:
            enemyX_change[i]*=-1
            enemyY[i]+=enemyY_change[i]
        if isCollision(enemyX[i],enemyY[i],bulletX,bulletY):
            bulletY=PLAYER_Y
            bullet_state="ready"
            score_+=1
            enemyX[i]=r.randint(0,SCREEN_WIDTH-64)
            enemyY[i]=r.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX)
        Enemy(enemyX[i],enemyY[i],i)
    if bulletY<=0:
        bulletY=PLAYER_Y
        bullet_state="ready"
    elif bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    player(playerX,playerY)
    showScore(textX,textY)
    p.display.flip()



