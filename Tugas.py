import pandas as pd

# Data awal
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

# Membuat DataFrame
df = pd.DataFrame(data)

# Pertanyaan 1
for index, row in df.iterrows():
    df.at[index, 'Gaji'] = (lambda x: x + x * 0.05)(row['Gaji'])

# Pertanyaan 2
print("DataFrame setelah peningkatan 5% gaji:")
print(df)

# Pertanyaan 3
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = (lambda x: x + x * 0.02)(row['Gaji'])

# Pertanyaan 4
print("\nDataFrame setelah peningkatan tambahan untuk usia di atas 30:")
print(df)

# Ringkasan
summary = df.describe()
print("\nRingkasan Perubahan:")
print(summary)




# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.