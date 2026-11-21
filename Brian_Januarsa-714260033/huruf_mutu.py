nilai = float(input("masukan  nilai akhir (0-100):  "))

if nilai >= 80:
    huruf = "A"
elif nilai >= 70:
    huruf = "B"
elif nilai >= 60:
    huruf = "C"
elif nilai >= 50:
    huruf = "D"
else:
    huruf = "E"

print(f"nilai{nilai} huruf {huruf}")