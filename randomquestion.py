import random

def multiplechoicequestiontemplate(num_of_choices=2, rand_start=1, rand_end=10):
# NOTE: Starting with lists as the guestionbuffer. Later on with better knowledge, change to tuple to allow more complex values(e.g. floats, strings).
# NOTE: May alo need to change randint to provide things like floats and strings if possible.

    global questionbuffer, count #, num_of_choices, rand_end # removed to allow function parameter arguements to work
    questionbuffer = []
    questionpairs = []
    count = 0
    #operatorlist = [+, -, *, /, %, =, ==, !, ~, ++. --, <<, >>, <, <=, >, >=, !=, |, &&, ||, +=, -+, *=, /=, %=, &=, ^=, |=, >>=, <<=] # Doesn't work
    #num_of_choices = 2 #\
    #rand_start = 1 #----| removed in favour of function parameter arguements instead
    #rand_end = 10 #-----/

    for x in range(num_of_choices):
        questionbuffer.append(random.randint(rand_start,rand_end))
        if len(questionbuffer) % 2 == 0: # odd numbers
            while questionbuffer[0+count+1]!= questionbuffer[-1]:
                questionpairs.append(questionbuffer[0+count], questionbuffer[0+count+1])
                count += 1

        else: # even numbers
            while questionbuffer[0]+count != questionbuffer[-1]:
                    questionpairs.append(questionbuffer[0]+count)
                    questionpairs.append(questionbuffer[0]+count+1)
                    count += 1		
            else:
                    questionpairs.append(questionbuffer[0]+count)
    #print(questionbuffer,questionpairs,count) # for debugging

# NOTE: Doesn't seem to be adding the 2nd integer to questionbuffer

def multiplechoicequestion(): #---------------------------------------------------------\<- that didn't work
    errorcount = 0                                                                     #|
    #useranswer = "" #----------|created just to allow multiplechoicequestion() to loop |
    #while useranswer != -999: #|
    try:
        while errorcount != 3:                                                             #|
            multiplechoicequestiontemplate() #----------------------------------------------/find a way to link them
            useranswer = int(input("What is: {} + {}? ".format(questionbuffer[0],questionbuffer[1]))) # find a way to specify the operator and facilitate larger numebr of integers
            if useranswer == questionbuffer[0] + questionbuffer[1]:                                    # find a way to specify the operator 
                print(useranswer,"is Correct!")
            else:
                print("Incorrect. The correct answer was:", questionbuffer[0] + questionbuffer[1])     # find a way to specify the operator
                errorcount += 1
    except KeyboardInterrupt as ki:
        print("Thanks for playing!")

multiplechoicequestion()

# idea behind num_of_choices change:
#   always have num_of_choices[-1] be the end
#   for odd num_of_choices length:
#       have sections of 2 entries (e.g. num_of_choices[0], num_of_choices[1]) be input as  num_of_choices[-1] will correctly finish it
#   for even num_of_choices lenth:
#       have an if statement comparing final entry with num_of_choices[-1], if true, ?delete final entry?

# idea behind the operator:
# ???

