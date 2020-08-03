a = input('Введи текст :')
b = a.replace(' ','')

steps = 0
p = False
while steps < len(b):
	if b[steps] == b[-steps -1]:
		p = True
	else:
		p = False
		break
	steps += 1

if p:
	print('Слово "',a,'" - палиндром')
else:
	print('Слово "',a,'" - не палиндром')
