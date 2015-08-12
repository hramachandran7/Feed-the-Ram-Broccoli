import sys
whileloophelper=0
hunger=0
money=0
inputn=input("Hi what is your name?: ")
print("Hi",inputn,", welcome to feed the ram broccoli V 1.2")
print("In this game you will learn the basics of math!")
inputa=input("Press I for instructions or any key to skip: ").lower()
if inputa == "i":
    print("The ram has a hunger level in which 0 is very hungry and 10 is not hungry. You will be told the hunger level of the ram and will be asked to type in how many pieces of broccoli you must feed the ram to make the ram not hungry assusming 1 piece broccoli accounts for 1 hunger. If you get the answer correct, you earn 1 money. You start off with 0 money. If you feed the ram too little or too much, the ram will either fall unconscious due to hunger, or have its stomach explode. If the ram falls unconscious or explodes, you can pay 1 money to take it to the doctor. If you do not have sufficient money to take the ram to the doctor, the game is over.")
if inputa == "s":
    while whileloophelper==0:
        inputb=input("Press C to continue: ").lower()
        if inputb == "c":
            inputc=input("Press P to play: ").upper()
        if inputc == "P":
            import random
            rn = random.randint(1, 9);
            s=10-rn
            print("The hunger level is", rn)
            inputd = input("How much broccoli will you feed him?: ")
            inputdb = float(inputd)
            if inputdb == s:
                print("That is correct!")
                money = money+1
                print("You now have", money, "money!")
                print("Press any key to continue.")
                inputz=input()
            elif inputdb > s:
                print("The ram's stomach exploded")
                print("Press any key to continue.")
                inputz=input()
                if money>0:
                    inpute=input("Would you like to spend 1 money to take the ram to the doctor? y/n: ").lower()
                else:
                    print("Game Over!")
                    inputv=input("Press Q to quit or any other key to restart: ").upper()
                    if inputv == "Q":
                        sys.exit()
                    else:
                        print("Try to beat your high score of",money,"!")
                        money=0
                        continue
                if inpute == "y":
                    money = money-1
                    print ("The ram is now fixed.")
                if inpute == "n":
                    print("Game Over")
                    inputv=input("Press Q to quit or any other key to restart: ").upper()
                    if inputv == "Q":
                        sys.exit()
                    else:
                        print("Try to beat your high score of",money,"!")
                        money=0
                        continue
            elif inputdb < s:
                print("The ram fell unconscious due to hunger")
                print("Press any key to continue.")
                inputz=input()
                if money>0:
                    inpute=input("Would you like to spend 1 money to take the ram to the doctor? y/n: ").lower()
                else:
                    print("Game Over!")
                    inputv=input("Press Q to quit or any other key to restart: ").upper()
                    if inputv == "Q":
                        sys.exit()
                    else:
                        print("Try to beat your high score of",money,"!")
                        money=0
                        continue
                if inpute == "y":
                   money = money-1
                   print ("The ram is now fixed.")
                if inpute == "n":
                    print("Game Over")
                    inputv=input("Press Q to quit or any other key to restart: ").upper()
                    if inputv == "Q":
                        sys.exit()
                    else:
                        print("Try to beat your high score of",money,"!")
                        money=0
                        continue
            while whileloophelper == 0:
                import random
                rn = random.randint(1, 9);
                s=10-rn
                print("The hunger level is", rn)
                inputd = input("How much broccoli will you feed him?: ")
                inputdb = float(inputd)
                if inputdb == s:
                    print("That is correct!")
                    money = money+1
                    print("You now have", money, "money!")
                    print("Press any key to continue.")
                    inputz=input()
                elif inputdb > s:
                    print("The ram's stomach exploded")
                    print("Press any key to continue.")
                    inputz=input()
                    if money>0:
                        inpute=input("Would you like to spend 1 money to take the ram to the doctor? y/n: ").lower()
                    else:
                        print("Game Over!")
                        inputv=input("Press Q to quit or any other key to restart: ").upper()
                        if inputv == "Q":
                            sys.exit()
                        else:
                            print("Try to beat your high score of",money,"!")
                            money=0
                            continue
                    if inpute == "y":
                        money = money-1
                        print ("The ram is now fixed.")
                    if inpute == "n":
                        print("Game Over")
                        inputv=input("Press Q to quit or any other key to restart: ").upper()
                        if inputv == "Q":
                            sys.exit()
                        else:
                           print("Try to beat your high score of",money,"!")
                           money=0
                           continue
                elif inputdb < s:
                    print("The ram fell unconscious due to hunger")
                    print("Press any key to continue.")
                    inputz=input()
                    if money>0:
                        inpute=input("Would you like to spend 1 money to take the ram to the doctor? y/n: ").lower()
                    else:
                        print("Game Over!")
                        inputv=input("Press Q to quit or any other key to restart: ").upper()
                        if inputv == "Q":
                            sys.exit()
                        else:
                            print("Try to beat your high score of",money,"!")
                            money=0
                            continue
                    if inpute == "y":
                        money = money-1
                        print ("The ram is now fixed.")
                    if inpute == "n":
                        print("Game Over")
                        inputv=input("Press Q to quit or any other key to restart: ").upper()
                        if inputv == "Q":
                            sys.exit()
                        else:
                           print("Try to beat your high score of",money,"!")
                           money=0
                           continue
