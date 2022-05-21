user_no = input("Please enter a number: ")

try:
    user_no = int(user_no)
    print("Hooray! You have entered a number.")

    if user_no < 0:
        raise ValueError("Please enter a positive number")

except:
    print("This is not a number.")