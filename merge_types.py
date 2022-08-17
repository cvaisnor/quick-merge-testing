"""This script contains the Merge Algoritm. This is an iterative and linked-list based implementation."""


def merge(array_1: list, array_2: list) -> list:
  """This function merges two arrays into one.
  Input: array_1, array_2
  Output: merged array"""
 
  # initialize the merged array
  merged_array = []
 
  # initialize the pointers for the two arrays
  pointer_1 = 0
  pointer_2 = 0
 
  # loop until one of the arrays is empty
  while pointer_1 < len(array_1) and pointer_2 < len(array_2):
    if array_1[pointer_1] < array_2[pointer_2]:
      merged_array.append(array_1[pointer_1])
      pointer_1 += 1
    else:
      merged_array.append(array_2[pointer_2])
      pointer_2 += 1
 
  # add the remaining elements of the array
  merged_array.extend(array_1[pointer_1:])
  merged_array.extend(array_2[pointer_2:])
 
  return merged_array


def merge_sort(array: list) -> list:
  """This function sorts an array using the natural merge algorithm.
  This is an iterative implementation of the merge sort algorithm."""

  # if the array is empty or has only one element, return the array
  if len(array) <= 1:
    return array

  # initialize the left and right arrays
  left_array = []
  right_array = []

  # loop through the array and split it into two halves
  for i in range(len(array)):
    
    if i < len(array) / 2: 
      left_array.append(array[i])
    else:
      right_array.append(array[i])

  # sort the left and right arrays iteratively
  left_array = merge_sort(left_array)
  right_array = merge_sort(right_array)

  # merge the left and right arrays
  return merge(left_array, right_array)