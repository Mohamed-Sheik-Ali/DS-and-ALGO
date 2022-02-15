import time  # To check the time taken by the function

start = time.time()


def Bubble_sort(list):

    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

    return list


time.sleep(1)

end = time.time()


unsorted_list = [54, 0, 88, 9, 11, 21, 12]

print(Bubble_sort(unsorted_list), f"Time Taken: {end-start}")
