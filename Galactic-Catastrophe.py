# Imports
import pygame
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Catastrophe!"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)
DARK_BLUE = (2, 0, 17)

# Images
ship_img = pygame.image.load('assets/images/player_ship.png')
hurtflash_img = pygame.image.load('assets/images/player_ship-1.png')
laser_img = pygame.image.load('assets/images/catrunx4-2-1.png')

mob_img1 = pygame.image.load('assets/images/enemy_ship-1.png')
mob_img2 = pygame.image.load('assets/images/enemy_ship-2.png')
mob_img3 =  pygame.image.load('assets/images/last_enemy.png')

bomb_img = pygame.image.load('assets/images/UFO-2.png')

background = pygame.image.load('assets/images/background-stars.png')
start = pygame.image.load('assets/images/start_screen_img.png')

 
health_img = pygame.image.load('assets/images/health_unit.png') 



# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_XL = pygame.font.Font("assets/fonts/space_age.ttf", 96)


# Sounds
EXPLOSION = pygame.mixer.Sound('assets/sounds/explosion.ogg')
                                        
hongkong97 = pygame.mixer.Sound('assets/sounds/hong_kong_97.ogg')
stickers = pygame.mixer.Sound('assets/sounds/stickers.ogg')
music =  pygame.mixer.Sound('assets/sounds/party-stronger.ogg')
music2 =  pygame.mixer.Sound('assets/sounds/Tung_The_Icelandic.ogg')

shoot = pygame.mixer.Sound('assets/sounds/shoot.ogg')
ouch =  pygame.mixer.Sound('assets/sounds/hit_noise.ogg')

music2.play(-1)

# Stages
START = 0
PLAYING = 1
END = 2



# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 3
        self.shield = 5

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    def shoot(self):
        laser = Laser(laser_img)
        laser.rect.centerx = self.rect.centerx
        laser.rect.centery = self.rect.top
        lasers.add(laser)
        shoot.play()
                

    def update(self, bombs, image, hurt):
        hit_list = pygame.sprite.spritecollide(self, bombs, True,
                                               pygame.sprite.collide_mask)

        for hit in hit_list:
            # play hit sound
            self.shield -= 1
            ouch.play()

            
        hit_list = pygame.sprite.spritecollide(self, mobs, False)

        if len(hit_list) > 0:
            self.shield = 0
            self.image = hurt



        if self.shield == 0:
            stickers.play()

            EXPLOSION.play()
        
            self.kill()
            
            
        if self.rect.x < -25:
            self.rect.x = -25

        elif self.rect.x > 950:
            self.rect.x = 950
            

class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()
    
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True,
                                               pygame.sprite.collide_mask)

        if len(hit_list) > 0:
            
            EXPLOSION.play()
            player.score += 1
            self.kill()

class Mob2(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.shield = 3


    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True,
                                               pygame.sprite.collide_mask)

        for hit in hit_list:
            # play hit sound
            self.shield -= 1            


    
            
        if self.shield == 0:            
            EXPLOSION.play()
            
            player.score += 10
            
            self.kill()

class Mob3(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.shield = 10


    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True,
                                               pygame.sprite.collide_mask)

        for hit in hit_list:
            # play hit sound
            self.shield -= 1            


    
            
        if self.shield == 0:            
            EXPLOSION.play()
            
            player.score += 100
            
            self.kill()



'''
class Health(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
   


    def update(self, ship, bomb):
        hit_list = pygame.sprite.spritecollide(ship, bombs, True,
                                               pygame.sprite.collide_mask)

        if len(hit_list) > 5:
            
            EXPLOSION.play()
            player.score += 1
            self.kill()


'''
    
class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        
        if self.rect.bottom > 600:
            self.kill()

    
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.moving_right = True
        self.speed = 5
        self.bomb_rate = 60

    def move(self):
        reverse = False
        
        for m in mobs:
            if self.moving_right:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True
            else:
                m.rect.x -= self.speed
                if m.rect.left <=0:
                    reverse = True

        if reverse == True:
            self.moving_right = not self.moving_right
            for m in mobs:
                m.rect.y += 32
            

    def choose_bomber(self):
        rand = random.randrange(0, self.bomb_rate)
        all_mobs = mobs.sprites()
        
        if len(all_mobs) > 0 and rand == 0:
            return random.choice(all_mobs)
        else:
            return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            bomber.drop_bomb()

    
# Make game objects
'''
health1 = Health(0, 715, health_img)
health2 = Health(50, 715, health_img)
health3 = Health(100, 715, health_img)
health4 = Health(150, 715, health_img)
heatlh5 = Health(200, 715, health_img)
'''

ship = Ship(384, 485, ship_img)
mob6 = Mob(128, 200, mob_img1)
mob7 = Mob(256, 200, mob_img1)


mob1 = Mob(128, 0, mob_img1)
mob2 = Mob(256, 0, mob_img1)
mob3 = Mob(384, 0, mob_img1)
mob4 = Mob(512, 0, mob_img1)


mob5 = Mob2(600, 0, mob_img2)

mob8 = Mob2(500, 0, mob_img3)


# Make sprite groups
player = pygame.sprite.GroupSingle()
player.add(ship)

player.score = 0

lasers = pygame.sprite.Group()

mobs = pygame.sprite.Group()
mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8)

bombs = pygame.sprite.Group()
                    

fleet = Fleet(mobs)

# set stage
stage = START

# Game helper functions
def show_title_screen():

    screen.blit(start, (0,0))

    title_text = FONT_XL.render("Catastrophe!", 1, WHITE)
    screen.blit(title_text, [40, 204])


def show_stats(player):
    score_text = FONT_SM.render(str(player.score), 1, RED)
    screen.blit(score_text, [32, 32])

    shield_text = FONT_SM.render("Health: " + str(ship.shield), 1, RED)
    screen.blit(shield_text, [32, 568])

'''keep thinking on ways to display the health thing
def health_meter():

    h_y = 32
    h_x = 800

    
    screen.blit(health_img, [h_x, h_y])
'''

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    ship.shoot()
                if event.key == pygame.K_p:
                    stage = END
            elif stage == END:
                if event.key == pygame.K_p:
                    stage = PLAYING

                
    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            ship.move_left()
        elif pressed[pygame.K_RIGHT]:
             ship.move_right()
                                
    
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:

        
    
        player.update(bombs, ship_img, hurtflash_img)
        lasers.update()   
        mobs.update(lasers)
        bombs.update()
        fleet.update()
        
        if len(player) == 0:
            stage == END
        

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)


    screen.blit(background, (0,0))
    lasers.draw(screen)
    player.draw(screen)
    bombs.draw(screen)
    mobs.draw(screen)
    show_stats(player)
    #health_meter()

    if stage == START:
        show_title_screen()

        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
