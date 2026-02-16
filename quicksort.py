# By Derrick Mburu
# Implementation of the Quick Sort Algorithm using the "Divide and Conquer" strategy
# Quick Sort: O(n log n) average case, O(n²) worst case, in-place sorting

def quick_sort(arr):
    """
    Sorts a list using the Quick Sort algorithm.
    Time Complexity: Average O(n log n), Worst O(n^2).
    Space Complexity: O(n) due to the creation of new sub-lists.
    """
    
    # BASE CASE: A list with 0 or 1 elements is sorted by definition.
    # This acts as the "exit condition" for our recursive calls.
    if len(arr) <= 1:
        return arr

    # DIVIDE: Select a 'pivot' value to serve as the benchmark for comparison.
    # Choosing the middle element (index len//2) helps maintain efficiency 
    # even if the input list is already partially sorted.
    pivot_index = len(arr) // 2
    pivot_value = arr[pivot_index]

    # CONQUER (Partitioning): Categorize all elements based on the pivot.
    # This "Three-Way Partition" naturally handles duplicate values by 
    # isolating them in 'equal_elements' so they don't need further sorting.
    smaller_elements = []  # Values mathematically less than the pivot
    equal_elements = []    # Values identical to the pivot (handles duplicates)
    larger_elements = []   # Values mathematically greater than the pivot

    for element in arr:
        if element < pivot_value:
            smaller_elements.append(element)
        elif element == pivot_value:
            equal_elements.append(element)
        else:
            larger_elements.append(element)

    # RECURSION: Independently sort the smaller and larger sub-problems.
    # We do NOT recurse on 'equal_elements' because they are already 
    # in their final sorted position relative to the other two groups.
    sorted_left_side = quick_sort(smaller_elements)
    sorted_right_side = quick_sort(larger_elements)

    # COMBINE: Reassemble the three segments into a single sorted list.
    # Order matters: [Smaller] -> [Equal/Pivot] -> [Larger]
    full_sorted_list = sorted_left_side + equal_elements + sorted_right_side
    
    return full_sorted_list

# --- Execution Logic ---
test_array = [82, 45, 12, 9, 104, 27, 45, 1, 63]
result = quick_sort(test_array)

# Display results for verification
print(f"Original: {test_array}")
print(f"Sorted:   {result}")