from turtle import Screen ,Turtle, bye, position, st
import time
import random as rn




screen= Screen()
screen.setup(width= 600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("snake game")

fruit=Turtle(shape="circle")
fruit.turtlesize(0.5,0.5,0.5)
fruit.color("blue")
fruit.penup()

def init_snake_with_postion(postion):
    snake_bit=Turtle(shape="square")
    snake_bit.color("white")
    snake_bit.turtlesize(0.75,0.75,0.75)
    snake_bit.penup()
    snake_bit.goto(postion[0],postion[1])
    return snake_bit

def move_fruit_to(Snake):
    height= int((screen.window_height())/2)
    width=int((screen.window_width())/2)
    fruit_position=[rn.randint(10,height-10),rn.randint(10,width-10)]
    i=0
    while True:
        snake_p= list(Snake[i].pos())


        if snake_p[0] - fruit_position[0]>10 or snake_p[1] - fruit_position[1]>10 or snake_p[0] - fruit_position[0]< -10 or snake_p[1] - fruit_position[1]< -10 :

            i+=1
        else:
            fruit_position=[rn.randint(10,height-10),rn.randint(10,width-10)]
            i=0
        if i == (len(Snake)-1):
            break


    fruit.goto(fruit_position[0],fruit_position[1])


def dont_eat_yourslef(Snake,status):
    hight=(screen.window_height()/2)-10
    width=(screen.window_width()/2)-10
    postion=list(Snake[0].pos())
    #print( postion)
    if hight - postion[0] < 0 or hight+ postion[0] <0 or width- postion[1]<0 or width+ postion[1] <0:
        status=False
        return status
    for part in Snake:
        if part == Snake[0]:
            pass
        elif Snake[0].distance(part)<10:
            print("should close ")
            status=False
            break


    return status

def score_count(score,Score_bord):

        Score_bord.clear()
        Score_bord.write(arg=f"your score: {score}",align="center",font=('Arial', 20, 'normal'))

def game_over(Score,Score_bord):
    Score_bord.clear()
    Score_bord.goto(0,0)
    Score_bord.write(arg=f"game over: {Score}",align="center",font=('Arial', 20, 'normal'))


Score_bord= Turtle()
Score_bord.color("white")
Score_bord.penup()
Score_bord.goto(10,250)
Score_bord.hideturtle()

snake=[]
pos=[0,0]
for snake_length in range(2):
    snake.append(init_snake_with_postion(pos))
    pos[0]-=15

move_fruit_to(snake)

game_is_on=True
speed=0.1
Score=0
check=[0,0]
i=1


while game_is_on:

    screen.update()
    time.sleep(speed)
    for Snake_bit in range (len(snake)-1,0,-1):
        x_cor=snake[Snake_bit-1].xcor()
        y_cor=snake[Snake_bit-1].ycor()
        snake[Snake_bit].goto(x_cor,y_cor)
    snake[0].forward(16)


    if (snake[0].heading()==0.0):
        def w_press():
            snake[0].left(90)
        def s_press():
            snake[0].left(-90)
        def d_press():
            pass
        def a_press():
            pass
        screen.listen()
        screen.onkeypress(key="w",fun=w_press)
        screen.onkeypress(key="s",fun=s_press)
        screen.onkeypress(key="d",fun=d_press)
        screen.onkeypress(key="a",fun=a_press)





    elif (snake[0].heading()==180.0):

        def w_press():
            snake[0].left(90)
        def s_press():
            snake[0].left(-90)
        def d_press():
            pass
        def a_press():
            pass
        screen.listen()
        screen.onkeypress(key="w",fun=s_press)
        screen.onkeypress(key="s",fun=w_press)
        screen.onkeypress(key="d",fun=d_press)
        screen.onkeypress(key="a",fun=a_press)
    elif (snake[0].heading()==270.0):
        def w_press():
            pass
        def s_press():
            pass
        def d_press():
            snake[0].left(90)
        def a_press():
            snake[0].left(-90)
        screen.listen()
        screen.onkeypress(key="w",fun=w_press)
        screen.onkeypress(key="s",fun=s_press)
        screen.onkeypress(key="d",fun=d_press)
        screen.onkeypress(key="a",fun=a_press)

    elif (snake[0].heading()==90.0):
        def w_press():
            pass
        def s_press():
            pass
        def d_press():
            snake[0].left(90)
        def a_press():
            snake[0].left(-90)
        screen.listen()
        screen.onkeypress(key="w",fun=w_press)
        screen.onkeypress(key="s",fun=s_press)
        screen.onkeypress(key="d",fun=a_press)
        screen.onkeypress(key="a",fun=d_press)

    fruit_pos=list(fruit.pos())
    snake_pos=list(snake[0].pos())
    check[0]=fruit_pos[0]-snake_pos[0]
    check[1]=fruit_pos[1]-snake_pos[1]
    if check[0]<10 and check[1]<10 and check[0]>-10 and check[1]>-10:
        move_fruit_to(snake)
        Score+=1
    game_is_on=dont_eat_yourslef(snake,game_is_on)
    score_count(Score,Score_bord)

    if Score-(2*i) ==0:
        snake.append(init_snake_with_postion(list(snake[(len(snake)-1)].pos())))
        speed*=0.9
        i+=1


game_over(Score,Score_bord)
screen.exitonclick()

