import pygame as p
p.init()
screen=p.display.set_mode((500,500))
p.display.set_caption("Image game")
backImage=p.transform.scale(p.image.load("backgroundpyhton.png").convert(),(500,500))
penguinImage=p.transform.scale(p.image.load("penguinpython.png").convert_alpha(),(500,500))
penguin_rect=penguinImage.get_rect(center=(500//2,500//2-30))
text=p.font.Font(None,36).render("hello i am penguin",True,p.Color("blue"))
text_rect=text.get_rect(center=(500//2,500//2+110))
def gameloop():
    clock=p.time.Clock()
    running=True
    while running:
        for event in p.event.get():
            if event.type==p.QUIT:
                running=False
        screen.blit(backImage,(0,0))
        screen.blit(penguinImage,penguin_rect)
        screen.blit(text,text_rect)
        p.display.flip()
        clock.tick(30)
    p.quit()
if __name__=="__main__":
    gameloop()