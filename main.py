import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import *

def display_score(screen, score):
    font = pygame.font.Font(None, 30)
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_surface, (10,10))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0,0,0)
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    player.containers = (updatable, drawable)
    player.add(updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    game_mat = AsteroidField()
    game_mat.add(updatable)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids: 
            if asteroid.collision_check(player) == True:
                print("Game over!")
                print(f"Final Score: {score}")
                pygame.quit()
                sys.exit()
            for shot in shots: 
                if asteroid.collision_check(shot) == True:
                    score += 1
                    asteroid.split()
                    shot.kill()
        screen.fill(black)
        display_score(screen, score)
        for agent in drawable:
            agent.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
    if __name__ == "__main__":
        main()

main()