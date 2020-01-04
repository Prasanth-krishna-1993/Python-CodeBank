def dayOfWeek(i):
	if (i==1):
		print('Sunday')
	elif(i==2):
		print('Monday')
	elif(i==3):
		print('Tuesday')
	elif(i==4):
		print('Wednesday')
	elif(i==5):
		print('Thrusday')
	elif(i==6):
		print('Friday')
	elif(i==7):
		print('Saturday')
	else:
		print('Invaild Input.')


dayOfWeek(int(raw_input('Enter the Day of Week')))
