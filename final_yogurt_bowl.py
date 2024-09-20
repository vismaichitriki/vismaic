#making a yogurt bowl
import turtle as trtl
yogurt = trtl.Turtle()
yogurt.speed(0)


#background
yogurt_bowl = "azure"
yogurt.pencolor(yogurt_bowl)
yogurt.penup()
yogurt.goto(0, -2000)
yogurt.pendown()
yogurt.begin_fill()
yogurt.pensize(15)
yogurt.circle(2500)
yogurt.fillcolor(yogurt_bowl)
yogurt.end_fill()




#Welcome title
def reset1():
    yogurt.color("deepskyblue4")
    yogurt.shapesize(0.2)
    yogurt.pensize(1)
    yogurt.penup()
 
yogurt.goto(0,0)
yogurt.shapesize(90)
yogurt.shape("circle")
yogurt.color("azure")




reset1()
yogurt.goto(-358, 325)
yogurt.write("Welcome to the Yogurt Bowl!", font=("Comic Sans MS", "40", "normal"))
print("title)")


'''
#toppings bar
yogurt.penup()
yogurt.goto(-395, -240)
yogurt.pendown()
yogurt.begin_poly
yogurt.pensize(15)
yogurt.pencolor("lightsteelblue")
yogurt.begin_fill()
yogurt.forward(900)
yogurt.right(90)
yogurt.forward(200)
yogurt.right(90)
yogurt.forward(900)
yogurt.right(90)
yogurt.forward(200)
yogurt.fillcolor("lightsteelblue3")
yogurt.end_fill()
'''


#order taking
question = (input('Hello, would you like a Yogurt Bowl? '))
if question == ("yes"):
  print("Okay, lets get started")
else:
  print("...why are you still here")






#bowl
yogurt_bowl= "linen"
yogurt.pencolor("antiquewhite2")
yogurt.penup()
yogurt.goto(0, -205)
yogurt.pendown()
yogurt.begin_fill()
yogurt.pensize(2)
yogurt.circle(250)
yogurt.fillcolor(yogurt_bowl)
yogurt.end_fill()




#bowl lining
yogurt_bowl= "indianred"
yogurt.pencolor(yogurt_bowl)
yogurt.penup()
yogurt.goto(-2, -181)
yogurt.pendown()
yogurt.begin_fill()
yogurt.pensize(15)
yogurt.circle(228)
yogurt.fillcolor(yogurt_bowl)
yogurt.end_fill()
yogurt.hideturtle








#making the yogurt
print("Todays Special: Strawberry Guava")
yogurt.penup()
yogurt.goto(2, -173)
yogurt.pendown()




yogurt_color = "lightcoral"
yogurt.pencolor(yogurt_color)




yogurt.begin_fill()
yogurt.pensize(20)




yogurt.circle(220)




yogurt.fillcolor(yogurt_color)
yogurt.end_fill()




#Adding bananas
question = (input('Would you like bananas? '))
if question == ("yes"):
  print("Okay! Adding the bananas")
else:
  print("...I'm gonna add them anyway")




#bananas
num_dots = 1
xpos = -95
ypos = -110
yogurt.pensize(50)
yogurt.pencolor("lemonchiffon")




# draw two sets of dots
while (num_dots <= 3 ):
  yogurt.penup()
  yogurt.goto(xpos, ypos)
  yogurt.pendown()
  yogurt.circle(20)
  yogurt.penup()
  yogurt.goto(xpos - 65, ypos + 60)
  yogurt.pendown()
  yogurt.circle(20)




  # position next dots
  ypos = ypos + 80
  xpos = xpos + 0
  num_dots = num_dots + 1
  yogurt.penup()
  yogurt.goto(-95, 127)
  yogurt.pendown()
  yogurt.circle(20)




yogurt.hideturtle()




#banana insides
num_dots = 1
xpos = -95
ypos = -105
yogurt.pensize(50)
yogurt.pencolor("moccasin")
# draw two sets of dots
while (num_dots <= 3 ):
  yogurt.penup()
  yogurt.goto(xpos, ypos)
  yogurt.pendown()
  yogurt.circle(15)
  yogurt.penup()
  yogurt.goto(xpos - 65, ypos + 60)
  yogurt.pendown()
  yogurt.circle(15)




  # position next dots
  ypos = ypos + 80
  xpos = xpos + 0
  num_dots = num_dots + 1
  yogurt.penup()
  yogurt.goto(-95, 131)
  yogurt.pendown()
  yogurt.circle(15)
print("Bananas done!")
 
yogurt.hideturtle()




#Adding blueberries
question = (input('Would you like blueberries? '))
if question == ("yes"):
  print("Okay! Adding the blueberries")
else:
  print("Well that’s too bad...")
  print("Added the blueberries anyway")




#blueberries


yogurt.penup()
yogurt.goto(110, 40)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(114, 40)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#berry2
yogurt.penup()
yogurt.goto(180, 0)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(182, 0)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#berry3
yogurt.penup()
yogurt.goto(125, -25)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(123, -27)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#berry4
yogurt.penup()
yogurt.goto(160, -70)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(160, -70)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#berry5
yogurt.penup()
yogurt.goto(170, 65)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(172, 65)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#berry6
yogurt.penup()
yogurt.goto(115, -108)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(113, -97)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#berry7
yogurt.penup()
yogurt.goto(125, 105)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(125, 107)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#berry8
yogurt.penup()
yogurt.goto(182, 125)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(185, 128)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#berry9
yogurt.penup()
yogurt.goto(140, 165)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(145, 168)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#berry10
yogurt.penup()
yogurt.goto(103, 203)
yogurt.pendown()
yogurt.pensize(30)
yogurt.pencolor("darkslateblue")
yogurt.circle(10)
yogurt.penup()
yogurt.goto(106, 200)
yogurt.pendown()
yogurt.pensize(5)
yogurt.pencolor("midnightblue")
yogurt.circle(3)




