try:
    Data = []
    inputBuah = int(input("\nMasukan jumlah buah : \n"))
    def sortStringByChar(Data):
        Buah = 0
    while True :
        for Buah in range (0, inputBuah):
                Buah += 1
                namaBuah = str(input("Masukan Nama Buah ke-" + str(Buah) + " = "))
                Data.append(namaBuah)
                if Buah == inputBuah:
                    print(Data)
                    break
                    continue

        print("\nHasil Sort Data Buah : ")
        Data.sort(key = len, reverse = True)
        print(Data)
        sortStringByChar(Data)
        break

except ValueError:
    print('\nData yang dimasukkan salah')
