print("Decomposition is the act of dividing a problem down into smaller ones and writing specific functions to correct them individually.\n")
print("You can create your own functions by using the def (define) keyword, choosing a function name, signifying it as a function with parentheses (): and then writing your code indented.\n")
print("When a function is invoked, the code jumps to where the function is defined and runs the code from there, returning to the step after where the function was invoked when finished.\n")
print("Functions must be defined in code above the points where it is invoked for use later, as Python reads code from top to bottom.\n")
print("Parameters are variables that exist online inside functions and is only assigned to it at the time of the function’s invocation.\nParameters live inside functions whereas arguments exist outside functions and can carry values to parameters.\n")
print("Parameters can be used to require arguments from a function and pass the value into the function during invocation.\n")
def test1(First,Middle,Last):
    print("Hello, my name is: ",First,Middle,Last)
print("Using positional parameter passing, values can be passed and reused across every iteration it is called upon from within the function.\nThese passed values are called positional arguments.")
test1("James","Robert","Whale\n")
print("Keyword argument passing passes values based on the argument’s name, instead of its position like positional parameter passing.")
test1(Last="Whale\n",Middle="Robert",First="James")
print("Both positional parameter passing and keyword argument passing can be used at the same time if you wish, but positional parameter passing must come first.")
test1("James", Last="Whale\n", Middle="Robert")
def test2(Name="Spanky",Gender="Male\n"):
    print("Welcome to the He-man Woman Hater's club. Can I take your name and sex please?" + Name + ":" + Gender)
    print("Thank you,", Name + ".", "It does appear you are indeed a", Gender)
print("You can set default values to the arguments using the assignment operator followed by the default value.")
test2("James")
def test3(explode=True):
    print(3)
    print(2)
    print(1)
    if not explode: return
    print("Boom!\n")
print("The return function on its own is used to immediately terminate a functions execution and return to the point of invocation.")
test3()
def test4(Name="Spanky",Gender="Male\n"): return "Welcome to the He-man Woman Hater's club. Can I take your name and sex please?"
x = test4()
print("The return function extended with an expression also immediately terminate a functions execution and return to the point of invocation but additionally evaluates the expressions value and returns it as the function’s result.\n" + x + "\n")
print("The None keyword can be used to assign a variable with no value or in comparison with a variable to diagnose its internal state.")
if x == None: print("This variable has no value.\n")
else: print("This variable contains a value.\n")
print("If a function doesn’t return a certain value using a return expression clause, it returns None.")
def course_interest(i):
    if (i > 5): return("This course is interesting.")
print("Interest in this course:",course_interest(0),"\n")
def course_list(n):
    list = []
    for i in range(1, n+1): list.insert(0,i)
    return list
print("Lists can also be a function result.", course_list(3),"\n")
print("Variables that exist outside of functions can be used inside them, but variables that exist inside functions cannot be used outside them.\nThat is because the variable is only inside the scope of the function and does not exist elsewhere.")
def test5():
    var1 = "I exist only inside the test5 variable."
    print(var1, "var2 cannot be called inside me - It is outside my scope.",end=" ")
var2 = "I exist outside the test5 variable."
test5()
print(var2,"\n")
print("Because variables inside a function’s scope don’t exist outside, it is possible for two functions with the same name to exist and have different values assigned to each.")
def test6():
    var3 = "I wish this course was a lot shorter."
    print(var3)
var3 = "It would be a lot shorter if you stopped bitching.\n"
test6()
print(var3)
print("You can define specific variables that exist inside a scope with the global keyword, which will make said variable(s) accessible from outside.")
def test7():
    global var4
    var4 = "I can be called anywhere now that I'm global.\n"
