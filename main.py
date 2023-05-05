import pygame
import random
import time
import os

def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, (0, 0, 0))
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((572, 350))

def game_over() :
    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, (255, 0, 0))

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (572 / 2, 350 / 4)

    screen.fill((0, 0, 0))
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    quit()

if not os.path.exists("data/save.dat") :
    f = open("data/save.dat", 'w')
    f.write(str(0))
    f.close()
v = open("data/save.dat", 'r')
topScore = int(v.readline())
v.close()

pygame.display.set_caption('Ну, погоди!')

background = pygame.image.load('image/game-bg.jpg')
wolf_pic = pygame.image.load('image/wolf-p-0.png')
wolf_pic2 = pygame.image.load('image/wolf-p-1.png')
basket_down_left = pygame.image.load('image/basket-p-0-0.png')
basket_up_left = pygame.image.load('image/basket-p-0-1.png')
basket_down_right = pygame.image.load('image/basket-p-1-0.png')
basket_up_right = pygame.image.load('image/basket-p-1-1.png')
egg_pic = pygame.image.load('image/egg.png')
loss_pic = pygame.image.load('image/loss.png')

font = pygame.font.SysFont(None, 30)

screen.blit(background, (0, 0))

pygame.mixer.music.load('music/Tobu - Candyland.mp3')
pygame.mixer.music.play()

pos1 = [(45, 120, 289), (61, 130, 248), (80, 140, 280), (94, 148, 65), (110, 160, 0)]
pos2 = [(45, 195, 280), (62, 203, 254), (75, 213, 200), (95, 224, 90), (107, 233, 10)]
pos3 = [(505, 120, 0), (488, 128, 45), (472, 140, 105), (454, 145, 220), (441, 159, 290)]
pos4 = [(505, 195, 350), (489, 203, 20), (474, 215, 90), (455, 221, 200), (441, 233, 320)]

left_right = 0
up_down = 0
cnt = -1
score = 0
score2 = 0
save_time = 0
lvl = 1
speed = 1
loss = 0
check = True
while check:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score > topScore:
                g = open("data/save.dat", 'w')
                g.write(str(score))
                g.close()
                topScore = score
            pygame.quit()
            check = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_right = 0
            elif event.key == pygame.K_RIGHT:
                left_right = 1
            elif event.key == pygame.K_UP:
                up_down = 0
            elif event.key == pygame.K_DOWN:
                up_down = 1

    screen.blit(background, (0, 0))

    if left_right == 0:
        screen.blit(wolf_pic, (179, 164))
        if up_down == 0:
            screen.blit(basket_up_left, (126, 158))
        else:
            screen.blit(basket_down_left, (124, 233))
    else:
        screen.blit(wolf_pic2, (297, 166))
        if up_down == 0:
            screen.blit(basket_up_right, (368, 166))
        else:
            screen.blit(basket_down_right, (362, 241))

    if time.time() - save_time > speed:
        save_time = time.time()
        if cnt == -1:
            drop = random.randint(1, 4)
        if drop == 1:
            if cnt == 4:
                if up_down == 0 and left_right == 0:
                    score += 1
                    score2 += 1
                else:
                    loss += 1
                cnt = -2
            cnt += 1
        elif drop == 2:
            if cnt == 4:
                if up_down == 1 and left_right == 0:
                    score += 1
                    score2 += 1
                else:
                    loss += 1
                cnt = -2
            cnt += 1
        elif drop == 3:
            if cnt == 4:
                if up_down == 0 and left_right == 1:
                    score += 1
                    score2 += 1
                else:
                    loss += 1
                cnt = -2
            cnt += 1
        elif drop == 4:
            if cnt == 4:
                if up_down == 1 and left_right == 1:
                    score += 1
                    score2 += 1
                else:
                    loss += 1
                cnt = -2
            cnt += 1
        if score2 == 4:
            score2 = 0
            lvl += 1
            speed /= 2

    if drop == 1:
        egg_pic_rotated = pygame.transform.rotate(egg_pic, int(pos1[cnt][2]))
        screen.blit(egg_pic_rotated, (int(pos1[cnt][0]), int(pos1[cnt][1])))
    elif drop == 2:
        egg_pic_rotated = pygame.transform.rotate(egg_pic, int(pos2[cnt][2]))
        screen.blit(egg_pic_rotated, (int(pos2[cnt][0]), int(pos2[cnt][1])))
    elif drop == 3:
        egg_pic_rotated = pygame.transform.rotate(egg_pic, int(pos3[cnt][2]))
        screen.blit(egg_pic_rotated, (int(pos3[cnt][0]), int(pos3[cnt][1])))
    elif drop == 4:
        egg_pic_rotated = pygame.transform.rotate(egg_pic, int(pos4[cnt][2]))
        screen.blit(egg_pic_rotated, (int(pos4[cnt][0]), int(pos4[cnt][1])))

    draw_text('Level:' + str(lvl), font, screen, 350, 50)
    draw_text('Score:' + str(score), font, screen, 350, 80)
    draw_text('Top Score:' + str(topScore), font, screen, 350, 20)

    if loss == 1:
        crop_rect = pygame.Rect(0, 0, 38, 32)
        cropped_image = loss_pic.subsurface(crop_rect)
        screen.blit(cropped_image, (326, 114))
    if loss == 2:
        crop_rect = pygame.Rect(0, 0, 76, 32)
        cropped_image = loss_pic.subsurface(crop_rect)
        screen.blit(cropped_image, (326, 114))
    if loss == 3:
        crop_rect = pygame.Rect(0, 0, 114, 32)
        cropped_image = loss_pic.subsurface(crop_rect)
        screen.blit(cropped_image, (326, 114))
        if score > topScore:
            g = open("data/save.dat", 'w')
            g.write(str(score))
            g.close()
            topScore = score
        game_over()

    pygame.display.update()
