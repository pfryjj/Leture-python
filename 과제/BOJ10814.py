n = int(input())          # 회원 수
members = []

for _ in range(n):
    age, name = input().split()
    members.append([int(age), name])

members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)