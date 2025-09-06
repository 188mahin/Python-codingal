import pygame as p
import random as r
SCREEN_WIDTH=500
SCREEN_HEIGHT=500
MOVEMENT_SPEED=5
FONT_SIZE=72
p.init()
BG=p.transform.scale(p.image.load(r"/Users/mahin/Python codingal/lesson 28/bg.jpg"),(SCREEN_WIDTH,SCREEN_HEIGHT))
FONT=p.font.SysFont("Times New Roman",FONT_SIZE)
class Sprite(p.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=p.Surface([width,height])
        self.image.fill(p.Color("dodgerblue"))
        p.draw.rect(self.image,color,p.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change,SCREEN_WIDTH-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+y_change,SCREEN_HEIGHT-self.rect.height),0)
screen=p.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
p.display.set_caption("Collision")
all_sprites=p.sprite.Group()
all_sprites=p.sprite.Group()
sp1=Sprite(p.Color("red"),50,50)
sp1.rect.x,sp1.rect.y=r.randint(0,SCREEN_WIDTH-sp1.rect.width),r.randint(0,SCREEN_HEIGHT-sp1.rect.height)
all_sprites.add(sp1)
sp2=Sprite(p.Color("green"),50,50)
sp2.rect.x,sp2.rect.y=r.randint(0,SCREEN_WIDTH-sp2.rect.width),r.randint(0,SCREEN_HEIGHT-sp2.rect.height)
all_sprites.add(sp2)
running,won=True,False
clock=p.time.Clock()
while running:
    for event in p.event.get():
        if event.type==p.QUIT or (event.type==p.KEYDOWN and event.type==p.K_x):
            running=False
    if not won:
        keys=p.key.get_pressed()
        x_change=(keys[p.K_RIGHT]-keys[p.K_LEFT])*MOVEMENT_SPEED
        y_change=(keys[p.K_DOWN]-keys[p.K_UP])*MOVEMENT_SPEED
        sp1.move(x_change,y_change)
        if sp1.rect.colliderect(sp2.rect):
            all_sprites.remove(sp2)
            won=True
    screen.blit(BG,(0,0))
    all_sprites.draw(screen)
    if won:
        win=FONT.render("you win",True,p.Color("black"))
        screen.blit(win,((SCREEN_WIDTH-win.get_width())//2,(SCREEN_HEIGHT-win.get_height())//2))
    p.display.flip()
    clock.tick(90)
p.quit()


    
