print("Objects in OOP have a name, properties and activities.\nThe objects can inherit properties from their parent classes. All classes form into a tree-shaped hierarchy, with the upper-most class being a superclass and all beneath subclasses.")
print("\nClasses are created by calling the class keyword, then an identifier which will name the class, followed by a colon to nest it’s contents inside.")
print("\nA stack is a structure developed to store data in a specific way that has a ‘Last in, first out’ approach. It pushes entries to the top of the stack, and pops entries out of the top of the stack.")
stack = []
def push(val): stack.append(val)
def pop():
    val = stack[-1]
    del stack[-1]
    return val
push(3)
push(2)
push(1)
print(pop())
print(pop())
print(pop())
print("\nIf you wish to create a class that performs a certain function every time it is invoked, the __init__(): constructor function is used to define these instructions, and usually takes (self): as its argument.")
print("\nCalling the objects name, followed by a dot (self.) invokes the method, whereas calling the objects name followed by parentheses (self()) access a property.")
print("\nPrefixing two underscores to a name (__stack) makes it private, meaning it can only be accessed from within its class and cannot be called when calling the class. This is how Python implements the encapsulation concept.")
print("\nAll functions created within the class need to at least have self as a parentheses argument for the function to be able to be called and operate outside of itself.")
print("\nBy creating a function within a class, said class can be used as a template and replicated into new objects, creating multiple copies of the same function that aren’t tied to each other.")
class Stack:
	def __init__(self): self.__stk = []

	def push(self, val): self.__stk.append(val)

	def pop(self):
    		val = self.__stk[-1]
    		del self.__stk[-1]
    		return val

little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()
little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)
print(funny_stack.pop())
print("\nTo improve upon an already created class without changing the original class at all, a new class can be created, invoking the superclass it wants to call upon within its parentheses.\nOnce done, the new class needs to be initialised with __init__(self): immediately followed by initialising the classes derives from with OriginalClass.__init__(self):")
class AddingStack(Stack):
	def __init__(self):
		Stack.__init__(self)
		self.__sum = 0

	def getSum(self): return self.__sum

	def push(self, val):
		self.__sum += val
		Stack.push(self,val)

	def pop(self):
	 	val = Stack.pop(self)
	 	self.__sum -= val
	 	return val

stack = AddingStack()
for i in range(5): stack.push(i)
print(stack.getSum())
for i in range(5): print(stack.pop())
print("\nThe hasattr() function takes two arguments and can safely check if any object/class contains a specified property, with the class/object in question being the first argument and the name of the property to be checked for as the second argument.")
print(hasattr(AddingStack,'push'))
print("\nA method is a function embedded inside a class that is obliged to have at least one parameter, which is usually named self.")
print("\nTo access a method which has been hidden inside a class by having two underscores prefixed to it, you can invoke it by calling the object._class__method()")
class Classy:
     def visible(self): print("visible")
     def __hidden(self): print("hidden")
obj = Classy()
obj.visible()
try: obj.__hidden()
except: print("failed")
obj._Classy__hidden()
print("\nThe __name__ attribute when affixed to a class will uninterestingly return the name of said class. The same method doesn’t work on objects though, needing type(object). Affixed to __name__.")
print(AddingStack.__name__,type(obj).__name__)
print("\nThe __module__ attribute returns the definition of the class, returning __main__ if the file is currently being run.")
print(AddingStack.__module__, obj.__module__)
print("\nThe __bases__ attribute is a tuple that contains classes. When affixed to a class, it returns superclasses for the class, and simply returns object if affixed to an object.")
class Super1: pass
class Super2: pass
class Sub(Super1, Super2): pass
def printbases(cls):
	print('( ',end='')
	for x in cls.__bases__: print(x.__name__,end=' ')
	print(')')
printbases(Super1)
printbases(Super2)
printbases(Sub)
print("\nIf you want your class/object to return a string, it tries to invoke a method named __str__(); by defining the string you desire to be returned to that method, when ran the class/object will return that instead of a generic message saying what point in memory its saved at.")
class Star:
	def __init__(self,name,galaxy):
		self.name = name
		self.galaxy = galaxy
	def __str__(self): return self.name + ' in ' + self.galaxy
