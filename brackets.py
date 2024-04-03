brackets = {'(':')','[':']','{':'}'}
checklist1 = []
def check_bracket_balance(string):
    for i in string:
        if i in brackets:
            checklist1.append(i)
        elif i in brackets.values():
            if i == brackets[checklist1[-1]]:
                checklist1.pop()
    if checklist1:
        return 0
    else:
        return 1

value = check_bracket_balance(input('Enter the string: '))
if value:
    print('Brackets are balanced')
else:
    print('Brackets are not balanced')
    