# Introduction to Programming - Python
## Module 7
### Creating GitHub Webpages
________________________________________________________


*italics*  _italics_

**bold** __bold__

**bold and nested _italic_**

***all bold and italic***

~~strikethrough~~

----------------------------------------------------------


**Quote using >**

In the words of Guido van Rossum
> Python is an experiment in how much freedom programmers need. Too much freedom and nobody can read another's code; too little and expressiveness is endangered.

**Quote inline code** `return 'Some custom error message'` with backticks on either side

**Quote blosks of code:** Fence code with triple back ticks to assign its own block
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
**Numbered list and nested list**

 
1) list item one   
2) list item two   
   * nested one   
     * nested two 
4) list item three   
5) list item four   
  

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

|     **Header1**        |      **Header2**        |      **Header 3**       |
|:------------------     |:-------------------:    |--------------------:    |
|   content goes here    |   and more content      |  plus more here         | 
|  apples                |   bananas               | oranges                 | 

* use colons to the left or right to indicate right and left line adjustment respectively
* use two colons on either side of 3 or more dashes to indicated centered text



_______________________________________________________

**Add images**



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

URL of GitHub webpaage is: https://seattle15.github.io/IntroToProg-Python-Mod07/  


