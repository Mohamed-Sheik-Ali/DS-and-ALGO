def Selection_Sort(list):
    for i in range(len(unsorted_list)-1):

        min_val = min(list[i:])
        min_val_index = list.index(min_val, i)  # where "i" is the start index
        if list[i] != list[min_val_index]:
            list[i], list[min_val_index] = list[min_val_index], list[i]

    return list


unsorted_list = [77, 2, 88, 22, 1, 29, 0, 77, 21, 0, 1, 22]
print(Selection_Sort(unsorted_list))
