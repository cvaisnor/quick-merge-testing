# Lab 4 - Testing Quicksort / Merge Sort

### Programmer: Chris Vaisnor

### Python Verison: 3.9.7

### IDE'S Used: VSCode and PyCharm

__Note:__ A Python virtual environment was used for manipulating the output of sorting the input_files directory. I wanted to have more control of the graphing and table manipulation characteristics, compared to using Microsoft Excel. I will include the libraries used in that environment in the requirements.txt file. 

The virtual environment is **NOT** needed for running the program, **lab4.py**.

### How to Use:
The program reads .txt files in the input_files folder. Each .txt file must have one element(integer) per line with no leading or trailing spaces.

The program has multiple mode options:
* Choose F for File Mode
* Choose D for Directory Mode
* Choose M for Manual Mode

Each mode passes an array into each sorting function and prints the counts of the comparisons and swaps to the console. If the input array is less than or equal to 50 elements, the unsorted input and sorted output will also be printed.

File Mode lets the user specify ONE of the default files. Directory Mode uses ALL of the default files. Manual Mode prompts the user for an array to be sorted manually. The input array must have a space between each element.

### Running The Program:
In the terminal, run:
```commandline
python3 lab4.py
```



