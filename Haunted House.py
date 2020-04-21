import pygame
size = (800, 600)
screen = pygame.display.set_mode(size)

'''Colours'''
white = 0xFB, 0xF5, 0xF3
black = 0x07, 0x07, 0x07

lightGrey = 0xA2, 0xA7, 0xA5
dirtyGrey = 0x39, 0x3E, 0x41

dirtyRed = 0x51, 0x3B, 0x3C

blackBlue = 0x01, 0x11, 0x0A

brownClock = 133, 92, 60
darkBrownClock = 105, 53, 12

brown = 0x6B, 0x65, 0x4B
red = 0xA2, 0x00, 0x21

darkRed = 0x64, 0x0D, 0x14

beige = 0xE8, 0xD4, 0xB3

blue = 0x36,0x85,0xB5
pictureBrown = 0x66, 0x0C, 0x0c
pictureFrameGold = 255, 215, 0
'''Colours'''

done = False
 
clock = pygame.time.Clock()

#coordinates for bell
rect_x = 150
rect_y = 85 

#coordinates for eye
roll_x = 1
rollChangeX = 5

#coordinates for ghost
ghost_x = 100
ghost_y = 489

ghostChange_x = 5
ghostChange_y = 5

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ghostChange_y = -50
                ghost_y += ghostChange_y
            elif event.key == pygame.K_DOWN:
                ghostChange_y = 50
                ghost_y += ghostChange_y
            elif event.key == pygame.K_RIGHT:
                ghostChange_x = 50
                ghost_x += ghostChange_x
            elif event.key == pygame.K_LEFT:
                ghostChange_x = -50              
                ghost_x += ghostChange_x
    
    screen.fill(white)
    
    #The room
    pygame.draw.rect(screen, darkRed, [0,300,800,300])
    pygame.draw.rect(screen, black, [0,0,800,300])
    
    pygame.draw.rect (screen, dirtyGrey, [0,290,800,15])
    for y_offset in range (0, 290, 10):
        pygame.draw.rect(screen, dirtyGrey, [0,0 + y_offset,800,2])
        
    #Rolling Eye
    pygame.draw.ellipse (screen, white, [roll_x, 300, 25, 25])
    pygame.draw.ellipse (screen, blue, [roll_x + 5, 305, 15, 15])
    
    roll_x += rollChangeX
    
    if roll_x <= 0 or roll_x >= 450:
        rollChangeX = rollChangeX * -1
        
    #The carpet
    pygame.draw.ellipse (screen, blackBlue, [240, 270, 580, 250])
    pygame.draw.ellipse (screen, dirtyRed, [260, 290, 550, 200])
    
    #Painting
    for x_offset in range (0, 800, 200):
        pygame.draw.rect (screen, pictureFrameGold, [40+ x_offset,40,70,70])
        pygame.draw.rect (screen, pictureBrown, [50 + x_offset,50,50,50])
        pygame.draw.circle (screen, white, [75+x_offset,75],15)
        pygame.draw.line (screen, black, [x_offset + 70, 80], [x_offset + 70,90],3)
        pygame.draw.line (screen, black, [x_offset + 80, 80], [x_offset + 80,90],3)
        
        
        pygame.draw.circle (screen, black, [70 + x_offset,70], 5)
        pygame.draw.circle (screen, black, [83 + x_offset,70], 5)
        
    #The Bedpost
    pygame.draw.rect (screen, brown, [300, 250, 25, 150])
    pygame.draw.rect (screen, brown, [775, 250, 25, 150])
    pygame.draw.rect (screen, red, [750,150,50,150])
    
    #The Bed
    pygame.draw.rect (screen, red, [300,250,500,100])
    pygame.draw.rect (screen, white, [300,250,451,5])
    
    #The Pillow
    pygame.draw.polygon (screen, white, [[700,250],[750,170],[750,250]])
    
    #The grandfather clock
    pygame.draw.rect (screen, brownClock,[100, 75,100,250])
    pygame.draw.rect (screen, darkBrownClock, [95, 325,110,5])
    pygame.draw.rect (screen, white, [110, 85,80,230])
    pygame.draw.rect (screen, darkBrownClock, [95,75, 115,5])

    #The animated bell
    pygame.draw.rect (screen, pictureFrameGold, [rect_x,rect_y, 5,115])
    pygame.draw.ellipse (screen, pictureFrameGold, [rect_x-25, rect_y + 100,50,50]   )
    rect_x += 5

    if rect_x > 0 or rect_x < 150:
        rect_x *= -1
    
    #The ghost

    pygame.draw.rect (screen, white, [ghost_x, ghost_y + 11, 50, 50])
    pygame.draw.circle (screen, white, [ghost_x + 25, ghost_y + 10], 25)
    pygame.draw.circle (screen, black, [ghost_x + 35, ghost_y], 5)
    
    if ghost_x <= 0 or ghost_x >= 800:
        ghostChange_x = ghostChange_x * -1
    
    if ghost_y <= 0 or ghost_y >= 600:
        ghostChange_y = ghostChange_y * -1
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
pygame.quit()