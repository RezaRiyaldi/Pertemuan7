import random
print(43*"=")
print("= Bilangan acak yang lebih kecil dari 0,5 =")
print(43*"=")
jum = int( input("Masukan nilai: "))
i = 0
for i in range(jum):
    i += 1
    angkaDec = random.uniform(0,0.5)
    print("Data ke :", i, "=>", angkaDec)
print("Selesai")
