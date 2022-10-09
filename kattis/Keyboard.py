master_dict ={"clank": "a",
"bong": "b",
"click": "c",
"tap": "d",
"poing": "e",
"clonk": "f",
"clack": "g",
"ping": "h",
"tip": "i",
"cloing": "j",
"tic": "k",
"cling": "l",
"bing": "m",
"pong": "n",
"clang": "o",
"pang": "p",
"clong": "q",
"tac": "r",
"boing": "s",
"boink": "t",
"cloink": "u",
"rattle": "v",
"clock": "w",
"toc": "x",
"clink": "y",
"tuc": "z",
"whack": " ",
"bump": 0, "pop": 1, "dink": 2, "thumb": 3}

word_list =[]

def input_function():
    word_count = int(input())
    for i in range(word_count):
        word = input()
        word_list.append(master_dict[word])

def print_function():
    
    caps = False
    shift = False
    final_string = []
    for i in word_list:
        if i == 0:
            caps = not caps
        elif i == 1:
            final_string.pop()
        elif i == 2:
            shift = True
        elif i == 3:
            shift = False
        else:
            if ((caps == True) and (shift ==True)) or ((caps == False) and (shift == False)):
                final_string.append(i)
            else:
                final_string.append(i.upper())
    return("".join(final_string))


def main():
    input_function()
    #print(word_list)
    print(print_function())
main()