var4 = "I'm in danger!"
test7()
print(var4)
print("A sequence type is a type of data in Python which is able to store more than one value (or less than one, as a sequence may be empty), and these values can be sequentially (hence the name) browsed, element by element.\nThe for loop is a tool especially designed to iterate through sequences, we can express the definition as: a sequence is data which can be scanned by the for loop.\nYou’ve encountered one Python sequence so far – the list. The list is a classic example of a Python sequence, although there are some other sequences worth mentioning, and we’re going to present them to you now.\nThe second notion – mutability – is a property of any of Python’s data that describes its readiness to be freely changed during program execution. There are two kinds of Python data: mutable and immutable.\nMutable data can be freely updated at any time – the following instruction modifies the data freely: list.append(1)\nImmutable data cannot be modified in this way. A tuple is an immutable sequence type.\n")
print("To distinguish the differences between lists and tuples, tuples prefer to use parenthesis () whereas lists prefer brackets [], but its also possible to create a tuple from sets of values separated by commas.")
list1 = [1,2,3,4]
tuple1 = (5,6,7,8)
tuple2 = 9, 10., .11, "twelve"
print(list1,tuple1,tuple2,"\nNotice how tupples can contain elements of different types\n")
print("To create a tuple with just one element, the item must end with a comma after it to signify that it is in fact a tuple and not a variable.")
notatuple = (1)
tuple3 = (1,)
print(notatuple,tuple3,"\n")
print("You use the same conventions to get tuple elements as you do with lists.")
print("Specifying a value in the parameter returns said value: ",tuple2[0],"\nSlices work the same also: ",tuple2[1:],tuple2[:-3],"\n")
print("You can’t append, insert, delete, etc. elements to tuples like you can with lists though – this is a result of the immutable sequence type.\nInstead, values can be added to tuples through concatenation (+) of the values of one tuple to another.")
tuple1 += tuple2
print(tuple1,"\n")
print("You can use the len() function, concatenate+, multiply* and in/not in operators on tuples.\n",len(tuple1),end=" ")
tuple3*=2
tuple1+=tuple3
print(len(tuple1),"Thirteen" in tuple1, 4 not in tuple1,"\n", tuple1,"\n")
print("Tuples can appear on the left side of the assignment operator and can also store variables.\n")
print("The Dictionary is another Python data structure that is not a sequence type and is mutable.\nThey work the same way as normal dictionaries, linking one word (key) to another (value).\nEach key must be unique.\nA key can be of any data type (i.e. float, int, str.)\nA dictionary is not a list – a list contains a set of numbered values, while a dictionary holds pairs of values.\nThe len() function works on dictionaries too.\nThe dictionary is a one-way tool. You can use a key to search for a value, but not the other way round.\n")
dct = {'mutable':'A property of any of Python’s data that describes its readiness to be freely changed during program execution. Mutable data can be freely updated at any time.','immutable':'Immutable data cannot be modified freely. Appending an element to the end of the list would require the recreation of the list from scratch. You would have to build a completely new list, consisting of the all elements of the already existing list, plus the new element.'}
phone = {'Hastings' : 8001066, 'Emergency' : 999}
print(dct,"\n",phone,"\n")
print("Dictionaries are defined with curly brackets {}, pair keys and values with colons (key:value) and commas to separate different entries (1:2, 3:4).\nDictionaries do not store entries in any order and how it does so is not controllable.\n")
print("To return a value from a dictionary, the desired key must be included in the dictionary’s index (dict[key]) and must be entered exactly – strings as ‘strings’,etc. and case sensitive.\n", dct['mutable'],phone['Emergency'],"\n")
print("To prevent runtime errors occurring should a value be searched for that doesn’t exist within the dictionary, the use of in/not in operators can be used to rule invalid entries out.")
keys = ['mutable', 'immutable']
def dictsearch(word='immutable'):
    #word = input("Please enter a word to search: ")
    if word in dct:
        print(word,"->",dct[word])
    else:
        print(word, "is not in the dictionary.")
dictsearch('Python')
dictsearch()
phonetic = {'A':'Alfa' , 'B':'Bravo', 'C':'Charlie' , 'D':'Delta', 'E':'Echo' , 'F':'Foxtrot', 'G':'Golf' , 'H':'Hotel', 'I':'India' , 'J':'Juliett', 'K':'Kilo' , 'L':'Lima', 'M':'Mike' , 'N':'November', 'O':'Oscar' , 'P':'Papa', 'Q':'Quebec' , 'R':'Romeo', 'S':'Sierra' , 'T':'Tango', 'U':'Uniform' , 'V':'Victor' , 'W':'Whiskey' , 'X':'Xray' , 'Y':'Yankee' , 'Z':'Zulu'}
print("The .keys() method returns a list built of all the keys gathered within the dictionary (dct.keys():).\nPrefixing sorted to the function will try to sort the dictionary into order (sorted(dct.keys()):).")
def dictsearch(dictionary=dct, opt=0, word='immutable'):
    if opt == 1: word = input("Please enter a word to search: ")
    elif opt == 2:
        if word in dictionary:
            print(word,"->",dictionary[word])
        else:
            print(word, "is non-existent.")
    else:
        for key in dictionary.keys():
            print(key,"->",dictionary[key])
dictsearch(phonetic)
print("\nAppending the .items() method returns a list of tuples where each tuple is a key-value pair.")
for letter,alpha in phonetic.items():
    print(letter,"->",alpha)
print("\nThe .values() method is similar to .keys() but returns a list of values.")
for letter in phonetic.keys():
    print(letter, end=", ")
print()
for alpha in phonetic.values():
    print(alpha)
print("\nYou can assign new values to an existing key easily as dictionaries are mutable.\nAssign new values to the dictionary by assigning the value to a non-existent key.")
phonetic["A"] = "Alpha"
phonetic["1"] = "One"
phonetic["Remaining interest"] = "Zero"
print(phonetic,"\n")
print("Deleting a key with the del instruction will also delete the value assigned to it.")
del phonetic['Remaining interest']
dictsearch(phonetic,2,"Remaining interest")
