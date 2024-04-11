# Write a function that accepts an integer n andastring s as parameters, and returns a string of s repeated exactly n times.
def stringRepeat(string, count):
    return string * count

print(stringRepeat("Hello", 3)) # HelloHelloHello
print(stringRepeat("World", 5)) # WorldWorldWorldWorldWorld

