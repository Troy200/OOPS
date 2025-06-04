import pygame

pygame.init()

WIDTH=600
HEIGHT=600

screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("orange")

class rect():

    def __init__(self,x,y,h,w,c,t):
        self.surf=screen
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.c=c
        self.t=t

    def draw(self):
        pygame.draw.rect(self.surf,self.c,(self.x,self.y,self.w,self.h),self.t)



rect1= rect(300,300,300,300,"green",0)
rect1.draw()
rect2= rect(0,0,300,300,"yellow",10)
rect2.draw()

class circ():

    def __init__(self,x,y,r,c,t):
        self.surf=screen
        self.x=x
        self.y=y
        self.r=r
        self.c=c
        self.t=t


    def draw(self):
        pygame.draw.circle(self.surf,self.c,(self.x,self.y),self.r,self.t)


circ1= circ (450,150,125,"blue",10)
circ2= circ (150,450,125,(112, 34, 161),0)
circ1.draw()
circ2.draw()


run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
    pygame.display.update()


    



