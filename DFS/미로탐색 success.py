# https://www.acmicpc.net/problem/2178
"""
1은 이동 가능, 0은 이동 불가능
(1, 1) ~ (N, M) 이동 시 지나야 하는 최소의 칸 수를 구하는 프로그램
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동 가능
15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함
"""
from collections import deque
# 주의: 공백으로 분리된 것은 split(), 아닌 것은 input()만 해야 list로 변경 가능
len_y, len_x = map(int, input().split())
path = []

for i in range(len_y):
    path.append(list(map(int, input())))

visited = [[False]*len_x for _ in range(len_y)]

# print("visited: ", str(visited))
# print("path: ", str(path))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    q = deque()
    q.append((x, y, 1))
    visited[y][x]=True

    while q:
        x, y, cnt = q.popleft()

        if (x, y) == (len_x-1, len_y-1):
            return cnt

        for i in range(4):
            cur_x = x + dx[i]
            cur_y = y + dy[i]
            # print("cur x: {}, cur y: {}".format(cur_x, cur_y))

            if 0 <= cur_y < len_y and 0 <= cur_x < len_x:
                if not visited[cur_y][cur_x] and path[cur_y][cur_x]!=0:
                    q.append((cur_x, cur_y, cnt+1))
                    visited[cur_y][cur_x]=True


print(dfs(0, 0))