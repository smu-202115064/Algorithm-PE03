import collections
import itertools
import sys


EMPTY = 0
WALL = 1
VIRUS = 2


def solve(height: int, width: int, graph: list[list[int]]):
    # 시뮬레이션에 걸리는 시간:
    #   BFS: O(NM) = 64
    # 벽을 세울 장소를 선정하는 경우의 수:
    #   64C3 = (64*63*62)/(3*2*1) = 41,664
    # 최적화를 좀 해서 전수조사 말고 일부는 건너뛰자

    visited = [[False] * width for y in range(height)]
    virus = []
    coordinates = []
    for y in range(height):
        for x in range(width):
            coordinates.append((y, x))
            if graph[y][x] != VIRUS:
                continue
            virus.append((y, x))

    def bfs(walls):
        for y, x in coordinates:
            visited[y][x] = (graph[y][x] == WALL)
        for y, x in walls:
            visited[y][x] = True
        queue = collections.deque(virus)
        while queue:
            y, x = queue.popleft()
            if visited[y][x]:
                continue
            visited[y][x] = True
            if y > 0 and not visited[y-1][x]:
                queue.append((y-1, x))
            if y < height-1 and not visited[y+1][x]:
                queue.append((y+1, x))
            if x > 0 and not visited[y][x-1]:
                queue.append((y, x-1))
            if x < width-1 and not visited[y][x+1]:
                queue.append((y, x+1))

    def count_safe():
        cnt = 0
        for y, x in coordinates:
            if not visited[y][x]:
                cnt += 1
        return cnt

    answer = 0
    for walls in itertools.combinations(coordinates, 3):
        for y, x in walls:
            if graph[y][x] == VIRUS:
                break
            if graph[y][x] == WALL:
                break
        else:
            bfs(walls)
            answer = max(count_safe(), answer)
    print(answer)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
    solve(N, M, graph)
