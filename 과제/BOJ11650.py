n = int(input())
points = []

for _ in range(n):
    x, y = input().split()
    points.append([int(x), int(y)])   # 둘 다 숫자로 변환

points.sort(key=lambda p: (p[0], p[1]))   # x 먼저, 같으면 y

for x, y in points:
    print(x, y)