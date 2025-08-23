import pygame
pygame.init()
screen=pygame.display.set_mode((1000,1000))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(35,125,210),pygame.Rect(30,30,60,60))
    pygame.display.flip()