x = 0
while x <= 100:
    if x % 2 == 1:
        print(f"Sayı tek {x}")
    else:
        print(f"Sayı çift {x}")
    x += 1    
print("Bitti.")
name = '' #False
while not name.strip(): #Boş karakter False değer ürettiği için "not" ifadesini kullanmak False'u True değere çevirir.
    name = input("İsminizi giriniz: ")
print(f"Merhaba {name}")