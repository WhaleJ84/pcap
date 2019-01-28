from random import randint as rint # gave randint an alias to prevent me from having to type random.randint every time.

class qtemplate:
    def __init__(self):
        self.qbuffer = []
        self.count = 0
        #print("Debug 0")

    def fillbuffer(self,values=2,rstart=1,rend=10):
        for x in range(values):
            self.qbuffer.append(rint(rstart,rend))
            #print("Debug 1",self.qbuffer)

    def shufflebuffer(self,values=2,rstart=1,rend=10):
        for x in range(values):
            while self.count != len(self.qbuffer):
                 self.qbuffer[0+self.count] = rint(rstart,rend)
                 self.count += 1
                 #print("Debug 3",self.qbuffer)
        self.count = 0
        
class scquestion(qtemplate):
    def __init__(self):
        super().__init__()
        self.errorcount = 0
        self.uanswer = ()
        self.fillbuffer()
        #print("Debug 2")

    def singlechoicequestion(self):
        while self.errorcount != 3:
            try:
                self.uanswer = input("\nWhat is {} + {}? ".format(self.qbuffer[0],self.qbuffer[1]))
                if int(self.uanswer) == self.qbuffer[0] + self.qbuffer[1]:
                    print("correct.")
                else:
                    print("Incorrect. The correct answer was:",self.qbuffer[0] + self.qbuffer[1])
                    self.errorcount += 1
                self.shufflebuffer()
                #print("Debug 4")
            except KeyboardInterrupt as ki:
                break
            except ValueError as ve:
                print("{} is not a valid answer.".format(self.uanswer))
        print("\nThanks for playing!")

# Automatically runs the program on start.
if __name__ == "__main__":
    quest = scquestion()
    quest.singlechoicequestion()
