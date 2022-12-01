for item in range(10):
    print(item)

for item in range(2, 10):
    print(item)

for item in range(10, 50, 10):
    print(item)

print(list(range(10, 50, 10)))

index = 0
greeting = "Hello"
for letter in greeting:
    print(f"index: {index}; letter: {letter}")
    index += 1

greeting = "Hello"
for index, letter in enumerate(greeting):
    print(f"index: {index}; letter: {letter}")

greeting = "Hello"
for item in enumerate(greeting):
    print(item)

#zip metodunu kullanarak iki listeyi birleştirme
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
list3 = [100, 200, 300, 400, 500]
print(list(zip(list1, list2, list3)))
for item in zip(list1, list2, list3):
    print(item)
for a, b, c in zip(list1, list2, list3): #liste elemanlarından istenenleri yazdırma
    print(a, b)