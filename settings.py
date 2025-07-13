from pathlib import Path
class Settings:

    def __init__(self):
        self.name: str = "Cupid Invasion"
        self.screen_w = 1200
        self.screen_l = 800
        self.FPS = 60 
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'heartbackground.png'

        self.arrow_file = Path.cwd() / 'Assets' / 'images' / 'arrow.png'
        self.arrow_w = 100
        self.arrow_h = 160

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'heart.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'arrowlaser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 80
        self.bullet_h = 80
        self.bullet_amount = 5 