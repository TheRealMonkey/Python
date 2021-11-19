def enterInt(prompt, badInputPrompt):
    inputValue = 0
    inputValue = 0
    badInput = True
    while(badInput):
        keyboardValue = input(prompt)
        try:
            inputValue = int(keyboardValue)
            badInput = False
        except:
            print(badInputPrompt)
    return inputValue

#inval = enterInt("Please enter a number: ", "That is not a number")
# print(inval)


def convert(convertTo, originalAmount):

    if(convertTo == "metric"):
        return 2.24 * originalAmount
    if(convertTo == "imperial"):
        return originalAmount/2.24


for x in ["metric", "imperial"]:
    for i in [50, 20, 10, 5, 1]:
        print(f"{i} converted to {x} is {convert(x, i):.2f}")
