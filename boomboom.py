from lib2to3.pgen2 import pgen
import pygame
import time
import random
import logging

####################################<GLOBAL VARIABLES>##################################################


display_width=800
display_height=600
car_width=130
car_height=166
#<Colors>

white=(255,255,255)
black=(0,0,0)
pink=(255,182,193)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,100)
block_color= (53,115,255)
background_color=(255,255,0)

#</Colors>

highscore=0
flag1=0
flag2=0


####################################</GLOBAL VARIABLES>##################################################



#####################################<INITIALIZE THE SCREEN>##############################################



pygame.init()
gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Speedy Racers")
clock = pygame.time.Clock() 

carImg = pygame.image.load("Car.png")
explosion = pygame.image.load("Explosions.png")



#####################################</INITIALIZE THE SCREEN>##############################################



def current_score(count,hs):
    font = pygame.font.SysFont(None,25)
    score = font.render("Score "+str(count),True,black)
    if(count>hs):
        hs=count
    hScore = font.render("High Score "+str(hs),True,black)
    gameDisplay.blit(score,(0,0))
    gameDisplay.blit(hScore,(0,15))

def message_display2(text):
    largeText=pygame.font.Font('freesansbold.ttf',100)
    textSurf,textRect= text_objects(text,largeText)
    textRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf,textRect)
    
    pygame.display.update()

def blocks(x,y,width,height,color):
    pygame.draw.rect(gameDisplay,color,[x,y,width,height])

def blocks(x,y,width,height,color):
    pygame.draw.rect(gameDisplay,color,[x,y,width,height])

def crash():
    message_display("Boom Boom")


def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',100)
    textSurf,textRect= text_objects(text,largeText)
    textRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()
    time.sleep(2)

    start_game()

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface , textSurface.get_rect()
    
    

def car(x,y):
    gameDisplay.blit(carImg,(x,y))


    
def start_game():

        
    exitGame=0
    x=(display_width*0.45)
    y=(display_height*0.7)
    x_new=0
    y_new=0
    score=0
    

    ###############################<BLOCK DIMENSIONS>#################################
    
    block_speed = 3
    block_width=100
    block_height=100
    
    block_startx1 = random.randrange(0,display_width-block_width)           #BLOCK 1
    block_starty1 = -600
    
    block_startx2 = random.randrange(0,display_width-block_width)           #BLOCK 2
    block_starty2 = -600
    
    block_startx3 = random.randrange(0,display_width-block_width)           #BLOCK 3
    block_starty3 = -600

    ###############################</BLOCK DIMENSIONS>#################################



    ##############################<KEYBOARD INPUTS AND CAR MOVEMENT>###########################################


    
    while (exitGame==0):
        
        for event in pygame.event.get():

            mouse= pygame.mouse.get_pos() 

            
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()


            if (event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_LEFT):
                    x_new=-5
                elif(event.key==pygame.K_RIGHT):
                    x_new=5
                elif(event.key==pygame.K_ESCAPE):
                    pygame.quit()
                    quit()
            if (event.type==pygame.KEYUP):
                if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                    x_new=0
            
        x+=x_new
       


    ##############################</KEYBOARD INPUTS AND CAR MOVEMENT>###########################################


        
        gameDisplay.fill(background_color)
        
        
        if(block_starty1==-600):
            for i in range(3,0,-1):
                num=str(i)

                if(i==3):
                    gameDisplay.fill(red)
                elif(i==2):
                    gameDisplay.fill(background_color)
                elif(i==1):
                    gameDisplay.fill(green)
    
                message_display2(num)
                time.sleep(1)
                pygame.display.update()
            gameDisplay.fill(pink)
            message_display2("GO")
            time.sleep(2)
            highscore=score
        car(x,y)
        
###################################<LOAD THE BLOCKS ON THE SCREEN>#########################################        
        blocks(block_startx1,block_starty1,block_width,block_height,block_color)
        
        if(score>=10):
            flag1=1
            blocks(block_startx2,block_starty2,block_width,block_height,red)

        else:
            flag1=0
        if(score>=20):
            flag2=1
            blocks(block_startx3,block_starty3,block_width,block_height,green)
        
        else:
            flag2=0

###################################</LOAD THE BLOCKS ON THE SCREEN>#########################################


####################################<BOX SPEEDS>############################################################

            
        block_starty1+=block_speed*0.8
        block_starty2+=block_speed
        block_starty3+=block_speed*0.7


######################################</BOX SPEEDS>#########################################################




######################################<BOUNDARY CRASH CONDITION>############################################   

        if(x>(display_width-car_width) or x<0):
            gameDisplay.blit(explosion,(x,y))
            crash()

######################################</BOUNDARY CRASH CONDITION>############################################


            
################################<SPAWN NEW BLOCK WHEN IT AT BOTTOM>#########################################
        if(block_starty1>display_height):
            block_starty1=0-block_height
            block_startx1 = random.randrange(0,display_width-block_width)
            score+=1
            block_speed+=0.1

        if(flag1==1):
            
            if(block_starty2>display_height):
                block_starty2=0-block_height
                block_startx2 = random.randrange(0,display_width-block_width)
                score+=1
                block_speed+=0.1
                
        if(flag2==1):
            
            if(block_starty3>display_height):
                block_starty3=0-block_height
                block_startx3 = random.randrange(0,display_width-block_width)
                score+=1
                block_speed+=0.1

#################################</SPAWN NEW BLOCK WHEN IT AT BOTTOM>######################################
                
        
#############################<CHECK THE CRASH CONDITIONS>################################################
        if (y<(block_starty1+block_height)):
            

            if( (x<(block_startx1+block_width) and (x+car_width)>(block_startx1+block_width)) or ((x+car_width)>block_startx1 and x<block_startx1) or (x>block_startx1 and (x+car_width)<(block_startx1+block_width))):
               print("Collision",i)
               i+=1
               gameDisplay.blit(explosion,(x,y))
               crash()

        if(flag1==1):
               
            if(y<(block_starty2+block_height)):
                 
                if((x<(block_startx2+block_width) and (x+car_width)>(block_startx2+block_width)) or ((x+car_width)>block_startx2 and x<block_startx2) or (x>block_startx2 and (x+car_width)<(block_startx2+block_width))):
                    print("Collision",i)
                    i+=1
                    gameDisplay.blit(explosion,(x,y))
                    crash()
                    
        if(flag2==1):
               
            if(y<(block_starty3+block_height)):
                 
                if((x<(block_startx3+block_width) and (x+car_width)>(block_startx3+block_width)) or ((x+car_width)>block_startx3 and x<block_startx3) or (x>block_startx3 and (x+car_width)<(block_startx3+block_width))):
                    print("Collision",i)
                    i+=1
                    gameDisplay.blit(explosion,(x,y))
                    crash()
                    

##################################</CHECK THE CRASH CONDITIONS>#####################################

                    
        current_score(score,highscore)


##################################<FINAL UPDATE OF SCREEN>#######################################

        
        pygame.display.update()
        clock.tick(60)

##################################</FINAL UPDATE OF SCREEN>#######################################


    
start_game()
pygame.quit()

quit()
