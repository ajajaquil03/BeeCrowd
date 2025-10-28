a,b,c = map(float, input().split())

print(f"TRIANGULO: {(0.5*a*c):.3f}")
print(f"CIRCULO: {(3.14159*c**2):.3f}")
print(f"TRAPEZIO: {((a+b)/2)*c:.3f}")
print(f"QUADRADO: {b**2:.3f}")
print(f"RETANGULO: {a*b:.3f}")