# Make a program that filters a list of strings and returns a list with only your friends name init.
# Ifaname has exactly 4 letters init, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# x Input = ["Ryan’, Kieran’, "Jason", "Yous"], Output = ["Ryan’, "Yous"]
# friend ["Ryan", "Kieran", "Mark"] “shouldBe* ["Ryan”, “Mark"]
# Note: keep the original order of the names in the output.
def friendOrFoe(names):
    return [i for i in names if len(i) == 4]

print(friendOrFoe(['sara', 'joe', 'greg', 'leonardo']))
