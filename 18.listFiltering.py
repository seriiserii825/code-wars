# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
def listFiltering(l):
    return sorted([i for i in l if type(i) is int])

print(listFiltering(['a', 'b',  8, 'some', 5, 2]))
