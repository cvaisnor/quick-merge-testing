"""This is the main module for Lab 4."""

# Lab 4: Sorting Methods Testing
# Programmer: Chris Vaisnor
# IDE: VS Code
# Python Version: 3.8.10

from partition_types import partition_left
from quicksort_types import quicksort_first
from utils import verify_sorted

def main():
  """This is the main function for the program."""

  # array of random numbers
  array = [1,7,2,5,9,3,4,6,8]
  left=0
  right=len(array)-1

  # print original array
  print("Original array:", array)

  # quick sort the array using the first item as the pivot
  sorted_array = quicksort_first(array, left, right)

  # print the sorted array
  print('Sorted Array:', sorted_array)

  # verify the array is sorted
  sorted = verify_sorted(sorted_array)

  if sorted:
    print("The array is sorted.")
  else:
    print("The array is not sorted.")


if __name__ == '__main__':
  print("This is the main module for Lab 4.")
  print('Programmer: Chris Vaisnor')
  print('IDE: VS Code')
  print('Python Version: 3.8.10')
  print()
  print('------------------------------------------------------------')

  main()