from pygame import * 


class  GameSprite(sprite.Sprite):
    def __init__(self,player_img, p_x, p_y,size_w,size_h, p_speed):
        super().__init__()
        self.w = size_w
        self.h = size_h
        self.image = transform.scale( image.load(player_img) , (self.w ,self.h) )
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y) )

class Player(GameSprite):
    def update_L(self):
        self.reset()
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed
    def update_R(self):
        self.reset()
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed
win_w = 700
win_h = 500

display.set_caption('Shoter')
window = display.set_mode( (win_w,win_h ))

p1 =  Player("Снимок экрана 2022-04-03 171222.png",10,0,10,60,10)
p2 =  Player("Снимок экрана 2022-04-03 171222.png",670,0,10,60,10)

ball = GameSprite("b7ea4111c4b19f8-removebg-preview.png",310,210,80,80,3)

v_x = 3
v_y = 3

font.init()
font = font.Font(None,35)
lose1 = font.render("player 1 LOSEE!!!", True, (50,0,0))
lose2 = font.render("player 2 LOSEE!!!", True, (50,0,0))

run = True
finish = False

back = Surface((700,500))
back.fill((225,255,255))



while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

     

    if not finish:
        window.blit(back,(0,0))
        ball.rect.x += v_x
        ball.rect.y += v_y

        if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
            v_x *= -1

        if ball.rect.y < 0 or ball.rect.y > 500 - 80:
            v_y *= -1

        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1,(350,250))
        if ball.rect.x > 700 :
            finish = True
            window.blit(lose2,(350,250))





        p1.update_L()
        p2.update_R()
        ball.reset()
        
        display.update()
        time.delay(60)