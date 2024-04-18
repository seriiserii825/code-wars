def extractDomain(url):
    url = url.replace('http://', '').replace('www.', '').replace('https://', '')
    return url.split('.')[0]


print(extractDomain('http://github.com/carbonfive/raygun'))
print(extractDomain('http://www.zombie-bites.com'))
print(extractDomain('http://www.cnet.com'))
print(extractDomain('www.bitbucket.com'))

