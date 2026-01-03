import math

# x = 9.9

# # print(math.pi)
# # print(math.e) 
# # print(math.sqrt(x))
# # print(math.ceil(x))
# print(math.floor(x))    


#a = 10

#a += 5 #addition
#a -= 3 #subtraction
#a *= 2 #multiplication
#a /= 4 #division
#a %= 3 #remainder / moduls
#a **= 2 #exponation
#a //= 4 #floor division

#Math Operations
# x = 3.14
# y = -4
# z = 5

# #result = round(x) #rounding off
# #result = abs(y) #absolute value
# #result = pow(z, 3) #exponentiation
# #result = max(x, y, z) #maximum value
# result = min(x, y, z) #minimum value

# print(result)

#Exercise

# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference,2)}")

# radius = float(input("Enter the area of a circle: "))
# area = math.pi * pow(radius, 2)
# print(f"The area is: {round(area,2)} cm^2")

a = float(input("Enter the Side of A : "))
b = float(input("Enter the Side of B : "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C is : {round(c)}")