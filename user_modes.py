"""This script contains the modes for the program."""


from quicksort_types import quicksort_type1, quicksort_type2, quicksort_type3, quicksort_type4
from verifications import verify_sorted, write_to_file
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

  # print the file name
  print(f'Sorting {file_name}')
  print()

  # sort the array using each of the sorting algorithms
  list_sorting_function = [quicksort_type1, quicksort_type2, quicksort_type3, quicksort_type4]
  
  for sorting_function in list_sorting_function:
    sorted_array, comparison_count, swap_count = sorting_function(array_from_file)
    print(f'{sorting_function.__name__}')
    verify_sorted(sorted_array, comparison_count, swap_count)
    write_to_file(file_name, sorted_array, sorting_function) # write to file
      
  if len(sorted_array) <= 50: # only print the array if it is less than 50 elements
    print('The input array is:', array_from_file)
    print()
    print('The sorted array is:', sorted_array)
    print()
  return


def sort_filenames(file_name: str) -> tuple:
  """This function parses the file name.
  Input: file_name
  Output: tuple (order, size)"""

  if file_name.endswith('.txt'): # only sort text files
    order, size = file_name.split('_') # split the file name into a list of strings
    size = size.split('.')[0] # get the file size from the file name
    return order, int(size)
  
  else:
    return ('', 0)


def sort_directory_mode():
  """This function sorts all the text files in the input directory and prints to console.
  If the file is less than 50 elements, it is also written to a file in output directory."""
  import os

  # open input directory
  input_directory = os.path.join(os.getcwd(), 'input_files')

  file_names = os.listdir(input_directory) # get the list of files in the input directory
  file_names.sort(key=sort_filenames) # sort the list of files by the file name

  for file_name in file_names: # loop through all the files in the input directory
    
    if file_name.endswith('.txt'): # only sort text files

      print(f'Sorting {file_name}')
      print()

      array_from_file = read_file(file_name) # read the file into an array
  
      # sort the array using each of the sorting algorithms
      list_sorting_function = [quicksort_type1, quicksort_type2, quicksort_type3, quicksort_type4]

      for sorting_function in list_sorting_function:
        sorted_array, comparison_count, swap_count = sorting_function(array_from_file)
        print(f'{sorting_function.__name__}')
        verify_sorted(sorted_array, comparison_count, swap_count)
        write_to_file(file_name, sorted_array, sorting_function) # write to file
        
      if len(sorted_array) <= 50:
        print('The input array is:', array_from_file)
        print()
        print('The sorted array is: ', sorted_array)
        print()
        
      print('Moving to next file...')
      print('------------------------------------------------------')
      print()
  return