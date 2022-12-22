import pygame
import random

"""
	A simple Starfield using Pygame.
"""


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
Z_MAX = 256 # Distance from the observer.
NUM_STARS = 70
SPEED = 0.001


def spawn_star():
	x = random.randint(0, SCREEN_WIDTH) - SCREEN_WIDTH // 2
	y = random.randint(0, SCREEN_HEIGHT) - SCREEN_HEIGHT // 2
	z = random.randint(1, Z_MAX - 1)
	return [x,y,z]


def get_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True

def main():
	looping = False
	star_list = []
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
		
	pygame.init()
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Star Field")
	clock = pygame.time.Clock()
	
	
	# Spawn initial stars.
	for i in range(NUM_STARS):
		star_list.append(spawn_star())

	# ---------- Main Loop ----------
	while not looping:
		# Get events.
		looping = get_events()
		# Update star positions.
		for i in range(NUM_STARS):
			x = star_list[i][0] * Z_MAX / star_list[i][2]
			y = star_list[i][1] * Z_MAX / star_list[i][2]
			z = star_list[i][2] - SPEED
			if x <= -SCREEN_WIDTH / 2 or x >= SCREEN_WIDTH / 2 or y <= -SCREEN_WIDTH / 2 or y >= SCREEN_WIDTH / 2 or z <= 0:
				star_list[i] = spawn_star() # If out of bounds spawn a new star.
			else:
				star_list[i] = [x, y, z] # Else update coords.
		# Update screen.
		screen.fill(BLACK)
		for i in range(NUM_STARS):
			# Perspective projection.
			x = (star_list[i][0] * Z_MAX / star_list[i][2]) + SCREEN_WIDTH / 2
			y = (star_list[i][1] * Z_MAX / star_list[i][2]) + SCREEN_HEIGHT / 2
			pygame.draw.circle(screen, WHITE, [x, y], 1)
		clock.tick(60)
		pygame.display.flip()
	pygame.quit()
 
if __name__ == "__main__":
    main()
