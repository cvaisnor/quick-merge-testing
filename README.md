# Lab 4 - Testing Quicksort / Merge Sort

Programmer: Chris Vaisnor

Python Verison: 3.9.7

IDE: VSCode and PyCharm

__Note:__ A Python virtual environment is located in /env. This venv contains the libraries used in the manipulation of the output .csv table used in the 'comparing_sorts.ipynb' file. I wanted to have more control of the graphing and table manipulation characteristics, compared to using Microsoft Excel.

This venv is __NOT__ needed for 'lab4.py'. Any Python 3 version should work fine for running the program.

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



