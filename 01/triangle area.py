import math
a = float(input("enter the lenght of side a : "))
b = float(input("enter the lenght of side b : "))
c = float(input("enter the lenght of side c : "))
s = (a + b + c)/2
Area = math.sqrt(s*(s - a)*(s - b)*(s - c))
print(Area)


