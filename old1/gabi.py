import pygame
import socket
import select
def game(screen):
    pygame.init()
    screen = pygame.display.set_mode((800, 800),0)
    screen.blit(img3,(0,0))
    running = True
    Username = raw_input("what is your name?")
    s=socket.socket()
    s.connect(("127.0.0.1",5000))
    s.send(Username)
    Da= None
    while running:
        rlist,wlist,xlist=select.select([s],[s],[])
        if len(rlist)!=0:
            DA= s.recv(1024)
            if DA == "looser":
                running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                #if esc clicked, quit
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.flip()
    s.close()    
                    
    
pygame.init()
img = pygame.image.load('Super-Smash-Bros.jpg')
img2 = pygame.image.load('Super_Smash_Bros._Logo.png')
img3 =  pygame.image.load('boared.jpg')
img3 = pygame.transform.scale(img3, (800,800))
#pygame.mixer.music.load('start.ogg')
#pygame.mixer.music.play(-1)
myfont = pygame.font.SysFont('Comic Sans MS', 40)
white = (255, 255, 255)
play_ = myfont.render('PLAY', False, white)
options_ = myfont.render('OPTIONS', False, white)
quit_ = myfont.render('QUIT', False, white)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
img = pygame.transform.scale(img, pygame.display.get_surface().get_size())
img2 = pygame.transform.scale(img2, (pygame.display.get_surface().get_size()[0]/2,pygame.display.get_surface().get_size()[1]/5*2))
screen.fill((white))
running = True
blue=(0,0,255)
screen.blit(img,(0,0))
screen.blit(img2,(pygame.display.get_surface().get_size()[0]/4,0))
pygame.draw.rect(screen,blue,(pygame.display.get_surface().get_size()[0]*3/8,pygame.display.get_surface().get_size()[1]/2,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
pygame.draw.rect(screen,blue,(pygame.display.get_surface().get_size()[0]*3/8,pygame.display.get_surface().get_size()[1]/1.6,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
pygame.draw.rect(screen,blue,(pygame.display.get_surface().get_size()[0]*3/8,pygame.display.get_surface().get_size()[1]/1.34,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
button_play = screen.blit(play_,(pygame.display.get_surface().get_size()[0]*30/64,pygame.display.get_surface().get_size()[1]/2))
button_options = screen.blit(options_,(pygame.display.get_surface().get_size()[0]*28/64,pygame.display.get_surface().get_size()[1]/1.6))
button_quit = screen.blit(quit_,(pygame.display.get_surface().get_size()[0]*30/64,pygame.display.get_surface().get_size()[1]/1.34))
disconnect = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            disconnect = True
        elif event.type == pygame.KEYDOWN:
            #if esc clicked, quit
            if event.key == pygame.K_ESCAPE:
                running = False
                disconnect = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            #if quit button clicked, quit
            if button_quit.collidepoint(pos):
                running = False
                disconnect = True
            elif button_play.collidepoint(pos):
                running = False
                
    pygame.display.flip()
if disconnect: 
    pygame.quit()
else:    
    game(screen)
    pygame.quit()
