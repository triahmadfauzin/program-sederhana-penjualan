pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
        Fashion Kita Bersama
          List Nama produk 
 
    ==============================
    A. Sepatu : Rp 150.000
    B. Baju   : Rp 120.000
    C. Celana : Rp 110.000
    D. Sarung : Rp 140.000
    ==============================
    """)
    pesan=str(input("masukkan list produk ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama= "Sepatu"
        harga=(150000*jumlahpesan)
        if jumlahpesan >= 10:
            diskon = int(harga*0.10)
            totalharga=int(harga-diskon)
        elif jumlahpesan >= 5:
             diskon = int(harga*0.05)
             totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "b":
        listnama= "Baju"
        harga = (120000*jumlahpesan)
        if jumlahpesan >= 10:
            diskon = int(harga*0.10)
            totalharga=int(harga-diskon)
        elif jumlahpesan >= 5:
             diskon = int(harga*0.05)
             totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga =int(harga)
    elif pesan == "c":
        listnama= "Celana"
        harga=int(110000*jumlahpesan)
        if jumlahpesan >= 10:
            diskon = int(harga*0.10)
            totalharga=int(harga-diskon)
        elif jumlahpesan >= 5:
             diskon = int(harga*0.05)
             totalharga=int(harga-diskon)
        else:
            diskon=0
            totalharga=int(harga)
    elif pesan == "d":
        listnama= "Sarung"
        harga=int(140000*jumlahpesan)
        if jumlahpesan >= 10:
            diskon = int(harga*0.10)
            totalharga=int(harga-diskon)
        elif jumlahpesan >= 5:
             diskon = int(harga*0.05)
             totalharga=int(harga-diskon)
        else:
            diskon=0
            totalharga = int(harga)
    else:
        listnama = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
    print("--------------------------")
    print       ("Fashion Kita Bersama")
    print("--------------------------")
    print("produk :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")