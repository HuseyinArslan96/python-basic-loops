# Bir sayının asal olup olmadığını bulunuz.
sayi = int(input("Sayı girin: "))
if sayi > 1:
   
   for i in range(2, sayi):
       if (sayi % i) == 0:
           print(sayi,"asal sayı değildir.")
           break
   else:
       print(sayi,"asal sayıdır.")
 
else:
   print(sayi,"asal sayı değildir.")

# Alternatif
sayi = int(input('Sayı: '))
asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print('Sayı asaldır.')
else:
    print('Sayı asal değildir.')