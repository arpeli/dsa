# By Derrick Mburu
#Implementation of the Quick Sort algorithm using the "Divide and Conquer" strategy

def quick_sort(arr):
    # BASE CASE: If the list has 0 or 1 elements, it is already "sorted"
    # This stops the recursion from running forever.
    if len(arr) <= 1:
        return arr

    # DIVIDE: Choose a 'pivot' element to compare others against.
    # Here, we are picking the middle element of the current array.
    pivot_index = len(arr) // 2
    pivot_value = arr[pivot_index]

    # CONQUER (Partitioning): Group elements based on their relationship to the pivot.
    smaller_elements = []  # Elements strictly less than the pivot
    equal_elements = []    # Elements equal to the pivot (handles duplicates)
    larger_elements = []   # Elements strictly greater than the pivot

    for element in arr:
        if element < pivot_value:
            smaller_elements.append(element)
        elif element == pivot_value:
            equal_elements.append(element)
        else:
            larger_elements.append(element)

    # RECURSION: Apply the same logic to the 'smaller' and 'larger' sub-lists.
    # This continues breaking the problem down into smaller chunks.
    sorted_left_side = quick_sort(smaller_elements)
    sorted_right_side = quick_sort(larger_elements)

    # COMBINE: Join the sorted parts back together in order.
    # The pivot(s) go in the middle.
    full_sorted_list = sorted_left_side + equal_elements + sorted_right_side
    
    return full_sorted_list

# --- Testing the code ---
test_array = [82, 45, 12, 9, 104, 27, 45, 1, 63]
result = quick_sort(test_array)

# Output the final result
print(f"Original: {test_array}")
print(f"Sorted:   {result}")
