import pygame

pygame.init()

display_width = 1000
display_height = 600
title = True
win = False
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Portle')

font = pygame.font.SysFont("comicsansms", 200)
font1 = pygame.font.SysFont("comicsansms", 75)
font2 = pygame.font.SysFont("comicsansms", 10)
victoryfont = pygame.font.SysFont("comicsansms", 100)
returnfont = pygame.font.SysFont("comicsansms", 10)
text = font.render("Portle", True, (0, 128, 0))
instructions = font2.render("Q to make a blue portle, E to take it back, R to make an orange portle, F to take it back, and the rectanlges display where the portles will be made. Try to make it to the green rectangle", True,(255,255,255))
play = font1.render("Play", True, (0, 128, 0))
victory = victoryfont.render("You win!", True, (255,255,255))
victory2 = returnfont.render("press t to return to title screen, winner. However, the portles are now drunk. Just restart the program for another playthrough without bugs", True, (255,255,255))
crashed = False


x = 255
y = 255
r = x
u = y
b = x
l = y
x_change = 0
y_change = 0
r_change = 0
u_change = 0
b_change = 0
l_change = 0

portalblue = False
portalorange = False
while not crashed:
#runs if the title needs to be made
    if title == True:
        gameDisplay.fill((255,255,255))
        gameDisplay.blit(text, (300, 100))
        #pygame.display.update()
        pygame.draw.rect(gameDisplay, (255,165,0),(400,420,200,69+31))
        
        gameDisplay.blit(play, (440, 410))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 400 < event.pos[0] < 600 and 400 < event.pos[1] < 470:
                    title = False


#game code runs here
    elif title == False:
        gameDisplay.fill((90,90,90))
        pygame.draw.rect(gameDisplay, (255,255,255),(x,y,50,50))
    #Green objective
        pygame.draw.rect(gameDisplay, (0,255,0), (800,300,70,70))
       
   
        
    #line that you can't cross
        pygame.draw.line(gameDisplay, (0,0,0),(500,600),(500,0),15)
        #instructions
        gameDisplay.blit(instructions, (0,0))
        
        for event in pygame.event.get():
            #controls
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                elif event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_s:
                    y_change = 5
                elif event.key == pygame.K_q:
                    portalblue = True
                elif event.key == pygame.K_e:
                    portalblue = False
                elif event.key == pygame.K_r:
                    portalorange = True
                elif event.key == pygame.K_f:
                    portalorange = False
            #when the keys are not pressed the position of the sprite cannot change
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
        x += x_change
        y += y_change
        r += r_change
        u += u_change
        b += b_change
        l += l_change
        #borders
        if x > 950:
            x = 950
        if y < 0:
            y = 0
        if x < 0:
            x = 0
        if y > 550:
            y = 550
        #line in middle that can't be crossed
        if 460 > x > 450:
            x = 450
        if 500 < x < 510:
            x = 510
        r_change = x_change
        u_change = y_change
        b_change = x_change
        l_change = y_change
        if portalblue == True: 
            r_change = 0
            u_change = 0
            drawme(r,u)
            if event.type == pygame.KEYDOWN:

    #going into the new portle
                if event.key == pygame.K_s and x < r+400+35 and x > r+400-35 and y < u+35 and y > u-35:
                    x = b+100
                    y = l+70
                elif event.key == pygame.K_w and x < r+400+35 and x > r+400-35 and y < u+35 and y > u-35:
                    x = b+100
                    y = l-70
                elif event.key == pygame.K_a and x < r+400+35 and x > r+400-35 and y < u+35 and y > u-35:
                    x = b+100-70
                    y = l
                elif event.key == pygame.K_d and x < r+400+35 and x > r+400-35 and y < u+35 and y > u-35:
                    x = b+100+70
                    y = l
            
        if portalorange == True: 
            b_change = 0
            l_change = 0
            drawyou(b,l)
            if event.type == pygame.KEYDOWN:
    #going into the new portle
                if event.key == pygame.K_s and x < b+100+35 and x > b+100-35 and y < l+35 and y > l-35:
                    x = r+400
                    y = u+70
                elif event.key == pygame.K_w and x < b+100+35 and x > b+100-35 and y < l+35 and y > l-35:
                    x = r+400
                    y = u-70
                elif event.key == pygame.K_a and x < b+100+35 and x > b+100-35 and y < l+35 and y > l-35:
                    x = r+400-70
                    y = u
                elif event.key == pygame.K_d and x < b+100+35 and x > b+100-35 and y < l+35 and y > l-35:
                    x = r+400+70
                    y = u
        
    
        if portalorange == False:
            pygame.draw.rect(gameDisplay,(255,165,0),(x+100,y,30,30))
        if portalblue == False:
            pygame.draw.rect(gameDisplay,(0,0,255),(x+400,y,30,30))
#if the player gets the epic victory royale
        if x < 835 and x > 765 and y < 335 and y > 265:
            win = True
        if win == True:
            gameDisplay.fill((90,90,90))
            gameDisplay.blit(victory, (350,200))
            gameDisplay.blit(victory2, (200,400))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    title = True
                    win = False
                    x = 255
                    y = 255
                    portalorange = False
                    portalblue = False
            
            
            
           
                        
        
        #while not portal:
            #pygame.draw.rect(gameDisplay,(90,90,90),(x+400,y,70,70))
            
    pygame.display.update()
               
    clock.tick(60)
        
   
    def drawyou(b,l):
        pygame.draw.rect(gameDisplay,(255,165,0),(b+100,l,70,70))
    def drawme(r,u):
        pygame.draw.rect(gameDisplay,(0,0,255),(r+400,u,70,70))

