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
#### *read, write, and append modes*

* can define a function for each in your script
* if you try reading a file that does not exist you will get an error message; this is not the case in write and append modes
* use ‘for loop’ with read mode to iteratively read rows of data and append it to a list (or tuple or string)

#### *reading data options*
	
* .readline(): reads one row at a time and then advances to the next row
  * use repeatedly to read more lines, for example with a while loop

* .readlines(): reads all lines of data and returns a list. .read() reads all lines and returns a string
   *everything is pulled in from file and stored in memory; rather that the option of iterating thru lines and only saving the data you wanted

#### *combining reading and writing*

* you can write a function that contains options for all three (read, write, and append) modes (i.e., a custom wrapper function)
  * or have separate custom functions for each
  * note that the concept of write and append modes may be more clearly presented as overwrite and write to the user; so that they understand that with the ‘write mode’ they would be losing all prior data


### Working with binary files
#### *pickling*
* saving data in a binary format (instead of plain text). This can obscure the file's content (but not encrypt it) and may reduce the file's size
* import pickle, pickle.dump(), pickle.load()

### Structured error handling (try-except)
Trap errors due to interactions of humans with your code in a try-except block. Other languages may call if a try-catch block. Gives the programmer more control over the error handling messages that users will see

#### *using the exception class*
* a class is used to create objects. Python creates an Exception object when an error occurs that includes the information about the error. The except block allows you to capture a variable containing the error message generated  the error

* in the except block, you must specify the type of ‘Exception as e’ – which is counter to how Python usually works. You can then print out more data about ‘e’ (Box 1)   



**Box 1**
--------------------------------------------------------------------
**Try-except block script**
```
try:
    quotient = 5/0
    print(quotient)
except Exception as e:
    print("There was an error! << Custom Message")

    print("Built-In Pythons error info: ")
    print(e)
    print(type(e))
    print(e.__doc__)   # class attribute __doc__ of object
    print(e.__str__())  # base exception; return str(self)
```
**Running**
>C:\Python39\python.exe C:/_PythonClass/ModDemos/test_Mod07.py     
There was an error! << Custom Message   
Built-In Pythons error info:    
division by zero    
><class 'ZeroDivisionError'>    
Second argument to a division or modulo operation was zero.    
division by zero    
--------------------------------------------------------
 


#### *catching specific exceptions*
* the exception class can catch any type of error, but you can catch specific errors using more specific exception classes. These are illustrated in Box 2. Note that blocks 1-3 of code are executed (and corresponding running section demonstrated) for the first to third lines of the try block respectively (with the other lines commented out). They are included in this Box all together for demonstration purposes. 
* the generic exception block should always be the last one, otherwise, it will catch all errors and the error will never reach the more specific exceptions

* <https://docs.python.org/3/library/exceptions.html#bltin-exceptions> (external site) There is class hierarchy for built-in exceptions and the first two tiers of this hierarchy are summarized in Box 3   Figure 1. Screen capture of instructions on GitHub for setting up a repository



 **Box 2**   
 ------------------------------------------------------------   
 **Try-except block script with specific exceptions**   
 *Note that blocks 1-3 correspond to lines 1 to 3 in try block- with other lines commented out*
 ```
 try:
    quotient = 5/0
    f = open('SomeFile.txt', 'r+')  # the read plus option gives an error if file does not exist
    f.write(quotient)  # causes an error if the file does not exist

except ZeroDivisionError as e:                       #block 1
    print("Please do not use Zero for the second number!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

except FileNotFoundError as e:                       # block 2
    print("Text file must exist before running this script!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

except Exception as e:                               # block 3
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

```
**Running**
>C:\Python39\python.exe C:/_PythonClass/ModDemos/test_Mod07.py  
Please do not use Zero for the second number!        
Built-In Python error info:    
division by zero   
Second argument to a division or modulo operation was zero.   
><class 'ZeroDivisionError'> 
>
>Text file must exist before running this script!        
Built-In Python error info:    
[Errno 2] No such file or directory: 'SomeFile.txt'   
File not found.   
><class 'FileNotFoundError'>   
>
>There was a non-specific error!          
Built-In Python error info:    
name 'f' is not defined   
Name not found globally.      
><class 'NameError'>   

