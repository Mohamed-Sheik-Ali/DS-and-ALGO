import time

start = time.time()


def Pivot_Placement(list, first, last):
    pivot = list[first]
    left = first+1
    right = last
    while True:
        while left <= right and list[left] <= pivot:
            left = left+1

        while left <= right and list[right] >= pivot:
            right = right-1

        if right < left:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[first], list[right] = list[right], list[first]
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
