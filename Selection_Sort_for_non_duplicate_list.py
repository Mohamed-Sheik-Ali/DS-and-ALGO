def Selection_Sort(list):
    for i in range(len(unsorted_list)):

        min_val = min(list[i:])
        min_val_index = list.index(min_val)
        list[i], list[min_val_index] = list[min_val_index], list[i]

    return list


unsorted_list = [77, 2, 88, 22, 1, 29, 0]
print(Selection_Sort(unsorted_list))
