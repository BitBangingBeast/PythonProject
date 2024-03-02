from turtle import Screen ,Turtle, bye, position, st
import time
import random as rn

def menu():
    print("MENU:")
    how_many_point=int(input("For how many point you want to play: "))
    return how_many_point
max_point=menu()
time.sleep(4)

screen= Screen()
screen.setup(width= 900, height=600)
screen.tracer(0) 
screen.bgcolor("black")
screen.title("Pong game")


def init_map():
    player_bat=[]
    AI_bat=[]
    map_div=[]
    Score_bord=[]
    pos=[-430,0]
    for i in range(2):
        for bat_bit in range(5):
            bat_bit=Turtle(shape="square")
            bat_bit.color("white")
            bat_bit.turtlesize(0.75,0.75,0.75)
            bat_bit.penup()
            bat_bit.goto(pos)
            if i==0:
                player_bat.append(bat_bit)
            else:
                AI_bat.append(bat_bit)
            pos[1]=pos[1]-15
        pos[0]=423
    pos=[0,-300]
    while True:
        div_bit=Turtle(shape="square")
        div_bit.color("white")
        div_bit.turtlesize(0.9,0.3,0.9)
        div_bit.penup()
        div_bit.goto(pos)
        map_div.append(div_bit)
        pos[1]=pos[1]+35
        if pos[1]>300:
            break
    pos=[-85,230]
    for score in range(2):
        score= Turtle()
        score.color("white")
        score.penup()
        score.goto(pos)
        score.hideturtle()
        Score_bord.append(score)
        pos=[85,230]
            
    ball=Turtle(shape="circle")
    ball.turtlesize(0.9,0.9,0.9)
    ball.color("white")
    ball.penup()        
    

    return Score_bord, AI_bat,player_bat,ball

def rest_ball(Ball):
    Ball.home()
    direction=rn.uniform(-70,70)
    Ball.setheading(direction)
    random_start=rn.random()
    
    if random_start>0.5:
        ball_movment=+10
    else:
        ball_movment=-10
    

    return Ball ,ball_movment
def score_count(score,Score_bord):
        for i in range(2):
            Score_bord[i].clear()
            Score_bord[i].write(arg=f"{score[i]}",align="center",font=('Arial', 30, 'normal'))



def move_up(bat):
    
    bat[0].setheading(90)
    if bat[0].ycor()<=280:
   
        for Player_bit in range (len(bat)-1,0,-1):
            
            x_cor=bat[Player_bit-1].xcor()
            y_cor=bat[Player_bit-1].ycor()
            
            bat[Player_bit].goto(x_cor,y_cor)
        bat[0].fd(16)

def move_down(bat):
    bat[len(bat)-1].setheading(270)
    if bat[len(bat)-1].ycor()>=-280:
   
        for Player_bit in range (0,len(bat)-1):
            
            x_cor=bat[Player_bit+1].xcor()
            y_cor=bat[Player_bit+1].ycor()
            
            bat[Player_bit].goto(x_cor,y_cor)
        bat[len(bat)-1].fd(16)


def control_ball(ball,player_bat,AI_bat,ball_movment):
    player_ball_out=False
    AI_ball_out=False
    
    if ball_movment>0:
        ball.fd(ball_movment)
        if  ball.xcor()>=410 and ball.xcor()<=450:
            for bat_bit in range(0,len(AI_bat)):
                if (Turtle.distance(AI_bat[bat_bit],ball))<=10:
                
                    ball_movment=-ball_movment
                    
                    if bat_bit<3:
                        random_change=rn.random()*20
                    else:
                        random_change=(rn.random()*20)
                    ball.setheading(-(ball.heading()+random_change))
                    break
        elif ball.xcor()>=450:
            AI_ball_out=True
    
            
        
    else:
        ball.bk(-ball_movment)
        
        if ball.xcor()<=-405 and ball.xcor()>=-450:
            for bat_bit in range(0,len(player_bat)):
               
                if (Turtle.distance(player_bat[bat_bit],ball))<=10:
                    
                    ball_movment=-ball_movment
                    if bat_bit<3:
                        random_change=rn.random()*20
                    else:
                        random_change=(rn.random()*20)

                    ball.setheading(-(ball.heading())+random_change)
                    break
        elif ball.xcor()<=-450:
            player_ball_out=True
            
    
          
                
    if ball.ycor()>=290 or ball.ycor()<=-290:
        ball.setheading(-(ball.heading()))

    
 
    return ball,ball_movment,player_ball_out,AI_ball_out

def AI_bat_control(AI_bat,ball):
    if AI_bat[2].ycor()>0 and ball.ycor()>0:
        if (AI_bat[2].ycor()-ball.ycor())>=10:
            move_down(AI_bat)
        elif (AI_bat[2].ycor()-ball.ycor())<=10:
            move_up(AI_bat)
    elif AI_bat[2].ycor()>0 and ball.ycor()<0:
        if AI_bat[2].ycor()+ball.ycor()>=10 or AI_bat[2].ycor()+ball.ycor()<=10:
            move_down(AI_bat)
    elif AI_bat[2].ycor()<0 and ball.ycor()>0:
        if AI_bat[2].ycor()+ball.ycor()<=10 or AI_bat[2].ycor()+ball.ycor()>=10:
            move_up(AI_bat)
    elif AI_bat[2].ycor()<0 and ball.ycor()<0: 
        if (AI_bat[2].ycor()-ball.ycor())>=10:
            move_down(AI_bat)
        elif (AI_bat[2].ycor()-ball.ycor())<=10:
            move_up(AI_bat)
 

    

def game_over(Score,Score_bord):
    Score_bord.clear()
    Score_bord.goto(0,0)
    Score_bord.write(arg=f"game over: {Score}",align="center",font=('Arial', 20, 'normal'))


    
score_bord,AI_bat,player_bat,Ball=init_map()
Ball,ball_movment=rest_ball(Ball)
score=[0,0]

Game_over=False
speed=0.01
while True:
    screen.update()
    time.sleep(speed)

    Ball,ball_movment,player_ball_out,AI_ball_out=control_ball(Ball,player_bat,AI_bat,ball_movment)
    AI_bat_control(AI_bat,Ball)
    

    def W_press():
        move_up(player_bat)
    def s_press():
        move_down(player_bat)
    
    
    screen.onkeypress(key="w",fun=W_press)
    screen.onkeypress(key="s",fun=s_press)
    screen.listen()
    
    if AI_ball_out or player_ball_out:
        Ball,ball_movment=rest_ball(Ball)
        if AI_ball_out:
            score[0]=score[0]+1
        else:
            score[1]=score[1]+1

    score_count(score,score_bord)
    for Score in score:
        if Score==max_point:
            loser="player lost"
            Game_over=True
        
        elif Score==max_point:
            loser="the computer lost"
            Game_over=True
        if Game_over==True:
            game_over()


        
screen.exitonclick()
    