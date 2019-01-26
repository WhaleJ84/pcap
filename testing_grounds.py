import random

#for x in range(10):
#    print(random.randint(1,101)*5)

def multiplechoicequestiontemplate():
#    questbuffer = []
#    for x in range(VARIABLE PER QUEST):
#        questbuffer.append(random.randint(start,end))

#        answ = input("What is:", questbuffer(0), questoperator(VARIABLE PER QUEST), questbuffer(1))
#        if answ == TOTAL OF QUESTION ABOVE:
#            print("Well done! That is correct!")
#        else:
#            print("Incorrect. The answer was:", TOTAL OF QUESTION ABOVE, "\nThe explanation of this is...")

# NOTE: Starting with lists as the guestbuffer. Later on with better knowledge, change to tuple to allow more complex answers.
# NOTE: May alo need to change randint to provide things like floats and strings if possible.

    global num_of_choices, rand_start, rand_end, questionbuffer    # list of variables that will need to be used by other functions using the template
    questionbuffer = []                                            # stores a range of random integers of whose quantity is defined by num_of_choices
    #operatorlist = [+, -, *, /, %, =, ==, !, ~, ++. --, <<, >>, <, <=, >, >=, !=, |, &&, ||, +=, -+, *=, /=, %=, &=, ^=, |=, >>=, <<=]
    num_of_choices = 2                                             # defines the number of random integers that will be stored in the questionbuffer list
    rand_start = 1                                                 # specifies what number the randint range will start at
    rand_end = 10                                                  # specifies what number the randint range will end at

    for x in range(num_of_choices):                                # runs the following program a number of times determined by the num_of_choices variable
        questionbuffer.append(random.randint(rand_start,rand_end)) # adds random numbers to the questionbuffer list determiend by the rand_start and rand_end variables
    print(questionbuffer)                                          # prints list for debug

def multiplechoicequestion():
    multiplechoicequestiontemplate()
    useranswer = int(input("What is: {} + {}? ".format(questionbuffer[0],questionbuffer[1])))
    if useranswer == questionbuffer[0] + questionbuffer[1]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer was:", questionbuffer[0] + questionbuffer[1])

multiplechoicequestion()
