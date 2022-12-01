sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# 1. sayilar listesini while metoduyla ekrana yazdırın.
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1
# 2. Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
baslangic = int(input('başlangıç: '))
bitis = int(input('bitiş: '))
i = baslangic
while i < bitis:
    i += 1
    if (i % 2 == 1):
        print(i)
# 3. 1-100 arasındaki sayıları azalan biçimde yazdırın.
x = 100
while x > 0:
    print(x)
    x -= 1
print("Bitti.")
# 4. Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
numbers = []
i = 0
while i < 5:
    sayi = int(input('Sayı: '))
    numbers.append(sayi)
    i += 1
numbers.sort()
print(numbers)
# 5. Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın.
# - Ürün sayısını kullanıcıya sorun.
# - Dictionary yapısı "name, price" biçiminde olsun.
# - Ürün ekleme işlemi bittiğinde ürünleri ekranda while ile sıralayın.
urunler = []
adet = int(input('Kaç ürün eklemek istiyorsunuz: '))
i = 0
while (i < adet):
    name = input('Ürün adı: ')
    price = input('Ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1
for urun in urunler:
    print(f'Ürün adı: {urun["name"]}; ürün fiyatı: {urun["price"]}')
