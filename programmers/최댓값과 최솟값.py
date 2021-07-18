# 문제

```
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
입출력 예
s	return
"1 2 3 4"	"1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	"-1 -1"
```

# 풀이 방법
split를 이용해서 공백마다 나누어 저장시켜주었고 최대 최소를 구해서 str로 바꾸어서 옳은 결과값으로 만들어 주었다.

    

# 코드
```
def solution(s):
    answer = ''
    lst=list(map(int, s.split(' ')))
    min_s=str(min(lst))
    max_s=str(max(lst))
    answer=min_s + ' ' + max_s
    return answer

```

# 출처
    https://programmers.co.kr/
