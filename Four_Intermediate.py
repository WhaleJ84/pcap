print("Decompositioning code from large programs down into smaller chunks to be more manageable is done through modules.\n")
print("A list of all the pre-existing modules provided by Python are available at: https://docs.python.org/3/library/index.html\nModules contain entities, which can be functions, variables, constants, classes and objects.\n")
print("You import modules by using the import keyword, followed by the modules you wish to import, separated with commas.\n")
print("A namespace is a space in which some names exist and the names don’t conflict with each other.\n")
print("Entities within a module are in the module’s namespace and wont conflict with entities outside the module of the same name because of that.\n")
print("Module entities are called into code by using the syntax of module(dot)entity, for example, math.pi.\n")
print("You can import specific entities from a module into code using the syntax of from (module) import (entity(s)). Doing so will add them into your namespace and can be called without having to specify their originating module first.\n")
print("Because the entities are brought into your namespace, that allows you to adapt and edit them to suit your needs better.\n")
print("You can import the modules/entities later in code to replace your pre-existing entities if needs be.\n")
print("It is possible to import all entities into code using the asterisk (from math import *) but is not recommended as a solution as you may not need all the entities and it can cause conflicts.\n")
print("Modules can be given aliases to shorten their names or change them to work around your code by using the as keyword in an example such as import math as M but doing so will make the original name un-callable.\n")
print("Similarly, entity names can be given aliases also with a syntax example of from math import pi and PI, sin as sine.\n")
print("The dir(module) function is used to show all the entities available for use inside a module when used on a module imported as a whole (e.g. import math instead of ‘from math import…’)")
import math
print(dir(math),"\n")
print("The random module is a useful one to generate pseudo-random floating-point numbers for your code.")
from random import random
for i in range(5):
    print(random(),end=" ")
print("The seed() entity from the random module is used to interact with the random number generator’s seed, using seed() to set the seed with the current time, or seed(i) to set the seed with the integer value i.\n")
from random import seed
seed()
for i in range(5):
    print(random(), end=" ")
print("Randint generates random integers between the two specified numbers and randrange will generate a number between a range (beg, end, step) and is right-sided.\n")
from random import randrange, randint
print(randint(0,0),randrange(0,100,5))
print("To choose elements from a specified pool at random, the choice and sample entities can be used. Choice(sequence) chooses a random element from the sequence supplied to it (e.g. a list) and sample(sequence, elements_to_choose=1) allows you to specify how many elements will be chosen at random within the sequence (which by default is 1)\n")
from random import choice, sample
lst = [1,2,3,4,5,6,7,8,9,10]
print(choice(lst),sample(lst,5),sample(lst,10),"\n")
print("To gain information about the machine the code is running on, the platform module can provide feedback about certain hardware/software available.\nThe entity plaform (from platform import platform) takes two arguments, platform(aliased=False,terse=False). Alias, if set to True will provide underlying names if possible and Terse will provide a briefer result.\n")
from platform import platform
print(platform()+"\n"+platform(1)+"\n"+platform(0,1)+"\n")
print("Platform’s entity, machine() returns the generic name of the machine’s processor.")
from platform import machine
print(machine(),"\n")
print("Platform’s entity, processor() returns the real processor name if possible.")
from platform import processor
print(processor(),"\n")
print("Platform’s entity, system() returns the generic OS name.")
from platform import system
print(system(),"\n")
print("Platform’s entity, version() returns the OS version.")
from platform import version
print(version(),"\n")
print("Python_implementation and python_version_tuple returns the current Python version.")
from platform import python_implementation, python_version_tuple
print(python_implementation())
for atr in python_version_tuple():
    print(atr)
