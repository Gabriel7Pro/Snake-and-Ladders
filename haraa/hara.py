import pygame
pygame.init()
white = (255, 255, 255)
img = pygame.image.load('Soccer_ball.png')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
img = pygame.transform.scale(img, (pygame.display.get_surface().get_size()[0]/20,pygame.display.get_surface().get_size()[1]/20))
running = True
x=500
y=500
while running:
    screen.fill((white))
    screen.blit(img,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #if esc clicked, quit
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x=x-10
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x=x+10
            if event.key == pygame.K_UP or event.key == ord('w'):
                y=y-10
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y=y+10
                    
        pygame.display.flip()
pygame.quit()        
