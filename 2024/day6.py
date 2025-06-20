file = open('day6.txt')
data = file.readlines()

graph = []

directions = [(-1,0), (0,1), (1,0), (0,-1)]

index = 0

height = len(data)
width = len(data[0])

visited = [[0] * width for i in range(height)]

for i in range(len(data)):
    line = data[i]
    # print(line)
    length = len(line)
    for j in range(len(line)):
        if line[j] == "^":
            location = (i,j)
    graph.append(line)

print(location)
# print(graph)
ret = 0

visited[location[0]][location[1]] = 1

while True:
    vertical, horizontal = directions[index]
    nextLocation = (location[0] + vertical, location[1]+horizontal)
    if nextLocation[0] >= height or nextLocation[0] < 0 or nextLocation[1] >= length or nextLocation[1] < 0:
        break
    if graph[nextLocation[0]][nextLocation[1]] == "#":
        index += 1
        index = index % 4
        vertical, horizontal = directions[index]
        nextLocation = (location[0] + vertical, location[1]+horizontal)
        # if nextLocation[0] >= height or nextLocation[0] < 0 or nextLocation[1] >= length or nextLocation[1] < 0:
        #     break
    # print(nextLocation)
    location = nextLocation
    visited[location[0]][location[1]] = 1

    
# for line in visited:
#     ret += sum(line)


# for line in graph:
#     print(line)

def check_cycle(obstacle_row, obstacle_col, graph, location):
    slow = location
    fast = location
    while True:
        vertical, horizontal = directions[index]
        nextLocation = (location[0] + vertical, location[1]+horizontal)
        if nextLocation[0] >= height or nextLocation[0] < 0 or nextLocation[1] >= length or nextLocation[1] < 0:
            return False
        if graph[nextLocation[0]][nextLocation[1]] == "#":
            index += 1
            index = index % 4
            vertical, horizontal = directions[index]
            nextLocation = (location[0] + vertical, location[1]+horizontal)
            # if nextLocation[0] >= height or nextLocation[0] < 0 or nextLocation[1] >= length or nextLocation[1] < 0:
            #     break
        # print(nextLocation)
        location = nextLocation
        visited[location[0]][location[1]] = 1


for i in range(height):
    for j in range(width):
        if check_cycle(i, j, graph, location):
            ret += 1

# print(ret)

#part 2... i could do it the hard way, and slow and fast, eventually if theres a cycle, it would catch up i would have to simulate each position having an obstacle

'''
def simulate_blocking(row, col, )
    while true:
        slow += position
        position += position
        fast += position
        if slow == fast:
            ret += 1:
        else if fast added positioning breaks:
            return
'''
