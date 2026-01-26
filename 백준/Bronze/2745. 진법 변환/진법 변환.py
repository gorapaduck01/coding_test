N, B = input().split()
B = int(B)

result = 0
sq = 0

for i in range(len(N)):
    c = N[len(N)-1-i]
    sq = B**i
    NN = int(c) if c.isdigit() else ord(c) - 55
    result += NN *sq

print(result)