import pygame 
# DO SCORE AND RESTart button
pygame.init()
pygame.display.set_caption('TICTACTOE')
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
screen_w = 500
screen_h = 600
screen = pygame.display.set_mode((screen_w,screen_h))
screen.fill(white)

font = pygame.font.SysFont('arial',18)
msg_rest = font.render('RESTART',False,red)
restart = pygame.draw.rect(screen,red,(0,0,100,50),2)
screen.blit(msg_rest,(restart.centerx-40,restart.centery-10))
block1 = pygame.draw.rect(screen,red,(250,300,50,50),1)
check1,check2,check3,check4,check5,check6,check7,check8,check9 = False,False,False,False,False,False,False,False,False
b1,b2,b3,b4,b5,b6,b7,b8,b9 = None,None,None,None,None,None,None,None,None
block2 = pygame.draw.rect(screen,red,(200,300,50,50),1)
block3 = pygame.draw.rect(screen,red,(300,300,50,50),1)
block4 = pygame.draw.rect(screen,red,(250,250,50,50),1)
block5 = pygame.draw.rect(screen,red,(200,250,50,50),1)
block6 = pygame.draw.rect(screen,red,(300,250,50,50),1)
block7 = pygame.draw.rect(screen,red,(250,200,50,50),1)
block8 = pygame.draw.rect(screen,red,(200,200,50,50),1)
block9 = pygame.draw.rect(screen,red,(300,200,50,50),1)

