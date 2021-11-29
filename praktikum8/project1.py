try:
	    count = int(input('ingin memasukkan berapa angka? '))
	    loop = 0
	    data = []
	    while loop < count:
	        number = int(input("Masukkan bilangan bulat ke-{0} : ".format(loop+1)))
	        data.append(number)
	        loop += 1
	

	    data.sort(reverse=True)
	    print('\nHasil data dengan urutan dari angka besar ke kecil\n',data)
except ValueError:
	    print('data yang anda masukan bukan angka / salah')
