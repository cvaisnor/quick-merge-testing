"""This script contains the Merge Algoritm. This is an iterative and linked-list based implementation."""


def merge(array, left_index, middle_index, right_index) -> list:
  """This function merges two arrays into one.
  Input: array, left_index, middle_index, right_index
  Output: merged array"""
  
  comparison_count = 0

  merged_array = []
 
  # initialize the pointers for the two arrays
  pointer_1 = left_index
  pointer_2 = middle_index + 1
 
  # loop until one of the arrays is empty
  while pointer_1 <= middle_index and pointer_2 <= right_index:
    comparison_count += 1
    if array[pointer_1] < array[pointer_2]:
      merged_array.append(array[pointer_1])
      pointer_1 += 1
    else:
      merged_array.append(array[pointer_2])
      pointer_2 += 1
 
  # add the remaining elements of the array
  while pointer_1 <= middle_index:
    merged_array.append(array[pointer_1])
    pointer_1 += 1
  
  while pointer_2 <= right_index:
    merged_array.append(array[pointer_2])
    pointer_2 += 1

  # return the merged array
  return merged_array, comparison_count


def merge_sort(array: list) -> list:
  """This function sorts an array using the natural merge algorithm.
  This is an iterative implementation of the merge sort algorithm."""

  comparison_count = 0
  swap_count = 0
  k = 1

  while k < len(array):
    for i in range(0, len(array), k*2):
      
      left_index, middle_index, right_index = i, min(i+k-1, len(array)-1), min(i+2*k-1, len(array)-1)

      # merge the subarrays into one array
      merged_array, merged_comparison_count = merge(array, left_index, middle_index, right_index)
      comparison_count += merged_comparison_count

      # copy the merged array into the original array
      for j in range(len(merged_array)):
        array[left_index+j] = merged_array[j]
        swap_count += 1

    k *= 2

  return array, comparison_count, swap_count
  
