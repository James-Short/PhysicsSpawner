
class Ball:
    def __init__(self, x, y, radius):
        import random
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = random.randint(-15, 15)
        self.vy = 0
    
    def update(self):
        self.vy += 0.5
        self.y += self.vy
        
        self.x += self.vx
        
        
        
        if self.y + self.radius >= 600:
            self.y = 600 - self.radius
            
            if abs(self.vy) < 1:
                self.vy = 0
            else:
                self.vy *= -0.8
        
        elif self.y - self.radius <= 0:
            self.y = self.radius
            

            if abs(self.vy) < 1:
                self.vy = 0
            else:
                self.vy *= -0.8
        
        if self.x + self.radius >= 600:
            self.x = 600 - self.radius
            self.vx *= 0.8
            
            if abs(self.vx) < 1:
                self.vx = 0
            else:
                self.vx *= -0.8
        
        elif self.x - self.radius <= 0:
            self.x = self.radius
            
            if abs(self.vx) < 1:
                self.vx = 0
            else:
                self.vx *= -0.8
    
    def draw(self, screen):
        import pygame
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
        