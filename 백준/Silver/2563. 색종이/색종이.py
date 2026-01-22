#수학적으로 겹치는 넓이를 계산해서 빼는 방법은 생각보다 훨씬 복잡합니다 (위에서 말한 3중 겹침 등).
# 대신 문제 제목이 '색종이'이고 도화지의 크기가 $100 \times 100$으로 고정되어 있다는 점에 주목해 보세요.
# 힌트: 도화지를 **거대한 2차원 리스트(행렬)**라고 생각하고, 색종이가 붙은 칸을 0에서 1로 색칠한다고 상상해 보세요. 
# 이미 1로 칠해진 곳에 다른 색종이가 올라와도 그 칸은 여전히 1이겠죠? 마지막에 1의 개수만 세면 어떻게 될까요?

count = int(input())
paper = [list(map(int,input().split())) for _ in range(count)]

# 전체 도화지 100*100 배열 선언
rows,cols = 100,100
area = [[0 for _ in range(cols)] for _ in range(rows)]

for i, (x,y) in enumerate(paper):
    for row in range(x, x + 10):
        for col in range(y,y+10):
            area[row][col] = 1

total_sum = 0

total_sum = sum(sum(row) for row in area)

print(total_sum)