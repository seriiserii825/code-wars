# This time no story, no theory. The examples below show you how to write function accum :
# Examples:
# accum("abed") -> "A-Bb-Ccc-Dddd”
# accum("RqaEzty") -> “R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt”


# def mumbling(string):
#     result = ""
#     for index, value in enumerate(string):
#         if index == 0:
#             value = value.capitalize()
#             result += value
#         elif(index == len(string) - 1):
#             result += value * (index + 1)
#         else:
#             result += value * (index + 1) + '-'
#
#     print(result)
            

def mumbling(s):
    result = '-'.join([s[i].upper() + (s[i].lower() * i) for i in range(len(s))])
    print(result)

mumbling('HelloWorld')

