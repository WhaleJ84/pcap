print("= is the assignment operator. == is the comparison operator. Both binary operators have left-sided binding.\n")
print("Comparing an int and a float that are both the same number (e.g. 2 == 2.) will return True.\n")
print("The comparison operator == has a low priority.\n")
print("""Other operators that can compare are: != < <= > >=.\nThis is the updated priority table.
+ -       | unary
**        |
* / %     |
+ -       | binary
< <= > >= |
== !=     |\n""")
print("You can use conditional statements to make decisions.\nConditional statements need their conditional keyword (if) followed by an expression (condition you’re querying) and a colon to end the line :.Instructions to be executed once conditions have been met are written beneath in an indented manner.\n")
print("Code that will be ran regardless of conditions should remain outside the indentation of statements.\n")
print("You can specify as many instructions to be executed within a statement as needed.\n")
print("else: statements are used to define what happens when a condition isn’t met.\n")
print("More than 1 if statement can be nested inside another.\n")
print("For a conditional statement to work, the use of a single if statement is required at the top of the cascade. If needed, as many elif statements can be used to specify other conditions beneath the if, and finally the use of a single else statement can be used at the very bottom of the cascade.\nif there is an else branch in the cascade, only one of all the branches is executed. if there is no else branch, it’s possible than none of the available branches is executed.\n")
print("If there is only one instruction after a statement, it may be placed on the same line as the condition, after the comma.\n")
#if conditional_expression: print("This is an if statement\nI am required in all if statements.")
#elif conditional_expression: print("Example text")
#elif conditional_expression:
#    print("This is an elif statment\nAs long as there is no else statement beneath me, its possible none of us will be ran.")
#    print("If I didn't have this additional instruction, the above instruction could be on the same line as elif.")
#else: print("This is an else statement.\nBecause I exist, only one branch will execute.")
print("if performs its statements only once; while repeats the execution as long as the condition evaluates to True.")
print("For loops can be used to repeat a task a specific number of times.\n")
print("For = loop keyword, I = control variable, in = syntax element, range = function argument, (100) = function parameter.\n")
print("The range parameter updates the control variable after every iteration specified in the function parameter.\n")
print("The range function can accept up to three parameters; start int, end count and int increment. (e.g. range(2,8,3) will start at number 2, end at number 8 but increment by 3)\n")
print("The break command finishes and exits the loop, going onto the next bit of code.\n")
print("The continue command skips onto the next bit of code as if the current had finished.\n")
print("Else commands can also be used with while and for statements.\n")
print("And statements are conjunctions.\nOr statements are disjunctions.\nBoth the above are logical operators.\n")
print("""And statements are binary operators with a lower priority than ones expressed with comparison operators.\nAnd truth table
Left  | Right | L AND R
False | False | False
False | True  | False
True  | False | False
True  | True  | True\n""")
print("""Or statements are binary operators with a lower priority than and.\nOr truth table
Left  | Right | L OR R
False | False | False
False | True  | True
True  | False | True
True  | True  | True\n""")
print("""Not statements are unary operators with a very high priority along with unary +/-.\nNot truth table
Arg   | NOT Arg
False | True
True  | False\n""")
print("Bitwise operators manipulate single bits of data whereas logical operators take their arguments as a whole.\n& (ampersand) is the bitwise conjunction operator that requires exactly two 1’s to provide 1 as the result.\n| (bar) is the bitwise disjunction operator that requires at least one 1 to provide 1 as the result.\n^ (carat) is the bitwise exclusive (xor) operator that requires exactly one 1 to provide 1 as the result.\nBitwise operators can only be performed on integers.\n")
print("~ (tilde) is the bitwise negation operator that inverts the bits.\n", ~3,"\n")
print("""FlagRegister = 0x1234 (4660 in decimal, 0001 0010 0011 0100 in binary)
TheMask = 8 (the 8th bit (i.e. 1000))
‭‭0001 0010 0011 0100‬  4660
1110 1101 1100 0011 -4669
iiii iiii iiii xiii FlagRegister ^= ~TheMask: inverts all bits but the mask, resulting in negative value.

0001 0010 0011 0100‬  4660
‭0001 0010 0011 1100‬  4668
0000 0000 0000 i000 FlagRegister ^= TheMask: inverts mask bit.

‭0001 0010 0011 0100‬  4660
1111 1111 1111 0111    -9
ssss ssss ssss xsss FlagRegister |= ~TheMask: sets all bits but the mask, resulting in negative value.

0001 0010 0011 0100‬  4660
‭0001 0010 0011 1100‬  4668
0000 0000 0000 s000 FlagRegister |= TheMask: sets mask bit.

0001 0010 0011 0100‬  4660
0001 0010 0011 0100‬  4660
cccc cccc cccc xccc FlagRegister &= ~TheMask: checks all bits but the mask.

0001 0010 0011 0100‬  4660
0000 0000 0000 0000‬     0
0000 0000 0000 c000 FlagRegister &= TheMask: checks mask bit.\n""")
int1 = 17
intR = int1 >> 1
intL = int1 << 2
print("<< and >> are shifting operators shift all bits however many bits specified to whatever direction defined.\n", int1,intL,intR,"\n0001 0001\n0100 0100\n0000 1000\n")
print("""Updated table of operator priorities.
! ~ (type) ++ -- + -              | unary
* / %                             |
+ -                               | binary
<< >>                             |
< <= > >=                         |
== !=                             |
&                                 |
|                                 |
&&                                |
||                                |
= += -= *= /= %= &= ^= |= >>= <<= |\n""")
print("Variables that only hold one value are sometimes called scalars.\n")
numbers = [10,5,7,2,1]
print("Lists are variables that can contain multiple values at once, including strings, integers, floats, lists and more.\nEach item in a list is assigned a number, starting from 0.\nA list is a collection of elements, but each element is a scalar.\n",numbers,"\n")
numbers[0] = 111
print("You can edit individual values by specifying the assigned number in the brackets.\n",numbers,"\n")
numbers[1] = numbers[4]
print("Values can be copied from pre-existing items in a similar way.\n",numbers,"\nThe value inside the brackets which selects one element of the list [num] is called an index.\n")
print("You can access individual values from a list by specifying that value in the index.\n", numbers[0],"\n")
print("You can return the length of a list using the len() (length) function.\n", len(numbers),"\n")
del numbers[1]
print("Items can be deleted from a list with the del instruction and specifying the item in the index.\n",numbers,"\n")
print("Negative numbers can be used in the index [] to select numbers in reverse. For example [-3] will select the 3rd from last item in a list.\n",numbers[-3],"\n")
print("A function doesn’t belong to any data – it gets data, it may create new data and it (generally) produces a result.\nA method does all these things but is also able to change the state of a selected entity. A method is owned by the data it works for, while a function is owned by the whole code.\n")
print("A typical method invocation usually looks like: result = data.method(arg).\n")
numbers.append(5)
print("Append(). is a method that can be used to add items onto the end of an existing list, increasing its length by one.\n",numbers,"\n")
numbers.insert(0,23)
print("The insert(). method can be used to specify where to add what inside a list with (where,what) and will shift all existing items over a number in the list.\n",numbers,"\n")
print("Empty lists can be created using empty brackets [].\n")
sum = 0
for i in range(len(numbers)): sum += numbers[i]
print("You can use len() on a list in a loop to run the loop on every item in the list regardless of size without having to manually specify the number of loops required.\n",sum,"\n")
sum = 0
for i in numbers: sum += i
print("It may be more efficient to run without len() and use the entire list variable instead.\n",sum,"\n")
numbers[0], numbers[5] = numbers[5], numbers[0]
numbers[1], numbers[4] = numbers[4], numbers[1]
numbers[2], numbers[3] = numbers[3], numbers[2]
print("You can rearrange variables manually using this template.\n",numbers,"\n")
n = len(numbers)
for i in range(n//2): numbers[i], numbers[n-i-1] = numbers[n-i-1],numbers[i]
print("You can rearrange variables in a list of any length using this template.\n",numbers,"\n")
numbers.sort()
print(".sort() is a method that can be used to sort a list as fast as possible.\n",numbers,"\n")
numbers1 = numbers
print("Lists can be stored within lists.\n",numbers1,"\nThe name of an ordinary variable is the name of its content.\nThe name of a list is the name of a memory location where the list is stored.\n")
numbers1 = numbers[:]
numbers.append(11)
print(": (colon) is the slice element that can be used to copy elements.\n",numbers1, numbers,"\n")
numbers2 = numbers[0:5]
print("Start and end positions can be added to the slice to specify where within the list will be copied. [start:end] 0 begins copying from the beginning, but 5 stops at 5-1. Negative values can also be used akin to indexing.\n",numbers2,"\n")
print("Start is the index of the first element included in the slice. End is the index of the first element not included in the slice.\n")
print("If the start specifies an element lying further than the one described by the end (from the list’s beginning point of view), the slice will be empty.\n")
numbers3 = numbers[:4]
print("0’s in the starting slice can be omitted.\n",numbers3,"\n")
numbers4 = numbers[2:]
print("Similarly, the ending slice can be omitted if you want to slice at the end of the element.\n",numbers4,"\n")
del numbers4[1:3]
print("You can delete slices with the del instruction also, specifying start and end points if desired.\n",numbers4,"\n")
print("The in and not in operators can be used to check whether specific values are stores within a list or not.\nIs 11 in list:", 11 in numbers4,"Is 5 not in list: ",5 not in numbers4,"\n")
print("List comprehension can be used to fill out massive lists during program execution.\n")
EMPTY = ""
board = [[EMPTY for i in range(8)] for j in range(8)]
print("Using list comprehension, it is possible to create a two-dimensional array, which is sometimes called a matrix.\n",board,"\n")
board[2][3] = "X"
print("To access specific data within the matrix, you need to specify the [row] and the [field number within the row (column)] starting from 0.\n",board,"\n")

