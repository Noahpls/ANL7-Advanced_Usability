def main():
    userInput = ""
    userName = "Noah"
    parrotName = "Parrot"
    question = "TALK TO ME"

    while True:
        userInput = input(sayStuff(parrotName, question) + "\n" + sayStuff(userName,""))
        if userInput.lower() == "bye":
            print(sayStuff(parrotName, "Bye " + userName + " :("))
            break
        elif userInput.strip() == "":
            continue
        else:
            question = userInput

def sayStuff(name, message):
    return '{:<8s} {:<1s}'.format(name,  "| " + message)

main()