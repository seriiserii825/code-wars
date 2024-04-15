
# Write function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You
# can guarantee that input is non-negative. x
# Example: The binary representation of 1234 is 10011010010 ,so the function should return 5 inthis case
def bitCounting(number):
    return bin(number).count('1')

print(bitCounting(88))


