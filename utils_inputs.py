"""This script contains utility functions for program."""


def get_user_mode():
  """This function prompts the user for which mode to run the program in."""

  while True:
    print('Choose A Mode, The Options Are:')
    print('(F) Sort an Individual File, (D) Sort All Directory Files')
    print('(M) Manually Enter An array, or (Q) to Quit.')
    print()
    mode = input('Enter F, D, M, or Q: ')
    print()
    mode = mode.upper()
    if mode == 'F':
      print('You chose to sort an individual file.')
      print()
      return mode
    elif mode == 'D':
      print('You chose to sort the directory of files.')
      print()
      return mode
    elif mode == 'M':
      print('You chose to manually enter an array.')
      print()
      return mode
    elif mode == 'Q':
      print('You chose to quit.')
      return mode
    else:
      print('Invalid input.')
      print()
      continue


def get_file_version_size() -> tuple:
  """This function prompts the user for which file version and size to sort."""

  while True:
    print("There are 3 data orders and 5 file sizes to sort choose from.")
    print()
    print('First, choose a data order (Enter 1, 2, or 3):')
    data_order = input('(1) Ascending, (2) Descending, (3) Random: ')
    print()
    if data_order == '1':
      print('You chose Ascending.')
      print()
      break
    elif data_order == '2':
      print('You chose Descending.')
      print()
      break
    elif data_order == '3':
      print('You chose Random.')
      print()
      break
    else:
      print('Invalid input.')
      print()
      continue

  while True:
    print('Next, choose a file size in integers (Enter A, B, C, D, or E):')
    file_size = input('(A) 50, (B) 1000, (C) 2000, (D) 5000, (E) 10000: ')
    file_size = file_size.upper()
    if file_size == 'A':
      print('You chose 50.')
      file_size = 50
      break
    elif file_size == 'B':
      print('You chose 1000.')
      file_size = 1000
      break
    elif file_size == 'C':
      print('You chose 2000.')
      file_size = 2000
      break
    elif file_size == 'D':
      print('You chose 5000.')
      file_size = 5000
      break
    elif file_size == 'E':
      print('You chose 10000.')
      file_size = 10000
      break
    else:
      print('Invalid input.')
      print()
      continue
  
  return data_order, file_size


def get_file_name(data_order: int, file_size: int) -> str:
  """This function returns the file name to sort.
  Input: data_order, file_size (from get_file_version_size)
  Output: file_name"""

  if data_order == '1':
    filename = 'ascending_' + str(file_size) + '.txt'
  elif data_order == '2':
    filename = 'descending_' + str(file_size) + '.txt'
  elif data_order == '3':
    filename = 'random_' + str(file_size) + '.txt'
  else:
    print('Invalid Inputs.')
    return None
  return filename
  

# function to read a file into an array
def read_file(file_name: str) -> list:
  """This function reads a file and returns an array of integers from the file."""

  with open(file_name, 'r') as f:
    array = f.readlines()
    array = [int(i) for i in array]
  return array
