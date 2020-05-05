def print_equations (Max):
    temp = ''
    for things in Max:
        temp += str(things) + ' '
    temp += "= "
    print(temp, end="")

while(True):
    Input = input("Please enter a equation: ")
    Input = Input.split(" ")
    Input[0] = int(Input[0])
    Input[2] = int(Input[2])
    if (Input[1] == '*'):
        print_equations(Input)
        print(Input[0] * Input[2])
    elif (Input[1] == '+'):
        print_equations(Input)
        print(Input[0] + Input[2])
    elif (Input[1] == '/'):
        print_equations(Input)
        print(Input[0] / Input[2])
    elif (Input[1] == '-'):
        print_equations(Input)
        print(Input[0] - Input[2])
    elif (Input[1] == '%'):
        print_equations(Input)
        print(Input[0] % Input[2])
    elif (Input[1] == '//'):
        print_equations(Input)
        print(Input[0] // Input[2])