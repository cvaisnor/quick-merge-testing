"""This is the script containing the sorting functions."""


def verify_sorted(array: list) -> bool:
  """This function verifies that the array is sorted in ascending order."""

  for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
      return False
  return True


def verify_sorted_file(filename: str) -> bool:
  """This function verifies that the file is sorted in ascending order."""

  list = []

  with open(filename, 'r') as file:
    array = file.readlines()
    for i in range(len(array) - 1):
      list.append(int(array[i]))

  return verify_sorted(list)


# partition the array, and return the index of the pivot
def partition(array: list, start: int, end: int) -> int:
  """This function partitions the array around the pivot. The pivot is selected as the first item of each partition."""
  
  pivot = array[start]
  
  print('The array is:', array)
  print('The pivot value is:', pivot)
  print()

  done = False
  
  # iterate through the array and move items that are less than the pivot to the left of 
  # the pivot and the items that are greater than the pivot to the right of the pivot
  while (not done):
    for i in range(start, end + 1):
      if array[i] < pivot:
        
        # swap the pivot with the start index
        array[start], array[end] = array[end], array[start]
        start += 1
        break
      
      elif pivot < array[end]:
        end -= 1

    if start == end:
      done = True

  # print the array
  print('The array after partition is:', array)
  
  return start


def partition_v1(array: list, start: int, end: int) -> int:
  """V1: This function partitions the array around the pivot. The pivot is selected as the first item
  of each partition."""
  
  print('The array is:', array)

  pivot = array[start]
  print('The pivot value is:', pivot)
  print()
  
  done = False

  swap_postion = start
  
  # iterate through the array and moves the items that are less than the pivot to the left of the pivot
  # and the items that are greater than the pivot to the right of the pivot
  while(not done):
    for i in range(start + 1, end + 1):
      if array[i] < pivot:
        array[i], array[swap_postion] = array[swap_postion], array[i]
        swap_postion += 1
      else:
        pass
    if swap_postion == end:
      done = True

  # print the array
  print('The array after partition is:', array)

  # return the index of the pivot
  return start


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


def quicksort_v1(array: list) -> list:
  """This function performs the quicksort algorithm. Verison 1: pivot is the first element."""
  
  pivot = array[0] # select the first element as the pivot
  pass