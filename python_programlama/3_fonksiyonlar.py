#okuryazarlik

print

print()

len()

#?print

print("a","b", sep = '----')

#fonksiyon nasil yazilir?


def kare_al(x):
    print(x*9)
    
kare_al(3)    


def kare_al(x):
    print('Girilen Sayı:' + str(x) + ' Sonuç:' + str(x*9)+"'dir")
    
kare_al(3)   


def kare_al(x, y):
    print(x*9/y)
    
kare_al(3,1)    


kare_al(8)



def kare_al(x, y = 1):    
    print(x*9/y)
    
kare_al(8) 

#ne zaman fonksiyon yazılır?

3 * 5 + 98 / 44 * 12


def iot_hesap(isi, nem, isik, pil, saat):
    print(isi * nem + isik / pil * saat)
    
iot_hesap(3,5,98,44,12)



def uyari_mesaji():
    print("burada uzun bir seyler yazmaktadir. kullanıya")



uyari_mesaji()



def iot_hesap(isi, nem, isik, pil, saat):
    uyari_mesaji()
    print(isi * nem + isik / pil * saat)


iot_hesap(3,5,98,44,12)

#fonksiyon ciktisini girdi olarak kullanmak


def carp_bol(x, y):    
    print(x*y/y)

cikti = carp_bol(2,3)

cikti
print(cikti)


def carp_bol(x, y):
    return x*y/y   
    
cikti = carp_bol(2,3)
cikti


#local ve global degiskenler

x = 10
y = 10

def carp_bol(x, y):
    return x*y/y   


carp_bol(1,2)



x = []
#del x

def yeni_eleman_ekleme(y):
    x.append(y)

yeni_eleman_ekleme("a")

x

def yeni_eleman_ekleme(y):
    global x
    x += [y]

x
yeni_eleman_ekleme("a")

x

yeni_eleman_ekleme(1)
x






























































