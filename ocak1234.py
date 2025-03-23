# Kullanıcıdan ad, yaş ve doğum yılı alma
isim = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))
dogum_yili = 2023 - yas  # Güncel yıla göre doğum yılı hesaplama

# Kullanıcıya mesaj yazdırma
print(f"Merhaba {isim}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.")

# Kullanıcıdan iki sayı alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlemleri gerçekleştirme
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız"  # Bölme işlemi sıfıra bölmeye karşı kontrol edilir

# Sonuçları ekrana yazdırma
print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")

# Kullanıcının girdiği sayının tek mi çift mi olduğunu bulma
sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
    print("Girilen sayı çifttir.")
else:
    print("Girilen sayı tektir.")

# Kullanıcının notunu alarak harf notunu hesaplama
notu = int(input("Notunuzu girin: "))
if 90 <= notu <= 100:
    print("Harf notunuz: A")
elif 80 <= notu <= 89:
    print("Harf notunuz: B")
elif 70 <= notu <= 79:
    print("Harf notunuz: C")
elif 60 <= notu <= 69:
    print("Harf notunuz: D")
else:
    print("Harf notunuz: F")

# Kullanıcının yaşına göre yaş grubunu belirleme
if yas <= 12:
    print("Yaş grubunuz: Çocuk")
elif 13 <= yas <= 19:
    print("Yaş grubunuz: Genç")
elif 20 <= yas <= 59:
    print("Yaş grubunuz: Yetişkin")
else:
    print("Yaş grubunuz: Yaşlı")

# 1'den 100'e kadar olan sayıları ekrana yazdırma
for i in range(1, 101):
    print(i, end=" ")
print()

# 1'den 100'e kadar olan çift sayıları ekrana yazdırma
for i in range(2, 101, 2):
    print(i, end=" ")
print()

# Kullanıcının girdiği sayının faktöriyelini hesaplama
sayi = int(input("Faktöriyelini hesaplamak için bir sayı girin: "))
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i
print(f"{sayi}! = {faktoriyel}")

# 1'den 100'e kadar olan asal sayıları bulma
def asal_mi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("1'den 100'e kadar olan asal sayılar:")
for i in range(1, 101):
    if asal_mi(i):
        print(i, end=" ")
print()

# Kullanıcıdan 5 adet sayı alarak listeye ekleme ve işlemler
sayilar = []
for _ in range(5):
    sayi = float(input("Bir sayı girin: "))
    sayilar.append(sayi)

print(f"Toplam: {sum(sayilar)}")
print(f"Ortalama: {sum(sayilar) / len(sayilar)}")
print(f"En büyük sayı: {max(sayilar)}")
print(f"En küçük sayı: {min(sayilar)}")

# Kullanıcıdan kelimeler alıp ters sıralama
kelimeler = []
for _ in range(5):
    kelime = input("Bir kelime girin: ")
    kelimeler.append(kelime)

kelimeler.reverse()
print("Ters sıralı kelimeler:", kelimeler)

# Tekrar eden elemanları kaldıran program
ornek_liste = [int(x) for x in input("Liste elemanlarını boşlukla ayırarak girin: ").split()]
tekrarsiz_liste = list(set(ornek_liste))
print("Tekrar edenler kaldırıldı:", tekrarsiz_liste)
