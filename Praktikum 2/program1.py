modal = 100000000
laba = [modal * 0, modal* 0, modal * 1/100, modal * 1/100, modal * 5/100, modal * 5/100, modal * 5/100, modal * 3/100]
bulan = 0
sum = 0
print(39*"=")
print(5*"=","Menghitung Total Keuntungan", 5*"=")
print(39*"=")
print(f"Modal awal pengusaha {modal}")
for i in laba:
    sum = sum + i
    bulan += 1
    print(f"Laba pada bulan ke - {bulan}, mendapat laba = {i}")
print(f"Keuntungan yang didapat selama {bulan} bulan = {sum}")
