# https://www.acmicpc.net/problem/14503
"""
d: 0 (북쪽), 1 (동쪽), 2 (남쪽), 3 (서쪽)
"""
from collections import deque

y_len, x_len = map(int, input().split())
y, x, direction = map(int, input().split())
path = []

for _ in range(y_len):
    path.append(list(map(int, input().split())))
visited = [[False] * x_len for _ in range(y_len)]

# 북 -> 서 -> 남 -> 동
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def dfs(x, y, direc):
    q = deque()
    q.append((x, y, direc))
    visited[y][x] = True
    cnt = 1

    while q:
        x, y, direc = q.popleft()

        if not visited[y][x]:
            cnt = cnt + 1

        # for plus in range(direc + 1, direc + 5):
        #     cur_direction = plus % 4
        for idx in range(direc+3, direc-1, -1):
            cur_direction = idx % 4
            cur_x = x + dx[cur_direction]
            cur_y = y + dy[cur_direction]

            if 0 <= cur_x < x_len and 0 <= cur_y < y_len:
                if not visited[cur_y][cur_x] and path[cur_y][cur_x] == 0:
                    q.append((cur_x, cur_y, cur_direction))
                    cnt = cnt + 1
                    visited[cur_y][cur_x] = True
                    # print("x = {}, y = {}, direction: {}, cur_x: {}, cur_y: {}.".format(x, y, cur_direction, cur_x, cur_y))
                    break

        if not q:
            # print("뒤로 가기 실행")
            cur_direction = (direc + 2) % 4
            cur_x = x + dx[cur_direction]
            cur_y = y + dy[cur_direction]

            if 0 <= cur_x < x_len and 0 <= cur_y < y_len and path[cur_y][cur_x] == 0:
                q.append((cur_x, cur_y, direc))
                if not visited[cur_y][cur_x]:
                    visited[cur_y][cur_x] = True
                    cnt = cnt + 1
            else:
                return cnt
    return cnt

print(dfs(x, y, direction))
