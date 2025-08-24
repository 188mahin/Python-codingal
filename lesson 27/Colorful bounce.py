import pygame as p
import random as r
p.init()
SPRITE_COLOR_CHANGE_EVENT=p.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT=p.USEREVENT+2
BLUE=p.Color("blue")
LIGHTBLUE=p.Color("lightblue")
DARKBLUE=p.Color("darkblue")

YELLOW=p.Color("yellow")
RED=p.Color("red")
GREEN=p.Color("green")
MAGENTA=p.Color("magenta")

class Sprite(p.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=p.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[r.choice([-1,1]),r.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        
        boundry_hit=False
        
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundry_hit=True
        if self.rect.top<=0 or self.rect.bottom>=500:
            self.velocity[1]=-self.velocity[1]
            boundry_hit=True
        if boundry_hit:
            p.event.post(p.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            p.event.post(p.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(r.choice([MAGENTA,YELLOW,RED,GREEN]))
def change_background_color():
    global bg_color
    bg_color=r.choice([BLUE,LIGHTBLUE,DARKBLUE])
all_sprite_list=p.sprite.Group()
sp1=Sprite(YELLOW,50,30)
sp1.rect.x=(r.randint(0,450))
sp1.rect.y=(r.randint(0,450))
all_sprite_list.add(sp1)
screen=p.display.set_mode((500,500))
bg_color=BLUE
screen.fill(bg_color)
exit=False
clock=p.time.Clock()
while not exit:
    for event in p.event.get():
        if event.type==p.QUIT:
            exit=True
        elif event.type==SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type==BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()
    all_sprite_list.update()
    screen.fill(bg_color)
    all_sprite_list.draw(screen)
    p.display.flip()
    clock.tick(240)
p.quit()