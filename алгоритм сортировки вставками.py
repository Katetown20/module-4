# алгоритм сортировки вставками

alist = [1,5,6,7,8,9,3,4,2]
print('Before: ',alist)

def insertion_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1

        while j >=0 and alist[j] > key:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = key


insertion_sort(alist)
print('After: ',alist)