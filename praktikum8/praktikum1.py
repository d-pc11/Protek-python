a = [1, 5, 6, 3, 6, 9, 11, 20, 12] 
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

print('data awal list a\n',a)
print('data awal list b\n',b)

a.insert(3, 10)
b.insert(2, 15)
print('\nsetelah disisipkan nilai 10 ke dalam indeks ke 3 dari a\n',a)
print('setelah disisipkan nilai 15 ke dalam indeks ke 2 dari b\n',b)

a.append(4)
b.append(8)
print('\nsetelah menyisipkan nilai 4 ke indeks terakhir dari a\n',a)
print('setelah menyisipkan nilai 8 ke indeks terakhir dari b\n',b)

a.sort()
b.sort()
print('\nsorting ascending list a\n',a)
print('sorting ascending list b\n',b)

c=(a[0:8])
d=(b[2:10])
print('\nlist c dengan elemen sublist a dari indeks 0 s/d 7\n',c)
print('list d dengan elemen sublist b dari indeks 2 s/d 9\n',d)

e=[]
for i in range(len(c)):
   e += [c[i]+d[i]]
print('\nhasil penjumlahan dari setiap elemen c dan d bersesuaian dengan indeksnya\n',e)
e=tuple(e)
print('\nmengubah e dari bentuk list ke tuple\n',e)

min=min(e)
max=max(e)
sum=sum(e)
print('\nnilai min dari seluruh elemen e\n',min)
print('nilai maks dari seluruh elemen e\n',max)
print('jumlahan seluruh elemen e\n',sum)

myString="python adalah bahasa pemrograman yang menyenangkan"
setmyString=set(myString)
print('\nsebuah string:\n',myString)
print('karakter huruf yang menyusun string:\n',setmyString)

setStringList=list(setmyString)
print('\nbentuk list dari myString\n',setStringList)
setStringList.sort()
print('sorting ascending alfabet himpunan karakter huruf dari myString\n',setStringList)