print("Functions can be contained within modules and similarly modules can be contained within packages.\n")
print("Like pre-existing modules, you can import your own modules in the form of .py files into a main file and run the code from there. Python is smart enough to remember what has been imported already.\n")
print("Every module has its own __name__ variable which stores the name of the module inside it if its a main or a module.\n",  __name__, "\n")
print("If you want to inform others that the code within a variable should not be modified by them, it is a convention to precede the variable’s name with _ or__ (e.g. __dont_touch_my_code)\n")
print("#!/usr/bin/env python3 #! Wont run in python as the hash signifies the line as a comment, but unix and unix-like OS’s will interpret the line instructing the OS how to execute the contents of the tile (i.e. go to this location and launch this).\n '''module.py - an example of Python module''' a string (maybe a multiline) placed before any module instructions (including imports) is called the doc-string, and should briefly explain the purpose and contents of the module\n")
print("Python’s main files are stored in C:\\Users\\*user*\\py\\progs, and modules are stored in C:\\Users\\*user*\\py\\modules by default in Windows.\n")
print("By default, Python can only import modules created within the same folder. Importing the path entity from the sys module allows you to specify the path to your desired modules by appending their location. (path.append(‘c:\\location\\to\\module’))\n")
print("When a package is formed, it is like a filesystem structure and its contents is called upon in the same way (e.g. extra.good.best.tau.funT():)\n")
print("You create a package by initialising the file with __init__.py – this tells python where to find the structure and what subpackages it contains. More than 1 file can contain __init__.py\n")
print("By appending the outermost package into the path, you can then import the function from the module within, rather than appending the absolute path to the specific module you’re after.\n")
print("Give long module names aliases to shorten them (e.g. import extra.good.best.sigma as sig).\n")
print("To try and prevent errors within your code, the try: and except: keywords can be used to test a piece of code with try: and run another bit of code if it fails with except:.")
try:
    print("1")
    x = 1 / 0
    print("2")
except: print("Oh dear, something went wrong!")
print("3\n")
print("You can have more than one exception block, allowing you to define more specific responses to errors.")
def try_exc(x=5):
    try:
        y = 1 / x
        return(y)
    except ZeroDivisionError: return('Cannot divide by zero – sorry!')
    except TypeError: return('You have to enter an integer value!')
    except KeyboardInterrupt: return('Oh, dear!')
print(try_exc(), try_exc(0), try_exc("3"))
print("\nThe except branches are searched in the same order in which they appear in the code\nyou must not use more than one except branch with a certain exception name\nthe number of different except branches is arbitrary – the only condition is that if you use try, you must put at least one except (named or not) after it\nthe except keyword must not be used without a preceding try\nif any of the except branches is executed, no other branches will be visited\nif none of the specified except branches matches the raised exception, the exception remains unhandled\nif an unnamed except branch exists (one without an exception name), it must be specified as the last.\n")
print("There are 63 built-in exceptions that all form a tree-shaped hierarchy.\n")
print("The exceptions are executed in order as written within your code (from top to bottom), so make sure to write the more specific exceptions first to ensure they always have a chance of getting run.\n")
print("If you want to handle two or more exceptions in the same way, you can use the following syntax except (exc1, exc2):\n")
print("Exceptions raised inside a function can handle exceptions both inside outside the function.\n")
print("The raise keyword can be used to arbitrarily raise the specified exception to simulate how your code will handle it.")
def try_exc2(n):
    raise ZeroDivisionError
try: try_exc2(0)
except ArithmeticError: print("What did you do?\n")
print("The raise instruction can be used on its own within an except branch to repeat the same exception.")
def try_exc3(n):
    try: return n/0
    except:
        print('I did it again!')
        raise
try: try_exc3(0)
except ArithmeticError: print("I see!\n")
print("The assert keyword can be used to ensure that only valid entries are allowed through, causing an error to happen if not. The use of assertion would be good for applications where correct data is critical.")
import math
x = 0#-999 will cause an error.
assert x >= 0.0
x = math.sqrt(x)
print(x)
print("""The following exceptions have these effects:
      ArithmeticError - an abstract exception including all exceptions caused by arithmetic operations like zero division or an argument’s invalid domain
      AssertionError - a concrete exception raised by the assert instruction when its argument evaluates to False, None, zero, or an empty string
      BaseException - the most general (abstract) of all Python exceptions – all other exceptions are included in this one; it can be said that except: and except BaseException: are equivalent
      Exception - an abstract exception including all exceptions caused by errors resulting from code malfunctions
      IndexError - a concrete exception raised when you try to access a non-existent sequence’s element
      KeyboardInterrupt - a concrete exception raised when the user uses a keyboard shortcut designed to terminate a program’s execution (Ctrl-C in most OSs); if handling this exception doesn’t lead to program termination, the program continues its execution.
      LookupError - an abstract exception including all exceptions caused by errors resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)
      MemoryError - a concrete exception raised when an operation cannot be completed due to a lack of free memory
      OverflowError - a concrete exception raised when an operation produces a number too big to be successfully stored
      ImportError - a concrete exception raised when an import operation fails
      KeyError - a concrete exception raised when you try to access a non-existent collection’s element (e.g., a dictionary’s)\n""")
