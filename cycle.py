word = input("Enter word: ")
symbol = input("Enter symbol: ")

count = 0
for i in word:
    if i == symbol:
        count += 1

print("Count:", count)
