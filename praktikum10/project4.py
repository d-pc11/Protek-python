file = open('D:\pemrograman terstuktur\chapter 10/biodata.txt','r')

cari = input("Masukan NIM yang ingin dicari : ")

hasil = False

for i in file:
    datafix = i.split("|").copy()
    nim = i.split("|")[0]
    if(nim == cari):
        hasil = datafix
        break
        
if(hasil):
    print("Data Mahasiswa")
    print("NIM         :", hasil[0])
    print("Nama        :", hasil[1])
    print("Alamat      :", hasil[2])
else:
    print("Data mahasiswa tidak ditemukan")
