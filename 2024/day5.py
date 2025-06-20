from collections import defaultdict, Counter, deque

file = open('day5.txt')
data = []
rules = []
orders = []
for line in file:
    if line.strip() == "":
        continue
    curr = line.split("|")
    if len(curr) == 2:
        rules.append(line.strip())
    curr = line.split(",")
    if len(curr) > 2:
        orders.append(line.strip())
    data.append(line)
# print(data)
# print(rules)
# print(orders)

preMap = defaultdict(set)
postMap = defaultdict(set)
for rule in rules:
    before, after = rule.split("|")
    preMap[before].add(after)
    postMap[after].add(before)

# print(preMap)

#for each item, check if it exists in a rule for the rest of the items after, if yes, break, if no return
ret = 0



for order in orders:
    pages = order.split(',')
    length = len(pages)
    found = False
    for i in range(length):
        curr = pages[i]
        for j in range(i+1, length):
            if pages[j] not in preMap:
                continue
            if curr in preMap[pages[j]]:
                found = True
                print(curr)
                # fix here but how do i fix it... whats the criterion its not a bubble swap right.. i have to pop at index and insert
                # print(pages[j])
    if not found:
        val = int(pages[length//2])
        # ret += val
        # print(val)
    else:
        new = []
        queue = deque([])
        dic = {key: len(preMap[key] & set(pages))}
        #some crap here
    
    

print(ret)