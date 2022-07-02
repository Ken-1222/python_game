import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Movement and Collisions!")

#Set game values
VELOCITY = 5

angry_bird             = pygame.image.load("angrybird.png")
angry_bird_rect        = angry_bird.get_rect()
angry_bird_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

keys = pygame.key.get_pressed()
if keys([pygame.K_LEFT]):
    angry_bird_rect.x -= VELOCITY
if keys([pygame.K_RIGHT]):
    angry_bird_rect.x += VELOCITY    
if keys([pygame.K_UP]):
    angry_bird_rect.y -= VELOCITY
if keys([pygame.K_DOWN]):
    angry_bird_rect.y += VELOCITY

    displayscreen.fill(BLACK)
    displayscreen.blit(angry_bird, angry_bird_rect)
    displayscreen.blit(coin, coin_rect)
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()