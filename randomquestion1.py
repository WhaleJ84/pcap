from random import randint as rint # gave randint an alias to prevent me from having to type random.randint every time.

class qtemplate:
    def __init__(self):
        self.count = 0
        self.values = 2
        #print("Debug 0")

    def fillbuffer(self,values,rstart=1,rend=10):
        self.qbuffer = tuple()
        for x in range(values):
            tuple1 = (rint(rstart,rend),)
            self.qbuffer += tuple1
            #self.qbuffer.append(rint(rstart,rend))
            #print("Debug 1",self.qbuffer)

class scquestion(qtemplate):
    def __init__(self):
        super().__init__()
        self.errorcount = 0
        self.uanswer = ()
        self.fillbuffer(self.values)
        #print("Debug 2")

    def singlechoicequestion(self,values):
        while self.errorcount != 3:
            try:
                print("\nWhat is {} ".format(self.qbuffer[0]),end="")
                for x in range(values - 1):
                    print("+ {} ".format(self.qbuffer[(x + 1)]))
                self.uanswer = input()
                if int(self.uanswer) == self.qbuffer[0] + self.qbuffer[1]:
                    print("correct.")
                else:
                    print("Incorrect. The correct answer was:",self.qbuffer[0] + self.qbuffer[1])
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
    quest.singlechoicequestion(2)
