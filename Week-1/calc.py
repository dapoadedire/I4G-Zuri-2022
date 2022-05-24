print("Welcome to simple Calculator")
is_running = True


while is_running:
    print("")
    user_operation = input("Operation: ")

    try:
        no1 = float(input("No 1: "))
        no2 = float(input("No 2: "))

    
    except:
        print('Failed, invalid number')
        continue

    if user_operation == '+':
        print(no1 + no2)

    elif user_operation == '-':
        print(no1 - no2)