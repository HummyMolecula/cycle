word = input("Enter word: ")
symbol = input("Enter symbol: ")
whileIndex = int(input("While index < "))

count = 0
index = 0
while index < whileIndex:
    for i in word[index]:
        if i == symbol:
            count += 1
    index += 1

print("Count:", count)
