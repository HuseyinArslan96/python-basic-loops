# Sayı Tahmin Oyunu
# 1. 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleriyle buldurmaya çalışın.
# 2. 100 üzerinden puanlama yapın. Hak sayısına göre puan belirleyin.
# 3. Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
import random # random modülünü çağırma

sayi = random.randint(1, 100) # 1-100 arasında rastgele integer sayı üretme
can = int(input('Kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler, {sayac}. defada bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1)}')
        break
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')
    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı: {sayi}')