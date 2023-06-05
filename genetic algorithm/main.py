from imports import *

creature_surface = pg.image.load("images/creature.svg")
creature_surface1 = pg.image.load("images/creature.svg")
creature_surface = pg.transform.scale(creature_surface, (10, 10))
creature_surface1 = pg.transform.scale(creature_surface, (10, 10))

def main():
    running = True
    
    while running:  
        # pygame.QUIT event means the user clicked the red X
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                continue

        screen.fill("#333333")

        screen.blit(creature_surface, (1*10, 1*10))
        screen.blit(creature_surface1, (99*10, 99*10))

        # flip() the display to put your work on screen
        pg.display.flip() 

        clock.tick(144)  # limits FPS to 144

    pg.quit()

if __name__ == '__main__':
    main()