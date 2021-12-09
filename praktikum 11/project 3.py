from datetime import datetime,timedelta

def getterlambat(x):
    sekarang = datetime.date(datetime.now())
    x = datetime.strptime(x,"%Y-%m-%d").date()
    return int((sekarang -x).days)

cari = input("Masukkan Kode Member : ")

file = open('D:\pemrograman terstuktur\chapter 11\hasil.txt', 'r')

hasil = False

for data in file:
    clone_data = data.split("|").copy()
    kode = data.split("|")[0]
    if(kode == cari):
        hasil = clone_data
        break

if(hasil):
    bataspinjam = hasil[4].rstrip('\n')
    terlambat = getterlambat(bataspinjam)

    if(terlambat <= 0):
        tulisanterlambat = "tidak terlambat"
        denda = "tidak ada denda "
    elif(terlambat > 0):
        textterlambat = str(terkambat) + " hari"
        denda = "Rp " + str(terlambat*2000)

    print("Data Peminjaman Buku ")
    print("Kode Member                     : ",hasil[0])
    print("Nama Member                     : ",hasil[1])
    print("Judul Buku                      : ",hasil[2])
    print("Tanggal Mulai Peminjaman        : ",hasil[3])
    print("Tanggal maks  Peminjaman        : ",bataspinjam)
    print("Tanggal Pengembalian            : ",datetime.date(datetime.now()))
    print("Terlambat                       : ",tulisanterlambat)
    print("Denda                           : ",denda)
else:
    print("Data MAhasiswa tidak ditemukan")

    
