file = open("sample.txt", "r")

data = file.read().lower()

word = input("Enter word: ").lower()

count = data.split().count(word)

print("Occurrences:", count)

file.close()