#Adding mangoes
question = (input('Would you like mangoes? '))
if question == ("yes"):
  print("Okay! Adding the mangoes ")
else:
  print("How could you say no to mangoes?!")


# mango loop


num_dots = 1
xpos = 78
ypos = 188
yogurt.pensize(10)
yogurt.pencolor("gold")




while (num_dots <= 5 ):
  yogurt.setheading(90)
  yogurt.penup()
  yogurt.goto(xpos, ypos)
  yogurt.fillcolor("darkgoldenrod1")
  yogurt.begin_fill()
  yogurt.pensize(10)
  yogurt.pencolor("darkgoldenrod1")
  yogurt.circle(70,155)
  yogurt.end_fill()


  yogurt.setheading(90)
  yogurt.penup()
  yogurt.goto(xpos-1, ypos-3)
  yogurt.fillcolor("gold")
  yogurt.begin_fill()
  yogurt.pensize(10)
  yogurt.pencolor("gold")
  yogurt.circle(68,150)
  yogurt.end_fill()
  #next mango
  ypos = ypos + -45
  xpos = xpos + 0
  num_dots = num_dots + 1


yogurt.hideturtle()


#Adding kiwiws
question = (input('Would you like a kiwi? '))
if question == ("yes"):
  print("Okay! Adding the kiwi ")
else:
  print("I'll add just one...")


yogurt.penup()
yogurt.goto(-45, -10)
yogurt.fillcolor("darkolivegreen1")
yogurt.begin_fill()
yogurt.pensize(10)
yogurt.pencolor("darkolivegreen1")
yogurt.circle(60)
yogurt.end_fill()


yogurt.penup()
yogurt.goto(-33, -18)
yogurt.fillcolor("darkolivegreen2")
yogurt.begin_fill()
yogurt.pensize(10)
yogurt.pencolor("darkolivegreen2")
yogurt.circle(45)
yogurt.end_fill()


yogurt.penup()
yogurt.goto(-20, -25)
yogurt.fillcolor("darkolivegreen3")
yogurt.begin_fill()
yogurt.pensize(10)
yogurt.pencolor("darkolivegreen3")
yogurt.circle(30)
yogurt.end_fill()


'''
#lines
lines = 8
length = 20
angle = 360/ lines
yogurt.pensize(20)
n = 0


while (n < lines):
  yogurt.goto(-15, -28)
  yogurt.setheading(angle*n)
  yogurt.forward(length)
  n = n + 1
yogurt.hideturtle()
'''


yogurt.penup()
yogurt.goto(-15, -28)
yogurt.fillcolor("palegoldenrod")
yogurt.begin_fill()
yogurt.pensize(10)
yogurt.pencolor("palegoldenrod")
yogurt.circle(25)
yogurt.end_fill()


#kiwi seeds
yogurt.penup()
yogurt.goto(-15, -28)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(-17, -48)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(-16, -38)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(-20, -36)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(-10, -18)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(-8, -20)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(18, -20)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(10, -15)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(15, -23)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(10, -15)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(5, -10)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(3, -15)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(28, -25)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(35, -35)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(30, -42)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()


#seed
yogurt.penup()
yogurt.goto(10, -65)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(5, -60)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(2, -65)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(-5, -60)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(-5, -63)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(13, -67)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(17, -57)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(22, -53)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()
#seed
yogurt.penup()
yogurt.goto(17, -63)
yogurt.fillcolor("saddlebrown")
yogurt.begin_fill()
yogurt.pensize(1)
yogurt.pencolor("saddlebrown")
yogurt.circle(2)
yogurt.end_fill()


#Adding kistrawberrieswiws
question = (input('Should I add in a couple strawberries? '))
if question == ("yes"):
  print("Okay, adding them!")
else:
  print("-It's free")


#strawberries
yogurt.penup()
yogurt.goto(-48, -125)
yogurt.fillcolor("brown2")
yogurt.begin_fill()
yogurt.pensize(10)
yogurt.pencolor("brown2")
yogurt.circle(35)
yogurt.end_fill()


yogurt.penup()
yogurt.goto(-40, -130)
yogurt.fillcolor("lightpink")
yogurt.begin_fill()
yogurt.pensize(10)
yogurt.pencolor("lightpink")
yogurt.circle(25)
yogurt.end_fill()


#strawberry2
yogurt.penup()
yogurt.goto(28, -118)
yogurt.fillcolor("brown2")
yogurt.begin_fill()
yogurt.pensize(10)
yogurt.pencolor("brown2")
yogurt.circle(35)
yogurt.end_fill()


yogurt.penup()
yogurt.goto(37, -123)
yogurt.fillcolor("lightpink")
yogurt.begin_fill()
yogurt.pensize(10)
yogurt.pencolor("lightpink")
yogurt.circle(25)
yogurt.end_fill()


print("Enjoy your order & have a nice day!")
print("See you next time :)")


wn = trtl.Screen()
wn.mainloop()







