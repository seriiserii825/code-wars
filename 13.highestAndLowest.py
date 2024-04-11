# In this little assignment you are given string of space separated numbers, and have to return the highest and lowest number.
def highestAndLowest(string):
    numbers = list(map(int, string.split()))
    return f"{max(numbers)} {min(numbers)}"

print(highestAndLowest("1 2 3 4 5")) # 5 1
print(highestAndLowest("1 2 -3 4 5")) # 5 -3
