def quicksort_first_recursive(array: list, leftindex: int, rightindex: int) -> tuple:
  """This is the quicksort algorithm (Type 1) and uses the first item as the pivot.
  This is the recursive implementation of the algorithm.
  Input: array, leftindex, rightindex
  Output: sorted array"""

  comparison_count = 0
  swap_count = 0
  
  if leftindex < rightindex:
    pivot_index, child_comp_count, child_swap_count = partition_left(array, leftindex, rightindex)
    comparison_count += child_comp_count
    swap_count += child_swap_count
    
    _, comp_count_left, swap_count_left = quicksort_first_recursive(array, leftindex, pivot_index) # recursive call on the left partition
    comparison_count += comp_count_left # add the comparison count from the left partition
    swap_count += swap_count_left # add the swap count from the left partition
    
    _, comp_count_right, swap_count_right = quicksort_first_recursive(array, pivot_index + 1, rightindex) # recursive call on the right partition
    comparison_count += comp_count_right # add the comparison count from the right partition
    swap_count += swap_count_right # add the swap count from the right partition

  return array, comparison_count, swap_count


def quicksort_median_recursive(array, leftindex, rightindex):
  """This is the quicksort algorithm (Type 3) and uses the median-of-three as the pivot.
  This is the recursive implementation of the algorithm."""

  if leftindex < rightindex:
    newpivotindex = partition_median(array, leftindex, rightindex)
    quicksort_median(array, leftindex, newpivotindex) # recursive call on the left partition
    quicksort_median(array, newpivotindex + 1, rightindex) # recursive call on the right partition
  
  return array