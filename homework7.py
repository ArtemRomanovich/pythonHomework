print('Введите минимальную инвестицию: ')
a = int(input())
print('Сколько у Майкла на кармане ?: ')
b = int(input())
print('Сколько у Ивана на кармане ?: ')
c = int(input())

if a < b and a < c:
    print(2)
elif a < b:
    print('Майкл')
elif a < c:
    print('Иван')
elif a < (b + c):
    print(1)
else:
    print(0)