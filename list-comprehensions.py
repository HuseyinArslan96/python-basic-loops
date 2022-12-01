numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)

numbers = [x for x in range(10)]
print(numbers)

for x in range(10):
    print(x**2)

numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x**2 for x in range(10) if x % 3 == 0]
print(numbers)

myString = "Hello"
myList = []
for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

years = [1971, 1996, 2003, 1973, 2005]
ages = [2021-year for year in years]
print(ages)

results = [x if x % 2 == 0 else "Tek" for x in range(1, 10)] #1'den 10'a kadar çift sayıları yazdırma
print(results)

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)

numbers = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)