print("All characters and numbers are converted to ASCII numbers which is a form that practically all other devices can understand.\n")
print("As the first 128 ASCII code points are used for the Latin alphabet, the remaining 128 aren’t enough to facilitate for all remaining languages. To overcome this limitation, different code pages are created, each page storing different characters in the ASCII spaces, so to use a specific language range in ASCII, you must first know the corresponding code page for it.\n")
print("Unicode is a better solution to ASCII limitations as it can store more than a million code points.\n")
print("UTF-8 is a format of Unicode that uses as many bits for each of the code points as it really needs to represent them, making it more efficient than UCS-4.\n")
print("Strings are immutable.\n")
print("You can create multi-line strings with “”” “”” or ‘’’ ‘’’.\n")
print("When using len() on a multi-line string, an extra character will be counted on every line other than the end, which is an end-line character (\\n).\n")
print("Strings can be concatenated(+) and replicated(*).\nWhen an operator has more than 1 function (+’s ability to add and concatenate), this ability is called overloading.\n")
print("The ord() (ordinial) function is used to return a character’s ASCII/UNICODE code point value and can only take a one-character string.\n",ord("t"))
print("Similarly, the chr() function can return the corresponding character of an ASCII/UNICODE code point.\n",chr(84), chr(104), chr(105), chr(115), chr(32), chr(99), chr(111), chr(117), chr(114), chr(115), chr(101), chr(32), chr(115), chr(117), chr(99), chr(107), chr(115), chr(46),"\n")
print("Strings are sequences, and although they aren’t lists, they can be treated like them in many cases through things such as indexing, iterating, slicing and boolean checks.\n")
print("Because strings are immutable, it means you can’t delete, append or insert items with them.\n")
print("You can somewhat substitute the lack of append and insert buy using concatenation to join new additions to the beginning or end of the desired string.")
suffer = 'will this '
suffer += 'end?'
suffer = 'When ' + suffer
print(suffer,"\n")
print("The min() function returns the minimum element of the sequence passed as an argument based on its ASCII reference.",min('aAbByYzZ'),"The result is A because it has the lowest page value of 65 with 'a' being 32 values above that.\n")
print("Max() does the opposite of min()",max('aAbByYzZ'),"\n")
print("The index() method searches the sequence from the beginning to find the first element of the specified value.",'This goes on forever.'.index('r'))
print("The list() function takes its argument (not necessarily a string) and creates a new list containing all the included characters, one per list element.\n",list('Please end'),"\n")
print("Count() method counts all occurrences of the element inside the sequence.\n", 'mississippi'.count('s'),"\n")
print("the .capitalize() method creates a new string of the affixed one and prints out said string with the first letter capitalised and the remaining in lower case. It does not work across different sentences in the same string.\n".capitalize())
print(".center() method makes a copy of the original string, trying to centre it inside a field of a specified width. If a 2 letter word had a center() width of 2, there would be no difference, but 4 would add a space either side.\n".center(232))
print("Adding a second parameter to .center() will use the latter provided character instead of spaces.".center(104,'*'),"\n")
print(".endswith() method checks if the given string ends with the specified argument and returns True or False depending on the check result.")
if "This course is tedious, isn't it?".endswith("it?"): print("Yes\n")
else: print("tedious is a bit of an understatement...")
print(".find() method is similar to .index() but wont crash when finding a non-existent substring, instead returning -1 and only works on strings.")
print("Fucks given about this course: ".find('Fucks'))
print("\nAdd an integer as a second parameter argument to specify where you want to begin the search from.")
print("Where's Wally?".find('here',2))
print("\nIncluding a third parameter to .find() will specify the position within the string where the search will stop.")
print("This is boring sample text".find('ring',0,13))
print("\n.isalnum() method takes no parameters and returns True if the string contains only letters or only numbers – returning false if a combination contains. Note that spaces also cause a False return.")
print("D035 TH15 5TR1NG C0NT41N 0NLY L3TT3R5?".isalnum())
print("\nWhere isalnum() replied if the string contained only either letters or numbers, isalpha() replies True if it has only letters, and isdigit() replies True if only numbers exist within.")
print("1337".isdigit(),"u wot m8?".isalpha())
print("\nSimilarly, islower(),isupper() and isspace() returns true if a string contains only lower-case, upper-case and spaces respectively.")
print("\nLower() method makes a copy of a source string, replacing all upper-case letters with their lower-case counterparts".lower(),"while upper() does the opposite.".upper())
print("\nLstrip()".lstrip()+" Method".lstrip()+" In".lstrip()+" It's".lstrip()+" Parameterless".lstrip()+" Form".lstrip()+" Returns".lstrip()+" A".lstrip()+" Newly".lstrip()+" Created".lstrip(),"string formed from the original one by removing all white spaces.")
print("X\nProviding a string argument within the lstrip() parentheses will remove all characters enlisted, not just white spaces.".lstrip('X'))
print("\nThe replace() method when provided with two parameters will return a copy of the original string in which all occurrences of the former argument have been replace with the latter.")
print("I can't stand this course".replace("can't stand",'detest'))
print("\nAdding a third parameter will specify the limit on how many replacements the replace() method can perform.")
print("\nrfind() with a single parameter will search for the provided string beginning from the right, opposing the find() method that begins from the left.\nAdding a second parameter will specify how far in rfind() will begin to search, and a third parameter will provide an end point.")
print("I think, therefore I am".rfind('e',12,15))
print("\nRstrip() does the same as lstrip() but is right-sided insteadX".rstrip("X")+".")
print("\n.split() method splits the string and builds a list of all detected substrings, assuming that the substrings are delimited by whitespaces.")
print("Fe Fi Fo Fum".split())
print("\nA mirror reflection of endswith(), startswith() checks if a given string starts with the specified substring.", "you enjoy this course".startswith("You"))
print(" \nStrip() ".strip()+" Combines ".strip()+" The ".strip()+" Effects ".strip()+" Caused ".strip()+" By ".strip()+" Rstrip() ".strip()+" And ".strip()+" Lstrip(), ".strip()+" Making ".strip()+" A ".strip()+" New ".strip()+" String ".strip()+" Lacking ".strip()+" All ".strip()+" The ".strip()+" Leading ".strip()+" And ".strip()+" Trailing ".strip()+" Whitespaces.".strip())
print("\nSwapcase() method makes a new string by swapping the case of all letters within the source string.".swapcase())
print("\nTitle() method makes a new string by swapping the first letter of every word to upper case and all others lower.".title())
print("\nComparison operators can be used on strings but only work in their literal sense, comparing absolute values (i.e. A is not the same as a).")
print("\nWhen two strings are compared with the greater/less than operators, the longer string is considered greater.", 'alpha' < 'alphabet')
print("\nWhen the strings are similar but with case-sensitive differences, lower case letters are taken as higher values than upper case ones.", 'beta' > 'Beta')
print("\nStrings that only contain numbers are still just strings, so using comparison operators on them won’t give results expected from their numerical counterparts.", '10' > '010')
print("\nComparing strings against numbers is a bad idea: == always returning False and != returning True. Greater/less-than operators cause an error.")
print("\nSorted() creates a new list containing the items of the original sorted in an alphabetical manner. Sort() performs the same operation but on the original list.")
lst1 = ['big','tiddy','goth','girlfriend']
print(sorted(lst1))
print("\nProviding the contained values will be legal within their new environment, strings that contain only numbers can be converted into strings and vice versa by prefixing int(),float() or str() accordingly.")
