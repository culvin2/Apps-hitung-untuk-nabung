
def Lama_Menabung(x,y):
    lama = y/x
    print("Sugih wajib nabung selama",int(lama),"hari")
def Jumlah_Ditabung(a,b):
    uang = b/a
    print("Sugih harus simpan uang ",int(uang),'per hari')

print("---SAVING---")
print('''   
1. Berapa lama nabung 
2. Berapa uang yang harus di simpan''')

aa = int(input("Saving? (1/2) : "))
if aa == 1:
    x = int(input("Uang yang di simpan : "))
    y = int(input("Harga Laptopnya     : "))
    Lama_Menabung(x,y)
elif aa == 2:
    a = int(input("Mau berapa lama Nabung : "))
    b = int(input("Harga Laptopnya        : "))
    Jumlah_Ditabung(a,b)
else:
    print("**")