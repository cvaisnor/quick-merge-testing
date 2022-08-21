"""This is the script containing the partitioning functions."""


def partition_left(array: list, left_index: int, right_index: int) -> tuple:
  """(Type 1) The pivot is selected as the first item of each partition.
  Input: array, left_index, right_index
  Output: new pivot index"""

  comparison_count = 0
  swap_count = 0

  pivot = array[left_index]

  i = left_index + 1
  for j in range(left_index + 1, right_index + 1):
    # keep track of comparisons
    comparison_count += 1

    if array[j] < pivot:
      # keep track of swaps
      swap_count += 1
      array[i], array[j] = array[j], array[i]
      i += 1

  array[left_index], array[i - 1] = array[i - 1], array[left_index]
  swap_count += 1

  pivot_index = i - 1

  return pivot_index, comparison_count, swap_count


def insertion_sort(array: list, left_index: int, right_index: int) -> tuple:
  """This function sorts the array using the insertion sort algorithm.
  This is only used for the quicksort algorithm Type 2 and Type 3."""
  
  comparison_count = 0
  swap_count = 0
  
  for i in range(left_index + 1, right_index + 1):
    j = i
    while j > left_index:
      # keep track of comparisons
      comparison_count += 1
      
      if array[j] < array[j-1]:
        swap_count += 1
        # swap the values
        array[j], array[j-1] = array[j-1], array[j]
        j -= 1
      else:
        break

  return array, comparison_count, swap_count

# ----------------------------------------------------------------------------------------------------------------------

def get_median(a: int, b: int, c: int) -> int:
  """This function returns the median of three values. Used in the partition_median function."""
  
  if (a - b) * (c - a) >= 0:
    return a

  elif (b - a) * (c - b) >= 0:
    return b

  else:
    return c


def partition_median(array: list, left_index: int, right_index: int) -> tuple:
  """(Type 4) This function partitions the array using the median-of-three as the pivot."""
  
  comparison_count = 0
  swap_count = 0

  middle = (left_index + right_index) // 2

  pivot = get_median(array[left_index], array[right_index], array[middle])

  pivot_index = array.index(pivot) # get the index of the pivot

  array[pivot_index] = array[left_index]
  array[left_index] = pivot # swap pivot with first item in array
  swap_count += 1

  i = left_index + 1
  for j in range(left_index + 1, right_index + 1):
    # keep track of comparisons
    comparison_count += 1

    if array[j] < pivot:
      # keep track of swaps
      swap_count += 1
      array[i], array[j] = array[j], array[i]
      i += 1

  array[left_index], array[i - 1] = array[i - 1], array[left_index]
  swap_count += 1

  pivot_index = i - 1

  return pivot_index, comparison_count, swap_count
