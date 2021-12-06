data = open('D:\pemrograman terstuktur\chapter 10/biodata.txt','w')

lagi = "y"
while (lagi == "y"):
    nim    = input("Masukkan NIM    :")
    nama   = input("Masukkan Nama   :")
    alamat = input("Masukkan Alamat :")

    data.write("{0}|{1}|{2}\n".format(nim,nama,alamat))

    lagi = input("ingin input lagi (y/n)  :")

data.close
