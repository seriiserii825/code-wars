def stringIncrementer(string):
    letters = string.rstrip('0123456789')
    numbers = string[len(letters):]

    if numbers == '': return string + '1'
    return letters + str(int(numbers) + 1).zfill(len(numbers))

    # index_int = 0
    # for i in string:
    #     if i.isdigit():
    #         index_int = string.index(i)
    #         break
    #     else:
    #         continue
    # if index_int == 0:
    #     return  f'{string[:4]}{1}'
    # else:
    #     number = string[index_int:]
    #     number = int(number) + 1
    #     return  f'{string[:4]}{str(number)}'

print(stringIncrementer('some33'))
print(stringIncrementer('some9'))
print(stringIncrementer('some0043'))
print(stringIncrementer('some'))

