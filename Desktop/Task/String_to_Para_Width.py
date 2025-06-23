#1st Program
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
print("Enter String")
S = input().strip()
print("Enter Value")
W = int(input().strip())

for i in range(0, len(S), W):
    print(S[i:i+W])
