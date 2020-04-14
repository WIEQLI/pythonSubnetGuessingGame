import ipaddress
import random
import playAgain
import clearScreen

def whatIsTheMask(): 

    #Set IP Class Ranges
    classA = range(1,126)
    classB = range(127,191)
    classC = range(192,223)
     
    #Generates random 32 bit number
    randoIP = random.getrandbits(32)

    #Converts the 32 bit number randoIP to an IPv4 address held in variable convertIP.
    convertIP = ipaddress.IPv4Address(randoIP)

    #Changes questionNetwork IPv4 address into a string
    questionNetworkString = str(convertIP)

    #Finds the first octet of randomly generated IP.

    firstOctet = questionNetworkString[0:questionNetworkString.find('.')]

    #Checks what range first octet is in.

    if int(firstOctet) in classA:
        #Generates random number 1-16777214 to be used as number of hosts required.
        hostsRequired = random.randrange(1,16777214,1)
        #Sets subnet mask to classful mask
        subnetMask = "/8"
        
    elif int(firstOctet) in classB:
        #Generates random number 1-65534 to be used as number of hosts required.
        hostsRequired = random.randrange(1,65534,1)
        #Sets subnet mask to classful mask
        subnetMask = "/16"
        
    else:
        #Generates random number 1-254 to be used as number of hosts required.
        hostsRequired = random.randrange(1,254,1)
        #Sets subnet mask to classful mask
        subnetMask = "/24"

    #concat strings to convert to interface type
    classfulNetwork = questionNetworkString + subnetMask

    #Converts string to IP interface
    classfulNetworkConverted = ipaddress.ip_interface(classfulNetwork)

    #Converts  interface into classful network
    networkConverted = classfulNetworkConverted.network


    #Prints question to the terminal.
    print("What is the longest possible mask to accomodate " + str(hostsRequired) + " hosts in network: " + str(networkConverted) + "?")
    print("\n Type your answer in CIDR Format.")

    #Takes user input as answer and sets variable userAnswer
    userAnswer = input("\nThe longest possible subnet mask is: ")

    #Based on the classful network given, checks the amount of hostsRequired and sets the correct answer to the mask required
    if int(firstOctet) in classA:
        if hostsRequired <= 2:
            correctAnswer = "/30"
        elif 3 <= hostsRequired <= 6:
            correctAnswer = "/29"
        elif 7 <= hostsRequired <= 14:
            correctAnswer = "/28"
        elif 15 <= hostsRequired <= 30:
            correctAnswer = "/27"
        elif 31 <= hostsRequired <= 62:
            correctAnswer = "/26"
        elif 63 <= hostsRequired <= 126:
            correctAnswer = "/25"
        elif 127 <= hostsRequired <= 254:
            correctAnswer = "/24"
        elif 255 <= hostsRequired <= 510:
            correctAnswer = "/23"
        elif 511 <= hostsRequired <= 1022:
            correctAnswer = "/22"
        elif 1023 <= hostsRequired <= 2046:
            correctAnswer = "/21"
        elif 2045 <= hostsRequired <= 4094:
            correctAnswer = "/20"
        elif 4095 <= hostsRequired <= 8190:
            correctAnswer = "/19"
        elif 8191 <= hostsRequired <= 16382:
            correctAnswer = "/18"
        elif 16383 <= hostsRequired <= 32766:
            correctAnswer = "/17"
        elif 32767 <= hostsRequired <= 65534:
            correctAnswer = "/16"
        elif 65535 <= hostsRequired <= 131070:
            correctAnswer = "/15"
        elif 131071 <= hostsRequired <= 262142:
            correctAnswer = "/14"
        elif 262143 <= hostsRequired <= 524286:
            correctAnswer = "/13"
        elif 524287 <= hostsRequired <= 1048574:
            correctAnswer = "/12"
        elif 1048575 <= hostsRequired <= 2097150:
            correctAnswer = "/11"
        elif 2097151 <= hostsRequired <= 4194302:
            correctAnswer = "/10"
        elif 4194303 <= hostsRequired <= 8388606:
            correctAnswer = "/9"
        elif 8388607 <= hostsRequired <= 16777214:
            correctAnswer = "/8"
        
    elif int(firstOctet) in classB:
        if hostsRequired <= 2:
            correctAnswer = "/30"
        elif 3 <= hostsRequired <= 6:
            correctAnswer = "/29"
        elif 7 <= hostsRequired <= 14:
            correctAnswer = "/28"
        elif 15 <= hostsRequired <= 30:
            correctAnswer = "/27"
        elif 31 <= hostsRequired <= 62:
            correctAnswer = "/26"
        elif 63 <= hostsRequired <= 126:
            correctAnswer = "/25"
        elif 127 <= hostsRequired <= 254:
            correctAnswer = "/24"
        elif 255 <= hostsRequired <= 510:
            correctAnswer = "/23"
        elif 511 <= hostsRequired <= 1022:
            correctAnswer = "/22"
        elif 1023 <= hostsRequired <= 2046:
            correctAnswer = "/21"
        elif 2045 <= hostsRequired <= 4094:
            correctAnswer = "/20"
        elif 4095 <= hostsRequired <= 8190:
            correctAnswer = "/19"
        elif 8191 <= hostsRequired <= 16382:
            correctAnswer = "/18"
        elif 16383 <= hostsRequired <= 32766:
            correctAnswer = "/17"
        elif 32767 <= hostsRequired <= 65534:
            correctAnswer = "/16"
            
    else:
        if hostsRequired <= 2:
            correctAnswer = "/30"
        elif 3 <= hostsRequired <= 6:
            correctAnswer = "/29"
        elif 7 <= hostsRequired <= 14:
            correctAnswer = "/28"
        elif 15 <= hostsRequired <= 30:
            correctAnswer = "/27"
        elif 31 <= hostsRequired <= 62:
            correctAnswer = "/26"
        elif 63 <= hostsRequired <= 126:
            correctAnswer = "/25"
        elif 127 <= hostsRequired <= 254:
            correctAnswer = "/24"
            
    #Checks userAnswer against correctAnswer
    if userAnswer == correctAnswer:
        print("\n\nWay to go, everything is perfect.")
    else:
        print("\n\nYour mask is too big and the network got hacked, better luck next time!")
        print("\nThe correct answer was: " + correctAnswer)
        print("You entered: " + userAnswer)

    #Play again loop starts here.
    if playAgain.playAgain() == "yes":
            clearScreen.clear()
            whatIsTheMask()
    else:
        clearScreen.clear()
        pass
    return


    return