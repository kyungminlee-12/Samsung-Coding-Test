from collections import deque

M = 3
some_list = [1, 2, 3, 4]
combi_list = []

def dfs(combi, depth):
    if len(combi) == M:
        combi_list.append(list(combi))
        return
    elif depth == len(some_list):
        return

    # 현재 depth의 값 포함 재귀 호출
    combi.append(some_list[depth])
    dfs(combi, depth+1)

    # 현재 depth의 값 미포함 재귀 호출
    combi.pop()
    dfs(combi, depth+1)

dfs(deque(), 0)
print(combi_list)