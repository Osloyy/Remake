

import pygame as pg 

pg.init()
size = 1280, 720

running = True

screen = pg.display.set_mode(size)
pg.display.set_caption("Remake")
playerimg = pg.image.load('player.png')
newh = 32
neww = newh
playerimg = pg.transform.scale(playerimg, (neww, newh))
playerrect = playerimg.get_rect()
playerrect.centerx = 1280 // 2
playerrect.centery = 720 // 2
playerspeed = 0.9
spritedir = 0
friction = 0.6
playervelocityx = 0


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    def input():
        global spritedir, playervelocityx
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            playervelocityx -= playerspeed
            spritedir = 1
        if keys[pg.K_d]:
            playervelocityx += playerspeed
            spritedir = 0


    input()
    playervelocityx *= (1 - friction)
    playerrect.x += playervelocityx
    screen.fill((0,0,0))
    if spritedir == 1:
        playerflip = pg.transform.flip(playerimg, True, False)
    else:
        playerflip = playerimg

    screen.blit(playerflip, playerrect)
    pg.display.flip()


pg.quit()