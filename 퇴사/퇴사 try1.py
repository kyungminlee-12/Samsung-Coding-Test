# https://www.acmicpc.net/problem/14501
"""
오늘부터 N+1일째 되는 날 퇴사를 하기 위해, 남은 N일 동안 최대한 많은 상담
기간: Ti, 금액 Pi
"""
N = int(input())
path = []
res = [0]*N
print("res: "+str(res))

for i in range(N):
    path.append(list(map(int, input().split())))

for idx in range(N-1, -1, -1):
    T, P = path[idx]
    print("T = {}, P = {}".format(T, P))

    if N < T+idx:
        continue
    elif N == T+idx:
        res[idx] = max(res[idx], res[idx+T-1]+P)
    elif N > T+idx:
        res[idx] = max(res[idx], res[idx+T]+P)

print(res[0])

