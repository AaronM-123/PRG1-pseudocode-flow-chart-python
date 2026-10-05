attempts = 0
password_correct = False

while password_correct == False and attempts < 3:
    password = input("Enter your password: ")
    attempts += 1

    if password == "password123":
        password_correct = True
        print("Logged in successfully!")
    else:
        if attempts == 3:
            print("Account locked. Too many incorrect attempts.")
        else:
            print("Incorrect password. Please try again.")
