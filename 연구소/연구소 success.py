# https://www.acmicpc.net/problem/14502
"""
바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다. (0: 빈 칸, 1: 벽, 2: virus)
새로 세울 수 있는 벽의 개수는 3개
안전 영역: 바이러스 X. 안전 영역 크기의 최댓값을 구하는 프로그램을 작성
"""
from collections import deque
from itertools import combinations

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

y_len, x_len = map(int, input().split())
virus_idx = []   # virus의 위치 담은 list
empty_li = []
result_res = []  # 가능한 안전 영역

path = []        # 전체 경로
for y in range(y_len):
    new_list = list(map(int, input().split()))
    path.append(new_list)
    for x in range(x_len):
        if new_list[x] == 2:
            virus_idx.append([x, y])
        elif new_list[x] == 0:
            empty_li.append([x, y])

# print("path: "+str(path))
empty_count = len(empty_li) - 3
# print("virus list: "+str(virus_idx))
# print("empty list: "+str(empty_li))

# 바이러스 퍼지게 하기
def bfs(virus_list, cur_path, zero_cnt):
    q = deque()
    for start_x, start_y in virus_list:
        q.append((start_x, start_y))
    # print("virus append: "+str(q))
    res = zero_cnt

    while q:
        x, y = q.popleft()

        for i in range(4):
            cur_x = x + dx[i]
            cur_y = y + dy[i]

            if 0 <= cur_x < x_len and 0 <= cur_y < y_len and cur_path[cur_y][cur_x] == 0:
                cur_path[cur_y][cur_x] = 2
                q.append((cur_x, cur_y))
                res = res - 1

    return res

for combi in combinations(empty_li, 3):
    # print("combi: ", str(combi))
    new_path = []
    for y in range(y_len):
        new_arr = []
        for x in range(x_len):
            new_arr.append(path[y][x])
        new_path.append(new_arr)

    for wall_x, wall_y in combi:
        new_path[wall_y][wall_x] = 1
    # print("new path: "+str(new_path))
    for_now = bfs(virus_idx, new_path, empty_count)
    # print("res: "+str(for_now))
    result_res.append(for_now)

result_res.sort()
# print("total res: "+str(result_res))
print(result_res[-1])

