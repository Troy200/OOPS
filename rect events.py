import pygame

pygame.init()

WIDTH=600
HEIGHT=600

screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((124, 191, 230))



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



    def up(self):
        self.y=self.y-10
        pygame.draw.rect(self.surf,self.c,(self.x,self.y,self.w,self.h),self.t)
        
     
    def down(self):
        self.y=self.y+10
        pygame.draw.rect(self.surf,self.c,(self.x,self.y,self.w,self.h),self.t)  
               

    def right(self):
        self.x=self.x+10
        pygame.draw.rect(self.surf,self.c,(self.x,self.y,self.w,self.h),self.t)  
    
    def left(self):
        self.x=self.x-10
        pygame.draw.rect(self.surf,self.c,(self.x,self.y,self.w,self.h),self.t) 

greenrect=rect(300,300,100,100,"green",0)
greenrect.draw()

    










run=True
while run:
    for event in pygame.event.get():

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                screen.fill((124, 191, 230))
                greenrect.up()
            
            if event.key==pygame.K_DOWN:
                screen.fill((124, 191, 230))
                greenrect.down()   

            if event.key==pygame.K_RIGHT:
                screen.fill((124, 191, 230))
                greenrect.right()
            if event.key==pygame.K_LEFT:
                screen.fill((124, 191, 230))
                greenrect.left()  
        if event.type== pygame.QUIT:
            pygame.quit()
    pygame.display.update()