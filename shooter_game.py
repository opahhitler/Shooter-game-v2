#Create your own shooter

from pygame import *

img_back = 'galaxy.jpg'
img_hero = 'roket v2.png'
img_enemy = 'ufo.png'
img_bullet = 'bullet.png'
img_ast = 'asteroid.png'

win_width = 700
win_height = 500
display.set_caption('Shooter game by biyu')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

score = 0
lost = 0
max_lost = 3
goal = 10

font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
font2 = font.Font(None, 36)
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
      bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
      bullets.add(bullet)



class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


class Enemy (GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost

        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

ship = Player('rocket.png', 5, 400, 80, 100, 10)

from random import randint

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy,randint(80, win_width - 80),-40,80,50,randint(1, 5))
    monsters.add(monster)

asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = Enemy(img_ast, randint(30, win_width-30), 40, 80, 50, randint(1, 7))
    asteroids.add(asteroid)

bullets = sprite.Group()

run = True
finish = False
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
          if e.key == K_SPACE:

            ship.fire()

    if not finish:
        window.blit(background, (0, 0))
        text = font2.render('Score:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render('Missed:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        monsters.update()
        monsters.draw(window)
        ship.update()
        ship.reset()
        bullets.update()
        bullets.draw(window)
        asteroids.update()
        asteroids.draw(window)
        
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width-80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))

        if sprite.spritecollide(ship, asteroids, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))

        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        display.update()
        
    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
          b.kill()

        for m in monsters:
          m.kill()

         "firstdelay(3000)
        for i in range(1, 6):
            monster = Enemy(img_enemy, randint(80, win_width-80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)      
    time.delay(50)        