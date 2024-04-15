# def moving0ToTheEnd(array):
#     free = []
#     for i in array:
#         if i != 0:
#             free.append(i)
#     return free + [0 for i in range(len(array) - len(free))]

def moving0ToTheEnd(array):
    return [i for i in array if i!= 0] + [0] * array.count(0)

print(moving0ToTheEnd([1,2,0,3,0,4, 8, 9]))
