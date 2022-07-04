def find_smallest(list):
    smallest_value = list[0]
    smallest_index = 0
    for i in range(len(list)):
        if list[i] < smallest_value:
            smallest_index = i
            smallest_value = list[i]
    return smallest_index


some_list = [8,1,58,4,8,98,75,24,3,35]
print(find_smallest(some_list))


def selection_sort(list):
    sorted_list = []
    for i in range(len(list)):
        smallest_elem = find_smallest(list)
        sorted_list.append(list.pop(smallest_elem))
    return sorted_list


print(selection_sort(some_list))