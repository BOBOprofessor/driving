country = input('請輸入你的國籍')
age = input('請問你今年幾歲?')
age = int(age)
if country == ('台灣'):
	if age >= 18:
		print('你可以考駕照喔!')
	else:
		print('你年紀太小孩不能考駕照!')
elif country == ('美國'):
	if age >= 16:
		print('你可以考駕照喔!')
	else:
		print('你年紀太小孩不能考駕照!')
elif country != ('台灣', '美國'):
	print('你只能輸入(台灣)或(美國)')
