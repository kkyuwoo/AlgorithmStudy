n = int(input())
result = n

for i in range(2, int(n**0.5)+1):
    if n % i == 0: #i가 소인수 인지 확인
        result -= result / i #결과값 = 결과값/현재값
        while n % i == 0: #n에서 현재 소인수 내역을 제거(2^7*11*13 -> 현재 소인수가 2일 때 11*13으로 변경)
            n /= i

if n > 1: #n이 마지막 소인수일 때 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
    result -= result / n

print(int(result))