sun = Star("Sun","Milky Way")
print(sun)
print("\nInheritance is the passing of attributes and methods from the superclasses to subclasses. All ‘relatives’ a class has inherited from are its superclasses.")
print("\nThe issubclass() function can return True or False based on the inheritance of the classes provided inside its parentheses.\n",issubclass(AddingStack,Stack))
print("\nEach class is considered a subclass of itself.")
print("\nThe isinstance() function is similar to issubclass() in that when provided with two arguments to work upon, returns if the former is an instance of the latter.",isinstance(AddingStack,Stack))
print("\nThe is operator can compare two variables refer to the same object.")
print("\nIf a class inherits from more than one superclass that obtains entities with the same names, the class that is specified in the argument will override the other classes in terms of duplicate entities.")
class Level0:
	Var = 100
	def fun(self): return 101
class Level1(Level0):
	Var = 200
	def fun(self): return 201
class Level2(Level1): pass
object = Level2()
print(object.Var, object.fun())
print("\nIf two classes are provided as superclass arguments that contain entities with the same name, the leftmost argument will override the rest.")
class Left:
	Var = 'L'
	VarL = 'LL'
	def fun(self): return 'left'
class Right:
	Var = 'R'
	VarR = 'RR'
	def fun(self): return 'right'
class Sub(Left,Right): pass
object = Sub()
print(object.Var, object.VarL, object.VarR, object.fun())
print("\nPolymorphism means that one and the same class can take various forms. Superclasses can be made to define specific entities that all subclasses will derive upon and use the polymorphism to enrich all other classes through the entities within the super.")
print("\nComposition is a different approach than inheritance. Where inheritance has a clear hierarchy of ancestry, composition allows an object to be created from multiple different classes without inheritance, creating a new instance on a level playing field.")
import time 
class Tracks:
	def changedirection(self,left,on): print("tracks: ", left, on)
class Wheels:
	def changedirection(self,left,on): print("wheels: ", left, on)
class Vehicle:
	def __init__(self, controller): self.controller = controller
	def turn(self,left):
		self.controller.changedirection(left, True)
		time.sleep(0.25)
		self.controller.changedirection(left, False)
wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())
wheeled.turn(True)
tracked.turn(False)
print("\nInheriting from multiple classes can be risky and is recommended as only a last resort - the use of composition is a better alternative.")
print("\nTry-exceptions can be used in lieu of if statements where Errors are highly likely to occur. When done so, an else: branch can be defined to run in the situation there is no error but must be placed at the very bottom of the statement, underneath the exceptions.")
print("\nFinally is another keyword that can be used within statements that isn’t dependant with else: in any way and can be used alongside or without it. Finally is always executed regardless of the operations above it and must be placed at the very bottom, underneath else: if used.")
def reciprocal(n):
	try: n = 1 / n
	except ZeroDivisionError:
		print("Division failed")
		n = None
	else: print("Everything went fine")
	finally:
		print("It's time to say good bye")
		return n
print(reciprocal(2))
print(reciprocal(0))
print("\nThe args property is introduced by the BaseException class any time an exception is raised, which stores all arguments provided to the entity in question that caused the error to occur. Args is a tuple that will store all arguments, excluding self.")
def printargs(args):
	lng = len(args)
	if lng == 0: print("")
	elif lng == 1: print(args[0])
	else: print(str(args))
try: raise Exception
except Exception as e:
	print(e,e.__str__(),sep=' : ',end=' : ')
	printargs(e.args)
try: raise Exception("my exception")
except Exception as e:
	print(e,e.__str__(),sep=' : ',end=' : ')
	printargs(e.args)
try: raise Exception("my", "exception")
except Exception as e:
	print(e,e.__str__(),sep=' : ',end=' : ')
	printargs(e.args)
print("\nIt is possible to create your own exceptions if needed by creating a new class (because exceptions are classes) and inheriting from the class you want to derive upon. If you wish to create a single exception, only inherit from the lowest possible subclass that you need to branch from, else if you need to create your own hierarchy, inherit from the uppermost class needed and work down from there.")
class MyZeroDivisionError(ZeroDivisionError): pass
def doTheDivision(mine):
	if mine: raise MyZeroDivisionError("worse news")
	else: raise ZeroDivisionError("bad news")
