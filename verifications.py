"""This script contains the verification functions for the algorithms."""


def verify_sorted(array: list, comparison_count, swap_count):
  """This function verifies that the array is sorted in ascending order. """

  sorted = True

  for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
      sorted = False
      break
    else:
      sorted = True

  if sorted:
    print("Comparison count: ", comparison_count)
    print("Swap count: ", swap_count)
    print()
    
  else:
    print('Error: the array is not sorted.')


def verify_sorted_file(filename: str) -> bool:
  """This function verifies that the file is sorted in ascending order. 
  Input: filename
  Output: True if sorted, False if not sorted"""

  list = []

  with open(filename, 'r') as file:
    array = file.readlines()
    for i in range(len(array) - 1):
      list.append(int(array[i]))

  return verify_sorted(list)