def add(a,b):
    print("sum=",a+b)
def sub(a,b):
    print("sub=",a-b)
def mul(a,b):
    print("mul=",a*b)
def div(a,b):
    print("Div=",a/b)
def mod(a,b):
    print("mod=",a%b)
while True:
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modolus")
    print("6.Exit")

    a=int(input("Enter first number="))
    b=int(input("Enter second number="))
    choice=int(input("Enter your choice="))

    match choice:
        case 1:
            add(a,b)
        case 2:
            sub(a,b)
        case 3:
            mul(a,b)
        case 4:
            div(a,b)
        case 5:
            mod(a,b)
        case 6:
            print("Program exited")
            break
        case _:
            print("Invalid choice")
