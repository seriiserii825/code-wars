# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive
# integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77] ,the output shouldbe 7.
# [10, 343445353, 3453445, 3453545353453] shouldreturn 3453455 .
def sumOfTwoLowestPositiveIntegers(array):
  return sum(sorted(array)[:2])

print(sumOfTwoLowestPositiveIntegers([2, 3, 4, 5]))
