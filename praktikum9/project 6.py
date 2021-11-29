nilai = [{'nim' : 'A01', 'nama' : 'Agustina',  'mid':50,  'uas'  : 80},
         {'nim' : 'A02', 'nama' : 'Budi',  'mid':40,  'uas'  : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*90)
print("NIM".ljust(10),"Nama".ljust(15),"N.MID".ljust(15),"N.UAS".ljust(15),"N.Akhir".ljust(15),"STATUS".ljust(15))
print("-" * 90)


for i in nilai:
    nilaiakhir = (i['mid'] + 2*i['uas'])/3
    status = "LULUS"
    if(nilaiakhir < 60):
        status = "TIDAK LULUS"

    print(i['nim'].ljust(10),i["nama"].ljust(15),str(i["mid"]).ljust(15),str(i["uas"]).ljust(15),str(round(nilaiakhir,2)).ljust(15),status.ljust(15))
print("=" * 85)