for mode in [False, True]:
	try: doTheDivision(mode)
	except ZeroDivisionError: print('Division by zero')
for mode in [False, True]:
	try: doTheDivision(mode)
	except MyZeroDivisionError: print('My division by zero')
	except ZeroDivisionError: print('Original division by zero')	
print("\nDefault values need to be specified for the constructor arguments of created Exceptions for them to work correctly.")
class PizzaError(Exception):
    def __init__(self, pizza='uknown', message=''):
        Exception.__init__(self,message)
        self.pizza = pizza
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100', message=''):
        PizzaError.__init__(self,pizza,message)
        self.cheese = cheese
def makePizza(pizza,cheese):
	if pizza not in ['margherita', 'capricciosa', 'calzone']: raise PizzaError
	if cheese > 100: raise TooMuchCheeseError
	print("Pizza ready!")
for (pz,ch) in [('calzone',0),('margherita',110),('mafia',20)]:
	try: makePizza(pz,ch)
	except TooMuchCheeseError as tmce: print(tmce, ':', tmce.cheese)
	except PizzaError as pe: print(pe, ':', pe.pizza)
print("\nThe range() function is an example of a generator, which returns a series of values and is generally invoked more than once. This differs to functions which returns one value and is invoked only once.")
print("\nThe yield keyword can be used in place of return and will store the ‘returned’ value without breaking out of the loop, allowing the generator to continue without the need for creating additional variables to store said values otherwise.")
def PowersOf2(n):
	pow = 1
	for i in range(n):
		yield pow
		pow *= 2
t = [ x for x in PowersOf2(5) ]
print(t)
print("\nBy using yield to compliment our generators, we can turn code like this: \n")
class Fib:
	def __init__(self, nn):
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1
	def __iter__(self):
		print("Fib iter")
		return self
	def __next__(self):
		self.__i += 1
		if self.__i > self.__n: raise StopIteration
		if self.__i in [1,2]: return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret
class Class:
	def __init__(self,n): self.__iter = Fib(n)
	def __iter__(self):
		print("Class iter")
		return self.__iter;
object = Class(8)
for i in object: print(i)
print("\nInto this: \n")
def Fib(n):
	p = pp = 1
	for i in range(n):
		if i in [0,1]: yield 1
		else:
			n = p + pp
			pp, p = p, n
			yield n
fibs = list(Fib(10))
print(fibs)
print("\nIt is possible to create lists in a more elegant manner using list comprehension, where the needed equations are provided within the brackets of the list, defining what needs to be done to populate said list.")
list1 = []
for ex in range(6): list1.append(10 ** ex)
list2 = [10 ** ex for ex in range(6)]
print(list1)
print(list2)
print("\nA conditional expression is where an argument is provided that gives an if/else statement that determines which value is returned. When used in turn with list comprehension, it can turn into a generator.")
list = [ 1 if x % 2 == 0 else 0 for x in range(10) ]
print(list)
print("\nIn regard to using generators with list comprehension, if defined within brackets – it makes a comprehension; if defined within parentheses – it makes a generator. The difference between them is that comprehension makes a list, whereas generators do not – they simply return the values one by one instead of storing them.")
list = [ 1 if x % 2 == 0 else 0 for x in range(10) ]
genr = ( 1 if x % 2 == 0 else 0 for x in range(10) )
for v in list: print(v, end=" ")
print()
for v in genr: print(v, end=" ")
print()
print("\nLambda is a function without a function name that can be used to define a function intended for a very specific use (often a one-time use). Correctly using lambdas can allow programs to remain shorter and more efficient by removing the need for additional functions.\nWithout lambda: \n")
def printfunction(args, fun):
	for x in args: print('f(',x,')=',fun(x),sep='')
def poly(x): return 2 * x**2 - 4 * x + 2
printfunction([x for x in range(-2,3)], poly)
print("\nWith lambda: \n")
def printfunction(args, fun):
	for x in args: print('f(',x,')=',fun(x),sep='')
