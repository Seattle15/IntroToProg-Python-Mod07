# Introduction to Programming - Python
## Module 7
### Creating GitHub Webpages
________________________________________________________

**Styling text**  

*italics*  _italics_

**bold** __bold__

**bold and nested _italic_**

***all bold and italic***

~~strikethrough~~

----------------------------------------------------------


**Quote using >, back ticks and spaces**

In the words of Guido van Rossum
> Python is an experiment in how much freedom programmers need. Too much freedom and nobody can read another's code; too little and expressiveness is endangered.

**Quote inline code** `return 'Some custom error message'` with backticks on either side

**Quote blocks of code:** Fence code with triple back ticks to assign its own block
```
try:
    new_file_name = input("Enter the name of the file you want to make: ")
    if new_file_name.isnumeric():
        raise Exception('Do not use numbers for the file\'s name')
    elif new_file_name.endswith('txt') == False:
        raise FileNotTXTError()
    else:
        raise CustomError()

except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
```

Or indent code with four spaces

    class CustomError(Exception):
    """  Some custom error info in the DocString  """
    def __str__(self):
        return 'Some custom error message'

    class FileNotTXTError(Exception):
    """  File extension must end with txt to indicate it is a text file  """
    def __str__(self):
        return 'File extension not txt'
        
            
  ______________________________________________________
**Numbered list**

 
1) list item one   
2) list item two   
3) list item three   
4) list item four   
  
  ______________________________________________________
**Nested list**

 
1) list item one   
2) list item two   
   * nested one   
     * nested two   
  
**********************************************************
**Unordered list**

* unordered list
- unordered list
+ unordered list

___________________________________________________
**Task Lists**

- [x] Task one
- [ ] Task two
- [ ] Task three

______________________________________________________________

**Links**

[Google](https://www.google.com/)

Google search website <https://www.google.com/>


______________________________________________________________


**Table 1. My first table in markdown**

|     **Header_1**        |      **Header_2**        |      **Header_3**       |
|:------------------      |:-------------------:     |--------------------:    |
|   left  adjusted cell   |   centered cell          |  right adjusted cell    | 
|  Python                 |   Java                   | SQL                     |   


* use colons to the left or right to indicate right and left line adjustment respectively
* use two colons on either side of 3 or more dashes to indicated centered text



_______________________________________________________

**Add image**



![Picture7 resized](https://user-images.githubusercontent.com/12945181/127597988-0375e87d-fdcd-4335-ae39-5ae65f86ce2b.png)


_______________________________________________________
**Paragraph**

The with keyword invokes a context manager for the file and automatically closes the file at the end of the block, i.e., there is no need to use obj_file.close(). It replaces older ways of file access. 

The general syntax is
```
with open(‘file_name.txt’, ‘r’) as obj_file:
    file_contents = obj_file.read()
print(file_contents)

```   

________________________________________________________

**URL of GitHub  is:** https://seattle15.github.io/IntroToProg-Python-Mod07/   
   
 ----------------------------------------------------------
 
Hedy Khalatbari   
July 30, 2021      
Foundations of Programming: Python   
Assignment07   
GitHub repo URL: https://github.com/Seattle15/IntroToProg-Python-Mod07

# Programming with Python: Module 7   
   
### Working with text files
#### read, write, and append modes: can define a function for each in your script

* if you try reading a file that does not exist you will get an error message; this is not the case in write and append modes
* use ‘for loop’ with read mode to iteratively read rows of data and append it to a list (or tuple or string)

#### reading data options
	
* .readline(): reads one row at a time and then advances to the next row
   * use repeatedly to read more lines, for example with a while loop

* .readlines(): reads all lines of data and returns a list. .read() reads all lines and returns a string
   *everything is pulled in from file and stored in memory; rather that the option of iterating thru lines and only saving the data you wanted

#### combining reading and writing

* you can write a function that contains options for all three (read, write, and append) modes (i.e., a custom wrapper function)
  * or have separate custom functions for each
  * note that the concept of write and append modes may be more clearly presented as overwrite and write to the user; so that they understand that with the ‘write mode’ they would be losing all prior data









