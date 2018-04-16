# Imports
import pygame

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Space War"
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
GREEN = (0, 255, 0)

# Images



# Game classes
class Ship:
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 3
        self.shield = 10


    def move_left(self):
        self.x -= self.speed
        
    def move_right(self):
        self.x += self.speed

    def shoot(self):
        
        laser = Laser(laser_img)
        laser.rect.centerx = self.rect.centerx
        laser.rect.centery = self.rect.top
        lasers.add(laser)


        if len(hit_list) > ):

    def draw(self):
        rect = [self.x, self.y, self.w, self.h]
        pygame.draw.rect(screen, RED, rect)
    
class Laser:
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 5

 
    def update(self):
        self.y -= self.speed
        
    def draw(self):
        rect = [self.x, self.y, self.w, self.h]
        pygame.draw.rect(screen, GREEN, rect)
        
class Mob(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect.x = x
        self.rect.y = y

    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)

        if len(hit_list) > 0:
            self.kill()



class Bomb:
    
    def __init__(self):
        pass

    def update(self):
        pass
    
    
class Fleet:

    def __init__(self):
        pass

    def update(self):
        pass

    
# Make game objects

ship = Ship(384, 536, ship_img)
           
mob1 = Mob(128, 64, mob_img)
mob2 = Mob(256, 64, mob_img)
mob3 = Mob(384, 64, mob_img)

#Make sprite groups

player = pygame.sprite.GroupSingle()
player.add(ship)

lasers = pygame.sprite.Group()

mobs = pygmae.sprite.Group()
mobs.add(mob1, mob2, mob3)

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        ship.move_left()
    elif pressed[pygame.K_RIGHT]:
        ship.move_right()
        
    
    
    # Game logic (Check for collisions, update points, etc.)
    player.update()
    lasers.update()   

        

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    lasers.draw(screen)
    player.draw(screen)

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