-------------------------------------------------------------------

 
![Mod7Box3](https://user-images.githubusercontent.com/12945181/127680612-93b555ad-3ab0-46e3-8453-5b66898c9141.png)   



#### *raising custom errors*
* use ‘raise Exception’ and you can print out a custom error message (Box 4)
* you can use the basic exception class or other classes
* you can use ‘raise Exception’ without a try-except block (last block row of code in Box 4)   




**Box 4**
----------------------------------------------------------------------
**Try-except bloc with raise Exception script**
```
try:
    new_file_name = input("Enter the name of the file you want to make: ")
    if new_file_name.isnumeric():
        raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
```
**Running**
>C:\Python39\python.exe C:/_PythonClass/ModDemos/test_Mod07.py   
Enter the name of the file you want to make: 123   
There was a non-specific error!   
Built-In Python error info:    
Do not use numbers for the file's name   
Common base class for all non-exit exceptions.  
<class 'Exception'>   

**Raise exception without a try-except block**
```
new_file_name = input("Enter the name of the file you want to make: ")
if new_file_name.isnumeric():
    raise Exception("Do not use numbers for the file's name")
```
**Running**
>C:\Python39\python.exe C:/_PythonClass/ModDemos/test_Mod07.py   
Enter the name of the file you want to make: 123   
Traceback (most recent call last):   
File "C:\_PythonClass\ModDemos\test_Mod07.py", line 3, in <module>   
raise Exception("Do not use numbers for the file's name")       
Exception: Do not use numbers for the file's name           
------------------------------------------------------------    
	
#### *creating custom exception classes*   
* you can create your own custom classes with more features   
	
### Creating advanced GitHub pages
* creating a Markdown file and formatting the page. I supplemented my learning with the course ‘How to deploy a website’ on Code Academy 

* use Jekyll to create a markdown (md) file; Jekyll engine converts markdown language to HTML
* some tips for formatting with Jekyll are summarized in Table 1
* GitHub Pages (public webpages that are hosted and published through GitHub) is used to deploy a website created with the Jekyll markdown (Figure 1)
* create a new public repository -> create an index.md file (via Add file -> Create new file -> docs/ -> index.md)
* you an edit the index.md file with markdown language in the ‘edit file’ tab and click ‘preview’ to see what it looks like


**Table 1- Jekyll markdown**    
![Mod7Table1](https://user-images.githubusercontent.com/12945181/127681235-5fa47262-c0eb-4609-8775-9c65d077723c.png)      
Source <https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github> (external site)   




![Mod7Fig1](https://user-images.githubusercontent.com/12945181/127681257-696940a6-8a02-48f0-9650-e1b28f6278b3.png)      

**Figure 1.** Screen capture of instructions on GitHub for setting up a repository   
	

* I tried out the markdown language on GitHub (Figure 2) and published it (Figure 3)
  * publish steps: Settings ->GitHub pages -> Source (select main and docs and then save)
  * my GitHub page URL: <https://seattle15.github.io/ITFnd100-Mod07/>
  * I checked that all the features (including the image) were performing as expected – I had to make minor changes to my list (ensuring that spaces were at the end of each entry to indicate a new line)
	
	
![Mod7Fig2](https://user-images.githubusercontent.com/12945181/127681272-dc7a5175-33e2-4c58-940c-8dc805b4255a.png) 

**Figure 2.** Screen captures of the ‘Edit File’ and ‘Preview’ contents demonstrating experimentation with markdown language on GitHub     
	
	

![Mod7Fig3](https://user-images.githubusercontent.com/12945181/127681463-e35c0ddd-c9f8-414a-94be-ba74d93a2d97.png)   

**Figure 3.** Screen capture of published GitHub page illustrating the result of using the markdown language   








