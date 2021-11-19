def enterInt(prompt, badInputPrompt):
    inputValue = 0
    badInput = True
    while(badInput):
        keyboardValue = input("Please enter a number: ")
        try:
            inputValue = int(keyboardValue)
            badInput = False
        except:
            print("That is not a number")

    return inputValue


#inval = enterInt("Please enter a number: ", "That is not a number")
# print(inval)


def convert(convertTo, originalAmount):
    if(convertTo == "metric"):
        return 2.24 * originalAmount
    if(convertTo == "imperial"):
        return originalAmount/2.24


testValues = [50, 20, 10, 5, 1]
for amount in testValues:
    converted = convert("metric", amount)
    print("amount: " + str(amount) + " result: " + "{0:.2f}".format(converted))
for amount in testValues:
    converted = convert("imperial", amount)
    print("imperial amount: " + str(amount) +
          " result: " + "{0:.2f}".format(converted))
