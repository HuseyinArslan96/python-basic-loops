name = "Hüseyin Arslan"
for letter in name:
    if letter == "a": # dizi içerisinde a karakteri varsa;
        # break => a karakterine gelince döngüyü durdurur.
        continue # a karakteri es geçilir.    
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break    
    print(x)
    x += 1

y = 0
while y < 5:
    if y == 2:
        continue    
    print(y)
    y += 1

z = 0
while z < 5:
    z += 1
    if z == 2:
        continue    
    print(z)

# 1'den 100'e kadar tek sayıların toplamı
x = 0
result = 0
while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x
print(f"Toplam: {result}")

  