import pygame
import time
pygame.init()

win=pygame.display.set_mode((600,400))
pygame.display.set_caption('game trial')

x=300
y=300
true=True

x1=20
y1=100
vel=4

def draw():
    global x, vel
    x += vel
    if x <= 0 or x >= 550:
        vel *= -1
    
    win.fill('black')
    pygame.draw.rect(win,('red'),(x,y,50,50))
    pygame.draw.rect(win,('blue'),(x1,y1,50,50))
    pygame.display.update() 

clock=pygame.time.Clock()
while true:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
          true=False
          
    key=pygame.key.get_pressed()
    
    if [pygame.K_LEFT]:
        x1-=4
    elif [pygame.K_RIGHT]:
        x1+=4
          
    draw()
    
          
pygame.quit()