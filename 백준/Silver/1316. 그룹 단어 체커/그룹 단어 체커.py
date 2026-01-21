count = int(input())
result = count

for _ in range(count):
    word = input()
    for j in range(len(word) - 1):
        if word[j] != word[j+1]:
            if word[j] in word[j+1:]:
                result -= 1
                break

print(result)