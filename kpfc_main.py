import re

### Функция для вычисления количества макронутриентов на 100 грамм
def count(x, w):
    return x * 100 / w

### Функция для подсчёта количества макронутриентов на имеющийся вес ингредиента
def total(n, j):
    return n * j / 100


def cyrillic(text):
    return bool(re.search('[а-я]', text))


ing = input('ingredient ')      ### Ввод ингредиента

try:
    ing = input('ingredient ')
    test = cyrillic(ing)
    if test == True:
        with open('data_kpfc.txt', encoding='utf-8') as book:
            x = book.read()
            s = x.split('=')
            a = [i for i in range(len(s)) if ing in s[i]]
            print(a)
            jtr = a[0]
            new = [s[jtr]]
            kpfch = (new[0])
    else:
        print('no numbers, no english, only cyrillic!')
except IndexError:
    print('absent value')

#if ing == 'курица':
#    kpfch = {'kcal': '113', 'proteins': '24', 'fats': '1.9', 'carbohydrates': '0.4'}

k = float(kpfch['kcal'])
p = float(kpfch['proteins'])
f = float(kpfch['fats'])
c = float(kpfch['carbohydrates'])

tw = float(input('total weight: '))
tk = total(k, tw)
tp = total(p, tw)
tf = total(f, tw)
tc = total(c, tw)

kpfct = {'kcal': tk, 'proteins': tp, 'fats': tf, 'carbohydrates': tc}

print(kpfct)

