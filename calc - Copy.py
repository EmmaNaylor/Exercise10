print("Welcome to the calculator app!\n")

firstNum = float(input("Please enter a number: "))
action = input("Please enter an action: ")
secondNum = float(input("Please enter a second number: "))

confirm = ""

while confirm.lower() != "yes":
    print("You asked me to calculate " + str(firstNum) + " " + action + " " + str(secondNum))
    confirm = input("... Is that right? ")
    if confirm.lower() != "yes":
        print("Okay no problem, let's start again")
        break


if action == "+":
    answer = firstNum + secondNum
    print("The answer is: " + str(answer))
elif action == "-":
    answer = firstNum - secondNum
    print("The answer is: " + str(answer))
elif action == "*":
    answer = firstNum * secondNum
    print("The answer is: " + str(answer))
elif action == "/":
    answer = firstNum / secondNum
    print("The answer is: " + str(answer))
