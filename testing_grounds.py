import operator as o

op = input("""+ - addition
- - subtraction
* - multiplication
/ - division\n""")

def question(operation = o.add):
    a=int(input("What is 2 {} 2? ".format(op)))
    if a == oper(2,2):
        print(":)")
    else:
        print(":(")
    
if op == '+':
    oper = o.add
elif op == '-':
    oper = o.sub
elif op == '*':
    oper = o.mul
elif op == '/':
    oper = o.truediv

question(oper)
