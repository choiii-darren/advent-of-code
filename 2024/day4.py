
data = open("day4.txt")
xlocations = set()
data = data.readlines()
height = len(data)
length = 0
# print(data)
for i in range(len(data)):
    line = data[i]
    # print(line)
    length = len(line)
    for j in range(len(line)):
        if line[j] == "A":
            xlocations.add((i, j))

# print(xlocations)

'''

directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]


mapping= {
    "X": "M",
    "M":"A",
    "A":"S"
}
ret = {"XMAS": 0}

def direction_search(row, col, curr, ret, direction):
    # print(row, col, curr)
    if curr == "XMAS":
        ret[curr] += 1
    else:
        last = curr[-1]
        vertical, horizontal = directions[i]
        # print(vertical, horizontal)
        if row + vertical == height or row + vertical < 0 or col + horizontal == length or col + horizontal < 0:
            return
        # print(data[row + vertical][col+horizontal])
        if data[row + vertical][col + horizontal] == mapping[last]:
            
            direction_search(row + vertical, col + horizontal, curr + mapping[last], ret, direction)

for row, col in xlocations:
    for i, value in enumerate(directions):
        horizontal = value[1]
        vertical = value[0]
        if row + vertical == height or row + vertical < 0 or col + horizontal == length or col + horizontal < 0:
            continue
        if data[row + vertical][col + horizontal] == mapping["X"]:
            print(i, value, row, col)
            direction_search(row + vertical, col + horizontal, "X" + mapping["X"], ret, i)
'''

directions = [(1,1), (1,-1), (-1,1), (-1,-1)]

backslash = [
    (1,1),
    (-1,-1)
]
forwardslash = [
    (1,-1), (-1,1)
]

mapping= {
    "X": "nah",
    "M":"S",
    "S":"M",
    "A":"nah"
}

ret = {"XMAS": 0}


def check_xmas(row, col, ret):
    letter_count = {}
    vertical1, horizontal1 = backslash[0]
    vertical2, horizontal2 = backslash[1]

    print(row, col, "new point")
    if row + vertical1 == height or row + vertical1 < 0 or col + horizontal1 == length or col + horizontal1 < 0 or row + vertical2 == height or row + vertical2 < 0 or col + horizontal2 == length or col + horizontal2 < 0:
        return
    
    if data[row + vertical1][col+horizontal1] != mapping[data[row+vertical2][col+horizontal2]]:
        return
    print(data[row + vertical1][col+horizontal1], data[row+vertical2][col+horizontal2] )
    
    vertical1, horizontal1 = forwardslash[0]
    vertical2, horizontal2 = forwardslash[1]

    if row + vertical1 == height or row + vertical1 < 0 or col + horizontal1 == length or col + horizontal1 < 0 or row + vertical2 == height or row + vertical2 < 0 or col + horizontal2 == length or col + horizontal2 < 0:
        return

    print(data[row + vertical1][col+horizontal1], data[row+vertical2][col+horizontal2] )

    
    if data[row + vertical1][col+horizontal1] != mapping[data[row+vertical2][col+horizontal2]]:
        return
    print(row, col, "found")
    ret["XMAS"] += 1

for row, col in xlocations:
    check_xmas(row, col, ret)

print(ret)