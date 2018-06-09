import pygame
import socket
import select
from Tkinter import *


class Player:

    def __init__(self):
        self.Username = ""
        self.Players = []
        self.master = Tk()
        self.entry = None
        self.screen = None
        self.white = (255, 255, 255)
        
    def gg(self):
        print "aaa"
        
    def return_entry(self,en):
        """Gets and prints the content of the entry"""
        self.Username = self.entry.get()
        self.master.destroy()

        
    def main_screen(self):
        pygame.init()
        img = pygame.image.load('Super-Smash-Bros.jpg')
        img2 = pygame.image.load('Super_Smash_Bros._Logo.png')
        #pygame.mixer.music.load('start.ogg')
        #pygame.mixer.music.play(-1)
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        
        play_ = myfont.render('PLAY', False, self.white)
        options_ = myfont.render('OPTIONS', False, self.white)
        quit_ = myfont.render('QUIT', False, self.white)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        img = pygame.transform.scale(img, pygame.display.get_surface().get_size())
        img2 = pygame.transform.scale(img2, (pygame.display.get_surface().get_size()[0]/2,pygame.display.get_surface().get_size()[1]/5*2))
        self.screen.fill((self.white))
        blue=(0,0,255)
        self.screen.blit(img,(0,0))
        self.screen.blit(img2,(pygame.display.get_surface().get_size()[0]/4,0))
        pygame.draw.rect(self.screen,blue,(pygame.display.get_surface().get_size()[0]*3/8,pygame.display.get_surface().get_size()[1]/2,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        pygame.draw.rect(self.screen,blue,(pygame.display.get_surface().get_size()[0]*3/8,pygame.display.get_surface().get_size()[1]/1.6,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        pygame.draw.rect(self.screen,blue,(pygame.display.get_surface().get_size()[0]*3/8,pygame.display.get_surface().get_size()[1]/1.34,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        button_play = self.screen.blit(play_,(pygame.display.get_surface().get_size()[0]*30/64,pygame.display.get_surface().get_size()[1]/2))
        button_options = self.screen.blit(options_,(pygame.display.get_surface().get_size()[0]*28/64,pygame.display.get_surface().get_size()[1]/1.6))
        button_quit = self.screen.blit(quit_,(pygame.display.get_surface().get_size()[0]*30/64,pygame.display.get_surface().get_size()[1]/1.34))
        running = True
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
        return disconnect


       
    def Login(self):
        pygame.init()
        img3 =  pygame.image.load('boared.jpg')
        img3 = pygame.transform.scale(img3, (800,800))
        self.screen = pygame.display.set_mode((800, 800),0)
        self.screen.blit(img3,(0,0))
        
        Label(self.master, text="Username: ").grid(row=0, sticky=W)
        self.master.title('Login')
        self.entry = Entry(self.master)
        self.entry.grid(row=0, column=1)
        # Connect the entry with the return button
        self.entry.bind('<Return>',self.return_entry)
        mainloop()
        self.game()

        
    def game(self):
        s=socket.socket()
        s.connect(("127.0.0.1",5000))
        s.send("nameeeeeeeeee" + self.Username)
        Da= None
        running = True
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

def main():
    player = Player()
    disconnect = player.main_screen()
    if disconnect: 
        pygame.quit()
    else:    
        player.Login()
        pygame.quit()

if __name__ == "__main__":
    main()
















            
     
