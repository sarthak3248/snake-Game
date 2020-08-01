import pygame
import time
import random



game_width=300
game_height=300

pygame.init()

pygame.font.init()

green=(0,255,0)
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
gameWindow = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()


block=30
FPS=10
clk=pygame.time.Clock()

font=pygame.font.SysFont(None,23)

def snake(block,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameWindow,green,[XnY[0],XnY[1],block,block])



def messagetoscreen(msg,color):
    screen_text=font.render(msg,True,color)
    gameWindow.blit(screen_text,[game_width/8.8,game_height/2])




background_img=pygame.image.load("backgroundimg.jpg").convert()

def loop():
    gameOver=False
    gameClose = False

    rAppleX=round(random.randrange(0,game_width-block)/20.0)*20.0
    rAppleY=round(random.randrange(0,game_height-block)/20.0)*20.0


    start_x = game_width / 2
    start_y = game_height / 2
    update_x = 0
    update_y = 0

    snakeList=[]
    snakelength=1


    while not gameClose:
        while gameOver==True:
            gameWindow.fill(white)
            messagetoscreen("You Loose!!!,Press 'r' to replay or Press 'q' to quit ", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameClose=True
                        gameOver=False
                    if event.key==pygame.K_r:
                        loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    update_x=-block
                if event.key==pygame.K_RIGHT:
                    update_x=+block
                if event.key==pygame.K_UP:
                    update_y=-block
                if event.key == pygame.K_DOWN:
                    update_y=+block
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    update_x=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    update_y=0
        if start_x>=game_width or start_y<0 or start_y>=game_height or start_y<0:
            gameOver=True
        start_x += update_x
        start_y+=update_y
        gameWindow.blit(background_img,[0,0])

        pygame.draw.rect(gameWindow,red,[rAppleX,rAppleY,block,block])

        snakeHead=[]
        snakeHead.append(start_x)
        snakeHead.append(start_y)
        snakeList.append(snakeHead)

        if len(snakeList)>snakelength:
            del(snakeList[0])

        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=True
        snake(block,snakeList)
        pygame.display.update()

        if start_x==rAppleX and start_y==rAppleY:
            rAppleX = round(random.randrange(0, game_width - block) / 20.0) * 20.0
            rAppleY = round(random.randrange(0, game_height - block) / 20.0) * 20.0
            snakelength += 1
        pygame.display.update()
        clk.tick(FPS)



    pygame.quit()
    quit()

loop()