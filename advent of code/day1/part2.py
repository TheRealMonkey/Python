import os
os.chdir("/workspace/Python/advent of code/day1")
with open("input.txt","r") as input:
    lines= [0,0]+input.read().splitlines()#input.read().splitlines()
    lines= [int(line) for line in lines]

    temp= lines[2]
    count=0
    for i in range(len(lines)):
        total_sum = sum(lines[i:i+3])
        if total_sum>temp:
            count+=1

        temp= total_sum
    print(count-2)

