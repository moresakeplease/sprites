from typing import Any
import pygame, sys
from pygame.locals import*

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        #create empty list
        self.jump_sound = pygame.mixer.Sound('jump.wav')
        self.sprites = [pygame.image.load(f'green_blob_00{str(i).zfill(2)}.png').convert_alpha() for i in range(8, 22)]
        self.curent_sprite = 0
        self.image = self.sprites[self.curent_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.jump_sound.play()
            self.is_jumping = True


    def update(self):
        if self.is_jumping == True:
            #using increments  with 0.2 will slow down the loop
            self.curent_sprite += 0.2

            if self.curent_sprite >= len(self.sprites):
                self.curent_sprite = 0
                #tell animation to run once
                self.is_jumping = False

            self.image = self.sprites[int(self.curent_sprite)]

#general setup 
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

#game screen
screen_width = 200
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

#Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(50, 100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()


    #Drawing
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()

    #frame rate control
    clock.tick(60)