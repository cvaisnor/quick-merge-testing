"""This script contains utility functions for program."""


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