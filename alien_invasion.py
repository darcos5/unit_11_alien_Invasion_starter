import sys
import pygame

#I installed github and pygames. I believe I followed all the steps nesscary but please let me know if I messed up 
#I added these following part so the game screen would appear 
#I followed pygame newbie guide for some of the structure 

#I think im going to change the "rocket" into hearts and make the game valentines theme
class AlienInvasion:
    def __init__(self):
        pygame.init()
        #self.baby_pink = (244, 194, 194) #need to define specific colors #needed RGB instead of HEX
        self.screen = pygame.display.set_mode((1280,800)) #screen size idea from pygames for newbies
        pygame.display.set_caption("Cupid Invasion")
        
        self.running = True
#went through walkthrough- fixed according to class video
    def run_game(self): #game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            #fix this in a bit, giving up on the pink background for now 
        #self.screen.fill(self.baby_pink) # fill display with solid color
        #note: isnt displaying the color i had chosen but i will come back to this later
        pygame.display.flip() #will make the screen update
        #render the graphics




if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()
   
        
    
