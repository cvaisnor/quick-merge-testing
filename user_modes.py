"""This script contains the modes for the program."""

from quicksort_types import quicksort_type1, quicksort_type2, quicksort_type3, quicksort_type4
from verifications import verify_sorted
from utils_inputs import get_file_version_size, get_file_name, read_file

def manual_input_mode():
  """This function prompts the user for an array to sort."""

  user_input = input('Enter an array of integers separated by spaces: ')
  print()
  user_input = user_input.split() # split the string into a list of strings
  unsorted_input = [int(i) for i in user_input] # list comprehension, convert string to int
  print('The unsorted array is:', unsorted_input)

  # sort the array  
  sorted_input, comparison_count, swap_count = quicksort_type1(unsorted_input)
  
  verify = verify_sorted(sorted_input)
  if verify:
    print('The sorted array is:', sorted_input)
    print('The number of comparisons is:', comparison_count)
    print('The number of swaps is:', swap_count)
    print()
  else:
    print('The array is not sorted.')
    print()
  return


def sort_file_mode():
  """This function prompts the user for a file to sort."""

  # prompt the user for the file version and size
  data_order, file_size = get_file_version_size() # (1: Ascending, 2: Decending, 3: Random), (50, 1000, 2000, 5000, 10000)
  file_name = get_file_name(data_order, file_size)
  
  # read the file into an array
  array_from_file = read_file(file_name)

  # sort the array
  sorted_array, comparison_count, swap_count = quicksort_type1(array_from_file)
  
  verify_sorted(sorted_array) # verify the array is sorted
  if verify_sorted(sorted_array):
    print('The array is sorted.')
    print('The number of comparisons is:', comparison_count)
    print('The number of swaps is:', swap_count)
    if len(sorted_array) <= 50:
      print('The sorted array is:', sorted_array)
    print()
  else:
    print('The array is not sorted.')
    print()
  return