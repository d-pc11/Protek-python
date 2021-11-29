nilai = [{'nim' : 'A01', 'nama' : 'Agustina',  'mid':50,  'uas'  : 80},
         {'nim' : 'A02', 'nama' : 'Budi',  'mid':40,  'uas'  : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*60)
print("NIM".ljust(10),"Nama".ljust(15),"N.MID".ljust(15),"N.UAS".ljust(15))
print("-" * 60)


for data in nilai:
    print(data['nim'].ljust(10),data["nama"].ljust(15),str(data["mid"]).ljust(15),str(data["uas"]).ljust(15))


print('='*60)
         
