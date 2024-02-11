import random, sys

def main():
    
    keepRunning = True

    while keepRunning:

        usrInp = ''
        #usrInp = input("Throw a dice to test your luck! Enter any number between 1 and 6, both inclusive:  ")
        usrInp = random.randrange(1,6)
        print ('User 1 dice showd up: ', str(usrInp))

        rndInp = random.randrange(1,6)
        print ('User 2 dice showd up: ', str(rndInp))

        if rndInp == usrInp:
                print ('User 1 output matches with User 2')
                print ("bye-bye have a good day ahead!")
                keepRunning = False
                sys.exit()

if __name__ == "__main__":
    main()