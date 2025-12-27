'''To add a tab to your text, use the character combination
\t:
>>> print("Python") 
Python 
>>> print("\tPython") 
    Python
To add a newline in a string, use the character
combination \n:
>>> print("Languages:\nPython\nC\nJavaScript") 
Languages: 
Python 
C 
JavaScript'''

'''Python can look for extra whitespace on the right and left
sides of a string. To ensure that no whitespace exists at the
right side of a string, use the rstrip() method:
❶ >>> favorite_language = 'python ' 
❷ >>> favorite_language 
'python ' 
❸ >>> favorite_language.rstrip() 
'python' 
❹ >>> favorite_language 
'python '
The value associated with favorite_language ❶ contains
extra whitespace at the end of the string. When you ask
Python for this value in a terminal session, you can see the
space at the end of the value ❷. When the rstrip() method
acts on the variable favorite_language ❸, this extra space is
removed. However, it is only removed temporarily. If you
ask for the value of favorite_language again, the string looks
the same as when it was entered, including the extra
whitespace ❹.
To remove the whitespace from the string permanently,
you have to associate the stripped value with the variable
name:
>>> favorite_language = 'python ' 
❶ >>> favorite_language = favorite_language.rstrip() 
>>> favorite_language 
'python'
To remove the whitespace from the string, you strip the
whitespace from the right side of the string and then
associate this new value with the original variable ❶.
Changing a variable value is done often in programming.
This is how a variable value can be updated as a program
is executed or in response to user input.
You can also strip whitespace from the left side of a string
using the lstrip() method, or from both sides at once using
strip():
❶ >>> favorite_language = ' python ' 
❷ >>> favorite_language.rstrip() 
' python' 
❸ >>> favorite_language.lstrip() 
'python ' 
❹ >>> favorite_language.strip() 
'python'
In this example, we start with a value that has whitespace
at the beginning and the end ❶. We then remove the extra
space from the right side ❷, from the left side ❸, and from
both sides ❹. Experimenting with these stripping functions
can help you become familiar with manipulating strings. In
the real world, these stripping functions are used most often
to clean up user input before it is stored in a program.'''

'''When working with strings, another common task is to
remove a prefix. Consider a URL with the common prefix
https://. We want to remove this prefix, so we can focus on
just the part of the URL that users need to enter into an
address bar. Here is how to do that:
>>> nostarch_url = 'https://nostarch.com' 
>>> nostarch_url.removeprefix('https://') 
'nostarch.com'
Enter the name of the variable followed by a dot, and then
the method removeprefix(). Inside the parentheses, enter the
prefix you want to remove from the original string.
Like the methods for removing whitespace, removeprefix()
leaves the original string unchanged. If you want to keep
the new value with the prefix removed, either reassign it to
the original variable or assign it to a new variable:
>>> simple_url = nostarch_url.removeprefix('https://')'''