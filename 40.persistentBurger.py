def persistentBurger(number):
    if len(str(number)) > 1:
        result = 1
        for i in str(number):
            result *= int(i)
        return 1 + persistentBurger(result)
    else: 
        return 0

print(persistentBurger(999))
