def kuadrat(bil):
	    if(isinstance(bil, list)):
	        for i in range(len(bil)):
	            bil[i] **= 2
	        return bil
	    return False
	

def getListFromUser():
	    try:
	        count = int(input('ingin memasukkan berapa angka? '))
	        loop = 0
	        data = []
	        while loop < count:
	            number = int(input("Masukkan bilangan bulat ke-{0} : ".format(loop+1)))
	            data.append(number)
	            loop += 1
	

	        return data
	    except ValueError:
	        print('data yang anda masukan bukan angka / salah')
	        return False
	

dataList = getListFromUser()
	

if(dataList):
	    print("\nHasil kuadrat dari list",dataList,':')
	    result = kuadrat(dataList)
	    print(result)
