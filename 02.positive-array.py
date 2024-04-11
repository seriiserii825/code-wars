# You get an array of numbers, return the sum of all of the positives ones.

def positiveSum(arr):
    if len(arr) == 0:
        print(0)
        return
    result = sum(x for x in arr if x > 0)
    print(result)

positiveSum([1, -4, 7, 12]) # 20
positiveSum([]) # 0
