def sum(n):
    if n<1:
        return 0
    else:
        return n + sum(n-1)

print(sum(3))
print(sum(10))