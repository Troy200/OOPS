import pygame

pygame.init()
pygame.font.init()
WIDTH=600
HEIGHT=600

screen= pygame.display.set_mode((WIDTH,HEIGHT))

bg=pygame.image.load("pro game devloper/games/images/bg.png")
rocket=pygame.image.load("pro game devloper/games/images/rocket.png")
rocket_x=300
rocket_y=200

#print(pygame.font.get_fonts())
font=pygame.font.SysFont("Arial",600)

run=True
while run:
    rocket_y=rocket_y+2   
    if rocket_y>600:
        screen.blit(bg,(0,0))
        text= font.render("Game Over",True,"white")
        screen.blit(text,(300,300))
    for event in pygame.event.get():

        if event.type== pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w and rocket_y>0:
                rocket_y=rocket_y-10
            if event.key==pygame.K_s and rocket_y<600:
                rocket_y=rocket_y+10
            if event.key==pygame.K_d and rocket_x<600:
                rocket_x=rocket_x+10
            if event.key==pygame.K_a and rocket_x>0:
    
                rocket_x=rocket_x-10


    screen.blit(bg,(0,0))
    screen.blit(rocket,(rocket_x,rocket_y))
    pygame.display.update()