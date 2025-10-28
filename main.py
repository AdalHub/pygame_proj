import pygame

pygame.init()

WINDOW= pygame.display.set_mode((640,640))

horse = pygame.image.load("evil_hd1.png").convert_alpha() # since we are using a transparent background, we use convert alpha to include alpha colors(aka include transparent)
horse = pygame.transform.scale(horse, (horse.height * 0.05, horse.width * .05)) # We transform our first object's size


def main():
    running = True
    x=0
    delta_time = 0.1

    clock = pygame.time.Clock()
    while running:
        WINDOW.fill((255,255,255)) # we fill in our screen white 
        WINDOW.blit(horse, (x,50)) # we add our first item to our screen
        # creating our horse hitbox
        hitbox= pygame.Rect(x, 50, horse.get_width(), horse.get_height())
        target = pygame.Rect(300, 50, 200, 200)
        mpos= pygame.mouse.get_pos()
        collision = hitbox.colliderect(target)
        m_collision = target.collidepoint(mpos)
        pygame.draw.rect(WINDOW, (255 * collision, 255 *m_collision, 0), target)

        x+=50 * delta_time
        # changes the fade of an item based on its position
        #first_item.set_alpha(max(0, 255-x))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()   # We update the frame to display new surface movement
        delta_time = clock.tick(60) / 1000 # adjusted for local monitor frame rate
        delta_time= max(0.001, min(0.1, delta_time)) # technically the minimum here is only required if tick is given an uncapped frame rate
    pygame.quit()
        
if __name__ == "__main__":
    main()