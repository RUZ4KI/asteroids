import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock =pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #create groups
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)

    Player.containers = (updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        screen.fill("black")
        #player.update(dt)
        for obj in updatable:
            obj.update(dt)
        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()