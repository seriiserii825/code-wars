# Return the number (count) of vowels in the given string.
# Wewill consider a, e, i, 0, u as vowels for this Kata (but not y ).
# The input string will only consist of lower case letters and/or spaces.
def vowelCount(sentence):
  return len([i for i in sentence if i in "aeiouAEIOU"])

print(vowelCount("Hello")) # 2
print(vowelCount("World")) # 1
print(vowelCount("Hello World")) # 3
