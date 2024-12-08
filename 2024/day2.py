'''
input = open("day2.txt")
ret = 0
for line in input:
    # print(line)
    nums = line.split(' ')
    curr = int(nums[0])
    ascend = True
    if int(nums[1]) < curr:
        ascend = False
    doAdd = True
    for i in range(1, len(nums)):
        new = int(nums[i])
        if ascend:
            if new - curr > 3 or new - curr <= 0:
                doAdd = False
                break
            curr = new
        else:
            if curr - new > 3 or curr - new <= 0:
                doAdd = False
                break
            curr = new
    if doAdd:
        ret += 1
        print("added to ret")

print(ret)
'''

input = open("day2.txt")
ret = 0
for line in input:
    # print(line)
    nums = line.split(' ')
    curr = int(nums[0])
    ascend = True
    if int(nums[1]) < curr:
        ascend = False
    doAdd = True
    for i in range(1, len(nums)):
        new = int(nums[i])
        if ascend:
            if new - curr > 3 or new - curr <= 0:
                doAdd = False
                break
            curr = new
        else:
            if curr - new > 3 or curr - new <= 0:
                doAdd = False
                break
            curr = new
    if doAdd:
        ret += 1
    else:
        for i in range(0, len(nums)):
            nums = line.split(' ')
            temp = nums.pop(i)
            curr = int(nums[0])
            ascend = True
            if int(nums[1]) < curr:
                ascend = False
            doAdd = True
            for i in range(1, len(nums)):
                new = int(nums[i])
                if ascend:
                    if new - curr > 3 or new - curr <= 0:
                        doAdd = False
                        break
                    curr = new
                else:
                    if curr - new > 3 or curr - new <= 0:
                        doAdd = False
                        break
                    curr = new
            nums.insert(i,temp)
            if doAdd:
                ret += 1
                break


print(ret)