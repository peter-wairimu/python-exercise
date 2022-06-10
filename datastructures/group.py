def number(group_num,n):
    for value in group_num:
        if n == value:
            return True
    return False


print(number([1, 5, 8, 3], 3))
print(number([5, 8, 3], -1))