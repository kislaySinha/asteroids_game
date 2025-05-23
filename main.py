import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    #time
    clock = pygame.time.Clock()
    dt = 0
    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #containers
    Asteroid.containers = (updatable,drawable,asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Shot.containers = (updatable,drawable,shots)

    #player object
    player1 = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    
    #screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #game loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        updatable.update(dt)

        for aster in asteroids:
            if player1.collisions(aster):
                print("Game over!")
                return

        for aster in asteroids:
            for sh in shots:
                if aster.collisions(sh):
                    aster.split()
                    sh.kill()

    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
