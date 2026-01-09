num = int(input())
star = []


for i in range(0, num*2 -1, 1) :
    if i < num:
        star.append([])

        for _ in range(num -1 -i):
                star[i].append(' ')

        for j in range(i*2 + 1):
            star[i].append('*')

    else :
        star.append(star[(num * 2 - 2) - i])

for i in star :
    for j in i:
        print(j,end="")
    print()

