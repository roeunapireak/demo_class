from pygame import *

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self, window):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(Gamesprite):

    def update_right(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y <= 380 :
            self.rect.y += self.speed

    def update_left(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y <= 380 :
            self.rect.y += self.speed