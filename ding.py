with open("dong.txt", "r") as file:
    lines = file.read().splitlines()
    final = []
    for i in lines:
        item = i+(" "*(82-len(i)))
        final.append("${bb}"+item+"${bo}")
    with open("ding.txt", "w") as file1:
        file1.write("\n".join(final))
