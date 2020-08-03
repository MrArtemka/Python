while True:
	a = int(input('Введи число от 0 до 10 :'))
	if a > 0 and a < 10:
		break
	else:
		print('Неправильное число, число должно быть больше 0 и меньше 10')
		
print('Результат: ', a * 5)
