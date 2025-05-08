print("Nama:Dodik Pratama : 24241140")

# Nilai angka yang ingin dicek (24 dan 40)
inputUser = 30
print("Masukkan angka yang bernilai antara 24 sampai 40:", inputUser)

# Pemeriksaan apakah bilangan berada di antara 16 dan 24
isDiAntara = (inputUser >= 24) and (inputUser <= 40)

# Output hasil pengecekan dengan penjelasan
if isDiAntara:
    print("Angka yang Anda masukkan VALID (berada di antara 24 dan 40).")
else:
    print("Angka yang Anda masukkan TIDAK VALID (di luar rentang 24 sampai 40).")