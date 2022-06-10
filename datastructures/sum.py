def number(i,j,k):
    sum = i + j + k
    if i == j == k:
        sum = sum * 3
    return sum
print(number(1,2,3)) 
print(number(5,5,5))
