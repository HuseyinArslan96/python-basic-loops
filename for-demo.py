sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# 1. Sayılar listesindeki hangi sayılar 3'ün katıdır?
# 2. Sayılar listesindeki sayıların toplamı kaçtır?
# 3. Sayılar listesindeki tek sayıların karesini alınız.
for sayi in sayilar:
    if (sayi%3==0):
        print(sayi)

toplam = 0
for sayi in sayilar:
    toplam += sayi
print("Toplam:", toplam)

for sayi in sayilar:
    if (sayi%2!=0): # alternatif => if (sayi%2==1):
        kare = sayi * sayi # alternatif => kare = sayi ** 2        
        print(f"Sayı: {sayi}; karesi: {kare}")

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
# 4. Şehirlerden hangileri en fazla beş karakterlidir?

for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)

urunler = [
    {'name': 'samsung s5', 'price': '2000'},
    {'name': 'samsung s6', 'price': '3000'},
    {'name': 'samsung s7', 'price': '4000'},
    {'name': 'samsung s8', 'price': '5000'},
    {'name': 'samsung s9', 'price': '6000'},
]
# 5. Ürünlerin fiyatları toplamı nedir?
toplam = 0
for urun in urunler:
   fiyat = int(urun['price'])
   toplam += fiyat
print('Toplam ürün fiyatı:', toplam)    

# 6. Ürünlerden fiyatı en fazla 4000 olan ürünleri gösteriniz?
for urun in urunler:
    if int(urun['price']) <= 4000:
        print(f"Ürün adı: {urun['name']}; fiyatı: {urun['price']} lira")