# https://www.acmicpc.net/problem/16236
# 대부분의 답 다 맞음
# 거리가 같고 더 위에 있는거 찾을 때 오류 (왼 -> 위, 위 -> 오 일 때 나는 위 -> 우 를 선택! 답은 왼 -> 위)
from collections import deque

# 첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

N = int(input())
path = []     # 물고기 위치
shark_x = 0
shark_y = 0

for y in range(N):
    new_list = list(map(int, input().split()))
    if 9 in new_list:
        shark_x = new_list.index(9)
        shark_y = y
    path.append(new_list)
path[shark_y][shark_x] = 0

def bfs(x, y, fish_cnt, shark_size, cur_res):

    cnt = 0
    q=deque()
    q.append((x, y, cnt, cur_res, fish_cnt, shark_size))   # cnt: 이동 거리, res: 총 이동 거리

    res_li = []
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True
    final_cnt = N*N

    while q:
        x, y, cnt, res, fish_cnt, shark_size = q.popleft()

        if cnt >= final_cnt:
            continue

        for i in range(4):
            cur_x = x + dx[i]
            cur_y = y + dy[i]

            if 0 <= cur_x < N and 0 <= cur_y < N and not visited[cur_y][cur_x]:
                if path[cur_y][cur_x] == 0 or path[cur_y][cur_x] == shark_size:
                    visited[cur_y][cur_x] = True
                    q.append((cur_x, cur_y, cnt + 1, res, fish_cnt, shark_size ))
                elif 0 < path[cur_y][cur_x] < shark_size:
                    visited[cur_y][cur_x] = True
                    res = res + cnt + 1
                    fish_cnt = fish_cnt + 1   # 크기 변동 후 먹은 물고기 개수
                    final_cnt = cnt + 1
                    if fish_cnt == shark_size:
                        res_li.append((cur_x, cur_y,  cnt + 1, res, 0, shark_size+1))
                    else:
                        res_li.append((cur_x, cur_y, cnt + 1, res, fish_cnt, shark_size))

    if len(res_li) >= 1:
        res = sorted(res_li, key=lambda x: (x[2], x[1], x[0]))
        # print("res: ", res)
        # print("answer: ", res[0])
        # x, y, fish_cnt, shark_size, cur_res
        path[res[0][1]][res[0][0]] = 0    # 최종적으로 선택된 x, y의 물고기만 먹기!! 
        return bfs(res[0][0], res[0][1], res[0][4], res[0][5], res[0][3])
    return cur_res

print(bfs(shark_x, shark_y, 0, 2, 0))