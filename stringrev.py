str = 'hello world'
wordlist = str.split(' ')
strlist = []
for i in wordlist:
    for j in i:
        strlist.append(j)
    for i in range(len(strlist)):
        print(strlist.pop(),end='')
    print(end=' ')