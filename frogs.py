froglist = [1,2,3,4,5]

def eat_frog(list1):
    if list1:
        for i in range(len(list1)-1):
            if list1[i] < list1[i+1]:
                list1[i+1] += list1[i]
                list1.pop(i)
                eat_frog(list1)
                return list1
    else:
        return 'list is empty'

result = eat_frog(froglist)
print(result)