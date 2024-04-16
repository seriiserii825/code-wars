def maximumSubArray(array):
    max_sum = array[0]
    current_sum = array[0]
    for i in range(1, len(array)):
        current_sum = max(array[i], current_sum + array[i])
        max_sum = max(max_sum, current_sum)
    return 0 if max_sum < 0 else max_sum

print(maximumSubArray([-1,2, 3])) # 6
