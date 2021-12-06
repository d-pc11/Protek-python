createfile = open('D:\pemrograman terstuktur\chapter 10/angka.txt', 'r')
fileresult = open('D:\pemrograman terstuktur\chapter 10/hasilangka.txt', 'a')

file=createfile.readlines()
data=[]
for i in range(len(file)):
    data1=file[i].split('|')
    data2=data1[1].replace('\n', '')
    data3=int(data1[0])+int(data2)
    data+=[data3]
    
for i in range(len(data)):
    fileresult.write(str(data[i])+'\n')



createfile.close()
fileresult.close()