switch_XO = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            if mouse_x> restart.left and mouse_x < restart.right and mouse_y>restart.top and mouse_y < restart.bottom:
                screen.fill(white)
                block1 = pygame.draw.rect(screen,red,(250,300,50,50),1)
                block2 = pygame.draw.rect(screen,red,(200,300,50,50),1)
                block3 = pygame.draw.rect(screen,red,(300,300,50,50),1)
                block4 = pygame.draw.rect(screen,red,(250,250,50,50),1)
                block5 = pygame.draw.rect(screen,red,(200,250,50,50),1)
                block6 = pygame.draw.rect(screen,red,(300,250,50,50),1)
                block7 = pygame.draw.rect(screen,red,(250,200,50,50),1)
                block8 = pygame.draw.rect(screen,red,(200,200,50,50),1)
                block9 = pygame.draw.rect(screen,red,(300,200,50,50),1)
                restart = pygame.draw.rect(screen,red,(0,0,100,50),2)
                screen.blit(msg_rest,(restart.centerx-40,restart.centery-10))
                check1,check2,check3,check4,check5,check6,check7,check8,check9 = False,False,False,False,False,False,False,False,False
                b1,b2,b3,b4,b5,b6,b7,b8,b9 = None,None,None,None,None,None,None,None,None
            if mouse_x > block1.x and mouse_x < block1.x+50 and mouse_y > block1.y and mouse_y<block1.y+50 and not check1:
                if switch_XO == 0:
                    pygame.draw.circle(screen,blue,(block1.center),25,2)
                    b1 = switch_XO
                    switch_XO=1
                else:
                    pygame.draw.line(screen,blue,(block1.x,block1.y),(block1.x+50,block1.y+50),2)
                    pygame.draw.line(screen,blue,(block1.x+50,block1.y),(block1.x,block1.y+50),2)
                    b1 = switch_XO
                    switch_XO=0
                print('1 : ',b1)
                if b1 ==b2 and b1==b3 and b2==b3:
                    if b1==0:
                        print('O WIN')
                    else:
                        print('X WIN')
                    pygame.draw.line(screen,red,(block2.x,block2.y+25),(block3.x+50,block3.y+25),3)
                if b1==b4 and b1==b7 and b4==b7:
                    pygame.draw.line(screen,red,(block1.centerx,block1.bottom),(block7.midtop),3)
                check1 =True
            if mouse_x > block2.x and mouse_x < block2.x+50 and mouse_y > block2.y and mouse_y<block2.y+50 and not check2:
                if switch_XO ==0:
                    pygame.draw.circle(screen,blue,(block2.center),25,2)
                    b2 = switch_XO
                    switch_XO=1
                else:
                    pygame.draw.line(screen,blue,(block2.x,block2.y),(block2.x+50,block2.y+50),2)
                    pygame.draw.line(screen,blue,(block2.x+50,block2.y),(block2.x,block2.y+50),2)
                    b2 = switch_XO
                    switch_XO=0
                print('2 : ',b2)
                if b1 ==b2 and b1==b3 and b2==b3:
                    pygame.draw.line(screen,red,(block2.x,block2.y+25),(block3.x+50,block3.y+25),3)
                if b2==b5 and b2==b8 and b5==b8:
                    pygame.draw.line(screen,red,(block2.midbottom),(block8.midtop),3)
                if b2==b4 and b2==b9:
                    pygame.draw.line(screen,red,(block2.bottomleft),(block9.topright),3)
                check2 =True
            if mouse_x > block3.x and mouse_x < block3.x+50 and mouse_y > block3.y and mouse_y<block3.y+50 and not check3:
                if switch_XO ==0:
                    pygame.draw.circle(screen,blue,(block3.center),25,2)
                    b3 = switch_XO
                    switch_XO =1
                else:
                    pygame.draw.line(screen,blue,(block3.x,block3.y),(block3.x+50,block3.y+50),2)
                    pygame.draw.line(screen,blue,(block3.x+50,block3.y),(block3.x,block3.y+50),2)
                    b3 = switch_XO
                    switch_XO=0
                check3 = True
                print('3 : ',b3)
                if b1 ==b2 and b1==b3 and b2==b3:
                    pygame.draw.line(screen,red,(block2.x,block2.y+25),(block3.x+50,block3.y+25),3)
                if b3==b6 and b3==b9 and b6==b9:
                    pygame.draw.line(screen,red,(block3.midbottom),(block9.midtop),3)
                if b3==b4 and b3==b8:
                    pygame.draw.line(screen,red,(block8.topleft),(block3.bottomright),3)
            if mouse_x > block4.x and mouse_x < block4.x+50 and mouse_y > block4.y and mouse_y<block4.y+50 and not check4:
                if switch_XO ==0:
                    pygame.draw.circle(screen,blue,(block4.center),25,2)
                    b4 = switch_XO
                    switch_XO =1
                else:
                    pygame.draw.line(screen,blue,(block4.x,block4.y),(block4.x+50,block4.y+50),2)
                    pygame.draw.line(screen,blue,(block4.x+50,block4.y),(block4.x,block4.y+50),2)
                    b4 =switch_XO
                    switch_XO =0
                print('4 : ',b4)
                if b1==b4 and b1==b7 and b4==b7:
                    pygame.draw.line(screen,red,(block1.centerx,block1.bottom),(block7.midtop),3)
                if b4==b5 and b4==b6:
                    pygame.draw.line(screen,red,(block5.midleft),(block6.midright),3)
                if b3==b4 and b3==b8:
                    pygame.draw.line(screen,red,(block8.topleft),(block3.bottomright),3)
                if b2==b4 and b2==b9:
                    pygame.draw.line(screen,red,(block2.bottomleft),(block9.topright),3)
                check4=True
            if mouse_x > block5.x and mouse_x < block5.x+50 and mouse_y > block5.y and mouse_y<block5.y+50 and not check5:
                if switch_XO ==0:
                    pygame.draw.circle(screen,blue,(block5.center),25,2)
                    b5 = switch_XO
                    switch_XO =1
                else:
                    pygame.draw.line(screen,blue,(block5.x,block5.y),(block5.x+50,block5.y+50),2)
                    pygame.draw.line(screen,blue,(block5.x+50,block5.y),(block5.x,block5.y+50),2)
                    b5 = switch_XO
                    switch_XO =0
                print('5 : ',b5)
                if b2==b5 and b2==b8 and b5==b8:
                    pygame.draw.line(screen,red,(block2.midbottom),(block8.midtop),3)
                if b4==b5 and b4==b6:
                    pygame.draw.line(screen,red,(block5.midleft),(block6.midright),3)
                
                check5=True
            if mouse_x > block6.x and mouse_x < block6.x+50 and mouse_y > block6.y and mouse_y<block6.y+50 and not check6:
                if switch_XO ==0:
                    pygame.draw.circle(screen,blue,(block6.center),25,2)
                    b6 = switch_XO
                    switch_XO =1
                else:
                    pygame.draw.line(screen,blue,(block6.x,block6.y),(block6.x+50,block6.y+50),2)
                    pygame.draw.line(screen,blue,(block6.x+50,block6.y),(block6.x,block6.y+50),2)
                    b6 = switch_XO
                    switch_XO =0
                print('6 : ',b6)
                if b3==b6 and b3==b9 and b6==b9:
                    pygame.draw.line(screen,red,(block3.midbottom),(block9.midtop),3)
                if b4==b5 and b4==b6:
                    pygame.draw.line(screen,red,(block5.midleft),(block6.midright),3)
                check6=True
            if mouse_x > block7.x and mouse_x < block7.x+50 and mouse_y > block7.y and mouse_y<block7.y+50 and not check7:
                if switch_XO ==0:
                    pygame.draw.circle(screen,blue,(block7.center),25,2)
                    b7 = switch_XO
                    switch_XO =1
                else :
                    pygame.draw.line(screen,blue,(block7.x,block7.y),(block7.x+50,block7.y+50),2)
                    pygame.draw.line(screen,blue,(block7.x+50,block7.y),(block7.x,block7.y+50),2)
                    b7 = switch_XO
                    switch_XO =0
                print('7 : ',b7)
                if b1==b4 and b1==b7 and b4==b7:
                    pygame.draw.line(screen,red,(block1.centerx,block1.bottom),(block7.midtop),3)
                if b7==b8 and b8==b9:
                    pygame.draw.line(screen,red,(block9.midright),(block8.midleft),3)
                check7=True
            if mouse_x > block8.x and mouse_x < block8.x+50 and mouse_y > block8.y and mouse_y<block8.y+50 and not check8:
                if switch_XO ==0:
                    pygame.draw.circle(screen,blue,(block8.center),25,2)
                    b8 = switch_XO
                    switch_XO=1
                else:
                    pygame.draw.line(screen,blue,(block8.x,block8.y),(block8.x+50,block8.y+50),2)
                    pygame.draw.line(screen,blue,(block8.x+50,block8.y),(block8.x,block8.y+50),2)
                    b8 = switch_XO
                    switch_XO =0
                check8=True
                print('8 : ',b8)
                if b2==b5 and b2==b8 and b5==b8:
                    pygame.draw.line(screen,red,(block2.midbottom),(block8.midtop),3)
                if b7==b8 and b8==b9:
                    pygame.draw.line(screen,red,(block9.midright),(block8.midleft),3)
                if b3==b4 and b3==b8:
                    pygame.draw.line(screen,red,(block8.topleft),(block3.bottomright),3)
            if mouse_x > block9.x and mouse_x < block9.x+50 and mouse_y > block9.y and mouse_y<block9.y+50 and not check9:
                if switch_XO ==0:
                    pygame.draw.circle(screen,blue,(block9.center),25,2)
                    b9 = switch_XO
                    switch_XO=1
                else:
                    pygame.draw.line(screen,blue,(block9.x,block9.y),(block9.x+50,block9.y+50),2)
                    pygame.draw.line(screen,blue,(block9.x+50,block9.y),(block9.x,block9.y+50),2)
                    b9 = switch_XO
                    switch_XO =0
                check9=True
                if b3==b6 and b3==b9 and b6==b9:
                    pygame.draw.line(screen,red,(block3.midbottom),(block9.midtop),3)
                if b7==b8 and b8==b9:
                    pygame.draw.line(screen,red,(block9.midright),(block8.midleft),3)
                if b2==b4 and b2==b9:
                    pygame.draw.line(screen,red,(block2.bottomleft),(block9.topright),3)
                print('9 : ',b9)
        pygame.display.update()
pygame.quit()