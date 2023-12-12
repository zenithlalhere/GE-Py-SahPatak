def check_name(name):
    if any(char.isdigit() or not char.isalpha() for char in name):
        raise ValueError("Name should contain only alphabetic characters")

try:
    user_name = input("Enter your name: ")
    check_name(user_name)
    print("Name entered:", user_name)
except ValueError as e:
    print("Invalid input:", e)
