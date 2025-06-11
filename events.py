import pygame

pygame.init()

WIDTH=600
HEIGHT=600

screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((124, 191, 230))


class circ():
    def __init__(self,x,y,r,c):
        self.x=x
        self.y=y
        self.r=r
        self.c=c
        self.surf=screen


    def draw(self):
        pygame.draw.circle(self.surf,self.c,(self.x,self.y),self.r)

    def biggercirc(self):
        self.r=self.r+10
        pygame.draw.circle(self.surf,self.c,(self.x,self.y),self.r)

    def up(self):
        self.y=self.y-10
        pygame.draw.circle(self.surf,self.c,(self.x,self.y),self.r)

    def right(self):
        self.x=self.x+10
        pygame.draw.circle(self.surf,self.c,(self.x,self.y),self.r)   


bluecirc=circ(300,300,10,"blue")
bluecirc.draw()

    










run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            redcirc=circ(pos[0],pos[1],10,"red")
            redcirc.draw()
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill((124, 191, 230))
            bluecirc.biggercirc()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                screen.fill((124, 191, 230))
                bluecirc.up()
            if event.key==pygame.K_RIGHT:
                screen.fill((124, 191, 230))
                bluecirc.right()
        if event.type== pygame.QUIT:
            pygame.quit()
    pygame.display.update()