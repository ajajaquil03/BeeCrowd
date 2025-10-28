N = int(input())
notes = [100, 50, 20, 10, 5, 2, 1]

print(N)
for note in notes:
    Q = int(N/note)
    R = N % note
    print(f"{Q} nota(s) de R$ {note},00")
    N = R
