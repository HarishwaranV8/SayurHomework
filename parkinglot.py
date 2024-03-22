import os
parking_lot = []
parking_revenue = 0

def init_parking():
	rows = int(input('Enter the no. of rows: '))
	columns = int(input('Enter the no. of columns: '))
	for i in range (rows):
		parking_lot.append([])
		for j in range(columns):
			parking_lot[i].append(0)
	for i in parking_lot:
		for j in i:
			print(j,end=' ')
		print()

def park_car():
	car_id = input('Enter the car ID: ')
	# for i in range(len(parking_lot)):
	# 	if 0 in parking_lot[i]:
	# 		parking_lot[i][parking_lot[i].index(0)] = car_id
	# 		print(i,parking_lot[i].index(car_id))
	# 		break
	# 	elif i != len(parking_lot):
	# 		continue
	# 	else:
	# 		print('Parking is full')
	# 		break
	for i in parking_lot:
		if 0 in i:
			i[i.index(0)] = car_id
			print(f'You car is in row: {parking_lot.index(i)} column : {i.index(car_id)}')
			break
		elif parking_lot.index(i) < len(parking_lot)-1:
			continue
		else:
			print('Parking is full')
			break
		
	for i in parking_lot:
		for j in i:
			print(j,end=' ')
		print()

def unpark_car():
	parking_cost = 50
	global parking_revenue
	car_id = input('Enter the car ID: ')
	for i in parking_lot:
		if car_id in i:
			i[i.index(car_id)] = 0
			parking_revenue += parking_cost
		elif car_id not in i:
			print('Your car is not in this parking lot')
		break
	for i in parking_lot:
		for j in i:
			print(j,end=' ')
		print()
	print('Total revenue:',parking_revenue)

def main():
	a = int(input('Enter your choice: '))
	match a:
		case 0:
			os._exit(0)
		case 1:
			park_car()
		case 2:
			unpark_car()
		case _:
			print('Enter a valid option')


print('0.Exit\n1.Park car\n2.Unpark car')
init_parking()
while 1:
	main()
