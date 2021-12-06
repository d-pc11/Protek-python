dataawal = open('D:\pemrograman terstuktur\chapter 10/fileaakhir.txt','r')
hasil = open('D:\pemrograman terstuktur\chapter 10/hasilp7.txt', 'a')

fileku = dataawal.read()

dataset = set(fileku)

dataset.remove(' ')

listku = list(dataset)

listku.sort()

n=2

file=fileku.replace(listku[0], chr(ord(listku[0])-n))
i = 1
while True:
    file = file.replace(listku[i], chr(ord(listku[i])-n))
    i += 1
    if (i==10):
        break

file = file.replace(chr(63), chr(89))
file = file.replace(chr(64), chr(90))

hasil.write(file)
dataawal.close()
hasil.close()
