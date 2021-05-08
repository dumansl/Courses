
A = 1
B = 0

A/B


try:
    print(A/B)
except ZeroDivisionError:
    print("Paydada Sıfır olur mu?")


A = 1
B = "2"

A/B


try:
    print(A/B)
except TypeError:
    print("Sayı girersen daha güzel olur")    
    
    
try:
    print(int(A)/int(B))
except TypeError:
    print("Sayı girersen daha güzel olur")    
    
    
    
    
    