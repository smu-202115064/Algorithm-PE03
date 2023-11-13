import collections
import sys


FRESH = '0'
RIPEN = '1'
EMPTY = '-1'

DY = (-1, 0, 0, 1)
DX = (0, -1, 1, 0)


M, N = map(int, sys.stdin.readline().split())
graph = [ sys.stdin.readline().split() for _ in range(N) ]

left = 0 # 앞으로 익어야 할 토마토의 개수
queue = collections.deque([]) # 갓 익은 토마토의 좌표들

# 갓 익은 토마토들의 좌표를 조사하여 스택에 저장.
# 아직 익지 않은 토마토들의 개수도 센다.
for y in range(N):
    for x in range(M):
        if graph[y][x] == FRESH:
            left += 1
        elif graph[y][x] == RIPEN:
            queue.append((y,x))

# BFS에서는 큐의 너비는 어제 갓 익은 토마토의 개수이고
# 탐색 깊이는 날짜가 얼마나 지났는지를 의미한다.
width = len(queue)
depth = -1 # 처음 밭의 상태를 적용했을 때 0일차 종료가 되게 하기 위하여 -1 부터 시작
while queue:
    y,x = queue.popleft()

    for dy, dx in zip(DY, DX):
        ny, nx = y+dy, x+dx
        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue
        if graph[ny][nx] == FRESH:
            graph[ny][nx] = RIPEN
            left -= 1
            queue.append((ny, nx))

    width -= 1
    if width == 0:
        width = len(queue)
        depth += 1

# 더 이상 새로 익는 토마토가 없는데, 아직 덜 익은 토마토가 있는지 검사한다.
if left > 0:
    print(-1)
else:
    print(depth)
