def star(n):
    for x in range(n):
        bintang = '*'*(2*x+1)
        print(bintang.center(1+2*n))

star(4)
