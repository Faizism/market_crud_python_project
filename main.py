### JCDS 0412 - 03/10/2024
### Exercise 1

# menentukan harga tiap buah
price_apple = 10_000
price_orange = 15_000
price_grape = 20_000

# menentukan stok buah
stock_apple = 10
stock_orange = 7
stock_grape = 6

# user menginput jumlah belanjaan untuk buah apel
amount_apple = input("Masukkan Jumlah Apel : ")
amount_apple = int(amount_apple)

# validasi stok apel
while amount_apple > stock_apple:
    print("Jumlah yang dimasukkan terlalu banyak")
    print(f"Stock Apel tinggal: {stock_apple}")
    amount_apple = input("Masukkan Jumlah Apel : ")
    amount_apple = int(amount_apple)

# user menginput jumlah belanjaan untuk buah jeruk
amount_orange = input("Masukkan Jumlah Jeruk : ")
amount_orange = int(amount_orange)

# validasi stok jeruk
while amount_orange>stock_orange :
    print("Jumlah yang dimasukkan terlalu banyak")
    print(f"Stock Jeruk tinggal: {stock_orange}")
    amount_orange = input("Masukkan Jumlah Jeruk : ")
    amount_orange = int(amount_orange)

# user menginput jumlah belanjaan untuk buah anggur
amount_grape = input("Masukkan Jumlah Anggur : ") 
amount_grape = int(amount_grape)

# validasi stok anggur
while amount_grape>stock_grape:
    print("Jumlah yang dimasukkan terlalu banyak")
    print(f"Stock Anggur tinggal: {stock_grape}")
    amount_grape = input("Masukkan Jumlah Anggur : ") 
    amount_grape = int(amount_grape)

# perhitungan total harga yang akan dibayarkan
print("\nDetail Belanja\n")
total_price_apple = price_apple*amount_apple
total_price_orange = price_orange*amount_orange
total_price_grape = price_grape*amount_grape

print(f"Apel {amount_apple} x {price_apple} = {total_price_apple}")
print(f"Jeruk {amount_orange} x {price_orange} = {total_price_orange}")
print(f"Anggur {amount_grape} x {price_grape} = {total_price_grape}")

total_cost = total_price_apple + total_price_orange + total_price_grape

print(f"\nTotal : {total_cost}\n")

### JCDS 0412 - 03/10/2024
### Exercise 2
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