flag = True;

while True:
    try:
        txt=input()

        for var in txt:
            if var == '"':
                if flag:
                    print("``", end='')
                else:
                    print("''", end='')
                flag = not flag
            else:
                print(var, end='')

        print(end='\n')
    except EOFError:
        break
