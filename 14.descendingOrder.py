# ‘Your task s to make a function that can take any non-negative integer as an
# rearrange the cits to create the highest possible number.
# x gument and return it with ts digits descending order. Essentially,
def descendingOrder(number):
    return ''.join(sorted(list(str(number)), reverse=True))
    num_array = list(str(number))
    num_array.sort()
    num_array = num_array[::-1]
    result = ''.join(num_array)
    return result

print(descendingOrder(15632)) #65321
print(descendingOrder(36722198352)) #9876532221

