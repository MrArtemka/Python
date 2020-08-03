# All Variables
a = input('Введи текст: ')

b = 0

c = 0
#--------------------------------
# Cycle for count
steps = 0
while steps < len(a):

	if a[steps].isupper():
 		b += 1
	elif a[steps].islower():
		c += 1
	else:
		print('Символ - "',a[steps],'"- не является прописным или строчным')
	steps += 1
#--------------------------------
# Output all value
print('Длина строки: ', len(a))
print('Количество прописных букв: ', b)
print('Количество строчных букв: ', c)