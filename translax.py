from sys import *

def dyametes(x):
    pass

def yexamora(x):
    pass


def main():
    if(argv[1] == "-help"):
        # Wish it looked nicer but this was readable

        print("######################")
        print("Welcome to Translax!  ")
        print("Translator for        ")
        print("Dyametes and Yexamora!")
        print("######################")
        print("                      ")
        print("Designed by Kai Lyons ")
        print("Translates custom ciphers DESIGNED by Kai Lyons")
        print("Technically these are translators for Yexamora-Minor")
        print("and Dyametes-Minor as the regular versions have their\nown symbols.")
        print("\nask twitter.com/KaiLikesLinux for more information")
        print("\nWorking comands:")
        print("-d             |  Prints out only Dyametes-Minor translations")
        print("-p             |  Prints out only Yexamora-Minor translations")
        print("-dy            |  Prints both Dyametes-Minor and Yexamora-Minor")
        print("-translations  |  Prints out the file that will allow tranlsation")
        print("-help          |  Displays this message")
    elif(argv[1] == "-d"):
        print("Dyametes-Minor Translation: ")
    elif(argv[1] == "-y"):
        print("Yexamora-Minor Translation: ")
    elif(argv[1] == "-dy"):

        print("Dyametes-Minor Translation: ")
        print("Yexamora-Minor Translation: ")
    elif(argv[1] == "-translations"):
        print("get the list of translations")
        if (argv[2] == "-d"):
            print("Display the Dyametes-Minor Translation")
        elif (argv[2] == "-y"):
            print("Display the Yexamora-Minor Translation")
    else:
        print("Error, unknown input, try translax -help")

main()
