# Pascal task


def pascal2( n, l=[1,1], i = 3):
    l2 = [1, 1]
    for k in range(1, i-2):
        l2.insert(k, (l[k-1]+l[k]))
    if i < n+1:
        i+=1
        return pascal2(n, l2, i)
    elif i == n+1:
        return ' '.join(str(x) for x in l2)
def pascal(n):
    if n == 1:
        return 1
    elif n == 2:
        return '1 1'
    else:
        return pascal2(n)
print(pascal(int(input())))
