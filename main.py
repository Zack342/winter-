import turtle

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')

t = turtle.Turtle()

#t.hideturtle()
t.speed(0)


t_ground=turtle.Turtle()
t_ground.speed(0)
t_ground.pencolor('white')
t_ground.fillcolor('white')

t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()


#stump
t.penup()
t.goto(200,0)
t.pensize(15)
t.pencolor('brown')
t.pendown()
t.goto(200,-100)


#top tree
t.penup()
t.pencolor('green')
t.fillcolor('green')
t.goto(200,50)


t.pendown()
t.begin_fill()
t.goto(160,10)


t.goto(240,10)


t.goto(200,50)
t.end_fill()
t.penup()






#second part thingy


t.goto(200,25)


t.pendown()
t.begin_fill()
t.goto(140,-25)


t.goto(260,-25)


t.goto(200,25)
t.end_fill()
t.penup()



#third part thingy


t.goto(200,0)


t.pendown()
t.begin_fill()
t.goto(120,-50)


t.goto(280,-50)


t.goto(200,0)
t.end_fill()
t.pensize(1)
t.pencolor('black')



#House
t.penup()
t.goto(-300,0)
t.pendown()
t.fillcolor('saddlebrown')
t.begin_fill()
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()


#roof
t.penup()
t.goto(-300,0)
t.pendown()
t.fillcolor('peru')
t.begin_fill()
t.goto(-150,0)
t.goto(-225,75)
t.goto(-300,0)
t.end_fill()



#door
t.penup()
t.goto(-200,-25)
t.pendown()
t.fillcolor('peru')
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)
t.right(90)
t.end_fill()

#doorknob
t.penup()
t.goto(-160,-65)
t.pendown()
t.fillcolor('saddlebrown')
t.begin_fill()
t.circle(3)
t.end_fill()




#snowflake
t.pensize(3)
t.pencolor('white')
t.penup()
t.goto(0,200)
t.pendown()
t.goto(20,180)


t.penup()
t.goto(0,180)
t.pendown()
t.goto(20,200)


t.penup()
t.goto(10,210)
t.pendown()
t.goto(10,170)





#snowflake2
t.pensize(3)
t.pencolor('white')
t.penup()
t.goto(-100,220)
t.pendown()
t.goto(-120,200)


t.penup()
t.goto(-100,200)
t.pendown()
t.goto(-120,220)


t.penup()
t.goto(-110,230)
t.pendown()
t.goto(-110,190)




#snowflake3
t.pensize(3)
t.pencolor('white')
t.penup()
t.goto(100,180)
t.pendown()
t.goto(120,160)


t.penup()
t.goto(100,160)
t.pendown()
t.goto(120,180)


t.penup()
t.goto(110,190)
t.pendown()
t.goto(110,150)





#ornaments
t.hideturtle()
t.penup()
t.goto(200,-50)
t.pendown()
t.pencolor("red")
t.fillcolor("red")
t.begin_fill()
t.circle(3)
t.end_fill()





#ornaments 2
t.hideturtle()
t.penup()
t.goto(170,-30)
t.pendown()
t.pencolor("orange")
t.fillcolor("orange")
t.begin_fill()
t.circle(3)
t.end_fill()








#ornaments 3
t.hideturtle()
t.penup()
t.goto(220,-30)
t.pendown()
t.pencolor("blue")
t.fillcolor("blue")
t.begin_fill()
t.circle(3)
t.end_fill()



t.pencolor("black")

#snowman
t.penup()
t.goto(0,-100)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(35)
t.end_fill()


t.penup()
t.goto(0,-60)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(30)
t.end_fill()


t.penup()
t.goto(0,-20)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(25)
t.end_fill()


#buttons
t.penup()
t.goto(0,-30)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


t.penup()
t.goto(0,-40)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


t.penup()
t.goto(0,-50)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


#snowman eyes
t.penup()
t.goto(10,10)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(-10,10)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()


#snowman arms
t.pensize(7)
t.pencolor('saddle brown')
t.penup()
t.goto(-25,-30)
t.pendown()
t.goto(-60,-20)


t.penup()
t.goto(25,-30)
t.pendown()
t.goto(60,-20)




#snowman mouth
t.pensize(1)
t.penup()
t.goto(0,-10)
t.pencolor('black')
t.fillcolor('black')
t.begin_fill()
t.pendown()
t.circle(2)
t.end_fill()
t.penup()
t.begin_fill()
t.goto(3,-9)
t.pendown()
t.circle(2)
t.end_fill()
t.penup()
t.begin_fill()
t.goto(5,-8)
t.pendown()
t.circle(2)
t.end_fill()
t.penup()
t.begin_fill()
t.goto(-3,-10)
t.pendown()
t.circle(2)
t.end_fill()
t.penup()
t.begin_fill()
t.goto(-5,-10)
t.pendown()
t.circle(2)
t.end_fill()
t.penup()
t.begin_fill()
t.goto(-5,-6)
t.pendown()
t.circle(2)
t.penup()
t.begin_fill()
t.goto(-7,-4)
t.pendown()
t.circle(2)
t.hideturtle()


#snowman nose
t.penup()
t.goto(-5,5)
t.pencolor('orange')
t.fillcolor('orange')
t.pendown()
t.begin_fill()
t.goto(-20,2)
t.goto(-5,-5)
t.goto(-5,5)
t.end_fill()






t.pencolor("black")
t.penup()
t.goto(0,50)
t.pendown()
t.write("Happy Holiday's", font=("impact", 15, "bold"), align="center")


t.pensize(10)
t.pencolor("green")
t.penup()
t.goto(-190,-35)
t.pendown()

t.circle(20)




#last line of code
turtle.done()




