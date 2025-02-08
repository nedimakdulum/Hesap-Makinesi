# Basit hesap makinesi

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sıfıra bölünemez!"
    return x / y

print("Hesap Makinesi")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")

num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print(f"{num1} + {num2} = {toplama(num1, num2)}")
elif secim == '2':
    print(f"{num1} - {num2} = {cikarma(num1, num2)}")
elif secim == '3':
    print(f"{num1} * {num2} = {carpma(num1, num2)}")
elif secim == '4':
    print(f"{num1} / {num2} = {bolme(num1, num2)}")
else:
    print("Geçersiz giriş!")
