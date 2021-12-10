import os
os.chdir("/workspace/Python/advent of code/day1")
with open("input.txt","r") as input:
    lines= input.read().splitlines()
    temp= lines[0]
    lines= lines[1:]
    count=0
    for i in lines:
        if i > temp:
            count+=1
        temp=i
    print(count)

