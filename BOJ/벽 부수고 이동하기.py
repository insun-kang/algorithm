from collections import deque


def bfs():
    pass


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visit = [[[0] * N for _ in range(N)] for _ in range(3)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

