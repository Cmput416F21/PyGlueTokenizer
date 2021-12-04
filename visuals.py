import pygame

if __name__ == "__main__":
    pygame.init()

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 40, 66)
    black = (0, 0, 0)
    X = 600
    Y = 400

    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Predicted Tokenization Sequence')
    bg = pygame.image.load("pygame-background.png")

    path = 'code2seq/Predictions.txt'
    with open(path) as f:
        line = f.readlines()

    font1 = pygame.font.Font('Roboto/Roboto-Light.ttf', 40)
    font2 = pygame.font.Font('Roboto/Roboto-Regular.ttf', 30)
    text2 = font2.render('Your predicted sequence is...', True, green, blue)
    text1 = font1.render(line[0], True, green, blue)
    textRect2 = text2.get_rect()
    textRect1 = text1.get_rect()

    # set the center of the rectangular object.
    textRect2.center = (X // 2, 140)
    textRect1.center = (X // 2, Y // 2)

    # infinite loop
    while True:
        display_surface.blit(bg, (0, 0))
        display_surface.blit(text1, textRect1)
        display_surface.blit(text2, textRect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            # Draws the surface object to the screen.
            pygame.display.update()