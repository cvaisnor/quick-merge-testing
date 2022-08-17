"""This is the main module for Lab 4."""

# Lab 4: Sorting Methods Testing
# Programmer: Chris Vaisnor
# IDE: VS Code
# Python Version: 3.8.10


from user_modes import manual_input_mode, sort_file_mode, sort_directory_mode
from utils_inputs import get_user_mode


def main():
  """This is the main function for the program."""

  while True:

    print('Input files must be in input_files folder.')
    print('Output files will be written to output_files folder.')
    print()

    # Get the user's mode
    user_mode = get_user_mode()
    
    if user_mode == 'F': # Sort File --------------------------------------------------------------
      sort_file_mode()
      continue

    elif user_mode == 'D': # Sort Directory (all the files at once, required for lab) -------------
      sort_directory_mode()
      continue

    elif user_mode == 'M': # Manually Enter An Array ----------------------------------------------
      manual_input_mode()
      continue

    elif user_mode == 'Q': # Quit The Program -----------------------------------------------------
      print('Exiting program...')
      break


if __name__ == '__main__':
  print("This is the main module for Lab 4.")
  print('Programmer: Chris Vaisnor')
  print('Python Version: 3.8.10')
  print()
  print('------------------------------------------------------------')
  print()

  main()