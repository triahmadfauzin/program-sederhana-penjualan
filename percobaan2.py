
print("""
    ==============================
        Fashion Kita Bersama
    ==============================
    A. Sepatu : Rp 150.000
    B. Baju   : Rp 120.000
    C. Celana : Rp 110.000
    D. Sarung : Rp 140.000
    ==============================
    """)
#input data
pesan=str(input("masukkan nama barang ="))
harga= int(input("masukan harga barang: "))
jumlah= int(input("masukan jumlah yang dibeli: "))
if jumlah >= 10:
        nama= "pakaian"
        harga=int(harga*jumlah)
        diskon = int(harga*0.10)
        totalharga=int(harga-diskon)
elif jumlah >= 5:
        nama= "pakaian"
        harga=int(harga*jumlah)
        diskon = int(harga*0.05)
        totalharga=int(harga-diskon)
elif jumlah <= 5:
        nama= "pakaian"
        harga=int(harga*jumlah)
        diskon = int(harga*0.0)
        totalharga=int(harga-diskon)
else:
        diskon =(0)
        totalharga=int(harga)

print(" ==============================")
print      ("Fashion Kita Bersama")
print(" ==============================")
print("Nama     :", nama)
print("Jumlah   :", jumlah)
print("Harga    :", harga)
print("Diskon   :", diskon)
print("--------------------------")
print("Jumlah Bayar :", totalharga)
print("Anda Berhak Mendapat Diskon :", diskon)
print("--------------------------")