print("Welcome to the calculator app!\n")

firstnum = float(input("Please enter a number: "))
action = input("Please enter an action: ")
secondnum = float(input("Please enter a second number: "))

confirm = ""

while confirm != "yes":
    print("You asked me to calculate " + str(firstnum) + " " + action + " " + str(secondnum))
    confirm = input("... Is that right? ")
    if confirm != "yes":
        print("Okay no problem, let's start again")
        break


if action == "+":
    answer = firstnum + secondnum
    print("The answer is: " + str(answer))
elif action == "-":
    answer = firstnum - secondnum
    print("The answer is: " + str(answer))
elif action == "*":
    answer = firstnum * secondnum
    print("The answer is: " + str(answer))
elif action == "/":
    answer = firstnum / secondnum
    print("The answer is: " + str(answer))
