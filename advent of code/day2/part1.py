import os
os.chdir("/workspace/Python/advent of code/day1")
with open("input.txt", "r") as input:
    lines = input.read().splitlines()

    depth = 0
    horizontal = 0
    for command in lines:
        if command.startswith("forward"):
            horizontal += int(command.split(" ")[1])
        elif command.startswith("up"):
            depth -= int(command.split(" ")[1])
        else:
            depth += int(command.split(" ")[1])
    print(depth*horizontal)
