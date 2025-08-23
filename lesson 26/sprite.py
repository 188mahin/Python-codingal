import pygame
def main():
    pygame.init()
    Swidth,Sheight=500,500
    window=pygame.display.set_mode((Swidth,Sheight))
    pygame.display.set_caption("color changing sprite")
    colors={
        'red':pygame.Color('red'),
        'green':pygame.Color('green'),
        'blue':pygame.Color('blue'),
        'yellow':pygame.Color('yellow'),
        'white':pygame.Color('white'),
    }
    currentColor=colors['white']
    x,y=30,30
    width,height=60,60
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:x-=3
        if pressed[pygame.K_RIGHT]:x+=3
        if pressed[pygame.K_UP]:y-=3
        if pressed[pygame.K_DOWN]:y+=3
        w=Swidth-width
        h=Sheight-height
        x=min(max(0,x),w)
        y=min(max(0,y),h)
        if x==0: currentColor=colors['blue']
        elif x==w: currentColor=colors['yellow']
        elif y==0: currentColor=colors['red']
        elif y==h: currentColor=colors['green']
        else:currentColor=colors['white']
        window.fill((0,0,0))
        pygame.draw.rect(window,currentColor,pygame.Rect(x,y,width,height))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__=="__main__":
    main()

