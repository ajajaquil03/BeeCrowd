a1,b1 = map(float, input().split())
a2,b2 = map(float, input().split())

x = ((a1-a2)**2 + (b1-b2)**2)**0.5
print(f"{x:.4f}")