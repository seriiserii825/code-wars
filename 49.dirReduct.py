def dirReduct(arr):
    d = {
            'NORTH': 'SOUTH',
            'SOUTH': 'NORTH',
            'WEST': 'EAST',
            'EAST': 'WEST'
            }
    for i in range(len(arr) - 1):
        if d[arr[i]] == arr[i + 1]:
            del arr[i:i + 2]
            return dirReduct(arr)
    print(arr)

dirReduct(['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH'])
