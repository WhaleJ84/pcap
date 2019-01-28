from random import randint as rint # gave randint an alias to prevent me from having to type random.randint every time.

class qtemplate:
    def __init__(self):
        self.count = 0
        self.values = 9 # stops working correctly when higher than 9
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
            self.qbtotal += self.qbuffer[x]
        print("Debug 5",self.qbtlist,self.qbtotal)

class scquestion(qtemplate):
    def __init__(self):
        super().__init__()
        self.errorcount = 0
        self.uanswer = ()
        self.fillbuffer(self.values)
        #print("Debug 2")

    def singlechoicequestion(self):
        while self.errorcount != 3:
            try:
                print("\nWhat is {} ".format(self.qbuffer[0]),end="")
                for x in range(self.values - 1):
                    print("+ {} ".format(self.qbuffer[(x + 1)]),end="")
                self.uanswer = input("\n")
                if int(self.uanswer) == self.qbtotal:
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
