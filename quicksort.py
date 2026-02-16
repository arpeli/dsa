# By Derrick Mburu
# Implementation of the Quick Sort Algorithm using the "Divide and Conquer" strategy
# Quick Sort: O(n log n) average case, O(n²) worst case, in-place sorting
# this was done to meet assignment requirements and to demonstrate the algorithm's logic clearly.


def quick_sort(arr):
    """
    Sorts a list using the Quick Sort algorithm.
    Note: This specific implementation uses $O(n)$ additional space for sub-lists.
    """
    
    # BASE CASE: A list with 0 or 1 elements is already sorted.
    # This prevents infinite recursion.
    if len(arr) <= 1:
        return arr

    # DIVIDE: Select a pivot value.
    # Using the middle index helps maintain $O(n \log n)$ performance on sorted input.
    pivot_index = len(arr) // 2
    pivot_value = arr[pivot_index]

    # CONQUER (Partitioning): Group elements into three buckets based on the pivot.
    # This "Three-Way Partition" handles duplicate values efficiently.
    smaller_elements = []  # Elements strictly less than the pivot
    equal_elements = []    # Elements equal to the pivot (avoids unnecessary recursion)
    larger_elements = []   # Elements strictly greater than the pivot

    for element in arr:
        if element < pivot_value:
            smaller_elements.append(element)
        elif element == pivot_value:
            equal_elements.append(element)
        else:
            larger_elements.append(element)

    # RECURSION: Recursively sort the smaller and larger partitions.
    # We do not need to sort 'equal_elements' as they are already grouped.
    sorted_left_side = quick_sort(smaller_elements)
    sorted_right_side = quick_sort(larger_elements)

    # COMBINE: Concatenate the results into a single sorted list.
    # Structure: [Sorted Left] + [Pivot/Equals] + [Sorted Right]
    full_sorted_list = sorted_left_side + equal_elements + sorted_right_side
    
    return full_sorted_list

# --- Test Execution ---
test_array = [82, 45, 12, 9, 104, 27, 45, 1, 63]
result = quick_sort(test_array)

# Output results
print(f"Original: {test_array}")
print(f"Sorted:   {result}")