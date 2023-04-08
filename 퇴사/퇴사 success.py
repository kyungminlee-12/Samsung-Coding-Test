# https://www.acmicpc.net/problem/14501
"""
오늘부터 N+1일째 되는 날 퇴사를 하기 위해, 남은 N일 동안 최대한 많은 상담
기간: Ti, 금액 Pi
"""
N = int(input())
path = []
res = [0]*N
# print("res: "+str(res))

for i in range(N):
    path.append(list(map(int, input().split())))

for idx in range(N-1, -1, -1):
    T, P = path[idx]
    # print("T = {}, P = {}".format(T, P))

    if idx == N-1 and T == 1:
        res[idx] = P
        continue
    if idx == N-1:
        continue

    # 현재 위치 값 count 무효: T일 후에는 퇴사
    if N < T+idx:
        res[idx] = max(res[idx + 1], res[idx])
    elif N == T+idx:
        res[idx] = max(res[idx + 1], P)
    else:
        res[idx] = max(res[idx + 1], res[idx + T] + P)
    """
    else:
        res[idx] = max(res[idx + 1], res[idx + T - 1] + P)
  
        res[idx] = max(res[idx+1], res[idx+T]+P)
        if N > T+idx:
            res[idx] = max(res[idx], res[idx+T]+P)
            """
    # print(res[idx])
print(res[0])

