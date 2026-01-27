nums, B = map(int, input().split())
result = 0
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums_cp = nums
arr = []

while nums_cp > 0:
    nums_cp, rest = divmod(nums_cp, B)
    arr.append(tmp[rest])

arr.reverse()
print("".join(arr))

