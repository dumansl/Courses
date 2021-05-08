#LISTELER 

#olusturma ve bicimlendirme

#[]

#list()


liste = ["a","b","c"]

type(liste)


liste = ["a",1,0.2]


liste = ["a","asdasdasdasda",999999999]

liste = ["a", 1, [1,2,3,4,5,6], ["a","b"]]

len(liste)

type(liste[3])


ali = 'aliatabakmayikesAllahaşkına'

type(ali)

listed_ali = list(ali)

type(listed_ali[0])

liste1 = [1,2,3,4,6]
liste2 = ["a","b","c"]
liste_tum = [liste1, liste2]



#eleman işlemleri


fis = "ali uzaya git"


len(fis)

fis[len(fis)-1]

fis[0:3]


fis[1:3]

fis[1:4]

fis[1:]

fis[:8]



liste = ["a",1, 789, [11,22,33]]

liste[0]

liste[2:3]

liste[3][2]


yeni_liste = liste[3]


yeni_liste[2]



for i in yeni_liste:
    print(i*2)
    

liste = ["ali","veli","isik", "ayse","berkcan"]

liste


liste[1] = "velinin_babasi"


liste


liste[2:5] = "isik_babasi","ayse_babasi","berkcan_babasi"

liste = liste + ["kemal"]

liste

type(liste)

del liste[0]



liste




#liste methodları


dir(list)


liste = ["ali","veli","isik"]
liste


liste.append("berkcan")

liste


liste.remove("berkcan")


liste

liste = ["ali","veli","isik"]

liste.insert(2, "ayse")
liste

liste[0] = "mehmet"

liste

liste.insert(4,"berk")

liste

liste.insert(len(liste),"berkcan")

liste


liste.pop(0)

liste

liste.pop(len(liste)-len(liste))

liste.pop(len(liste))


liste.pop(len(liste)-1)

liste.extend(["a"])

dir(list)




# TUPLE

#Olusturma

t = ("ali", "veli", 1,2,3, [1,2,3,4])


t = "ali", "veli", 1,2,3, [1,2,3,4]


t


t = tuple("abcd")
t


t = ("abcd",)
t


type(t)


#eleman islemleri


t = ("ali", "veli", 1,2,3, [1,2,3,4])

t[0]

type(t[0])


t[0:3]

t[2] = 99



# =============================================================================
# DICTIONARY - SOZLUKLER
# =============================================================================

# olusturma

sozluk = {"reg" : "regresyon modeli",
          "loj" : "lojistik regresyon",
          "cart" : "classification and regression trees"}


sozluk

len(sozluk)


sozluk2 = {"reg" : 10, 
           "loj" : 11,
           "cart" : 12}

sozluk2



sozluk3 = {"reg" : ["RMSE", 10], 
           "loj" : ["MSE", 11],
           "cart" : ["SSE", 12]}

sozluk3


#eleman


sozluk = {"reg" : "regresyon modeli",
          "loj" : "lojistik regresyon",
          "cart" : "classification and regression trees"}


sozluk[0]

sozluk["reg"]
sozluk["loj"]
sozluk["cart"]

sozluk3["reg"]

sozluk4 = {"reg" : {"RMSE": 10, 
                    "MSE": 11,
                    "SSE": 12},

            "loj" : {"RMSE": 111, 
                    "MSE": 2222,
                    "SSE": 333},
                     
            "cart" : {"RMSE": 99, 
                    "MSE": 00,
                    "SSE": 66}}



sozluk4["loj"]["SSE"]


sozluk = {"reg" : "regresyon modeli",
          "loj" : "lojistik regresyon",
          "cart" : "classification and regression trees"}


sozluk["gbm"] = "gradient boosting machines"

sozluk["reg"] = "coklu dogrusal regresyon modeli"

sozluk

sozluk[1] = "yapay sinir aglari"
sozluk


l = [1]

l


sozluk[l] = "yeni bir model"


t = ("tuple",)
t


sozluk[t] = "light gbm"

sozluk


# SETLER



s = set()
s
type(s)


l = [1,"a","b",123]

l

s = set(l)
s

t = ("a", "ali")
t


s = set(t)
s

s = {1,"a","b",123}
s

s[0]


ali = "ali lutfen ata bakmayı kes"
type(ali)

s = set(ali)

s

l = ["ali","lutfen","ata","bakmayi","kes", "ali","lutfen"]
l

s = set(l)
s


len(s)


dir(set)

l = ["ali","lutfen","ata","bakmayi","kes", "ali","lutfen"]

s = set(l)

s.add("ilik sut")

s.add("ali")

s


s.remove("ali")

s.remove("ali")


#kume islemleri

set1 = set([1,3,5])
set2 = set([1,2,3])


set1.difference(set2)

set2.difference(set1)


set1.symmetric_difference(set2)

set2 - set1

set2 + set1


set1.intersection(set2)

set1 & set2



birlesim = set1.union(set2)
birlesim


kesisim = set1.intersection(set2)
kesisim

set1.intersection_update(set2)

set1



#sorgu



set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])


set1.isdisjoint(set2)


set1.issubset(set2)


set2.issuperset(set1)



















