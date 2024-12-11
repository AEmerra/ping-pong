from pygame import* 


racket_img = "C:/Users/ahmed/desktop/racket.png"
ball_img = "C:/Users/ahmed/desktop/tenis_ball.png"


BACKGROUND_COLOR = (200, 255, 255)
width, height = 600, 500
window = display.set_mode((width, height))
window.fill(BACKGROUND_COLOR)
display.set_caption("Ping pong")

clock = time.Clock()
FPS = 60


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
    def fill(self):
        draw.rect(window, BACKGROUND_COLOR, self.rect)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#main player class
class Player(GameSprite):
    #method to control the sprite with arrow keys
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed
            

    #method to control the sprite with arrow keys
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 80:
            self.rect.y += self.speed


padal_1 = Player(racket_img, 30, 200, 50, 150, 4)
padal_2 = Player(racket_img, 530, 200, 50, 150, 4)
ball = GameSprite(ball_img, 200, 200, 50, 50, 4)


speed_x = 3
speed_y = 3

font.init()
font_1 = font.SysFont("Times", 35)

lose_1 = font_1.render("Player 1 lose the game", True, (0, 0, 0))
lose_2 = font_1.render("Player 2 lose the game", True, (0, 0, 0))

run = True
finish = False
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        padal_1.fill()
        padal_2.fill()
        ball.fill()

        padal_1.update_l()
        padal_2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball, padal_1) or sprite.collide_rect(ball, padal_2):
            speed_x *= -1 


        if ball.rect.x < 0:
            window.blit(lose_1, (200, 200))
            finish = True


        if ball.rect.x > width:
            window.blit(lose_2, (200, 200))
            finish = True


        padal_1.reset()
        padal_2.reset()
        ball.reset()



    display.update()
    clock.tick(FPS)

