def validParanthesis(string):
    k = 0
    for i in string:
        if i == '(':
            k += 1
        if i == ')':
            k -= 1
    return k == 0

print(validParanthesis('(()())'))
