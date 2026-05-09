def merge_sorted_arrays(arr1, arr2):
    # So the trick why python solution is easy because we are using extra memory
    i, j = 0, 0
    merged_array = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    # If there are remaining elements in arr1, add them to the merged array
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    
    # If there are remaining elements in arr2, add them to the merged array
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    
    return merged_array

print(merge_sorted_arrays([1, 3, 100, 200], [2, 4, 6, 8]))
