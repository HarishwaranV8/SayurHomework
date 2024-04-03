str = 'hello world'
wordlist1 = str.split(' ')
strlist1 = []
for i in wordlist1:
    for j in i:
        strlist1.append(j)
    for i in range(len(strlist1)):
        print(strlist1.pop(),end='')
    print(end=' ')