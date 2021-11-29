daftar = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print("\nDaftar Bauh :")
jml = 1
for x,y in daftar.items():
    print("{0}. {1} - {2}".format(jml,x,y))
    jml += 1

total = 0
lagi = 'y'
while lagi == 'y':
    try:
        pilih = input("\nNama buah yang dibeli : ")
        if(pilih in daftar):
            kg = float(input('Berapa Kg             : '))
            total += (daftar[pilih] * kg)
            lagi = input("Beli daftar yang lain (y/n) ? ")
        else:
            print('\n{0} tidak ada dalam daftar '.format(pilih))
        
    except ValueError:
        print('data yang anda masukan salah')

print('-------------------------------------------------------')
print("Total harga           :",total)

