# John Reeves
# A.I. Homework #1

from graphics import *
from random import *

def colorGenerator(blue, yellow, black, red):
  num = randint(1,4)
  checker = canColorBePicked(num, blue, yellow, black, red)
  while checker == False:
    num = randint(1,4)
    checker = canColorBePicked(num, blue, yellow, black, red)
  if num == 1:
    color = "blue"
  elif num == 2:
    color = "yellow"
  elif num == 3:
    color = "black"
  else:
    color = "red"
  return color

def canColorBePicked(number, blue, yellow, black, red):
  if number == 1:
    if blue == 10:
      return False
  elif number == 2:
    if yellow == 10:
      return False
  elif number == 3:
    if black == 9:
      return False
  else:
    if red == 9:
      return False
  return True

def main():
  blueColor = 0
  yellowColor = 0
  blackColor = 0
  redColor = 0
  
  win=GraphWin("Hungarian Puzzle", 800, 500)
  c1=Circle(Point(370,180), 20)
  c1.draw(win)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c1.setFill(color)
  c2=Circle(Point(350,225), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c2.setFill(color)
  c2.draw(win)
  c3=Circle(Point(350,275), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c3.setFill(color)
  c3.draw(win)
  c4=Circle(Point(370,320), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c4.setFill(color)
  c4.draw(win)
  c5=Circle(Point(400,360), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c5.setFill(color)
  c5.draw(win)
  c6=Circle(Point(435,385), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c6.setFill(color)
  c6.draw(win)
  c7=Circle(Point(477,398), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c7.setFill(color)
  c7.draw(win)
  c8=Circle(Point(520,398), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c8.setFill(color)
  c8.draw(win)
  c9=Circle(Point(563,386), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c9.setFill(color)
  c9.draw(win)
  c10=Circle(Point(600,360), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c10.setFill(color)
  c10.draw(win)
  c11=Circle(Point(630,320), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c11.setFill(color)
  c11.draw(win)
  c12=Circle(Point(650,275), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c12.setFill(color)
  c12.draw(win)
  c13=Circle(Point(650,225), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c13.setFill(color)
  c13.draw(win)
  c14=Circle(Point(630,180), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c14.setFill(color)
  c14.draw(win)
  c15=Circle(Point(600,140), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c15.setFill(color)
  c15.draw(win)
  c16=Circle(Point(563,115), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c16.setFill(color)
  c16.draw(win)
  c17=Circle(Point(520,100), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c17.setFill(color)
  c17.draw(win)
  c18=Circle(Point(477,100), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c18.setFill(color)
  c18.draw(win)
  c19=Circle(Point(435,115), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c19.setFill(color)
  c19.draw(win)
  c20=Circle(Point(430,320), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c20.setFill(color)
  c20.draw(win)
  c21=Circle(Point(450,275), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c21.setFill(color)
  c21.draw(win)
  c22=Circle(Point(450,225), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c22.setFill(color)
  c22.draw(win)
  c23=Circle(Point(430,180), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c23.setFill(color)
  c23.draw(win)
  c24=Circle(Point(400,140), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c24.setFill(color)
  c24.draw(win)
  c25=Circle(Point(365,115), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c25.setFill(color)
  c25.draw(win)
  c26=Circle(Point(323,100), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c26.setFill(color)
  c26.draw(win)
  c27=Circle(Point(280,100), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c27.setFill(color)
  c27.draw(win)
  c28=Circle(Point(235,115), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c28.setFill(color)
  c28.draw(win)
  c29=Circle(Point(200,140), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c29.setFill(color)
  c29.draw(win) 
  c30=Circle(Point(167,180), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c30.setFill(color)
  c30.draw(win)
  c31=Circle(Point(153,225), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c31.setFill(color)
  c31.draw(win)
  c32=Circle(Point(153,275), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c32.setFill(color)
  c32.draw(win)
  c33=Circle(Point(167,320), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c33.setFill(color)
  c33.draw(win) 
  c34=Circle(Point(200,360), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c34.setFill(color)
  c34.draw(win)
  c35=Circle(Point(235,386), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c35.setFill(color)
  c35.draw(win)
  c36=Circle(Point(280,398), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c36.setFill(color)
  c36.draw(win)
  c37=Circle(Point(323,398), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c37.setFill(color)
  c37.draw(win)
  c38=Circle(Point(365,386), 20)
  color = colorGenerator(blueColor, yellowColor, blackColor, redColor)
  if color == "blue":
    blueColor=blueColor+1
  elif color == "yellow":
    yellowColor=yellowColor+1
  elif color == "black":
    blackColor=blackColor+1
  else:
    redColor=redColor+1
  c38.setFill(color)
  c38.draw(win)
  
  win.getMouse()
  win.close()

main()
