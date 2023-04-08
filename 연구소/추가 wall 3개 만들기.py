# combination 사용해 구현
from itertools import combinations

results = []
path = []  # 0인 부분 list
virus = []  # 2인 부분 list

n, m = map(int, input().split())
for i in range(n):
    path.append(list(map(int, input().split())))

# print("path: ")
# print(path)

def bfs(x, y, paths):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cur_x = x
    cur_y = y
    for idx in range(4):
        cur_x = cur_x + dx[idx]
        cur_y = cur_y + dy[idx]

        if 0 <= cur_x < n and 0 <= cur_y < m:
            if paths[cur_x][cur_y] == 0:
                paths[cur_x][cur_y] = 2
                bfs(cur_x, cur_y, paths)

road = []
for i in range(n):
    for j in range(m):
        location = path[i][j]
        if location == 0:
            road.append([i, j])
        elif location == 2:
            virus.append([i, j])

# print("\ncombi")

cnt = 0
# 벽으로 바꿀 3 장소 지정
for combi in combinations(road, 3):
    print(combi)
    cnt = cnt + 1

    new_path = []
    for idx in path:
        new_path.append(idx)

    for x, y in combi:
        new_path[x][y] = 1

    # 바이러스 유출 시키기
    for x, y in virus:
        bfs(x, y, new_path)

    # 개수 count
    res = 0
    for x in range(n):
        for y in range(m):
            if new_path[x][y] == 0:
                res = res + 1

    results.append(res)

results.sort()
print(results)
print(results[0])
