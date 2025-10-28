from constants import *
import pygame
from player import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BLACK)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    


if __name__ == "__main__":
    main()
