def playAgain():
    while True:
        a = input("\n\nPlay again?\nEnter 'yes' to begin, 'no' to exit\n")
        if a=="yes":
            print("\n")
            return "yes"
        elif a=="no":
            print("\n")
            break
        else:
            print("\nEnter either yes/no \n")
    return