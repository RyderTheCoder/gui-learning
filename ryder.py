def menu():
    print "Welcome to calculator.py"
    print "your options are:"
    print " "
    print "1) +"
    print "2) -"
    print "3) x"
    print "4) /"
    print "5) Quit"
    print " "
    return input("Choose the option: ")


def add(a, b):
    print a, "+", b, "=", a + b


def sub(a, b):
    print b, "-", a, "=", b - a


def mul(a, b):
    print a, "*", b, "=", a * b


def div(a, b):
    print a, "/", b, "=", a / b


loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this: "), input("to this: "))
        loop = 0
    elif choice == 2:
        sub(input("Subtract this: "), input("from this: "))
        loop = 0
    elif choice == 3:
        mul(input("Multiply this: "), input("by this: "))
