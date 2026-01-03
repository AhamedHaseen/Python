name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age>=18:
    print(f"Hello {name}, You are eligible to vote.")
else:
    print(f"Hello {name}, You are not eligible to vote.")