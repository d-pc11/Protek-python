try:
    daftar = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
    print("\nDaftar Bauh :")
    jml = 1
    for x,y in daftar.items():
        print("{0}. {1} - {2}".format(jml,x,y))
        jml += 1

    pilih = input("\nNama buah yang dibeli : ")
    if(pilih in daftar):
        berat = float(input('Berapa Kg             : '))
        print('---------------------------------------------')
        print("Total harga           :",daftar[pilih] * berat)
    else:
        print('\n{0} tidak dalam daftar'.format(pilih))
except ValueError:
    print('data yang anda masukan salah')
