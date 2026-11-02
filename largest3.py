def largest_three(a,b,c):
    if a >= b or a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c
print(largest_three(2,9,5))