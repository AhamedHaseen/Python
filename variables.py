first_name = "Ahamed" #string variable
Last_name = "Haseen"
age = 22 #integer variable
is_Student = True #boolean variable
height = 5.7 #float variable
email = "ahamed.haseen@example.com" #string variable

name = first_name + " " + Last_name

print("My Name is : ", name)
print("My Age is: ", age)
print("Am I a Student?: ", is_Student)
print("My Height is: ", height)
print("My Email is ", email)

print()

#Formatted string

print(f"Hello {name}")
print(f"My Age is {age}")
print(f"Am I Student? : {is_Student}")
print(f"My Height Is {height}")
print(f"My Email is {email}")


print()

is_Citizen = False

if is_Citizen:
    print(f"Ahamed Haseen is a {is_Citizen}")
else:
    print(f"{name} is not a Citizen")