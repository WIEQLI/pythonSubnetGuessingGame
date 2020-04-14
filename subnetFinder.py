#import modules
import ipaddress
import random
import playAgain
import clearScreen

def guessSubnet():  
    #Generates random 32 bit number
    randoIP = random.getrandbits(32)
    
    #converts the 32 bit number randoIP to an IPv4 address held in variable convertIP
    convertIP = ipaddress.IPv4Address(randoIP)
    
    #changes convertIP IPv4 address to string
    ipToString = str(convertIP)
    
    #Generates random number 1-30 to be used as CIDR mask
    randoSub = random.randrange(1,30,1)
    
    #changes random CIDR mask integer to string type
    netToString = str(randoSub)      
      
    #concat a string to be used in converting to IP with CIDR mask to IPv4 interface type
    guessIPString = ipToString + '/' + netToString
    
    #Converts string of IP and CIDR mask to an interface type (What network is this IP in)
    convertIP = ipaddress.ip_interface(guessIPString)

    #Sets guessIPNetwork to correct answer by changing convertIP into the network, sets string variable for checking later
    guessIPNetwork = convertIP.network
    checkAgainst = str(guessIPNetwork)
    print('What is the network of ', guessIPString, '\n', 'Enter your answer in X.X.X.X Format \n')

    #Takes user input as answer
    userAnswer = input("This IP is in network: ")

    #Checks user answer against correct answer and Print results
    if userAnswer + '/' + netToString == checkAgainst:
        print('\n YES! You got it, rock-star!\n')
    else:
        print("\n \nMission failed. The hospital crashed, now you're fired.\n")
        print('\nThe answer was: ', guessIPNetwork)
        print('You answered: ' + userAnswer + "\n")        

    
    if playAgain.playAgain() == "yes":
        clearScreen.clear()
        guessSubnet()
    else:
        clearScreen.clear()
        pass
    return

