# реализация алгоритма бинарного поиска
from random import randint
lts = []
for i in range(11):
    lts.append(randint(1,100))

lts.sort()
print(lts)


search_num = int(input('Enter the search_num: '))


def b_search(lts, search_num):

    low = 0  # нижняя граница поиска
    high = len(lts) - 1  # верхняя граница поиска
    midl = (low + high) // 2  # находим середину

    while search_num != lts[midl] and low < high:
        if search_num > lts[midl]:
            low = midl + 1
        else:
            high = midl - 1
        midl = (low + high) // 2

    if search_num == lts[midl]:
        return print('ID:', midl)
    else:
        print('No search_num')
b_search(lts, search_num)