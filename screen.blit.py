import pygame

pygame.init()

WIDTH=600
HEIGHT=600

screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("grey")
star=pygame.image.load("pro game devloper/games/images/be4e11d2e7b2cc8936fff91eca045379.jpg")
sparkel=pygame.image.load("pro game devloper/games/images/star-sparkle-icon-futuristic-shapes-christmas-stars-icons-flashes-from-fireworks-png.webp")








run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()

    screen.blit(star,(200,0))
    screen.blit(sparkel,(10,10))
    pygame.display.update()
