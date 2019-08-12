import pygame
import numpy as np

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

dW = 1366
dH = 768

def coords(xy):
	return (xy[0] + (dW/2), xy[1] + (dH/2))

gameDisplay = pygame.display.set_mode((dW,dH))

gameDisplay.fill(white)
for i in range(100):
	gameDisplay.set_at((i, i), black)
	gameDisplay.set_at(coords((i, i)), black)

pygame.display.update()
pygame.image.save(gameDisplay, "test.png")

raw_input()

pygame.quit()
quit()
