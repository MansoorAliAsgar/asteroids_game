import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_obj = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    asteroid_fields = pygame.sprite.Group()
    AsteroidField.containers = updatable

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    asteroid_field_obj = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if obj.collision(player_obj):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if obj.collision(shot):
                    shot.kill()
                    obj.split()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        delta_time = clock_obj.tick(60)
        dt = delta_time / 1000


if __name__ == "__main__":
    main()
