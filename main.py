# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updateable.update(dt)

        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                return sys.exit()

            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.kill()

        screen.fill("black")
        
        for d in drawable:
            d.draw(screen)
    
        pygame.display.flip()
        # why we need to clock.tick(60) / 1000 ?
        # setting at 60 limits the framerate to 60 FPS
        # clock.tick(60) returns the number of milliseconds since the last frame
        # we want to convert that to seconds so we divide by 1000 and we store it in dt for use in the game loop
        dt = clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()

