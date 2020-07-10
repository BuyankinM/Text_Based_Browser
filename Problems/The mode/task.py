from collections import Counter

inp_list = input().split()
c = Counter(inp_list)
print(c.most_common(1)[0][0])