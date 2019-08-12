import pygame
import numpy as np
import operator as op

#STARTUP
pygame.init()
#COLOUR DEFINITION
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
#SCREEN RESOLUTION
dW = 1366
dH = 768
freqMatrix = [[0 for i in range(3*dH)] for j in range(3*dW)]
colorMatrix = [[(0, 0, 0) for i in range(3*dH)] for j in range(3*dW)]
freqFinal = [[0 for i in range(dH)] for j in range(dW)]
colorFinal = [[white for i in range(dH)] for j in range(dW)]
#binW = range(-(3.0*dW)/2, (3.0*dW)/2)
#binH = range(-(3.0*dH)/2, (3.0*dH)/2)
binW = np.linspace(-10, 10, dW*3)
binH = np.linspace(-10, 10, dH*3)
gameDisplay = pygame.display.set_mode((dW,dH))
gameDisplay.fill(white)
#SIERPINSKY
def f1(xy):
	x = xy[0]
	y = xy[1]
	return (-0.465 - 0.33333333*x, 0.2165 + 0.33333333*y)

def f2(xy):
	x = xy[0]
	y = xy[1]
	return (x, -y)

def f3(xy):
	x = xy[0]
	y = xy[1]
	return (x, 2-y)

def f4(xy):
	x = xy[0]
	y = xy[1]
	return (1+np.tan(x), 0.0075572037*y)

def f5(xy):
	x = xy[0]
	y = xy[1]
	return (-x, y)

def f6(xy):
	x = xy[0]
	y = xy[1]
	return (-0.1*x, 1+0.5*y)

def f7(xy):
	x = xy[0]
	y = xy[1]
	return (2*x, 2*y)

def f8(xy):
	x = xy[0]
	y = xy[1]
	return (np.sin(y)+np.sin(1/(x+0.9))*x, 0.1 + np.sin(x)*y)

#VARIABLES
xy = (0, 0)
maxIter = 10000000
prob = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3]
fList = [f1, f2, f3, f4, f5, f6, f7, f8]
cList = [black, black, black, black, black, black, cyan, white]
fNumber = 8
lastcolor = black
k = 0
#cumulative probability
for i in range(1, len(prob)):
	prob[i] += prob[i-1]

#print binW, binH

#CODE
print "Generating image..."
while k < maxIter:
	#pygame.display.update()
	
	'''rnd = np.random.randint(0, fNumber)
	for i in range(fNumber):
		if rnd == i:
			xy = fList[i](xy)
			gameDisplay.set_at(coords(xy), cList[i])'''
	rnd = np.random.uniform()
	#print len(colorMatrix), len(colorMatrix[1])
	for i in range(fNumber):
		if rnd < prob[i]:
			#update xy
			xy = fList[i](xy)
			#calculate the adequate bin
			a = np.digitize([xy[0]], binW)[0] - 1
			b = np.digitize([xy[1]], binH)[0] - 1
			#print a, b, i
			#update colours
			if i==1 or i==2 or i==4:
				cList[i] = lastcolor
			#colorMatrix[a][b] = ((cList[i][0]+colorMatrix[a][b][0])/2, 
			#	(cList[i][1]+colorMatrix[a][b][1])/2,
			#	(cList[i][2]+colorMatrix[a][b][2])/2) 
			colorMatrix[a][b] = cList[i]
			freqMatrix[a][b] += 1
			lastcolor = cList[i]
			break;
	k += 1

#Downsampling

print "Downsampling..."
for i in range(dW):
	for j in range(dH):
		w = i*3
		z = j*3
		sumFreq = 0
		sumColor = (0, 0, 0)
		for m in range(3):
			for n in range(3):
				sumFreq += freqMatrix[i*3 + m][j*3 + n]
				sumColor = tuple(map(op.add, sumColor, colorMatrix[i*3 + m][j*3 + n]))
		freqFinal[i][j] = float(sumFreq)/9
		colorFinal[i][j] = (sumColor[0]/9, sumColor[1]/9, sumColor[2]/9)





print "Rendering..."
for i in range(dW):
	for j in range(dH):
		gameDisplay.set_at((dW - i, dH - j), colorFinal[i][j])
pygame.display.update()
#print freqMatrix
print "Done!"
print "Insert file name:"
name = raw_input()
name = name+".png"

pygame.image.save(gameDisplay, name)

pygame.quit()
quit()