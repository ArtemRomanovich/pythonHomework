print('Введите пятизначное число: ')
one, two, three, four, five = map(float, list(input()))
print(one, two, three, four, five)
print(str(((four ** five) * three)/(one-two)))