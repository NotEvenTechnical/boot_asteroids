import pygame

from constants import *
from player import Player


def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)

    player = Player( x = SCREEN_WIDTH / 2 , y = SCREEN_HEIGHT / 2 )

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update to the clock delta
        updatables.update(dt)

        # rendering
        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # clock delta
        dt = ( clock.tick( 60 ) ) / 1000    # measure the dt in seconds




if __name__ == "__main__":
    main()
