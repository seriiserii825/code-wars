
# Write. function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!
def createPhoneNumber(numbers):
    numbers = ''.join([str(i) for i in numbers])
    return f"({numbers[0:3]}) {numbers[3:6]}-{numbers[6:]}"

print(createPhoneNumber([1,2,3,4,5,6,7,4,3,9]))
