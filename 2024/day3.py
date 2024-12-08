import re
data = open("day3.txt")
ret = 0
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

multiply = True
for line in data:
    line = line.strip()
    commands = re.findall(pattern, line)
    for command in commands:
        if command == "don't()":
            print("switch to false")
            multiply = False
        elif command == "do()":
            print("switch to true")
            multiply = True
        else:
            if multiply:
                left, right = re.findall(r"\d+", command)
                print(left, right)
                ret += int(left)*int(right)
            else:
                print("false",command)
    print(commands)
print(ret)
    
