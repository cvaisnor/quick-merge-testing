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

  k = 1

  while k < len(array):
    
    # divide the array into k-sized subarrays
    subarrays = []
    for i in range(0, len(array), k):
      print('i: ', i)
      subarrays.append(array[i:i+k])
      print('subarrays: ', subarrays)
  
    # merge the subarrays
    array = []
    for subarray in subarrays:
      print('subarray to merge: ', subarray)
      array = merge(array, subarray)
    
    k *= 2
    print('k: ', k)
  
  return array
