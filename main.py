### JCDS 0412 - 03/10/2024
### Exercise 1

# Buat dictionary nama buah, stok, harga
dict_fruit ={
    0 :{'Nama' : 'Apel', 'Stok' : 10, 'Harga' : 10_000 },
    1 :{'Nama' : 'Jeruk', 'Stok' : 7, 'Harga' : 15_000 },
    2 :{'Nama' : 'Anggur', 'Stok' : 6, 'Harga' : 20_000 }
}

# Menampilkan daftar menu & user input menu
print("Selamat Datang di Pasar Buah\nList Menu: \n"
      "1. Menampilkan Daftar Buah\n"
      "2. Menambah Buah\n"
      "3. Menghapus Buah\n"
      "4. Membeli Buah\n"
      "5. Exit Program\n")
user_menu = int(input("Masukkan angka Menu yang ingin dijalankan : "))

# Menampilkan Daftar Buah
if user_menu == 1 :
    print("Daftar Buah :\n")
    print(f"{('index').ljust(20)}|{('Nama').ljust(20)}|{('Stok').ljust(20)}|Harga")
    for i in dict_fruit :
        print (f"{str(i).ljust(20)}|{str(dict_fruit[i]['Nama']).ljust(20)}|{str(dict_fruit[i]['Stok']).ljust(20)}|{str(dict_fruit[i]['Harga']).ljust(20)}")
    
# Menambah buah
if user_menu == 2:
    add_name = input("Masukkan Nama Buah: ")
    add_stock = input("Masukkan Stock Buah: ")
    add_price = input("Masukkan Harga Buah: ")
    dict_fruit[3] = ({'Nama' : add_name ,
                      'Stok' : add_stock ,
                      'Harga' : add_name })
    print("Daftar Buah :\n")
    print(f"{('index').ljust(20)}|{('Nama').ljust(20)}|{('Stok').ljust(20)}|Harga")
    for i in dict_fruit :
        print (f"{str(i).ljust(20)}|{str(dict_fruit[i]['Nama']).ljust(20)}|{str(dict_fruit[i]['Stok']).ljust(20)}|{str(dict_fruit[i]['Harga']).ljust(20)}")

# Menghapus Buah
if user_menu == 3 :
    print("Daftar Buah :\n")
    print(f"{('index').ljust(20)}|{('Nama').ljust(20)}|{('Stok').ljust(20)}|Harga")
    for i in dict_fruit :
        print (f"{str(i).ljust(20)}|{str(dict_fruit[i]['Nama']).ljust(20)}|{str(dict_fruit[i]['Stok']).ljust(20)}|{str(dict_fruit[i]['Harga']).ljust(20)}")
    erased_fruit = int(input("Masukkan index buah yang ingin dihapus : "))
    del dict_fruit[erased_fruit]
    for i, key in enumerate(dict_fruit) :
        print (f"{str(i).ljust(20)}|{str(dict_fruit[key]['Nama']).ljust(20)}|{str(dict_fruit[key]['Stok']).ljust(20)}|{str(dict_fruit[key]['Harga']).ljust(20)}")
    
# Membeli Buah
if user_menu == 4 :
    print("Daftar Buah :\n")
    print(f"{('index').ljust(20)}|{('Nama').ljust(20)}|{('Stok').ljust(20)}|Harga")
    for i in dict_fruit :
        print (f"{str(i).ljust(20)}|{str(dict_fruit[i]['Nama']).ljust(20)}|{str(dict_fruit[i]['Stok']).ljust(20)}|{str(dict_fruit[i]['Harga']).ljust(20)}")
    
    cart ={'Nama':[], 
           'Qty' :[], 
           'Harga':[]}
    user_confirmation = True
    
    while user_confirmation :
        user_choice = int(input("Masukkan index buah yang ingin dibeli: "))
        if user_choice <= int(len(dict_fruit)-1) :
            qty_fruit=int(input("Masukkan jumlah buah yang ingin di beli: "))
            if qty_fruit <= dict_fruit[user_choice]['Stok'] :
               dict_fruit[user_choice]['Stok']= dict_fruit[user_choice]['Stok']-qty_fruit
               cart['Nama'].append(dict_fruit[user_choice]['Nama'])
               cart['Qty'].append(dict_fruit[user_choice]['Stok']) 
               cart['Harga'].append(dict_fruit[user_choice]['Harga'])
            else :
                print("Stok Tidak Cukup")
        else :
            print("Index Tidak Ada/Invalid")

        print("Isi Chart")
        print(f"{('Nama').ljust(10)}|{('Qty').ljust(10)}|Harga")
        for i in range(len(cart['Nama'])):
            print (f"{str(cart['Nama'][i]).ljust(10)}|{str(qty_fruit).ljust(10)}|{str(cart['Harga'][i])}")
        user_confirmation = input("Mau beli yang lain? (ya/tidak): ") =='ya'

    if not user_confirmation :
        for i in range(len(cart['Nama'])):
            total_cost = 0
            total_cost = total_cost + (cart['Harga'][i]*cart['Qty'][i])
        print ("Total yang harus dibayar: ", total_cost)
        # user menginput jumlah uang yang akan dikeluarkan
        amount_money = input("Masukkan jumlah uang : ")
        amount_money = int(amount_money)

        # validasi uang dari user
        while(amount_money < total_cost):
            print("Transaksi anda dibatalkan")
            short = (total_cost - amount_money)
            print(f"uangnya kurang sebesar {short}")
            amount_money = input("Masukkan jumlah uang : ")
            amount_money = int(amount_money)
        if (amount_money == total_cost):
            print("Terimakasih")
        else :
            print("Terimakasih\n")
            change = (amount_money-total_cost)
            print(f"Uang kembali anda {change}")
elif user_menu == 5 :
    print("exit program")   

else:
    print ("menu tidak tersedia")