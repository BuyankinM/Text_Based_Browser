from collections import deque

d = deque()
inp = input()

for c in inp:
    if c == "(":
        d.append(c)
    elif c == ")":
        if d:
            d.pop()
        else:
            print("ERROR")
            break
else:
    if not d:
        print("OK")
    else:
        print("ERROR")
