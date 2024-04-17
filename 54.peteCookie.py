def peteCookie(recipes, have):
    return min([have[i] // recipes[i] if i in have else 0 for i in recipes])
    # result = []
    # for i in recipes:
    #     if have.get(i):
    #         result.append(have[i] // recipes[i])
    #     else:
    #         return 0
    # return min(result)

print(peteCookie({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 2200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))

