arr = [list(map(int, input().split())) for _ in range(9)]

max_list = []
max_idx = 0

for i in range(len(arr)):
    max_list.append([max(arr[i]), i+1, arr[i].index(max(arr[i]))+1])
    

max_num = max(max_list)


print(max_num[0])
print(max_num[1], max_num[2])