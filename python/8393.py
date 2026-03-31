# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

# n = input()
# n = int(n)

# sum = 0
# count = 0
# while count < n:
#     count += 1
#     sum = sum + count
# print(sum)  

n = int(input())

sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)
    