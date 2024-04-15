# Digital root is the recursive sum of all the digits in a number.
# Given n , take the sum of the digits of n . If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# The input will be a non-negative integer.
# Examples
# 16 --> 1+6
# 942 --> 9+4 a5 --> 14+5=6
# 132189 --> 1+3
# +
# 1+8+9=24 -> 2+4
# WN NA
# "
# o
# +
# 493193 --> 4+9
# 14943529 -» 2+9=11 --> 1+1=2
def sumOfDigits(number):
    return number if number < 10 else sumOfDigits(sum([int(i) for i in str(number)]))

print(sumOfDigits(88))
