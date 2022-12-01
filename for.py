sayilar = [1, 2, 3, 4, 5]
for sayi in sayilar:
    print(sayi)
for a in sayilar:
    print("Hello")
names = ["Hüseyin", "Hasan", "Nurdan"]
for name in names:
    print(f"Benim adım {name}")
name = "Hüseyin"
for n in name:
    print(n)
tuple1 = [1, 2, 3, 4, 5]
for t in tuple1:
    print(t)
tuple2 = [(1, 2), (1, 3), (3, 5), (5, 7)]
for a, b in tuple2:
    print(a)
tuple2 = [(1, 2), (1, 3), (3, 5), (5, 7)]
for a, b in tuple2:
    print(a, b)
d = {"k1": 1, "k2": 2, "k3": 3}
for item in d.items(): # dictionary veri tipinde for metoduyla elemanları sıralayabilmek için x.items() fonksiyonunun yazılması şarttır.
    print(item)
d = {"k1": 1, "k2": 2, "k3": 3}
for key, value in d.items():
    print(key)
for key, value in d.items():
    print(key, value)
