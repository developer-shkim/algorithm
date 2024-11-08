def get_package_count(suger):
    if suger % 5 == 0:
        return suger // 5

    if (suger % 5) % 3 == 0:
        return suger // 5 + (suger % 5) // 3

    remained_suger = suger
    while remained_suger >= 0:
        if remained_suger % 5 == 0:
            return (suger - remained_suger) // 3 + remained_suger // 5
        remained_suger -= 3

    return -1


n = int(input())
print(get_package_count(n))

"""
아이디어
1) 5킬로그램으로만 봉지를 구성
- n 이 5, 0 으로 끝나는 경우, n / 5 를 반환
- 예) 25 = 5*5

2) 5킬로그램으로 구성할 수 있는 최대의 봉지 수 구성, 나머지를 3킬로그램으로 구성
- (n % 5) % 3 == 0 인지 확인
- n / 5 + (n % 5) / 3 을 반환
- 예) 23 = 5*4 + 3*1

3) 대입해서 가능한 경우 중 5킬로그램이 최대인 경우로 구성
- 1) 에서 먼저 확인을 했기 때문에 3)은 3킬로그램이 최소 1개라도 포함될 것임
- countOfThree = 1 부터 실행해서 n - 3*countOfThree % 5 가 0 인 경우, 
  countOfThree + (n - 3*countOfThree / 5) 을 반환   
- 예) 21 = 5*3 + 3*2

4) 구성이 불가한 경우
- -1 반환
- 예) 4 
"""
