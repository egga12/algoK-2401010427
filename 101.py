print("perulangan 1")
for i in range(5):
    print(i)
    print()

print("perulangan 2")
for i in range(1,6):
    print(i)
    print()

print("perulangan dengan step")
for i in range(1,20,2):
    print(i)
    print()

print("perulangan meneghitung total nilai")
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num
    
print("Total nilai:", total)
print()

#Menampilkan Deret Bilangan Fibonacci
n = int(input("Masukkan jumlah angka Fibonacci: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

#Menentukan bilangan prima
number = int(input("Masukkan angka: "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print(number, "adalah bilangan prima.")
else:
    print(number, "bukan bilangan prima.")
    
