from pygame import *
import menu

def main_game():
    img_back = 'blackhole.webp' 
    img_hero = 'roket_v2.png'
    img_bullet = 'bullet.png'
    img_enemy = 'ufo_v2.png'

    win_width = 700
    win_height = 500
    display.set_caption('Shooter game V2 by biyu')
    window = display.set_mode((win_width, win_height))
    background = transform.scale(image.load(img_back), (win_width, win_height))#menentukan seberapa tinggi dan lebar background

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
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < win_width - 80:
                self.rect.y += self.speed
            if keys[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_RIGHT] and self.rect.x < win_width - 80:
                self.rect.x += self.speed

        def fire(self):
            bullet = Bullet(img_bullet, self.rect.centerx, self.rect.centery-10, 15, 20, 15)
            bullets.add(bullet)

    class Bullet(GameSprite):
        def update(self):
            self.rect.x += self.speed
            if self.rect.x > win_width:
                self.kill()

    class Enemy (GameSprite):
        def update(self):
            self.rect.x -= self.speed
            global lost

            if self.rect.x < 0:
                self.rect.y = randint(1, win_height)
                self.rect.x = 701
                lost = lost + 1

    ship = Player(img_hero, 5, 200, 100, 80, 10)

    from random import randint

    monsters = sprite.Group()
    for i in range(1, 6):
        monster = Enemy (img_enemy, 701, randint(1, win_height), 70, 50, 10)
        monsters.add(monster)

    bullets = sprite.Group()

    run = True
    finish = False
    #game loop
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

            collides = sprite.groupcollide(monsters, bullets, True, True)
            for c in collides:
                score = score + 1
                monster = Enemy (img_enemy, 701, randint(1, win_height), 70, 50, 10)
                monsters.add(monster)

            if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
                finish = True
                window.blit(lose, (200, 200))

            if score >= goal:
                finish = True
                window.blit(win, (200, 200))

            display.update()
            
        time.delay(50)

if __name__ == '__main__':
    start_game = menu.show_menu()
    if start_game:
        main_game()