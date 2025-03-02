#1. Asal Sayı Kontrolü
#Bir sayının asal sayı olup olmadığını kontrol eden bir Python fonksiyonu yazın.
def asal_mi(sayi):
    if sayi < 2:
        return f"{sayi} asal değildir."
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return f"{sayi} asal değildir"
    return f"{sayi} asaldır."

#Deneme
print(asal_mi(7))  # 7 asaldır.
print(asal_mi(10)) # 10 asal değişdir
print(asal_mi(29)) # 29 asaldır.


# 2. Basit Hesap Makinesi
# Kullanıcıdan iki sayı ve bir işlem türü alarak sonucu döndüren bir fonksiyon yazın.
def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
    elif islem == '-':
        return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
    elif islem == '*':
        return f"{sayi1} * {sayi2} = {sayi1 * sayi2}"
    elif islem == '/':
        if sayi2 == 0:
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"
    else:
        return "Geçersiz işlem türü!"

# Örnek Kullanım
print(hesap_makinesi(5, 3, '+'))  # 5 + 3 = 8
print(hesap_makinesi(10, 2, '/')) # 10 / 2 = 5.0
print(hesap_makinesi(4, 0, '/'))  # Bölme işlemi için ikinci sayı 0 olamaz!
print(hesap_makinesi(6, 2, '%'))  # Geçersiz işlem türü!
