# dosya adı
file_name = "output.txt"

# input alma
text = input("Bir metin girin: ")

# dosyaya yazma
with open(file_name, "w", encoding="utf-8") as file:
    file.writelines([text + "\n"])

# dosyayı okuma ve ekrana yazma
print("\nDosya içeriği:")
with open(file_name, "r", encoding="utf-8") as file:
    print("".join(file.readlines()))

# 5 farklı satır girdisi alma
print("\n5 farklı satır girin:")
lines = [input(f"Satır {i+1}: ") + "\n" for i in range(5)]

# Satırları dosyaya ekleme
with open(file_name, "a", encoding="utf-8") as file:
    file.writelines(lines)

# dosyanın son halini yazdıröma
print("\nGüncellenmiş dosya içeriği:")
with open(file_name, "r", encoding="utf-8") as file:
    print("".join(file.readlines()))
