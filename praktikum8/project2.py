def dataStat(x):
    if(isinstance(x, list)):
        X  = tuple(x)
        a  = sum(X) / len(X)
        b  = max(X) 
        c  = min(X)

        return [a, b, c]
    else:
        print('Data yang dimasukkan bukan bertipe data list')
        return False

def getListFromUser():
    try:
        inputData = int(input('Banyak angka yang ingin dimasukkan '))
        jum = 0
        data = []
        while jum < inputData:
            bilangan = int(input("Masukkan bilangan bulat ke-{0} : ".format(jum+1)))
            data.append(bilangan)
            jum += 1
        return data
    except ValueError:
        print('Data yang anda masukkan salah')
        return False


dataList = getListFromUser()
if(dataList):
    result   = dataStat(dataList)
    print("\nRata-rata dari list {0}        : {1}".format(dataList,result[0]))
    print("Nilai tertinggi dari list {0}  : {1}".format(dataList,result[1]))
print("Nilai terendah dari list {0}   : {1}".format(dataList,result[2]))
