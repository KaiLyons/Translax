from sys import *

def dyametes(x):
    d1 = x.replace("a", "^").replace("u", "^")
    d2 = d1.replace("o", "(").replace("e", "(")
    d3 = d2.replace("n", "<").replace("i", "|")
    d4 = d3.replace("b", "/").replace("z", "/")
    d5 = d4.replace("c", "#").replace("y", "#")
    d6 = d5.replace("d", "*").replace("w", "*")
    d7 = d6.replace("f", "&").replace("w", "&")
    d8 = d7.replace("g", "$").replace("v", "$")
    d9 = d8.replace("h", "}").replace("t", "}")
    d10 = d9.replace("j", ":").replace("s", ":")
    d11 = d10.replace("k", "]").replace("r", "]")
    d12 = d11.replace("l", "?").replace("q", "?")
    d13 = d12.replace("m", "@").replace("p", "@")
    return d13

def yexamora(x):
    y1 = x.replace("a", "^").replace("z", "^")
    y2 = y1.replace("b", "(").replace("y", "(")
    y3 = y2.replace("c", "|").replace("x", "|")
    y4 = y3.replace("d", "/").replace("w", "/")
    y5 = y4.replace("e", "#").replace("v", "#")
    y6 = y5.replace("f", "*").replace("u", "*")
    y7 = y6.replace("g", "$").replace("t", "$")
    y8 = y7.replace("h", "}").replace("s", "}")
    y9 = y8.replace("i", ";").replace("r", ";")
    y10 = y9.replace("j", "]").replace("q", "]")
    y11 = y10.replace("k", "?").replace("p", "?")
    y12 = y11.replace("l", "@").replace("o", "@")
    y13 = y12.replace("m", "<").replace("n", "<")
    return y13


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
        print("               |  -d as the 2nd argument shows the Dyametes-Minor translations")
        print("               |  -y as the 2nd argument shows the Yexamora-Minor translations")
        print("-help          |  Displays this message")
        print("\nExamples:")
        print("translax -y the string after the first one is recongnised")
        print("translax -translations -d")
    elif(argv[1] == "-d"):
        output = dyametes(str(argv).split("-d")[1].replace(",", "").replace("'", "").replace("]", "").lower())
        print("Dyametes-Minor Translation: ", output)
    elif(argv[1] == "-y"):
        output = yexamora(str(argv).split("-y")[1].replace(",", "").replace("'", "").replace("]", "").lower())
        print("Yexamora-Minor Translation: ", output)
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
