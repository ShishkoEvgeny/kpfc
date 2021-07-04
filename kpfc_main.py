import re


### Функция для вычисления количества макронутриентов на 100 грамм
def count(x, w):
    return x * 100 / w


### Функция для подсчёта количества макронутриентов на имеющийся вес ингредиента
def total(n, j):
    return n * j / 100


def cyrillic(text):
    return bool(re.search('[а-я]', text))


while True:
    try:
        ing = input('ingredient: ')      ### Ввод ингредиента

        test = cyrillic(ing)
        if test == True:
            with open('data_kpfc.txt', encoding='utf-8') as book:
                x = book.read()
                # print(x)
                s = x.split('=')
                # print(s)
                a = [i for i in range(len(s)) if ing in s[i]]
                jtr = a[0]
                # print(jtr)
                new = [s[jtr]]
                # print(new)
                kpfch = (new[0])
                # print(type(kpfch))
                break
        else:
            print('no numbers, no english, only cyrillic!')
    except IndexError:
        print('absent value')
print(kpfch)
f = kpfch.split(',')




print('product -', f[0])
kcal = float(f[1])
proteins = float(f[2])
fats = float(f[3])
carbohydrates = float(f[4])

print('kcal on 100g -', kcal)
print('proteins on 100g -', proteins)
print('fats on 100g -', fats)
print('carbohydrates on 100g -', carbohydrates)

tw = float(input('total weight: '))
kcal = total(kcal, tw)
proteins = total(proteins, tw)
fats = total(fats, tw)
carbohydrates = total(carbohydrates, tw)

kpfct = [kcal, proteins, fats, carbohydrates]
print()
print('kcal on', tw, 'weight', '-', kcal)
print('proteins', tw, 'weight', '-', proteins)
print('fats on', tw, 'weight', '-', fats)
print('carbohydrates on', tw, 'weight', '-', carbohydrates)

print(kpfct)

