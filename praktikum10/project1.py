file = open('D:\pemrograman terstuktur\chapter 10/data1.txt','r')


bil_ganjil= 0
bil_genap = 0
for data in file:
    try:
        if(int(data) % 2 == 0):
            bil_ganjil += 1
        else:
            bil_genap += 1

    except:
        print("bukan angka")
                

print("Banyaknya bilangan genap : ",bil_genap)


print("banyaknya bilangan ganjil : ",bil_ganjil)