printfunction([x for x in range(-2,3)], lambda x: 2 * x**2 - 4 * x + 2)
print("\nThe map(function, list) function takes at least two arguments, applying the former function to the latter list and returns an iterator delivering all subsequent function results.")
list1 = [ x for x in range(5) ]
try:list2 = list(map(lambda x: 2 ** x, list1)) # The course example didn't work
except: list2 = tuple(map(lambda x: 2 ** x, list1))
print(list2)
for x in map(lambda x: x * x, list2): print(x, end=' ')
print("\n\nThe filter() function expects the same kind of arguments as map() but filters its second argument based on directions from the function specified. Every element which returns True from the function passes the filter.")
from random import seed, randint
seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = tuple(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)
print("\nclosure is a technique which allows the storing of values although the context in which they have been created does not exist anymore. By defining a function within a function, we can use it as an alternative way to return values to the outer function to be worked on.")
def makeclosure(par):
	loc = par
	def power(p): return p ** loc
	return power
fsqr = makeclosure(2)
fcub = makeclosure(3)
for i in range(5): print(i,fsqr(i),fcub(i))
print("\nWhen implementing your program to work with OS files, your instructions go through handles/streams. Connecting to the stream is called opening the file and disconnecting is closing the file.")
print("\nYou can work with files in three modes: read, write and update. The former two are self-explanatory while the latter means both.")
print("\nIf the file your program intends to work with hasn’t been initiated with constructors, the methods open() and close() can be used to do so.")
print("\nLinux/Unix systems end lines with ASCII code 10 (\\n) whereas Windows uses ASCII code 13 and 10 (\\r\\n). This difference is an obstacle when trying to write for all systems.")
print("\nAn automated way to change the newline characters to suit the required OS was created to alleviate developers of this issue.")
print("\nThe open(file, mode=’r’, encoding=None) method can take three parameters but requires at least the file argument.")
try:
    stream = open("C:\\Users\\James\\OneDrive - Solent University\\BSc (Hons) Cyber Security Management (BCSMF)\\Programming Essentials in Python\\File_Permissions.txt","rt")
    print("File opened!")
    stream.close()
except Exception as exc:
    print("Open failed: ",exc)
print("\nSys.stdin, stdout, stderr are exempt from needing to be opened with the open() function. Stdin is standard input and is normally associated with the keyboard. Input() uses this. Stdout is output and associated with the monitor. Stderr is error output and can be used to output errors elsewhere.")
print("\nThe .close() function takes no arguments and closes the stream its appended to.")
print("\nThe IOError object is equipped with a property named errno which returns a value which can be compared with predefined symbolic constants defined in the errno module.")
import errno
try: 
	stream = open("c:/users/user/Desktop/file.txt","rt")
	# actual processing goes here
	stream.close()
except Exception as exc:
	if exc.errno == errno.ENOENT: print("The file doesn't exist")
	elif exc.errno == errno.EMFILE: print("You've opened to many files")
	else: printf("The error number is",exc.errno)
print("\nThe sterror function from the OS module can accept errno’s and return a string explaining the error for us without having to write our own messages.")
from os import strerror
try: 
	stream = open("c:/users/user/Desktop/file.txt","rt")
	# actual processing goes here
	stream.close()
except Exception as exc: print("File could not be opened:",strerror(exc.errno))
print("\nOne example as how a file can be read is by using the read() function, which takes an argument to specify how many characters from the file you want to be returned.")
try:
	cnt = 0
	s = open("C:\\Users\\James\\OneDrive - Solent University\\BSc (Hons) Cyber Security Management (BCSMF)\\Programming Essentials in Python\\File_Permissions.txt","rt")
	ch = s.read(1)
	while ch != '':
		print(ch,end='')
		cnt += 1
		ch = s.read(1)
	s.close()
	print("Characters in file:", cnt)
