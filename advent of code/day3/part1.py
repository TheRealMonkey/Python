import os
os.chdir("/workspace/Python/advent of code/day3")
with open("input.txt", "r") as file:
    lines = ["111000111001", "110001000011",
             "100000110100"]  # file.read().splitlines()
    zero_values = [0 for x in range(1, 13)]
    one_values = [0 for x in range(1, 13)]
    final = ""
    for line in lines:
        temp = 0
        for index in line:
            if int(index) == 0:
                zero_values[temp] += 1
            else:
                one_values[temp] += 1
            temp += 1

    for i in range(0, 12):

        if zero_values[i] > one_values[i]:
            final += "0"
        else:
            final += "1"
    print(int(final,2)*22)
