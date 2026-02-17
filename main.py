import pygame
import sys
from constants import *
from logger import log_state, log_event
from players import Player
from circleshape import CircleShape
from asteroidfield import AsteroidField
from asteroids import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group() #Creating groups to manage all our objects
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   
    Player.containers = (updatable, drawable) #Has to be done before Player object is instantiated
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    Shot.containers = (shots, updatable, drawable)
    

    while (1):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")
        
        updatable.update(dt)  #instead of individually calling the update method on each Player object
        
        for thing in asteroids:
            if thing.collides_with(player):
                log_event ("player_hit")
                print("Game Over!")
                sys.exit() #ending the game
            for each in shots: 
                if thing.collides_with(each):
                    log_event("asteroid_shot")
                    thing.split()
                    each.kill() 


        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        time = clock.tick(60)
        dt = time/1000
        
    
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
