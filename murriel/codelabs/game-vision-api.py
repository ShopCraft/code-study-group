import pygame, sys
from pygame.locals import *
from google.cloud import vision 

bucket = 'gs://murriel-generic-bucket'

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Let's learn with Machines!")
Black = (0,0,0)

img = pygame.image.load('images/cat05.jpeg')

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = f'{bucket}/codelabs/labels/cat05.jpeg'

response = client.label_detection(image=image)

print('Labels (and confidence score):')
print('=' * 79)
for label in response.label_annotations:
    print(f'{label.description} ({label.score*100.:.2f}%)')

while True: 
    DISPLAYSURF.fill(Black)
    xx = 10 
    yy = 10 

    DISPLAYSURF.blit(img, (xx, yy))
    
    for event in pygame.event.get(): 
        # print(event) # DEBUG ONLY
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
    pygame.display.update()