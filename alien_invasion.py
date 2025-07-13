import sys
import pygame
from settings import Settings
from arrow import Arrow
from arsenal import Arsenal

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

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)


        self.arrow = Arrow(self, Arsenal(self))
#went through walkthrough- fixed according to class video
    def run_game(self): #game loop
        while self.running:
            self._check_events()
            self.arrow.update()
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
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.arrow.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.arrow.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.arrow.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.arrow.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.arrow.moving_left = False
       

        #render the graphics




if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()
   
        
    
