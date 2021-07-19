def solution(numbers, hand):
    answer = ''
    point = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 
             6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1], 
            }
    lp=[3,0]
    rp=[3,2]
    
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            lp=point[number]
        elif number in [3,6,9]:
            answer += 'R'
            rp=point[number]
        else:
            if abs(point[number][0]-lp[0])+abs(point[number][1]-lp[1]) > abs(point[number][0]-rp[0])+abs(point[number][1]-rp[1]):
                answer += 'R'
                rp=point[number]
            elif abs(point[number][0]-lp[0])+abs(point[number][1]-lp[1]) < abs(point[number][0]-rp[0])+abs(point[number][1]-rp[1]):
                answer += 'L'
                lp=point[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    rp=point[number]
                else:
                    answer += 'L'
                    lp=point[number]
    return answer