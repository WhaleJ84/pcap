#!/usr/bin/env python3

##########################################################################################
#                                                                                        #
# Note that the mathematical equations calculated by this program are always left-sided, #
# meaning that BIDMAS or whatever it is has no power here.                               #
#                                                                                        #
# Future ideas for program:                                                              #
# - easy option for user to specify self.values number                                   #
# - latter operator influence based on former (i.e. if positive first, negative second)  #
# - save scores to an external .txt file and read best streaks                           #
# - timed questions                                                                      #
#                                                                                        # 
##########################################################################################

from random import randint as rint 
import operator as o

class qtemplate:
    def __init__(self):
        self.values = 3 # stops working correctly when higher than 9
        self.randop = ("+","-","*","%") # removed "/"
        self.ophist = tuple()

    def opchoice(self):
        self.temp = str(input("Would you like the operators to be randomly generated every iteration? (Y/n)"))
        if self.temp == "n" or self.temp == "N" or self.temp == "no" or self.temp == "No":
            self.specop = tuple(input("""Please enter {} operators without spaces, else ENTER for defaults.
+ addition
- subtraction
* multiplication
/ whole division
% integer division\n""".format(self.values-1)).replace(" ",""))
            self.operchoice = self.specop
        elif self.temp == "y" or self.temp == "Y" or self.temp == "yes" or self.temp == "Yes" or self.temp == "" or self.temp == " " or self.temp == "0":
            self.operchoice = self.randop

    def fillbuffer(self,values,rstart=1,rend=10):
        self.qbuffer = tuple()
        self.qbtlist = []
        self.qbtotal = 0
        for num in range(values):
            tuple1 = (rint(rstart,rend),)
            self.qbuffer += tuple1
        for num in range(len(self.qbuffer)):
            self.qbtlist.append(self.qbuffer[num])
        #self.qbtlist = list(self.qbuffer) # Can replace last 4 lines with this if code is redone
        #for num in range(len(self.qbtlist)):
            if num == 0: 
                self.qbtotal = self.qbuffer[num]
                print("DEBUG", self.qbtotal)
            else:
                self.opnum = rint(0, (len(self.operchoice)-1))
                self.operation(self.opnum)
                self.qbtotal = self.oper(self.qbtotal,self.qbuffer[num])
                print("DEBUG",self.qbtotal)
        if self.temp == "0": print("Debug cheat:",self.qbtotal)

    def operation(self,opnum=0):
        if len(self.ophist) <= (self.values-2):
            self.op = tuple(self.operchoice)
            if self.op[opnum] == "+":
                self.oper = o.add
            elif self.op[opnum] == "-":
                self.oper = o.sub
            elif self.op[opnum] == "*":
                self.oper = o.mul
            elif self.op[opnum] == "/":
                self.oper = o.truediv
            elif self.op[opnum] == "%":
                self.oper = o.floordiv
            else: print("{} is invalid.".format(self.op[opnum]))
            self.ophist += tuple(self.op[opnum],)

class scquestion(qtemplate):
    def __init__(self):
        super().__init__()
        self.successcount = 0
        self.errorcount = 0
        self.uanswer = ()
        self.opchoice()
        self.operation()
        self.fillbuffer(self.values)

    def singlechoicequestion(self):
        while self.errorcount != 3:
            try:
                print("\nWhat is {} ".format(self.qbuffer[0]),end="")
                for num in range(self.values - 1):
                    print("DEBUG:",self.values)
                    print("{} {} ".format(self.ophist[num],self.qbuffer[(num+1)]),end="")
                self.uanswer = input("\n")
                if float(self.uanswer) == round(self.qbtotal,1):
                    print("Correct.")
                    self.successcount +=1
                else:
                    print("Incorrect. The correct answer was:",round(self.qbtotal,1))
                    self.errorcount += 1
                self.ophist = tuple()
                self.fillbuffer(self.values)
            except KeyboardInterrupt as ki:
                break
            except ValueError as ve:
                print("{} is not a valid answer.".format(self.uanswer))
                self.errorcount += 1
        print("\nYour score was: {}\nThanks for playing!".format(self.successcount))

if __name__ == "__main__":
    quest = scquestion()
    quest.singlechoicequestion()
