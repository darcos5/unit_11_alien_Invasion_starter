import sys
import pygame
from settings import Settings
from arrow import Arrow

#I installed github and pygames. I believe I followed all the steps nesscary but please let me know if I messed up 
#I added these following part so the game screen would appear 
#I followed pygame newbie guide for some of the structure 

#I think im going to change the "rocket" into hearts and make the game valentines theme
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #self.baby_pink = (244, 194, 194) #need to define specific colors #needed RGB instead of HEX
        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_l)) #screen size idea from pygames for newbies
        pygame.display.set_caption(self.settings.name)
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,(self.settings.screen_w, self.settings.screen_l))
        
        self.running = True
        self.clock = pygame.time.Clock()


        self.arrow = Arrow(self)
#went through walkthrough- fixed according to class video
    def run_game(self): #game loop
        while self.running:
            self._check_events()


            self._update_screen() #will make the screen update
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg,(0,0))
        self.arrow.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
        #render the graphics




if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()
   
        
    
