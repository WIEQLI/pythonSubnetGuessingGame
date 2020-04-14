import ipaddress
import random
import playAgain
import clearScreen

def subnetsAndHosts():
    #Set IP Class Ranges
    classA = range(1,126)
    classB = range(127,191)
    classC = range(192,223)
     
    #Generates random 32 bit number
    randoIP = random.getrandbits(32)

    #Converts the 32 bit number randoIP to an IPv4 address held in variable convertIP.
    convertIP = ipaddress.IPv4Address(randoIP)

    #Changes convertIP IPv4 address to string
    ipToString = str(convertIP)

    #Finds the first octet of randomly generated IP.

    firstOctet = ipToString[0:ipToString.find('.')]

    #Checks what range first octet is in.

    if int(firstOctet) in classA:
        networkBits = 8
        #Generates random number 1-30 to be used as CIDR mask.
        randoSub = random.randrange(9,30,1)
    elif int(firstOctet) in classB:
        networkBits = 16
        #Generates random number 1-30 to be used as CIDR mask.
        randoSub = random.randrange(17,30,1)
    else:
        #Generates random number 1-30 to be used as CIDR mask.
        randoSub = random.randrange(25,30,1)
        networkBits = 24
        


    #changes random CIDR mask integer to string type
    netToString = str(randoSub)      
      
    #concat a string to be used in converting to IP with CIDR mask to IPv4 interface type
    guessIPString = ipToString + '/' + netToString

    #Converts string of IP and CIDR mask to an interface type (What network is this IP in)
    convertIP = ipaddress.ip_interface(guessIPString)

    #Sets guessIPNetwork to Correct Answer by changing convertIP into the network, sets string variable for checking later
    guessIPNetwork = convertIP.network
    checkAgainst = str(guessIPNetwork)
        

    #Subtracts network bits from prefix length.

    subnetBits = randoSub - networkBits

    #Calculates the number of subnets. 

    numberOfSubnets = 2 ** subnetBits

    #Calculates the number of useable hosts.
    countOfHosts = guessIPNetwork.hosts()
    answerOfHosts = sum(1 for host in countOfHosts)


    print('How many useable hosts are in ', checkAgainst, '\n')
    
    #Takes user input as answer
    while True:
        try:
            userAnswerHosts = int(input("Amount of useable hosts is: "))
            break
        except ValueError:
            print("You must enter an integer")
            continue
        else:
            break
        
    print('\nHow many subnets available in ', checkAgainst, '\n')

    #Takes user input as answer only allows integer
    while True:
        try:
            userAnswerSubnets = int(input("Amount of subnets is: "))
            break
        except ValueError:
            print("You must enter an integer")
            continue
        else:
            break
            
    #Checks Answers         
    if int(userAnswerHosts) == answerOfHosts and int(userAnswerSubnets) == numberOfSubnets:
        print("\nEVERYTHING IS PERFECT, YOU ARE THE MASTER MY FRIEND!!!!")
    else:
        print("\nBetter luck next time, buddy\n")
        print("The number of useable hosts was: " + str(answerOfHosts))
        print("The number of subnets was: " + str(numberOfSubnets))
        
    #starts playagain 
    if playAgain.playAgain() == "yes":
            clearScreen.clear()
            subnetsAndHosts()
    else:
        clearScreen.clear()
        pass
    return
    #Checking Values Erase in Final
    #print(checkAgainst)
    #print(numberOfSubnets)
    #print(answerOfHosts)
    return
