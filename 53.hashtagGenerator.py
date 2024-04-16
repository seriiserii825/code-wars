def hashtagGenerator(string):
    result = ''
    for char in string.split():
        result += char.capitalize()
    return False if len(string) == 0 or len(result) > 140 else f'#{result}'

print(hashtagGenerator('some new    string'))
print(hashtagGenerator(''))
print(hashtagGenerator('some new stringsome new stringsome new stringsome new stringsome new stringsome new stringsome new stringsome new stringsome new stringsome new stringsome new string'))
