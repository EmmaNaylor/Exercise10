pin = "sausages"
attempts = 3
failedSecQ = 0

print("Please note - your pin is case sensitive \nIf you would like to reset your pin - please hit enter without submitting a value")

while attempts > 0:
    supplied_pin = input("Enter your PIN: ")
    if supplied_pin == pin:
        print("Pin recognised... Enjoy browsing your account!")
        break
    elif supplied_pin != pin:
        if not supplied_pin:
            forgotPin = input("You haven't entered anything... Have you forgotten your pin? ")
            if not forgotPin:
                print("This is not going very well... please enter something")
            elif forgotPin.lower() == "yes":
                if failedSecQ == 1:
                    print("I told you - you only had one attempt at the security question - enter your pin or get lost.")
                else:
                    secQuestion = input(
                        "OK. I will ask your back up security question. Please note you will have only 1 attempt\nWhat is the name of your best friend's dog? ")
                    if not secQuestion:
                        print("Please enter something...")
                    elif secQuestion.lower() == "ozzy":
                        pin = input("That's correct! please enter a new PIN? ")
                        print("New pin accepted.\n\n")
                    else:
                        print("That's incorrect. Please enter your PIN or leave.")
                        failedSecQ += 1
            else:
                print("If you haven't forgotten your pin then please stop faffing around and enter it... ")
                continue
        else:
            attempts -= 1
            print("Incorrect pin! You have " + str(0 + attempts) + " attempts remaining")
            if attempts == 0:
                print("This clearly isn't your account! The Police are on their way!")