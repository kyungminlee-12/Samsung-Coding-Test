# https://www.acmicpc.net/problem/16236
# 대부분의 답 다 맞음
# 거리가 같고 더 위에 있는거 찾을 때 오류 (왼 -> 위, 위 -> 오 일 때 나는 위 -> 우 를 선택! 답은 왼 -> 위)
from collections import deque

# 첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

N = int(input())
path = []
shark_x = 0
shark_y = 0

for y in range(N):
    new_list = list(map(int, input().split()))
    if 9 in new_list:
        shark_x = new_list.index(9)
        shark_y = y
    path.append(new_list)
path[shark_y][shark_x] = 0
# print("shark status: x = {}, y = {}".format(shark_x, shark_y))
# print("path: ", str(path))

res = 0

def bfs(x, y, fish, size, cur_res):
    cnt = cur_res
    res = cur_res
    fish_cnt = fish   # 먹은 물고기 count
    shark_size = size    # 아기 상어 크기
    visited = [[False]*N for _ in range(N)]
    visited[y][x] = True

    q = deque()
    q.append((x, y, cnt, res, fish_cnt, shark_size))

    print("new start: shark_size = {}, res = {}, x = {}, y = {}".format(shark_size, res, x, y))

    while q:
        x, y, cnt, res, fish_cnt, shark_size = q.popleft()
        # print("x: {}, y: {}, res: {}, cnt: {}".format(x, y, res, cnt))

        if 0 < path[y][x] < shark_size:
            res = cnt
            fish_cnt = fish_cnt + 1
            # print("도착! x = {}, y = {}, fish cnt = {}, res = {}, cnt = {}".format(x, y, fish_cnt, res, cnt))
            path[y][x] = 0
            # print("current path: ", str(path))

            if fish_cnt == shark_size:
                return bfs(x, y, 0, shark_size+1, res)
            return bfs(x, y, fish_cnt, shark_size, res)

        for idx in range(4):
            cur_x = x + dx[idx]
            cur_y = y + dy[idx]

            if 0 <= cur_x < N and 0 <= cur_y < N and not visited[cur_y][cur_x] and path[cur_y][cur_x] <= shark_size:
                if path[cur_y][cur_x] == 0 or path[cur_y][cur_x] == shark_size:
                    visited[cur_y][cur_x] = True
                q.append((cur_x, cur_y, cnt+1, res, fish_cnt, shark_size))

    return res


print(bfs(shark_x, shark_y, 0, 2, 0))
