"""
e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
"""
e_bozor={}      #Bo'sh lug'at yaratiladi.
ishora=True     #Bu o'zgaruvchi while siklini nazorat qilish uchun ishlatiladi
while ishora:
#1. mahsulot --> kalit, narx --> qiymat sifatini qabul qilamiz
    mahsulot=input("mahsulot nomini kiriting: ")
    narx=input(f"{mahsulot} ning narxini kiriting")
#2. e_bozor lug'atga mahsulot o'zgaruvchini kalit sifatida va narx o'zgaruvchini qiymat qilib oladi
    e_bozor[mahsulot]=int(narx)
#3. While ni to'xtatish uchun kerak
    takrorlash=input("yana mahsulot qo'shishni xoxlaysizmi (ha/yo'q)")
    if takrorlash!="ha":
        ishora=False
#4. olingan ma'lumotlarni chop etish uchun kerak
for mahsulot, narx in e_bozor.items():
    print(f"{mahsulot}ning narxi {narx} so'm")




