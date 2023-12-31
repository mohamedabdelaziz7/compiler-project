def S():
    global i
    if s[i] in grammar['S']:
        i += 1
        B()
        if s[i] in grammar['b']:
            i += 1
        else:
            error()
    elif s[i] in grammar['c']:
        i += 1
        A()
    else:
        error()

def A():
    global i
    if s[i] in grammar['A'] or s[i] in grammar['c']:
        i += 1
    else:
        error()

def B():
    global i
    if s[i] in grammar['B'] or s[i] in grammar['b']:
        i += 1
    else:
        error()

def error():
    print("string is invalid")
    exit()

# Main code
i = 0
s = input("Enter the string: ")
grammar = {}

# Prompt the user to enter the grammar rules
grammar['S'] = input("Enter the production rules for S: ").split('/')
grammar['A'] = input("Enter the production rules for A: ").split('/')
grammar['B'] = input("Enter the production rules for B: ").split('/')
grammar['b'] = input("Enter the expected characters for b: ").split('/')
grammar['c'] = input("Enter the expected characters for c: ").split('/')

S()

if i == len(s):
    print("string is valid")
else:
    print("string is invalid")