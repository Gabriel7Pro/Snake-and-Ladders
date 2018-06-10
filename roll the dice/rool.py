import pygame
import random

white = (255, 255, 255)
pygame.init()

one = pygame.image.load('1.png')
one = pygame.transform.scale(one,(300,300))
two = pygame.image.load('2.png')
two = pygame.transform.scale(two,(300,300))
th = pygame.image.load('3.png')
th = pygame.transform.scale(th,(300,300))
fo = pygame.image.load('4.png')
fo = pygame.transform.scale(fo,(300,300))
fi = pygame.image.load('5.png')
fi = pygame.transform.scale(fi,(300,300))
si = pygame.image.load('6.png')
si = pygame.transform.scale(si,(300,300))
rr = pygame.image.load('rolling.png')
rr = pygame.transform.scale(rr,(300,300))


num = [rr,one,two,th,fo,fi,si]


pla=0
screen = pygame.display.set_mode((600, 600), 0)
screen.fill((white))
running = True
screen.blit(num[pla],(0,0))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #if esc clicked, quit
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            #if quit button clicked, quit
            if num[pla].get_rect().collidepoint(pos):
                pla = random.randint(1, 6)
                screen.blit(num[pla],(0,0))
    pygame.display.flip()
pygame.quit()