while whileloophelper == 0:
    inputb=input("Press C to continue: ").lower()
    if inputb == "c":
        inputc=input("Press P to play: ").upper()
    if inputc == "P":
        import random
        rn = random.randint(1, 9);
        s=10-rn
        print("The hunger level is", rn)
        inputd = input("How much broccoli will you feed him?: ")
        inputdb = float(inputd)
        if inputdb == s:
            print("That is correct!")
            money = money+1
            print("You now have", money, "money!")
            print("Press any key to continue.")
            inputz=input()
        elif inputdb > s:
            print("The ram's stomach exploded")
            print("Press any key to continue.")
            inputz=input()
            if money>0:
                inpute=input("Would you like to spend 1 money to take the ram to the doctor? y/n: ").lower()
            else:
                print("Game Over!")
                inputv=input("Press Q to quit or any other key to restart: ").upper()
                if inputv == "Q":
                    sys.exit()
                else:
                    print("Try to beat your high score of",money,"!")
                    money=0
                    continue
            if inpute == "y":
                money = money-1
                print ("The ram is now fixed.")
            if inpute == "n":
                print("Game Over")
                inputv=input("Press Q to quit or any other key to restart: ").upper()
                if inputv == "Q":
                    sys.exit()
                else:
                    print("Try to beat your high score of",money,"!")
                    money=0
                    continue
        elif inputdb < s:
            print("The ram fell unconscious due to hunger")
            print("Press any key to continue.")
            inputz=input()
            if money>0:
                inpute=input("Would you like to spend 1 money to take the ram to the doctor? y/n: ").lower()
            else:
                print("Game Over!")
                inputv=input("Press Q to quit or any other key to restart: ").upper()
                if inputv == "Q":
                    sys.exit()
                else:
                    print("Try to beat your high score of",money,"!")
                    money=0
                    continue
            if inpute == "y":
                money = money-1
                print ("The ram is now fixed.")
            if inpute == "n":
                print("Game Over")
                inputv=input("Press Q to quit or any other key to restart: ").upper()
                if inputv == "Q":
                    sys.exit()
                else:
                    print("Try to beat your high score of",money,"!")
                    money=0
                    continue
        while whileloophelper == 0:
            import random
            rn = random.randint(1, 9);
            s=10-rn
            print("The hunger level is", rn)
            inputd = input("How much broccoli will you feed him?: ")
            inputdb = float(inputd)
            if inputdb == s:
                print("That is correct!")
                money = money+1
                print("You now have", money, "money!")
                print("Press any key to continue.")
                inputz=input()
            if inputdb > s:
                print("The ram's stomach exploded")
                print("Press any key to continue.")
                inputz=input()
                if money>0:
                    inpute=input("Would you like to spend 1 money to take the ram to the doctor? y/n: ").lower()
                else:
                    print("Game Over!")
                    inputv=input("Press Q to quit or any other key to restart: ").upper()
                    if inputv == "Q":
                        sys.exit()
                    else:
                        print("Try to beat your high score of",money,"!")
                        money=0
                        continue
                if inpute == "y":
                    money = money-1
                    print ("The ram is now fixed.")
                if inpute == "n":
                    print("Game Over")
                    inputv=input("Press Q to quit or any other key to restart: ").upper()
                    if inputv == "Q":
                        sys.exit()
                    else:
                        print("Try to beat your high score of",money,"!")
                        money=0
                        continue
            elif inputdb < s:
                print("The ram fell unconscious due to hunger")
                print("Press any key to continue.")
                inputz=input()
                if money>0:
                    inpute=input("Would you like to spend 1 money to take the ram to the doctor? y/n: ").lower()
                else:
                    print("Game Over!")
                    inputv=input("Press Q to quit or any other key to restart: ").upper()
                    if inputv == "Q":
                        sys.exit()
                    else:
                        money=0
                        print("Try to beat your high score of",money,"!")
                        continue
                if inpute == "y":
                    money = money-1
                    print ("The ram is now fixed.")
                if inpute == "n":
                    print("Game Over")
                    inputv=input("Press Q to quit or any other key to restart: ").upper()
                    if inputv == "Q":
                        sys.exit()
                    else:
                        money=0
                        print("Try to beat your high score of",money,"!")
                        continue
        

    
    

        

    
    

