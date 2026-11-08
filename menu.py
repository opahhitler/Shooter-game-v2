from pygame import *

init()
font.init()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Shooter Game V2 - Menu')

try:
    background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))
except:
    background = None

font_title = font.Font(None, 60)
font_button = font.Font(None, 40)

title_text = font_title.render('SPACE SHOOTER V2', True, (255, 255, 255))
start_text = font_title.render('Press SPACE to Start', True, (0, 255, 0))
exit_text = font_title.render('Press ESC to Exit', True, (255, 100, 100))

def show_menu():
    run_menu = True
    while run_menu:
        for e in event.get():
            if e.type == QUIT:
              return False
            elif e.type == KEYDOWN:
              if e.key == K_SPACE:
                 return True
              elif e.key == K_ESCAPE:
                 return False

        if background:
            window.blit(background, (0, 0))
        else:
            window.fill((20, 20, 20))


        window.blit(title_text, (win_width / 2 - title_text.get_width() / 2, 150))
        window.blit(start_text, (win_width / 2 - start_text.get_width() / 2, 250))
        window.blit(exit_text, (win_width / 2 - exit_text.get_width() / 2, 310))

        display.update()
        time.delay(50)  
show_menu()