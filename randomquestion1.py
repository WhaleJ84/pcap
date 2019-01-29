from random import randint as rint 
import operator as o

class qtemplate:
    def __init__(self):
        self.count = 0
        self.values = 3 # stops working correctly when higher than 9
        self.op = tuple(input("Please enter {} operators without spaces, else ENTER for defaults.\n+,-,*,/,//\n".format(self.values-1)))
        #print("Debug 0")

    def fillbuffer(self,values,rstart=1,rend=10):
        self.qbuffer = tuple()
        self.qbtlist = []
        self.qbtotal = 0
        for x in range(values):
            tuple1 = (rint(rstart,rend),)
            self.qbuffer += tuple1
            #print("Debug 1",self.qbuffer)
        for x in range(len(self.qbuffer)): # Can be optimised by finding way to convert existing tuple into a new list.
            self.qbtlist.append(self.qbuffer[x])
            if x == 0:
                self.qbtotal = self.qbuffer[x]
                #print("Debug 5",self.qbtotal) 
            else:
                print("Debug",x,self.op)
                self.operation(x-1)
                self.qbtotal = self.oper(self.qbtotal,self.qbuffer[x])
            #print("Dedug 6", self.qbtotal)
        print("Debug 7",self.qbtlist,self.qbtotal)

    def operation(self,opx=0): 
        if self.op[opx] == "+":
            self.oper = o.add
        elif self.op[opx] == "-":
            self.oper = o.sub
        elif self.op[opx] == "*":
            self.oper = o.mul
        elif self.op[opx] == "/": # refine function to only require 1 decimal point.
            self.oper = o.truediv
        elif self.op[opx] == "//":
            self.oper = o.floordiv
        else:
            self.op = "+"
            self.oper = o.add
        print("Debug:",self.op)

class scquestion(qtemplate):
    def __init__(self):
        super().__init__()
        self.errorcount = 0
        self.uanswer = ()
        self.operation()
        self.fillbuffer(self.values)
        #print("Debug 2")

    def singlechoicequestion(self):
        while self.errorcount != 3:
            try:
                print("\nWhat is {} ".format(self.qbuffer[0]),end="")
                for x in range(self.values - 1):
                    print("{} {} ".format(self.op[x],self.qbuffer[(x + 1)]),end="")
                self.uanswer = input("\n")
                if float(self.uanswer) == self.qbtotal:
                    print("correct.")
                else:
                    print("Incorrect. The correct answer was:",self.qbtotal)
                    self.errorcount += 1
                self.fillbuffer(self.values)
                #print("Debug 4")
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
