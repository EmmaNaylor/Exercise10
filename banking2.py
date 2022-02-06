import getpass

pin = "sausages"
attempts = 3

print("Please note - your pin is case sensitive \nIf you would like to reset your pin - please hit enter without submitting a value")

while attempts > 0:
    supplied_pin = getpass.getpass("Enter your PIN: ")
    if not supplied_pin:
        forgotPin = input("You haven't entered anything... Have you forgotten your pin? ")
        if not forgotPin:
            print("This is not going very well... please enter something")
        elif forgotPin.lower() == "yes":
            secQuestion = input("OK. I will ask your back up security question. \nWhat is the name of your best friend's dog? ")
            if not secQuestion:
                print("Please enter something...")
            elif secQuestion.lower() != "ozzy":
                print("That's incorrect. Please enter your PIN or leave.")
                continue
            else:
                pin = input("That's correct! please enter a new PIN? ")
                print("New pin accepted.\n\n")
        else:
            print("If you haven't forgotten your pin then please stop faffing around and enter it... ")
            continue
    elif supplied_pin != pin:
        attempts -= 1
        print("Incorrect pin! You have " + str(0 + attempts) + " attempts remaining")
        if attempts == 0:
            print("This clearly isn't your account! The Police are on their way!")
    elif supplied_pin == pin:
        print("Pin recognised... Enjoy browsing your account!")
        break
    else:
        print("You haven't entered anything... Have you forgotten your password?")
