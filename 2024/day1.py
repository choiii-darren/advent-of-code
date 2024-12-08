"""
input = open("day1.txt")
leftHeap = []
rightHeap = []
ret = 0
for line in input:
    left, right = line.split('   ')
    leftHeap.append(left)
    rightHeap.append(right)

leftHeap.sort()
rightHeap.sort()

for i in range(len(leftHeap)):
    ret += abs(int(rightHeap[i]) - int(leftHeap[i]))

print(ret)
"""
input = open("day1.txt")
leftMap = {}
rightMap = {}
ret = 0
for line in input:
    left, right = line.split('   ')
    left = int(left)
    right = int(right)
    if left not in leftMap:
        leftMap[left] = 0
    leftMap[left] += 1
    if right not in rightMap:
        rightMap[right] = 0
    rightMap[right] += 1
# print(leftMap)
# print(rightMap)

for key, value in leftMap.items():
    if key in rightMap:
        ret += key * rightMap[key]
print(ret)


