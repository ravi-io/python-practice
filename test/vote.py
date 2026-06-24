# check you eligiblity to vote or not, if you are eligible to vote 
# then print your name, age and also whether you are working or not,
# why you are not eligible to vote

age = int(input("Enter your age: "))
if age >= 18:
    name = input("Enter your name: ")
    is_working = input("Are you working? (yes/no): ")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Working: {is_working}")
else:
    print("You are not eligible to vote.")
    print("Reason: You are not 18 years old.")
    print("you are not working currently.")