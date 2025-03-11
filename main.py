import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroids_c = pygame.sprite.Group()
    Asteroid.containers = (asteroids_c, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField_o = AsteroidField()
    Shots_c = pygame.sprite.Group()
    Shot.containers = (Shots_c, updatable, drawable)
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        player1.shoot_cooldown -= dt
        for asteroid in asteroids_c:
            if asteroid.collision(player1) == True:
                print("Game Over!")
                pygame.QUIT
                return
            for i in range(0, len(asteroids_c)):
                    if asteroid.collision(asteroids_c[i]) == True:
                        asteroid.split()
            for bullets in Shots_c:
                if bullets.collision(asteroid) == True:
                    asteroid.split()
                    bullets.kill()

        pygame.Surface.fill(screen,(0,0,0))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        
    
        
if __name__ == "__main__":
    main()