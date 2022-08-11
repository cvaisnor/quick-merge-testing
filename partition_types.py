"""This is the script containing the partitioning functions."""


def partition_left(array: list, leftindex: int, rightindex: int) -> tuple:
  """(Type 1) The pivot is selected as the first item of each partition.
  Input: array, leftindex, rightindex
  Output: new pivot index"""

  comparison_count = 0
  swap_count = 0

  pivot = array[leftindex]

  i = leftindex + 1
  for j in range(leftindex + 1, rightindex + 1):
    # keep track of comparisons
    comparison_count += 1

    if array[j] < pivot:
      # keep track of swaps
      swap_count += 1
      array[i], array[j] = array[j], array[i]
      i += 1

  array[leftindex], array[i-1] = array[i-1], array[leftindex]
  swap_count += 1

  pivot_index = i - 1

  return pivot_index, comparison_count, swap_count


def insertion_sort(array: list, leftindex: int, rightindex: int) -> tuple:
  """This function sorts the array using the insertion sort algorithm.
  This is only used for the quicksort algorithm Type 2 and Type 3."""
  
  comparison_count = 0
  swap_count = 0
  
  for i in range(leftindex + 1, rightindex + 1):
    j = i
    while j > leftindex:
      # keep track of comparisons
      comparison_count += 1
      
      if array[j] < array[j-1]:
        # swap the values
        swap_count += 1
        array[j], array[j-1] = array[j-1], array[j]
        j -= 1
      else:
        break

  return array, comparison_count, swap_count











# ----------------------------------------------------------------------------------------------------------------------


def get_median(a: int, b: int, c: int) -> int:
  """This function returns the median of three values. Used in the partition_median function."""
  
  if ( a - b) * (c - a) >= 0:
    return a

  elif (b - a) * (c - b) >= 0:
    return b

  else:
    return c


def partition_median(array: list, left: int, right: int) -> int:
  """(Type 3) This function partitions the array using the median-of-three as the pivot."""
  
  left = array[left]
  right = array[right-1]
  length = right - left
  
  if length % 2 == 0:
    middle = array[left + length/2 - 1]
  else:
    middle = array[left + length/2]

  pivot = get_median(left, right, middle)

  pivotindex = array.index(pivot) #only works if all values in array unique

  array[pivotindex] = array[left]
  array[left] = pivot

  i = left + 1
  for j in range(left + 1, right + 1):
    if array[j] < pivot:
      temp = array[j]
      array[j] = array[i]
      array[i] = temp
      i += 1

  leftendval = array[left]
  array[left] = array[i-1]
  array[i-1] = leftendval
  return i - 1 

