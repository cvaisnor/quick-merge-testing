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


def write_to_file(file_name: str, array: list, sorting_function) -> None:
  """This function writes the sorted array to a file in the output directory. 
  It is only used for files up to 50 elements.
  Input: file_name, sorted array, sorting_function.
  Output: None"""

  # make output directory if it doesn't exist
  import os
  if not os.path.exists('output_files'):
    os.makedirs('output_files')

  # remove the .txt from the file_name 
  file_name = file_name.split('.')[0]
  
  # add the sorting function to the file name
  file_name = file_name + '_sorted_with_' + sorting_function.__name__ + '.txt'

  with open('output_files/' + file_name, 'w') as file:
    for element in array:
      file.write(str(element) + '\n')
  
  return