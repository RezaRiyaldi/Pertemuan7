print(40*"=")
print(5*"=","Menentukan bilangan terbesar", 5*"=")
print(40*"=")
max = 0
while True:
    a = int(input("Masukan bilangan : "))
    if max < a:
        max = a
    if a==0:
        break

print("bilangan terbesar adalah", max)