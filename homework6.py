print('Введите слово из маленьких латинских букв: ')
word_list = list(input())
a = list(filter(lambda x: (x == 'a'), word_list))
e = list(filter(lambda x: (x == 'e'), word_list))
i = list(filter(lambda x: (x == 'i'), word_list))
o = list(filter(lambda x: (x == 'o'), word_list))
u = list(filter(lambda x: (x == 'u'), word_list))
if len(a) == 0 or len(e) == 0 or len(i) == 0 or len(o) == 0 or len(u) == 0:
    print(False)
