import pygame
import random as rd
from pygame import mixer
pygame.init()
rgb=(21, 28, 96 )
players_colors=(211, 90, 37 )
ball_color=(62, 101, 140)
line_color=(0,0,0)
mixer.music.load("ss.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.5)
screen_width=500
screen_height=400
size =(screen_width,screen_height)

screen=pygame.display.set_mode(size)
player_width=15
player_height=90
player_1_x=50
player_1_y=150
player_1_y_speed=0
player_2_x=430
player_2_y=150
player_2_y_speed=0
ball_x=250
ball_y=200
ball_radius=20
ball_speed_x=0.1
ball_speed_y=0.1
pygame.display.set_caption("pong")
player_1_score=0
player_2_score=0
score_font=pygame.font.Font("font.ttf",20)
won_font=pygame.font.Font("font.ttf",40)
player_1_score_x=10
player_1_score_y=10
player_2_score_x=screen_width-165
player_2_score_y=10
won_x=130
won_y=130
def show_score_1(x,y):
    score1=score_font.render("Jugador uno : " +str(player_1_score),True,(255, 255, 255) )
    screen.blit(score1,(x,y))
def show_score_2(x,y):
    score2=score_font.render("Jugador Dos: " +str(player_2_score),True,(255, 255, 255) )
    screen.blit(score2,(x,y))

icon=pygame.image.load("pongo.png")
pygame.display.set_icon(icon)

running= True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:


            if event.key==pygame.K_w:
                player_1_y_speed=-0.2
                
            if event.key==pygame.K_s:
                player_1_y_speed=0.2
            
            if event.key==pygame.K_UP:
                player_2_y_speed=-0.2
                
            if event.key==pygame.K_DOWN:
                player_2_y_speed=0.2

        if event.type == pygame.KEYUP:


            if event.key==pygame.K_s:
                player_1_y_speed=0
                
            if event.key==pygame.K_s:
                player_1_y_speed=0
                
            if event.key==pygame.K_UP:
                player_2_y_speed=0
                
            if event.key==pygame.K_DOWN:
                player_2_y_speed=0

    player_1_y += player_1_y_speed
                    
    player_2_y += player_2_y_speed 

    ball_x +=ball_speed_x
    ball_y +=ball_speed_y

    if ball_y >(screen_height-ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1

    if ball_x>screen_width:
        lose_sound=mixer.Sound("lost.wav")
        lose_sound.play()
        player_1_score+=10
        ball_x = screen_width/2
        ball_y= screen_height/2
        ball_speed_x*= rd.choice([-1,1])

    elif ball_x <0:
        lose_sound=mixer.Sound("lost.wav")
        lose_sound.play()
        player_2_score+=10
        ball_x = screen_width/2
        ball_y= screen_height/2
        ball_speed_x*= rd.choice([-1,1])
       
    if player_1_y <=0:
        player_1_y=0

    if player_1_y >=screen_height - player_height:
        player_1_y = screen_height - player_height 

    
    if player_2_y <=0:
        player_2_y=0

    if player_2_y >=screen_height - player_height:
        player_2_y = screen_height - player_height          
    screen.fill(rgb)

    player_1=pygame.draw.rect(screen,players_colors,(player_1_x,player_1_y,player_width,player_height))

    player_2=pygame.draw.rect(screen,players_colors,(player_2_x,player_2_y,player_width,player_height))    
    pygame.draw.aaline(screen,line_color,(screen_width/2,0),(screen_width/2,screen_height))
    ball=pygame.draw.circle(screen,ball_color,(ball_x,ball_y),ball_radius)
    
    if ball.colliderect(player_1):
        ball_speed_x *= -1.01
        ball_x+=1
        ball_sonido=mixer.Sound("choque.wav")
        ball_sonido.play()
    if ball.colliderect(player_2):
        ball_sonido=mixer.Sound("choque.wav")
        ball_speed_x *= -1.01 
        ball_x-=1
        
    if player_1_score ==50:
        ball_y=2000
        ball_speed_x=0
        ball_speed_y=0
        player_1_y_speed=0
        player_2_y_speed=0
        won_text=won_font.render("Jugador Uno Gana", True, (0,0,0))
        screen.blit(won_text,(won_x,won_y))

    elif player_2_score==50:  
        ball_y=2000
        ball_speed_x=0
        ball_speed_y=0
        player_1_y_speed=0
        player_2_y_speed=0
        won_text=won_font.render("Jugador Dos Gana", True, (0,0,0))
        screen.blit(won_text,(won_x,won_y))

    show_score_1(player_1_score_x,player_1_score_y)
    show_score_2(player_2_score_x,player_2_score_y)    
    

    pygame.display.flip()                                                                                     