except IOError as e: print("I/O error occurred: ", strerror(e.errno))
print("\nIn the previous example, one character was loaded into memory at a time and printed, but if no argument is provided to the read() function, it will try to load the entire file into memory at once. If the file is too large for the system memory to handle it can corrupt the OS.")
try:
	cnt = 0
	s = open("C:\\Users\\James\\OneDrive - Solent University\\BSc (Hons) Cyber Security Management (BCSMF)\\Programming Essentials in Python\\File_Permissions.txt",'rt')
	content = s.read()
	for ch in content:
		print(ch,end='')
		cnt += 1
	s.close()
	print("Characters in file:", cnt)
except IOError as e: print("I/O error occurred: ", strerr(e.errno))
print("\nAn alternative to read() is readline() which is self-explanatory and can also take a numerical argument.")
try:
	ccnt = lcnt = 0
	s = open('C:\\Users\\James\\OneDrive - Solent University\\BSc (Hons) Cyber Security Management (BCSMF)\\Programming Essentials in Python\\File_Permissions.txt','rt')
	line = s.readline()
	while line != '':
		lcnt += 1
		for ch in line:
			print(ch,end='')
			ccnt += 1
		line = s.readline()
	s.close()
	print("Characters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e: print("I/O error occurred: ", strerr(e.errno))
print("\nReadlines() is similar to readline() but can read more than 1 line at a time. It can be limited to only read lines beneath a particular size limit to protect against corruption.")
try:
	ccnt = lcnt = 0
	s = open('C:\\Users\\James\\OneDrive - Solent University\\BSc (Hons) Cyber Security Management (BCSMF)\\Programming Essentials in Python\\File_Permissions.txt','rt')
	lines = s.readlines(20)
	while len(lines) != 0:
		for line in lines:
			lcnt += 1
			for ch in line:
				print(ch,end='')
				ccnt += 1
		lines = s.readline(10)
	s.close()
	print("Characters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e: print("I/O error occurred: ", strerr(e.errno))
print("\nThe write() function is the opposite to read() and can also work on lines or characters but does not have newline characters by default, so those need to be created yourself if desired.")
try:
	fo = open('newtext.txt','wt')
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s: fo.write(ch)
	fo.close()
except IOError as e: print("I/O error occurred: ", strerr(e.errno))
try:
    fo = open('newtext.txt','rt')
    content = fo.read()
    for ch in content: print(ch,end='')
    fo.close()
except IOError as e: print("I/O error occurred: ", strerr(e.errno))
print("\nBytearray(bytes) can store binary data and isn’t a list nor a string, yet are mutable and subject of the len() function. They can only store integer byte elements between 0-255.")
data = bytearray(10)
for i in range(len(data)): data[i] = 10 + i
try:
	bf = open('file.bin', 'wb')
	bf.write(data)
	bf.close()
except IOError as e: print("I/O error occurred: ", strerr(e.errno))
print("\nThe readinto() function is used to read binary files and stores the data in a previously created bytearray.")
data = bytearray(10)
try:
	bf = open('file.bin', 'rb')
	bf.readinto(data)
	bf.close()
	for b in data: print(hex(b), end=' ')
except IOError as e: print("I/O error occurred: ", strerr(e.errno))
print("\n\nRead() can also read binary files but the data is immutable.")
try:
	bf = open('file.bin', 'rb')
	data = bytearray(bf.read())
	bf.close()
	for b in data: print(hex(b), end=' ')
except IOError as e: print("I/O error occurred: ", strerr(e.errno))
print("\nProviding an integer to the read() function will specify how many bytes will be read when used with a bytearray.")
srcname = input("Source file name?: ")
try: src = open(srcname, 'rb')
except IOError as e:
	print("Cannot open source file: ", strerror(e.errno))
	exit(e.errno)	
dstname = input("Destination file name?: ")
try: dst = open(dstname, 'wb')
except Exception as e:
	print("Cannot create destination file: ", strerr(e.errno))
	src.close()
	exit(e.errno)	
buffer = bytearray(65536)
total  = 0
try:
	readin = src.readinto(buffer)
	while readin > 0:
		written = dst.write(buffer[:readin])
		total += written
		readin = src.readinto(buffer)
except IOError as e:
	print("Cannot create destination file: ", strerr(e.errno))
	exit(e.errno)	
print(total,'byte(s) succesfully written')
src.close()
dst.close()
