daftar = { 'apel'  : 5000, 'jeruk' : 8500, 'mangga': 7800,'duku'  : 6500 }

def tampil(data):
    print('Data buah:')
    for i, j in data.items():
        print('- {0} (Harga Rp{1} / kg)'.format(i,j))
        print('')

tampil(daftar)
lagi = 'y'
while lagi == 'y':
    print('=================================')
    print('A. Tambah data buah')
    print('B. Beli buah')
    print('C. Keluar dari program')
    pilih = input("\nPilihan menu : ")
    pilihan = pilih.upper()
    if(pilihan == 'A'):
        inputbuah  = input('Masukkan nama buah    : ')
        if(inputbuah in daftar):
            print('buah sudah ada dalam daftar')
        else:
            while True:
                try:
                    harga = int(input('Masukkan harga satuan	: '))
                    daftar[inputbuah] = harga
                    tampil(daftar)    
                    break
                except ValueError:
                    print('data yang anda masukan salah')
                


    elif(pilihan == 'B'):
        tampil(daftar)
        total = 0
        beli = 'y'
        while beli == 'y':
            pilih = input("\nNama buah yang dibeli : ")
            if(pilih in daftar):
                while True:
                    try:
                        kg = float(input('Berapa Kg             : '))
                        total += (daftar[pilih] * kg)
                        beli = input("Beli buah yang lain (y/n) ? ")
                        break
                    except ValueError:
                        print('data yang anda masukan salah')
                
            else:
                print('\n{0} tidak ada dalam daftar buah'.format(pilih))

        print('--------------------------------')
        print("Total harga           :",total)
    else:
        break
