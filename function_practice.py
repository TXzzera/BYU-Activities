import math

def compute_area_square (side):
    return side*side

def compute_area_rectangle (lenght,width):
    return lenght * width

def compute_area_circle (radius):
    return math.pi **radius 

shape = " "

while shape != "quit":
  shape = input("What is the shape that you have? ").lower()

  if shape == "square":
    side = float(input("What is the value of the square sides? "))
    square_area = compute_area_square (side)
    print(f"The area of the square is {square_area} centimeters. ")
    
  elif shape == "rectangle":
    lenght = float(input("What is the lenght of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    rectangle_area = compute_area_rectangle (lenght, width)
    print(f"The area of the rectangle is {rectangle_area} centimeters. ")
  
  elif shape == "circle":
     radius = float(input("What is the radius of the circle? "))
     circle_area = compute_area_circle (radius)
     print(f"The area of the Circle is {circle_area} centimeters. ")

  else:
     break


