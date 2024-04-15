
# Your goal in this kata is to implement a difference function, which subtracts one list from another and retums the result.
# It should remove all values from list a , which are presentin list b keeping their order.
# array_diff({1,2],[1]) = [2]
# If avalueis present in b , all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) = [1,3]
def arrayDiff(array1, array2):
    result = []
    for i in array1:
        for n in array2:
            if i == n and i not in result:
                result.append(i)
    print(result)

print(arrayDiff([1, 2], [3, 4]))
