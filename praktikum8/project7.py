def Urut(data):
    isi = list(data.values())
    isi.sort(reverse=True)
    for x,y in data.items():
        if(isi[0] == y):
            return x
    

buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
hasil = Urut(buah)
print("Buah yang harga satuannya paling mahal yaitu : ", hasil)

