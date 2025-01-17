from pygame import*


BACKGROUND_COLOR= (255, 0, 0) 
width, height = 800, 650

window = display.set_mode((width, height))
window.fill(BACKGROUND_COLOR) 
display.set_caption("Ping pong")


clock = time.Clock()
FPS = 60
run = True

class GameSprite(sprite.Sprite):
 #class constructor
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #call for the class (Sprite) constructor:
       sprite.Sprite.__init__(self)


       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #every sprite must have the rect property that represents the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #method drawing the character on the window
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#main player class
class Player(GameSprite):


    def update_1(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < height - 80: 
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < height - 80: 
            self.rect.y += self.speed


while run:

    for e in event.get():
        if e.type == QUIT:
            run = False


    display.update()
    clock.tick(FPS)