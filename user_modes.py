"""This script contains the modes for the program."""

from traceback import print_tb
from quicksort_types import quicksort_type1, quicksort_type2, quicksort_type3, quicksort_type4
from verifications import verify_sorted
from utils_inputs import get_file_version_size, get_file_name, read_file

def manual_input_mode():
  """This function prompts the user for an array to sort."""

  user_input = input('Enter an array of integers separated by spaces: ')
  print()
  user_input = user_input.split() # split the string into a list of strings
  unsorted_input = [int(i) for i in user_input] # list comprehension, convert string to int

  # sort the array using each of the sorting algorithms
  list_sorting_function = [quicksort_type1, quicksort_type2, quicksort_type3, quicksort_type4]
  
  for sorting_function in list_sorting_function:
    sorted_array, comparison_count, swap_count = sorting_function(unsorted_input)
    print(f'{sorting_function.__name__}')
    verify_sorted(sorted_array, comparison_count, swap_count)

  print('The sorted array is:', sorted_array)
  print()
  return


def sort_file_mode():
  """This function prompts the user for a file to sort."""

  # prompt the user for the file version and size
  data_order, file_size = get_file_version_size() # (Ascending, Decending, Random), (50, 1000, 2000, 5000, 10000)
  file_name = get_file_name(data_order, file_size)
  
  # read the file into an array
  array_from_file = read_file(file_name)

  if len(array_from_file) <=50:
    print('The array is:', array_from_file)

  # sort the array using each of the sorting algorithms
  list_sorting_function = [quicksort_type1, quicksort_type2, quicksort_type3, quicksort_type4]
  
  for sorting_function in list_sorting_function:
    sorted_array, comparison_count, swap_count = sorting_function(array_from_file)
    print(f'{sorting_function.__name__}')
    verify_sorted(sorted_array, comparison_count, swap_count)
  
  if len(sorted_array) <= 50:
    print('The sorted array is:', sorted_array)
    print()

  return