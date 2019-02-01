#!/usr/bin/env python3

from random import randint as rint 
import operator as o

class qtemplate:
    def __init__(self):
        self.values = 3 # stops working correctly when higher than 9
        self.randop = ("+","-","*","/","%")
        #self.specop = tuple(input("""Please enter {} operators without spaces, else ENTER for defaults.
#+ addition
#- subtraction
#* multiplication
#/ whole division
#% integer division\n""".format(self.values-1)).replace(" ", ""))
        #print("Debug qtemplate")

    def fillbuffer(self,values,rstart=1,rend=10):
        self.qbuffer = tuple()
        self.qbtlist = []
        self.qbtotal = 0
        for x in range(values):
            tuple1 = (rint(rstart,rend),)
            self.qbuffer += tuple1
            #print("Debug fillbuffer 1:",self.qbuffer)
        for x in range(len(self.qbuffer)): # Can be optimised by finding way to convert existing tuple into a new list.
            self.qbtlist.append(self.qbuffer[x])
            if x == 0:
                self.qbtotal = self.qbuffer[x]
                #print("Debug fillbuffer 2a:",self.qbtotal) 
            else:
                #print("Debug fillbuffer 2b:",x,self.op)
                self.operation(x-1)
                self.qbtotal = self.oper(self.qbtotal,self.qbuffer[x])
        #print("Debug fillbuffer 2c:",self.qbtlist,self.qbtotal)

    def operation(self,opx=0): 
        self.op = tuple(self.randop)
        if self.op[opx] == "+":
            self.oper = o.add
        elif self.op[opx] == "-":
            self.oper = o.sub
        elif self.op[opx] == "*":
            self.oper = o.mul
        elif self.op[opx] == "/":
            self.oper = o.truediv
        elif self.op[opx] == "%":
            self.oper = o.floordiv
        else: print("Debug operation else:",self.op)
        #print("Debug operation:",self.op)

class scquestion(qtemplate):
    def __init__(self):
        super().__init__()
        self.errorcount = 0
        self.uanswer = ()
        self.operation()
        self.fillbuffer(self.values)
        #print("Debug scquestion")

    def singlechoicequestion(self):
        while self.errorcount != 3:
            try:
                print("\nWhat is {} ".format(self.qbuffer[0]),end="")
                for x in range(self.values - 1):
                    print("{} {} ".format(self.op[x],self.qbuffer[(x + 1)]),end="")
                self.uanswer = input("\n")
                if float(self.uanswer) == round(self.qbtotal,2):
                    print("correct.")
                else:
                    print("Incorrect. The correct answer was:",self.qbtotal)
                    self.errorcount += 1
                self.fillbuffer(self.values)
                #print("Debug singlechoicequestion")
            except KeyboardInterrupt as ki:
                break
            except ValueError as ve:
                print("{} is not a valid answer.".format(self.uanswer))
                self.errorcount += 1
        print("\nThanks for playing!")

# Automatically runs the program on start.
if __name__ == "__main__":
    quest = scquestion()
    quest.singlechoicequestion()
