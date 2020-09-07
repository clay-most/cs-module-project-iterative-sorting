def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0 
    end = (len(arr)-1)
    
    while end >= start:
        middle = start + end //2
        if arr[middle] == target:
            return middle
        else:
            if arr[middle] > target:
                end = middle - 1
            if arr[middle] < target:
                start = middle + 1


    return -1  # not found
