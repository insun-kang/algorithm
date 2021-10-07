trans = {
    '####.##.##.####': 0,
    '..#..#..#..#..#': 1,
    '###..#####..###': 2,
    '###..####..####': 3,
    '#.##.####..#..#': 4,
    '####..###..####': 5,
    '####..####.####': 6,
    '###..#..#..#..#': 7,
    '####.#####.####': 8,
    '####.####..####': 9
}

include = {
    0: [8],
    1: [0, 3, 4, 7, 8, 9],
    2: [8],
    3: [8],
    4: [8.9],
    5: [6, 8, 9],
    6: [8],
    7: [0, 3, 8, 9],
    8: [],
    9: [8]
}
N = int(input())
light = [list(input()) for _ in range(5)]

nums = [[''] for _ in range(N)]
answer = set()
result = [set() for _ in range(N)]
for y in range(5):
    idx = 0
    cnt = 0
    for x in range(3*N+(N-1)):
        if (x+1) % 4 != 0:
            nums[idx].append(light[y][x])
            cnt += 1
        if cnt == 3:
            idx += 1
            cnt = 0
        if idx == N:
            idx = 0
for i in range(N):
    tmp = ''.join(nums[i])
    if tmp in trans:
        answer.add(trans[tmp])
        result[i].add(trans[tmp])

for i in range(N):
    for j in include[answer[i]]:
        result[i].add(j)
print(result)
