from collections import Counter

print(list(Counter('good').keys()))

list1 = ['a','b','c','a','b']

print(list(Counter(list1).keys()))
for i,j in enumerate(list1):
    print(i,j)