# You probably know the “like” system from Facebook and other pages. People can “like" blog posts, pictures or other items. We want to create the
# text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the
# examples:
# 0] “no one Likes this”
# ["Peter™] “Peter likes this”
# ["Jacob", “Alex"] --> “Jacob and Alex Like this”
# ["Max", “John”, “Mark"] --> “Max, John and Mark Like this”
# ["Alex", "Jacob", “Mark”, "Max"] --> “Alex, Jacob and 2 others like this”
# Note: For 4 or more names, the number in “and 2 others” simply increases.
def whoLikesIt(array):
    if len(array) == 0:
        return 'no one Likes this'
    elif len(array) == 1:
        return f"{array[0]} likes this"
    elif len(array) == 2:
        return f"{array[0]} and {array[1]} Like this'"
    elif len(array) == 3: 
        return f"{array[0]}, {array[1]} and {array[2]} Like this"
    else:
        return f"{array[0]}, {array[2]} and {str(len(array) - 2)} others Like this'"

print(whoLikesIt(['John', 'Jake', 'Dorian', 'Sara']))

