dataawal = open('D:\pemrograman terstuktur\chapter 10/fileawal.txt', 'r')
hasil = open('D:\pemrograman terstuktur\chapter 10/fileaakhir.txt', 'a')

#membaca file
fileku = dataawal.read()
#mengubah list ke set
fileset = set(fileku)
#mengubah ke list
listku = list(fileset)

listku.sort(reverse=True)

n=2

file=fileku.replace(listku[0], chr(ord(listku[0])+n))
i = 1
while True:
    file = file.replace(listku[i], chr(ord(listku[i])+n))
    i += 1
    if (i==10):
        break

file = file.replace(chr(91), chr(65))
file = file.replace(chr(92), chr(66))

hasil.write(file)
dataawal.close()
hasil.close()
