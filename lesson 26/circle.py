import pygame
pygame.init()
window=pygame.display.set_mode((500,500))
window.fill((255,255,255))
GREEN=(0,255,0)
pygame.draw.circle(window,GREEN,(300,300),50)
pygame.draw.circle(window,GREEN,(100,100),50,5)
pygame.display.update()
running=True
while running:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            running=False
pygame.quit()