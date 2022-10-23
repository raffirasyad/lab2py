#Input nilai variabel
a=input("masukan nilai a:")
b=input("masukan nilai b:")

#Cetak nilai variabel
print("Variabel a=",a)
print("Variabel b=",b)

#Cetak hasil kedua variabel dengan String Format :
print("Hasil Penggabungan {1}&{0}=".format(a,b) + str(a+b))

#Konversi nilai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))

