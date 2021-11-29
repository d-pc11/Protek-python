def star1(n):
    for i in range(n):
        print(('*'*(2*i+1)).center(2*n-1))


def star2(n):
    for i in range(n):
        print(('*'*(2*(n-i)-1)).center(3*n-1))

def star3(n):
    if(n % 2 == 0):
        star1(n//2)
    else:
        star1(n//2 + 1)
    star2(n//2)
star3(7)

