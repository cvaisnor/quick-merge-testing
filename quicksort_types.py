"""This script contains the quicksort algorithm versions."""

from partition_types import partition_left, partition_median


def quicksort_first(array, leftindex, rightindex):
  """This is the quicksort algorithm (Type 1) and uses the first item as the pivot.
  This is the recursive implementation of the algorithm.
  Input: array, leftindex, rightindex
  Output: sorted array"""
  
  if leftindex < rightindex:
    newpivotindex = partition_left(array, leftindex, rightindex)
    quicksort_first(array, leftindex, newpivotindex) # recursive call on the left partition
    quicksort_first(array, newpivotindex + 1, rightindex) # recursive call on the right partition
  
  return array
















# ----------------------------------------------------------------------------------------------------------------------
def quicksort_median(array, leftindex, rightindex):
  """This is the quicksort algorithm (Type 3) and uses the median-of-three as the pivot.
  This is the recursive implementation of the algorithm."""

  if leftindex < rightindex:
    newpivotindex = partition_median(array, leftindex, rightindex)
    quicksort_median(array, leftindex, newpivotindex) # recursive call on the left partition
    quicksort_median(array, newpivotindex + 1, rightindex) # recursive call on the right partition
  
  return array