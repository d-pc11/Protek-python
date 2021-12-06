file = open('D:\pemrograman terstuktur\chapter 10/biodata.txt','r')

dataMhs ={}

i = 1
for data in file:
    dataterakhir = {}
    datanya = data.split("|")
    dataterakhir['nim'] = datanya[0]
    dataterakhir['nama'] = datanya[1]
    dataterakhir['alamat'] = datanya[2].rstrip("\n")

    dataMhs[i] = dataterakhir
    i += 1



print(dataMhs)
