'''name = input("Enter your name: ")
age = int(input("How old are you? "))

#age = int(age) 
age += 1

print(f"My Name is {name}")
print("Happy Birthday")
print(f"I am {age} years old.")'''

'''
#Exercise = Rectangle Area Calculation
length = float(input("Enter Length of Rectangle: "))
width = float(input("Enter Width of Rectangle: "))
area = length * width

#print(f"The area of the rectangle is {area}")
#number lock + alt + 0178 = ²
print(f"The area is {area} cm²")
'''
#Exercise = Shopping Cart Program
item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity you want to buy: "))

total_cost = price * quantity

print(f"You have purchased {quantity} {item}(s) for a total of ${total_cost}")