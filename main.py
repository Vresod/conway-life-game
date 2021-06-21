import classes as cw
import pygame
import pygame.locals

BLOCKSIZE = 16

def drawGrid():
	for x in range(WINDOW_WIDTH // BLOCKSIZE):
		for y in range(WINDOW_HEIGHT // BLOCKSIZE):
			rect = pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
			pygame.draw.rect(screen, (255,255,255), rect, 1)

def event_loop(event:pygame.event):
	if event.type != pygame.locals.MOUSEBUTTONDOWN:
		return False
	fill_square(event.pos[0] // BLOCKSIZE, event.pos[1] // BLOCKSIZE)

def fill_square(x, y):
	rect = pygame.Rect(x*BLOCKSIZE + 1, y*BLOCKSIZE + 1, BLOCKSIZE - 2, BLOCKSIZE - 2)
	pygame.draw.rect(screen, (255,0,0), rect)

if __name__=='__main__':
	global width, height, screen,WINDOW_WIDTH, WINDOW_HEIGHT
	# width = int(input("Width: "))
	# height = int(input("Height: "))
	width = 50
	WINDOW_WIDTH = width * BLOCKSIZE
	height = 50
	WINDOW_HEIGHT = height * BLOCKSIZE
	pygame.init()
	screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
	screen.fill((0, 0, 0))
	pygame.display.flip()
	while (event := pygame.event.wait()).type != pygame.locals.QUIT:
		drawGrid()
		event_loop(event)
		pygame.display.update()