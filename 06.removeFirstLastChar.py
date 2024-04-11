# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string, You're given one parameter, the
# original string. You don't have to worry with strings with less than two characters.
def removeFirstLastChar(string):
    return string[1:-1]

print(removeFirstLastChar("Hello")) # ell
print(removeFirstLastChar("World")) # orl
