"""This is the main module for Lab 4."""

# Lab 4: Sorting Methods Testing
# Programmer: Chris Vaisnor
# IDE: VS Code
# Python Version: 3.8.10

def main():
  
  # Verification function for the sorted files
  def verify_sorted(array: list) -> bool:
    """This function verifies that the array is sorted in ascending order."""

    for i in range(len(array) - 1):
      if array[i] < array[i + 1]:
        return False
    return True

  # partition the array, and return the index of the pivot
  def partition(array: list, start: int, end: int) -> int:
    """This function partitions the array around the pivot. The pivot is selected as the first item of each partition."""
      
    pivot = array[start]

 
    done = False
    
    # iterate through the array and swap items if they are less than the pivot
    while (not done):
      for i in range(start, end + 1):
        if array[i] < pivot:
          start += 1
          break
        else:
          pivot < array[end]
          end -= 1

    # swap the pivot with the start index
    array[start], array[end] = array[end], array[start]
    
    return start


  def quicksort_v1(array: list) -> list:
    """This function performs the quicksort algorithm. Verison 1: pivot is the first element."""
    
    pivot = array[0] # select the first element as the pivot
    pass


if __name__ == '__main__':
  print("This is the main module for Lab 4.")
  print('Programmer: Chris Vaisnor')
  print('IDE: VS Code')
  print('Python Version: 3.8.10')

  main()