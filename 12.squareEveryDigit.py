# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 9? is 81 and 17s 1.
# Note: The function accepts an integer and returns an integer
def squareEveryDigit(number):
    return int("".join([str(int(i)**2) for i in str(number)]))

print(squareEveryDigit(9119)) # 811181
print(squareEveryDigit(1234)) # 14916
