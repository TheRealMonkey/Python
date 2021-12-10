import os
os.chdir("/workspace/Python/advent of code/day2")
with open("input.txt", "r") as input:
    lines = input.read().splitlines()

    aim = 0
    horizontal = 0
    depth = 0
    for command in lines:

        x = int(command.split(" ")[1])

        if command.startswith("forward"):
            horizontal += x
            depth += aim*x
        elif command.startswith("up"):
            aim -= x
        else:
            aim += x
    print(depth*horizontal)
