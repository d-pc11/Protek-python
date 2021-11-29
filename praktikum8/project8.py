daftar = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
 
def reRata():
    jumlahBuah = 0
    harga = 0
    Rata = 0
    for key,value in daftar.items():
          harga += value
          jumlahBuah += 1

    Rata = harga / jumlahBuah
    print("Rata-Rata Harga buah adalah", Rata)

reRata()
