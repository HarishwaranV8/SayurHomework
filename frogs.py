froglist = [4,3,3,2,1]

def eat_frog(list):
    for i in range(len(froglist)-1):
        if froglist[i] < froglist[i+1]:
            eat_frog(froglist.pop(i))
        return froglist

print(eat_frog(froglist))