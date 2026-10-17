def bubble_sort(list_to_sort):
    for outer_index in range(len(list_to_sort)):
        for inner_index in range( len(list_to_sort) - 1, 0, -1):
            if list_to_sort[inner_index] > list_to_sort[inner_index - 1]:
                list_to_sort[inner_index], list_to_sort[inner_index - 1] = list_to_sort[inner_index - 1], list_to_sort[inner_index]
    return list_to_sort
my_list = [5, 2, 9, 1, 5, 6]
bubble_sort(my_list)
print(my_list)