num = list(map(int, input().split()))

def list_sum(num):
    if len(num) == 1:
        return num[0]
    else:
        return num[0] + list_sum(num[1:])

print(list_sum(num))