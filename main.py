import pygame
from ball import Ball

#Basic screen setup

screen = pygame.display.set_mode((600, 600))
black = (0, 0, 0)
clock = pygame.time.Clock()

#Utilizing balls

balls = []

balls.append(Ball(250, 0, 25))
balls.append(Ball(350, 0, 25))
balls.append(Ball(300, 0, 25))
balls.append(Ball(200, 0, 25))

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    
    for ball in balls:
        ball.update()
        ball.draw(screen)
    
    
    pygame.display.flip()
    clock.tick(50)
    