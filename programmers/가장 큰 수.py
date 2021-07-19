from itertools import permutations

def solution(numbers):
    answer = '0'
    numbers=list(map(str, numbers))
    numbers.sort(key=lambda x : x+x+x, reverse=True)
    # print(''.join(numbers))
#     for number in list(map(str, permutations(numbers, len(numbers)))):
#         temp=''
#         for num in number:
#             temp+=str(num)
#             if int(answer)<int(temp):
#                 answer=temp
#             else:
#                 continue
    
    return str(int(''.join(numbers)))