for t in range(10):
    abc = input()
    arr = input()
    stack = []
    flag = 1
    for item in arr:
        if item == '(' or item == '{' or item == '[' or item == '<':
            stack.append(item)
        elif item == ']':
            if stack.pop() != '[':
                flag = 0
                break
        elif item == ')':
            if stack.pop() != '(':
                flag = 0
                break
        elif item == '}':
            if stack.pop() != '{':
                flag = 0
                break
        elif item == '>':
            if stack.pop() != '<':
                flag = 0
                break
                 
    print('#' + str(t+1), flag)
