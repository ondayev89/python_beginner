"""
Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
agar taom menyuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q"
degan xabarni chiqaring
"""
# Restoran menusi lug'ati (Taom nomi : Narxi so'mda)
# menyu tuzishda Gemini AI dan foydalanildi
menu = {
    "Osh (Palov)": 35000,
    "Shashlik (qiymali)": 15000,
    "Qozon kabob": 45000,
    "Lag'mon": 30000,
    "Manti": 8000,
    "Mastava": 22000,
    "Somsa": 7000,
    "Salat (Sezar)": 40000,
    "Choy (qora/ko'k)": 5000,
    "Non": 4000,
    "Coca-Cola (0.5l)": 9000,
    "Pitsa (Kombinatsiya)": 65000
}
buyur1, buyur2, buyur3=input("3 ta taom buyiring\n")
buyur1=buyur1.lower()
buyur2=buyur2.lower()
buyur3=buyur3.lower()
#--------------------
buyur1_1=menu.get(buyur1,'kechirasiz bizda', buyur1," yo'q")
buyur2_1=menu.get(buyur2,'kechirasiz bizda', buyur2," yo'q")
buyur3_1=menu.get(buyur3,'kechirasiz bizda', buyur3," yo'q")
print(buyur1_1)
print(buyur2_1)
print(buyur3_1)
