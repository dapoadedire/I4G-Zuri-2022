import random



loop = True
while loop == True:
    user_shot = input("Enter jajssssdh")
    comuter_shot = random.choice(["r", "p", "s"])
    print("Computer shot: " + comuter_shot)
    print("User shot: " + user_shot)
    if user_shot not in ["r", "p", "s"]:
        print("Invalid input")
        continue
    else:
        if user_shot == comuter_shot:
           print("It is a tie")
           continue

        elif (user_shot == "r" and comuter_shot == "p") or (user_shot == "p" and comuter_shot == "s") or (user_shot == "s" and comuter_shot == "r"):
            print("User wins")

        else:
            print("Computer wins")
        break
