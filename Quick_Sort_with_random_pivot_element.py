import time
import random

start = time.time()


def Pivot_Placement(list, first, last):

    random_index = random.randint(first, last)
    list[random_index], list[last] = list[last], list[random_index]
    pivot = list[last]
    left = first
    right = last-1
    while True:
        # Just change it to >= for descending order
        while left <= right and list[left] <= pivot:
            left = left+1
        # Just change it to <= for descending order
        while left <= right and list[right] >= pivot:
            right = right-1

        if right < left:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[last], list[left] = list[left], list[last]
    return right


def QuickSort(list, first, last):
    if first < last:
        p = Pivot_Placement(list, first, last)
        QuickSort(list, first, p-1)
        QuickSort(list, p+1, last)


time.sleep(1)

end = time.time()

list = [99, 32, 1, 9, 0, 22, 43, 2]

QuickSort(list, 0, len(list)-1)
print(list, f"Time taken: {end-start}")
