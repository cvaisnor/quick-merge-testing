"""This script contains the merge sort algorithm versions."""


def natural_merge_sort(array: list, start: int, end: int) -> None:
  """This function sorts the array using the natural merge sort algorithm. This uses a linked implementation."""

  # base case
  if start == end:
    return
  
  # recursive case
  else:
    mid = (start + end) // 2
    natural_merge_sort(array, start, mid)
    natural_merge_sort(array, mid + 1, end)
    merge(array, start, mid, end)


def merge(array: list, start: int, mid: int, end: int) -> None:
  """This function merges the two partitions of the array."""

  # create temporary arrays
  left = array[start:mid + 1]
  right = array[mid + 1:end + 1]

  # merge the temporary arrays
  i = 0
  j = 0
  k = start
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      array[k] = left[i]
      i += 1
    else:
      array[k] = right[j]
      j += 1
    k += 1

  # copy the remaining items from the temporary arrays
  while i < len(left):
    array[k] = left[i]
    i += 1
    k += 1
  while j < len(right):
    array[k] = right[j]
    j += 1
    k += 1


def merge_sort(array: list, start: int, end: int) -> None:
    """This function sorts the array using the merge sort algorithm. This uses a linked implementation."""

    # base case
    if start == end:
      return
    
    # recursive case
    else:
      mid = (start + end) // 2
      merge_sort(array, start, mid)
      merge_sort(array, mid + 1, end)
      merge(array, start, mid, end)