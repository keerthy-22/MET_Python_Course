file = open("sample.txt", "r")

words = file.read().lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

file.close()
