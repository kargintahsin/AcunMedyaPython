import random 

#Bu kodlar verilen ödevin kısaltılmış halidir videolardaki konuların tamamına hakim oldğum için kısa ve öz şeyler yaparak bu ödevi tamamaladım. 
#Ödev için istenilenleri çok kez yaptığım için böyle bir yola başvurdum.

print("Kodlamaio")

baslik= "Tahsin"
print(baslik)
baslik = "MessiTaso"
print(baslik)

#float decimal
odeme=200.50
odeme2 = 250
#boolean
yukselisteMi=False


print(5+5)
print(odeme+12)

print(odeme-10)
print(odeme*10)

if odeme<odeme2:
    print("Odeme daha büyük")
else:
    print("odeme2 daha büyük")


print(type(odeme))
print(type(odeme2))
print(type(odeme+odeme2))
print(str(odeme+odeme2))
print(str(odeme)+str(odeme2))

isim="Tahsin"
metin="Merhaba {isim}".format(isim=isim)
print(metin)

metin= f"Merhaba {isim}"
print(metin)

liste=["a","b","c"]
print(type(liste))
print(liste)
print(liste[1])
print(len(liste))
liste.append("d")
print(liste)


for i in range(10):
    print(i)

for i in range(random.randint(10,50),100,7):
    print(i)

# while True:
#     print("y")

while odeme<220:
    print(odeme)
    odeme+=5

def sayHello(name):
    print("Merhab",name)

sayHello("Tahsin")


class Human:
    name="Halit"
    def talk(self):
        print(f"{self.name} is talking..")

    def walk(self):
        print("Human is walking..")

# instance => örnek
human1 = Human()
human1.talk()

human2=Human()
human2.name="MessiTaso"
human2.talk()