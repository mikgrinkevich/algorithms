def bubble_sort(list):
    swapped = False
    # looping from the last to the first
    for j in range(len(list)-1, 0, -1):
        for i in range(j):
            if list[i] > list[i+1]:
                swapped = True
                list[i], list[i + 1] = list[i + 1], list[i]       
        if not swapped:
            break  
    return list

some_list = [8,1,58,4,8,98,75,24,3,35]
print(bubble_sort(some_list))
