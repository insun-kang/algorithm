trans = {
    '####.##.##.####': '0',
    '..#..#..#..#..#': '1',
    '###..#####..###': '2',
    '###..####..####': '3',
    '#.##.####..#..#': '4',
    '####..###..####': '5',
    '####..####.####': '6',
    '###..#..#..#..#': '7',
    '####.#####.####': '8',
    '####.####..####': '9'
}

include = {
    0: [0, 8],
    1: [0, 1, 3, 4, 7, 8, 9],
    2: [2, 8],
    3: [3, 8],
    4: [8.9],
    5: [4, 6, 8, 9],
    6: [5, 8],
    7: [0, 3, 7, 8, 9],
    8: [8],
    9: [8, 9]
}

def count(lst):
    

N = int(input())
light = [list(input()) for _ in range(5)]
nums = [[] for _ in range(N)]
res = []
answer = []
for i in range(5):
    for j in range(0, len(light[0]), 4):
        nums[j//4] += light[i][j:j+3]
for i in nums:
    res.append(trans[''.join(i)])
count(res)