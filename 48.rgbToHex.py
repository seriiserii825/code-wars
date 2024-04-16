def rgbToHex(string):
    colors = []
    for i in string.split(','):
        result = ''
        for k in i:
            if k.isdigit() or k == '-':
                result += k
        result = int(result)
        if result < 0:
            result = 0
        elif (result > 255):
            result = 255
        colors.append(result)
    return f'#{colors[0]:02x}{colors[1]:02x}{colors[2]:02x}'
print(rgbToHex('rgb(823,182,18)'))
