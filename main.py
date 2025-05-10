import sys

import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player( x = SCREEN_WIDTH / 2 , y = SCREEN_HEIGHT / 2 )

    asteroids = pygame.sprite.Group()
    Asteroid.containers = ( asteroids, updatable, drawable)

    AsteroidField.containers = ( updatable )
    asteroidfield = AsteroidField()

    shot_group = pygame.sprite.Group()
    Shot.containers = ( shot_group, drawable, updatable )


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update to the clock delta
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding( player ):
                print ("Game over!")
                sys.exit()

            for bullet in shot_group:
                if asteroid.is_colliding ( bullet ):
                    asteroid.kill()
                    bullet.kill()

        # rendering
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # clock delta
        dt = ( clock.tick( 60 ) ) / 1000    # measure the dt in seconds




if __name__ == "__main__":
    main()
