a,b,c = map(int, input().split())

x = (a+b+abs(a-b))/2
y = (x+c+abs(x-c))/2
print(f"{y:.0f} eh o maior")