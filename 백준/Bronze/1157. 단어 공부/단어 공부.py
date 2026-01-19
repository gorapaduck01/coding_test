from collections import Counter

words = input()
upper_words = words.upper()

counts = Counter(upper_words)
largest = max(counts.values())

if list(counts.values()).count(largest) > 1:
    print("?")
    exit(0)

for item in counts:
    if counts[item] == largest:
        print(item)
        break