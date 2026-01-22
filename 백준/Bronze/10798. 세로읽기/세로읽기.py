toys = [input() for _ in range(5)]

for j in range(15):
    for i in range(len(toys)):
        if j < len(toys[i]):
            print(toys[i][j], end='')