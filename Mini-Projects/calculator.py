def add(a,b):
    answer = a+b
    print("\n",str(a) + " + " + str(b) + " = " + str(answer)+"\n")

def sub(a,b):
    answer = a - b
    print("\n",str(a) + " - " + str(b) + " = " + str(answer)+"\n")


def mul(a,b):
    answer = a*b
    print("\n",str(a) + " * " + str(b) + " = " + str(answer)+"\n")

def div(a,b):
    answer = a/b
    print("\n",str(a) + " / " + str(b) + " = " + str(answer)+"\n")

while True:
    print("A. ADDITION")
    print("B. SUBTRACTION")
    print("C. MULTIPICATION")     
    print("D. DIVISION")
    print("E. EXIT")

    choice = input("ENTER YOUR CHOICE :")
    if choice.lower() == "a":
        print("ADDITION")
        a = int(input("ENTER UR FIRST DIGIT:"))
        b = int(input("ENTER UR SECOND DIGIT:"))
        add(a,b)

    elif choice.lower() == "B":
        print("SUBTRACTION")
        a = int(input("ENTER UR FIRST DIGIT:"))
        b = int(input("ENTER UR SECOND DIGIT:"))
        sub(a,b)

    elif choice.lower() == "c":
        print("MULTIPICATION")
        a = int(input("ENTER UR FIRST DIGIT:"))
        b = int(input("ENTER UR SECOND DIGIT:"))
        mul(a,b)

    elif choice.lower() == "d":
        print("DIVISION")
        a = int(input("ENTER UR FIRST DIGIT:"))
        b = int(input("ENTER UR SECOND DIGIT:"))    
        div(a,b)

    elif choice.lower() == "e":
        print("PROGRAM IS ENDED")
        quit()