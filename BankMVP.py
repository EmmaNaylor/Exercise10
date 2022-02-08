pin = "sausages"
attempts = 3

while attempts > 0:
    supplied_pin = input("Enter your PIN: ")
    if supplied_pin == pin:
        print("Pin recognised... Enjoy browsing your account!")
        break
    elif not supplied_pin:
        print("You haven't entered anything... Have you forgotten your pin? ")
    else:
        attempts -= 1
        print("Incorrect pin! You have " + str(0 + attempts) + " attempts remaining")
        if attempts == 0:
            print("This clearly isn't your account! The Police are on their way!")