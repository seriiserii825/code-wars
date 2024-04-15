def camelCase(string):
    string = string.replace('-', ' ').replace('_', ' ')
    return ''.join([word.capitalize() if word != string.split()[0] else word for word in string.split()])

print(camelCase('hello-world'))
print(camelCase('hello_world'))

