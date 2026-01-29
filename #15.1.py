"""
Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
Lug'atdagi har bir kalit va qiymatni for tsikli yordamida,
alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
"""
lugat = {
    "apple": "olma",
    "book": "kitob",
    "school": "maktab",
    "teacher": "o'qituvchi",
    "student": "talaba",
    "water": "suv",
    "bread": "non",
    "city": "shahar",
    "friend": "do'st",
    "pencil": "qalam"
}
for kalit, qiymat in lugat.items():
    print(f" qiymat: {qiymat}")
    print(f" kalit: {kalit}")
