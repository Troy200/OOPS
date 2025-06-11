import pygame

pygame.init()

WIDTH=600
HEIGHT=600

screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((124, 191, 230))

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


face= circ (300,300,250,(252, 216, 71),0)
leye= circ (220,200,35,(133, 75, 34),0)
reye= circ (380,200,35,(133, 75, 34),0)
lsmile= circ (150,400,45,"white",0)
rsmile= circ (450,400,45,"white",0)
face.draw()
leye.draw()
reye.draw()
lsmile.draw()
rsmile.draw()


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



smilerect= rect(150,355,90,300,"white",0)
smilerect.draw()
teethmidline= rect(105,400,5,390,"black",0)
teethmidline.draw()
teethline1= rect(183,355,90,5,"black",0)
teethline1.draw()
teethline2= rect(261,355,90,5,"black",0)
teethline2.draw()
teethline3= rect(339,355,90,5,"black",0)
teethline3.draw()
teethline4= rect(417,355,90,5,"black",0)
teethline4.draw()



run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
    pygame.display.update()