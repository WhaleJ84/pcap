from random import randint as rint # gave randint an alias to prevent me from having to type random.randint every time.

class qtemplate:
    def __init__(self):
        self.qbuffer = []
        self.count = 0

    def fillbuffer(self,choices=2,rstart=1,rend=10):
        for x in range(choices):
            self.qbuffer.append(rint(rstart,rend))
        
class scquestion(qtemplate):
    def __init__(self):
        super().__init__()
        self.errorcount = ()
        self.uanswer = ()
        self.fillbuffer()

    def singlechoicequestion(self):
        try:
            while self.errorcount != 3:
                self.fillbuffer()
                self.uanswer = input("What is {} + {}? ".format(self.qbuffer[0],self.qbuffer[1]))
                if int(self.uanswer) == self.qbuffer[0] + self.qbuffer[1]:
                    print(self.uanswer,"is correct.")
                else:
                    print("Incorrect. The correct answer was:",self.qbuffer[0] + self.qbuffer[1])
                    self.errorcount += 1
        except KeyboardInterrupt as ki:
            print("Thanks for playing!")

# Automatically runs the program on start.
if __name__ == "__main__":
    quest = scquestion()
    quest.singlechoicequestion()
