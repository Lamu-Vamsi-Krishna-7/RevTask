print("Enter M Values")
m = int(input().strip())
M_set = set(map(int, input().split()))
print("Enter N Values")
n = int(input().strip())
N_set = set(map(int, input().split()))

sym_diff = M_set ^ N_set 

for val in sorted(sym_diff):
    print(val)
