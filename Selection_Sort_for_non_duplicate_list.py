unsorted_list = [77, 2, 88, 22, 1, 29, 0]

for i in range(len(unsorted_list)):

    min_val = min(unsorted_list[i:])
    min_val_index = unsorted_list.index(min_val)
    unsorted_list[i], unsorted_list[min_val_index] = unsorted_list[min_val_index], unsorted_list[i]

print(unsorted_list)
