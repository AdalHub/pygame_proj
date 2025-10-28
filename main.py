import pygame

pygame.init()

WINDOW= pygame.display.set_mode((640,640))

first_item = pygame.image.load("evil_hd1.png").convert_alpha() # since we are using a transparent background, we use convert alpha to include alpha colors(aka include transparent)
first_item = pygame.transform.scale(first_item, (first_item.height * 0.05, first_item.width * .05)) # We transform our first object's size
first_items = pygame.Surface((64,64), pygame.SRCALPHA)

def main():
    running = True
    x=0
    delta_time = 0.1

    clock = pygame.time.Clock()
    while running:
        WINDOW.fill((255,255,255)) # we fill in our screen white 
        WINDOW.blit(first_item, (x,50)) # we add our first item to our screen
        WINDOW.blit(first_items, (0, 50))       
        x+=50 * delta_time
        first_items.set_alpha(max(0, 255-x))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()   # We update the frame to display new surface movement
        delta_time = clock.tick(60) / 1000 # adjusted for local monitor frame rate
        delta_time= max(0.001, min(0.1, delta_time)) # technically the minimum here is only required if tick is given an uncapped frame rate
    pygame.quit()
        
if __name__ == "__main__":
    main()