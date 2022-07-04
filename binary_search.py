def binary_search(sorted_list, item):

    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        mid_position = (start + end) // 2
        mid_value = sorted_list[mid_position]

        if mid_value == item:
            return mid_position
        if mid_value < item:
            start = mid_position + 1
        if mid_value > item:
            end = mid_position - 1
            
    return None

some_sorted_list = [1, 5, 9, 13, 17, 21]
print(binary_search(some_sorted_list, 21))
