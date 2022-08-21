"""This script contains the quicksort algorithm versions."""

from partition_types import insertion_sort, partition_left, partition_median

# quicksort_type1 is the default version of the quicksort algorithm and partitions any size array
# quicksort_type2 uses insertion sort to finish arrays <= 100 elements
# quicksort_type3 uses insertion sort to finish arrays <= 50 elements
# quicksort_type4 uses the median of the first, middle, and last elements as the pivot, and partitions any size array

def quicksort_type1(array: list) -> tuple:
  """This is the quicksort algorithm (Type 1) and uses the first item as the pivot.
  This is the default version of the quicksort algorithm and partitions any size array.
  Input: array
  Output: array, comparison_count, swap_count"""

  stack = [] # stack of (leftindex, rightindex) tuples
  comparison_count = 0
  swap_count = 0

  stack.append((0, len(array) - 1)) # push the first (leftindex, rightindex) tuple onto the stack
  while len(stack) > 0: # while the stack is not empty
    leftindex, rightindex = stack.pop() # pop the (leftindex, rightindex) tuple from the stack
    if leftindex < rightindex: # if the leftindex is less than the rightindex
      pivot_index, child_comp_count, child_swap_count = partition_left(array, leftindex, rightindex) # partition the array
      comparison_count += child_comp_count # add the comparison count from partitioning
      swap_count += child_swap_count # add the swap count from partitioning
      
      stack.append((leftindex, pivot_index)) # push the (leftindex, pivot_index) tuple onto the stack
      stack.append((pivot_index + 1, rightindex)) # push the (pivot_index + 1, rightindex) tuple onto the stack
    
    else: # if the leftindex is equal to the rightindex
      continue # do nothing

  return array, comparison_count, swap_count


def quicksort_type2(array: list) -> tuple:
  """This is the quicksort algorithm (Type 2) where insertion sort is used to finish arrays <= 100 elements.
  Input: array
  Output: array, comparison_count, swap_count"""

  stack = [] # stack of (leftindex, rightindex) tuples
  comparison_count = 0
  swap_count = 0

  stack.append((0, len(array) - 1)) # push the first (leftindex, rightindex) tuple onto the stack
  while len(stack) > 0: # while the stack is not empty
    leftindex, rightindex = stack.pop() # pop the (leftindex, rightindex) tuple from the stack
    if leftindex < rightindex: # if the leftindex is less than the rightindex
      if rightindex - leftindex <= 100:
        array, child_comp_count, child_swap_count = insertion_sort(array, leftindex, rightindex)
        comparison_count += child_comp_count # add the comparison count from partitioning
        swap_count += child_swap_count # add the swap count from partitioning
      else:
        pivot_index, child_comp_count, child_swap_count = partition_left(array, leftindex, rightindex) # partition the array
        comparison_count += child_comp_count # add the comparison count from partitioning
        swap_count += child_swap_count # add the swap count from partitioning
        stack.append((leftindex, pivot_index)) # push the (leftindex, pivot_index) tuple onto the stack
        stack.append((pivot_index + 1, rightindex)) # push the (pivot_index + 1, rightindex) tuple onto the stack
    
    else: # if the leftindex is equal to the rightindex
      continue # do nothing

  return array, comparison_count, swap_count


def quicksort_type3(array: list) -> tuple:
  """This is the quicksort algorithm (Type 3) where insertion sort is used to finish arrays <= 50 elements.
  Input: array
  Output: array, comparison_count, swap_count"""

  stack = [] # stack of (leftindex, rightindex) tuples
  comparison_count = 0
  swap_count = 0

  stack.append((0, len(array) - 1)) # push the first (leftindex, rightindex) tuple onto the stack
  while len(stack) > 0: # while the stack is not empty
    leftindex, rightindex = stack.pop() # pop the (leftindex, rightindex) tuple from the stack
    if leftindex < rightindex: # if the leftindex is less than the rightindex
      if rightindex - leftindex <= 50:
        array, child_comp_count, child_swap_count = insertion_sort(array, leftindex, rightindex)
        comparison_count += child_comp_count # add the comparison count from partitioning
        swap_count += child_swap_count # add the swap count from partitioning
      else:
        pivot_index, child_comp_count, child_swap_count = partition_left(array, leftindex, rightindex) # partition the array
        comparison_count += child_comp_count # add the comparison count from partitioning
        swap_count += child_swap_count # add the swap count from partitioning
        stack.append((leftindex, pivot_index)) # push the (leftindex, pivot_index) tuple onto the stack
        stack.append((pivot_index + 1, rightindex)) # push the (pivot_index + 1, rightindex) tuple onto the stack
    
    else: # if the leftindex is equal to the rightindex
      continue # do nothing

  return array, comparison_count, swap_count


def quicksort_type4(array: list) -> tuple:
  """This is the quicksort algorithm (Type 4) and uses the median of the first, middle, and last items as the pivot.
  Input: array
  Output: array, comparison_count, swap_count"""

  stack = [] # stack of (leftindex, rightindex) tuples
  comparison_count = 0
  swap_count = 0

  stack.append((0, len(array) - 1)) # push the first (leftindex, rightindex) tuple onto the stack
  while len(stack) > 0: # while the stack is not empty
    leftindex, rightindex = stack.pop() # pop the (leftindex, rightindex) tuple from the stack
    if leftindex < rightindex: # if the leftindex is less than the rightindex
      pivot_index, child_comp_count, child_swap_count = partition_median(array, leftindex, rightindex) # partition the array
      comparison_count += child_comp_count # add the comparison count from partitioning
      swap_count += child_swap_count # add the swap count from partitioning
      stack.append((leftindex, pivot_index)) # push the (leftindex, pivot_index) tuple onto the stack
      stack.append((pivot_index + 1, rightindex)) # push the (pivot_index + 1, rightindex) tuple onto the stack
    
    else: # if the leftindex is equal to the rightindex
      continue # do nothing

  return array, comparison_count, swap_count
