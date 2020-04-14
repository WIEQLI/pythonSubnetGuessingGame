import subnetFinder
import useableHostsAndSubnets
import howManyBits
import clearScreen

while True:

    print("What game would you like to play?\n\n"
          "1.) Network address of an IP\n\n"
          "2.) Useable Hosts and Subnets\n\n"
          "3.) What is the Mask?\n\n"
          "4.) Quit")

    gameChoice = input("\nEnter a number from above"
                       " and press 'Enter' to begin: ")

    if gameChoice == "1":
        clearScreen.clear()
        subnetFinder.guessSubnet()
    elif gameChoice == "2":
        clearScreen.clear()
        useableHostsAndSubnets.subnetsAndHosts()
    elif gameChoice == "3":
        clearScreen.clear()
        howManyBits.whatIsTheMask()
    elif gameChoice == "4":
        break
    else:
        input("\nInvalid choice, press enter to try again.")
        clearScreen.clear()
        print("\n")
        