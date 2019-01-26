from random import randint as rint # gave randint an alias to prevent me from having to type random.randint every time.

class mcqtemplates:
    def __init__(self):
        global qbuffer, count   # might not need.
        self.qbuffer = []
        #qpairs = []   # what did I need this for?
        self.count = 0

    def fillbuffer(self,choices=2,rstart=1,rend=10):
        for x in range(choices):
            self.qbuffer.append(rint(rstart,rend))
        
o = mcqtemplates
o()

print(o.qbuffer)
