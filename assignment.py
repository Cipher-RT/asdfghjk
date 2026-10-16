# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.
from pickle import GLOBAL

# Exercise 1
Stack = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
TopOfStack = -1
# Write code here to fill Stack with 10 elements, all -1

def Push(DataToPush):
    # Write your code here
    global TopOfStack,Stack
    if TopOfStack==9:
        return False
    TopOfStack = TopOfStack +1
    Stack[TopOfStack]=DataToPush
    return True

    pass


def Pop():
    # Write your code here
    global TopOfStack,Stack
    if TopOfStack==-1:
        return -1
    TopOfStack = TopOfStack-1
    return Stack[TopOfStack+1]
    pass


# Exercise 2
def Peek():
    # Write your code here
    global TopOfStack,Stack
    if TopOfStack==-1:
        return -1
    return Stack[TopOfStack]
    pass


def IsEmpty():
    # Write your code here
    global TopOfStack,Stack
    if TopOfStack==-1:
        return True
    return False
    pass


def Size():
    # Write your code here
    global TopOfStack
    return TopOfStack+1
    pass


def ReverseList(Numbers):
    # Write your code here
    global TopOfStack,Stack
    for x in Numbers:
        if Push(x)!=True:
            print("Stack full")
            break
    Nums=[]
    for i in range(TopOfStack,-1,-1):
        Nums.append(Stack[i])
    return Nums
    pass

# Exercise 3
def Balanced(Expression):
    # Write your code here
    global Stack,TopOfStack
    Stack = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    TopOfStack = -1
    for chars in Expression:
        match chars:
            case '(':
                if Push(chars)!=True:
                    return False
            case '{':
                if Push(chars) != True:
                    return False
            case '[':
                if Push(chars) != True:
                    return False
            case ')':
                value=Pop()
                if value!='(' or value==-1:
                    return False
            case '}':
                value = Pop()
                if value!='{' or value==-1:
                    return False
            case ']':
                value = Pop()
                if value!='[' or value==-1:
                    return False
    if IsEmpty():
        return True
    return False
    pass
