# Invent with Python - Chapter 2
# 2020-04-30 
# http://inventwithpython.com/pygame/chapter2.html

import pygame, sys 
from pygame.locals import * 
import colors


# Required to initialize pygame
pygame.init()

# Create pygame surface object and set title + size. (Width, Height)
WIDTH=300
HEIGHT=300

DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
OVERLAYSURF = DISPLAYSURF.convert_alpha()

pygame.display.set_caption('Hello Pythonistas!')

DISPLAYSURF.fill(colors.Teal) 

# Draw Objects 
#pygame.draw.polygon(DISPLAYSURF, colors.NavyBlue, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

#pygame.draw.line(DISPLAYSURF, colors.Fuchsia, (120, 60), (60, 120))

# rangelength=int(((WIDTH/20)+(HEIGHT/20))) # error correct later to center for non integer results)
# print(rangelength)

# for i in range(rangelength):
#     x=i*20+20
#     y=y+20
#     pos=(x,y)
#     print(pos)
#     pygame.draw.circle(DISPLAYSURF, colors.Fuchsia, pos, 5, 0)

x_range=range(1,int(WIDTH/20))
y_range=range(1,int(HEIGHT/20))

xy_range=(x_range,y_range)
print(xy_range)

for i in range(1,14): 
    pygame.draw.circle(DISPLAYSURF, colors.Fuchsia, (x_range[i]*20,i*20),5,0)
    for  in range(1,14): 
        print(x_range[i])
        print(y_range[i])
        pygame.draw.circle(DISPLAYSURF, colors.Fuchsia, (i*20, y_range[i]*20),5,0)

# Main game loop
while True: 
    for event in pygame.event.get(): 
        # print(event) # DEBUG ONLY
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        pygame.display.update()