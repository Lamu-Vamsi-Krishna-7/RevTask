def print_rangoli(size):
    import string
    alphabets = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        left = alphabets[size-1:i:-1]
        mid = alphabets[i]
        right = alphabets[i+1:size]
        row = '-'.join(left + mid + right[::-1])
        lines.append(row.center(4*size-3, '-'))
    
    for line in lines[::-1]:
        print(line)
    for line in lines[1:]:
        print(line)

print_rangoli(3)
print_rangoli(5)
