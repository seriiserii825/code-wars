def humanReadableTime(time):
    # // - divide and floor(3600 - 1 hour)
    hours = time // 3600
    # % - divide and return remainder 
    minutes = (time % 3600) // 60
    # % - divide and return remainder 
    seconds = time % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'

print(humanReadableTime(219231))

