from abc import ABC, abstractmethod
import pygame
import random


class Observer(ABC):
    abstractmethod
    
    def update(self, subject):
        pass
    
    
class Rectangle(Observer):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self, self.x, self.y, self.width, self.height, self.color))

    def update(self, subject):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        

# Subject class (Publisher)
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.obervers = []
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self, self.x, self.y, self.radius, self.color))
        
    def attach(self, oberver):
        self.obervers.append(oberver)
    
    def notify(self):
        for oberver in self.obervers:
            oberver.update(self)
            
    def move(self, x, y):
        self.x = x
        self.y = y
        self.notify
        
        
def main():
    pygame.init()
    screen = pygame.display.set_mode(800, 600)
    running = True
    clock = pygame.time.Clock()
    circle = Circle(400, 300, 50, (255, 255, 255))
    rectangles = [
        Rectangle(100, 100, 50, 50, (255, 0, 0)),
        Rectangle(100, 100, 50, 50, (0, 255, 0)),
        Rectangle(100, 100, 50, 50, (0, 0, 255)),
    ]
    for rect in rectangles:
        circle.attach(rect)
    
    while running:
        screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    circle.draw(screen)
    for rect in rectangles:
        rect.draw(screen)
    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        circle.move(*mouse_pos)
    pygame.display.flip()
    clock.tick(60)

    pygame.quit()
    
    
if __name__ == '__main__':
    main()