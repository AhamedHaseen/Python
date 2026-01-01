
#name = int("Ahamed") # This will raise a ValueError
name = "Ahamed"
name_2 = ""
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
name = bool(name)
name_2 = bool(name_2)

print(type(age))       # Output: <class 'float'>
print(type(height))    # Output: <class 'int'>  
print(type(is_student))# Output: <class 'str'>
print(type(name))      # Output: <class 'bool'>
print(type(name_2))    # Output: <class 'bool'>

print()
print(age)             # Output: 22.0
print(height)          # Output: 5
print(is_student)      # Output: True
print(name)            # Output: True
print(name_2)          # Output: False