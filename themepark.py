from datetime import datetime as dt

now = dt.now()
ticket_price = 0
def calc_ticket(year):
    age = int(now.strftime('%Y'))-year
    
    if age in range(18,65):
        ticket_price = 75
    else:
        ticket_price = 50
    return ticket_price

def calc_discount(amount):
    if now.strftime('%A') in ['Tuesday','Thursday','Friday']:
        amount *= .8
    return amount

name = input('Enter your name: ')
dob = input('Enter your date of birth(dd.mm.yyyy): ')
final_ticket_price = calc_discount(calc_ticket(int(dob[-4:])))
print(final_ticket_price)