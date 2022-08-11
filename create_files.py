"""This script creates the input files for the sorting algorithms.
The 15 files are defined as follows:

    5 size files: 50, 1000, 2000, 5000, and 10000 integers.
    3 versions per file: random, decending, and ascending.

    Total of 15 files."""

from random import randint, shuffle


def create_file(filename: str, size: int, ascending: bool, random: bool) -> None:
  """This function creates a file with the given parameters."""

  with open(filename, 'w') as file:
    if random:
      array = list(range(size))
      shuffle(array)
      for i in range(len(array)):
        if i == size - 1:
          file.write(str(array[i]))
        else:
          file.write(str(array[i]) + '\n')
    elif ascending:
      for i in range(size):
        if i == size - 1:
          file.write(str(i))
        else:
          file.write(str(i) + '\n')
    else:
      for i in range(size):
        if i == size - 1:
          file.write(str(size - i))
        else:
          file.write(str(size - i) + '\n')
      

def create_files() -> None:
  for size in [50, 1000, 2000, 5000, 10000]:
    create_file('random_' + str(size) + '.txt', size, True, True)
    create_file('descending_' + str(size) + '.txt', size, False, False)
    create_file('ascending_' + str(size) + '.txt', size, True, False)


def check_for_duplicates_in_file(filename: str) -> bool:
  """This function checks for duplicates in a file."""

  with open(filename, 'r') as file:
    array = file.readlines()
    for i in range(len(array)):
      for j in range(i + 1, len(array)):
        if array[i] == array[j]:
          return True
  return False


def make_files_with_duplicates():
  for size in [50, 1000, 2000, 5000, 10000]:
    with open('test_random_' + str(size) + '.txt', 'w') as file:
      for i in range(size):
        file.write(str(randint(0, size)) + '\n')


# checking for duplicates in the test files
for size in [50, 1000, 2000, 5000, 10000]:
  if check_for_duplicates_in_file('test_random_' + str(size) + '.txt'):
    print('test_random_' + str(size) + '.txt has duplicates')
  else:
    print('test_random_' + str(size) + '.txt has no duplicates')

# checking for duplicates in all other 'random' files
for size in [50, 1000, 2000, 5000, 10000]:
  if check_for_duplicates_in_file('random_' + str(size) + '.txt'):
    print('random_' + str(size) + '.txt has duplicates')
  else:
    print('random_' + str(size) + '.txt has no duplicates')

