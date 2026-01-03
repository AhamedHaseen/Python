'''name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age>=18:
    print(f"Hello {name}, You are eligible to vote.")
elif age == 17:
    print(f"Hello {name}, You will be eligible to vote next year.")
else:
    print(f"Hello {name}, You are not eligible to vote.")'''

response = input("Do you want to continue? (Yes/No): ")

if response == "Yes":
    print("Check the Email for further instructions.")
elif response == "No":
    print("Thank you for your time.")
else:
    print("Invalid input. Please respond with 'Yes' or 'No'.")