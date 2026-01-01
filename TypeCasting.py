
#name = int("Ahamed") # This will raise a ValueError
name = "Ahamed"
age = 22
height = 5.9
is_student = True

print(type(name))      # Output: <class 'str'>
print(type(age))       # Output: <class 'int'>  
print(type(height))    # Output: <class 'float'>
print(type(is_student))# Output: <class 'bool'>

print()

age = float(age)
height = int(height)
is_student = str(is_student)

print(type(age))       # Output: <class 'float'>
print(type(height))    # Output: <class 'int'>  
print(type(is_student))# Output: <class 'str'>
