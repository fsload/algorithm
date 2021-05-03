def step1(arr):
    Stack = []
    prStack = []
    for a in arr:
        if a.isdigit():
            prStack.append(a)
        elif a != ')':
            if a == '+':
                for i in range(len(Stack) - 1, -1, -1):
                    if Stack[i] != '(':
                        prStack.append(Stack.pop())
                    else:
                        break
                Stack.append('+')
            elif a == '*':
                for i in range(len(Stack) - 1, -1, -1):
                    if Stack[i] == '*':
                        prStack.append(Stack.pop())
                    else:
                        break
                Stack.append('*')
            else:
                Stack.append(a)
        elif a == ')':
            for i in range(len(Stack) - 1, -1, -1):
                if Stack[i] != '(':
                    prStack.append(Stack.pop())
                else:
                    Stack.pop()
                    break
    if len(Stack) != 0:
        item = Stack.pop()
        prStack.append(item)
    prStack = ''.join(map(str, prStack))
    return prStack
 
 
def step2(arr):
    toCal = []
    for a in arr:
        if a.isdigit():
            toCal.append(a)
        elif a == '+':
            n1 = toCal.pop()
            n2 = toCal.pop()
            n1, n2 = map(int, (n1,n2))
            n3 = n1 + n2
            toCal.append(n3)
        elif a == '*':
            n1 = toCal.pop()
            n2 = toCal.pop()
            n1, n2 = map(int, (n1,n2))
            n3 = n1 * n2
            toCal.append(n3)
    return n3
 
 
for t in range(10):
    num = input()
    arr = input()
    toPrint = step1(arr)
    result = step2(toPrint)
 
    print('#' + str(t+1), result)
