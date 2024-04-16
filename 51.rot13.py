def rot13(string):

    list_small = [item for item in range(ord("a"), ord("z") + 1)]
    list_big = [item for item in range(ord("A"), ord("Z") + 1)]
    print(f'list_big: {list_big}')
    print(f'list_small: {list_small}')

    result = ''
    for char in string:
        if char.isupper():
            result += chr((ord(char) - 65 + 13) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + 13) % 26 + 97)
        else: 
            result += char
    print(result)

rot13('azome string')

