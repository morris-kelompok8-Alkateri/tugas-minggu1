angaka = float(input("Masukkan angka: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = angka + angka2
    print("Hasil:", hasil)
elif operator == "-":
    hasil = angka - angka2
    print("Hasil:", hasil)
elif operator == "*":
    hasil = angka * angka2
    print("Hasil:", hasil)
elif operator == "/":
    hasil = angka / angka2
    print("Hasil:", hasil)
else:
    print("Operator tidak valid")
    
    print("hasil:", hasil)