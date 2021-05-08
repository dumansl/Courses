elemanlar = ["reg","loj_reg","RF","ANN"]

elemanlar[1]


maaslar = [1000, 2000, 3000, 4000, 5000]

maaslar[0]*20/100 + maaslar[0]


for maas in maaslar:
    print(maas*20)



maaslar[0]*20/100 + maaslar[0]

def yeni_maas(x):
    print(x*20/100 + x)
    
    
yeni_maas(2000)    


for i in maaslar:
    yeni_maas(i)
    
    
maaslar = [1000, 2000, 3000, 4000, 5000]
    
def yeni_maas_ust(x):
    print(x*10/100 + x)


def yeni_maas_alt(x):
    print(x*20/100 + x)


for i in maaslar:
    if i >= 3000:
        yeni_maas_ust(i)
    else:
        yeni_maas_alt(i)    



#break & continue
        
ort_satis = [100, 90, 80, 110, 90, 150] 

for i in ort_satis:
    if i == 110:
        print("Kesildi, çünkü istenmeyen sayı geldi")        
        break
    print(i)
    
    
for i in ort_satis:
    if i == 110:
        continue
    print(i)



#while


sayi = 1


while sayi < 5:
    sayi += 1
    print(sayi)































    