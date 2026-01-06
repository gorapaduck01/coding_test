num_list = [int(input()) for _ in range(3)]
str_list = [str(num_list[i]) for i in range(3)]

def sum_num(num):
    res = num[0] + num[1] - num[2]
    return res

def sum_str(str):
    subset = str[0:2]
    res = int("".join(subset)) - int(str[2])
    return res

res1 = sum_num(num_list)
res2 = sum_str(str_list)

print(res1)
print(res2)