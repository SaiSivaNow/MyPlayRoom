

def evaluate(first,oper,second):
    
    
    if oper == '+':
        return a


def countStrings(r, l):

    operators = []
    operands = []
    
    flag = True
    pointer = 0
    while flag and pointer < len(r):
        x=r[pointer]
        if x == '(':
            operands.append(x)

        elif x == ')':

            oper = operators.pop()
            first = operands.pop()
            second = operands.pop()
            operands.append(evaluate(oper,first,second))
            
            

        
