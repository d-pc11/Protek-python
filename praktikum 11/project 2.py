from datetime import datetime,timedelta

def tanggalkembali(sekarang):
    return sekarang + timedelta(days=7)

ulangi = 'y'
text = ""

while ulangi =="y":
    kode = input("Masukkan Kode Member :")
    nama = input("Masukkan Nama Member :")
    judul = input("Masukkan Judul Buku :")


    sekarang = datetime.date(datetime.now())
    text += "{0}|{1}|{2}|{3}|{4}\n".format(kode,nama,judul,sekarang,tanggalkembali(sekarang))
    ulangi = input("Ulangi lagi(y/n) :")


hasilfile = open('D:\pemrograman terstuktur\chapter 11\hasil.txt', 'a')
hasilfile.write(text)
hasilfile.close
