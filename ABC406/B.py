N, K = map(int, input().split())
A = list(map(int, input().split()))
display = 1
for i in range(N):
    display *= A[i]
    if len(str(display)) > K:
        display = 1
print(display)
