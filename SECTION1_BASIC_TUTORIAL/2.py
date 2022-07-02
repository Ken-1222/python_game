import  pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Image!")

bird_topleft = pygame.image.load("angrybrid.png")
bird_topleft_rect = bird_topleft.get_rect()
bird_topleft_rect.topleft = (0, 0)

bird_topright = pygame.image.load("angrybrid.png")
bird_topright_rect = bird_topright.get_rect()
bird_topright_rect.topright = (WINDOW_WIDTH,0)

WHITE = (255, 255, 255)
GREEN = (0,   255,   0)
DARKGREEN = (10, 50, 10)

#fonts = pygame.font.get_fonts() //取得所有PTGAME內建字形]
system_font = pygame.font.SysFont("century", 50)
custom_font = pygame.font.Font("Attack.ttf", 50)

show_text_1             = system_font.render("Angry Bird Game", True, GREEN, DARKGREEN)
show_text_1_rect        = show_text_1.get_rect()
WHITE = (255, 255, 255)


sound_1 = pygame.mixer.Sound("sound_1.wav")
sound_2 = pygame.mixer.Sound("sound_1.wav")

sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

sound_2.set_volume(1.0)
sound_2.play

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    pygame.draw.line(displayscreen, WHITE, (0, 75), (WINDOW_WIDTH, 75), 5)

    displayscreen.blit(bird_topleft, bird_topleft_rect)
    displayscreen.blit(bird_topright, bird_topright_rect)
    pygame.display.update()

pygame.quit()