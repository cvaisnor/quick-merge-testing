"""This is the main module for Lab 4."""

# Lab 4: Sorting Methods Testing
# Programmer: Chris Vaisnor
# IDE: VS Code
# Python Version: 3.8.10

from sorting_functions import *

def main():
  """This is the main function for the program."""

  # array of random numbers
  array = [5,7,2,9,1,3,4,6,8]
  start=0
  end=len(array)-1


  # partition the array around the pivot
  pivot = partition_v1(array, start, end)


if __name__ == '__main__':
  print("This is the main module for Lab 4.")
  print('Programmer: Chris Vaisnor')
  print('IDE: VS Code')
  print('Python Version: 3.8.10')
  print()
  print('------------------------------------------------------------')

  main()