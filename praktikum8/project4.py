sayuran=["bayam", "kangkung", "wortel", "selada"]

lagi='y'
while lagi == 'y':
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilan data sayur')

    pilih=input("\nPilihan anda: ")
    if pilih=='A':
        tambah=input('\nTambahkan sayur yang anda inginkan: ')
        sayuran.append(tambah)

    elif pilih=='B':
        hapus=input('\nHapus sayur yang anda inginkan: ')
        try:
            sayuran.remove(hapus)
            print("\nMenghapus sayur bernama:%s"% hapus)
        except ValueError:
            print("\nTidak ditemukan data bernama:%s"% hapus)

    elif pilih=='C':
        print("\nData sayur:%s"% sayuran)

    else:
        print("\nPilihan tidak ada:%s"% pilih)

    lagi=input('\nMengolah data lagi (y/n)?')

