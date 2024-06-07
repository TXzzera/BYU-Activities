import math

def windchill_calc (T,V):
    return 35.74 + 0.6215 * T - 35.75 * (V**0.16) + 0.4275 * T * (V**0.16)

scale = " "

while scale != "QUIT":
  T = float(input("What is the temperature? "))
  scale = input("Fahrenheit or Celsius (F/C)? ").upper()

  if scale == "F":

    for V in range (5,65,5):
      windchill = windchill_calc (T,V)
      print (f"At temperature {T}F, and wind speed {V} mph, the windchill is: {windchill:.2f}F ")

  elif scale == "C":
    new_T = T * 9/5 + 32
    T = new_T

    for V in range (5,65,5):
      windchill = windchill_calc (T,V)
      print (f"At temperature {T}F, and wind speed {V} mph, the windchill is: {windchill:.2f}F ")

  elif scale == "QUIT":
    break

  else:
    print("You put an incorrect scale, please choose again. ")
