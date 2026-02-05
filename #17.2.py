""""
Muzeyga  chipta narhi foydalanuvchining yoshiga bog'liq:
7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm,
18-65 gacha 10000 so'm, 65 dan kattalarga bepul.
Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin
va chipta narhini chiqarsin.
Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin
(ikkita shartni ham tekshiring)
"""
#from operator import truediv
savol="yoshingizni kiriting"
savol+="(dasturni to'xtatish uchun 'exit' yoki 'quit deb yozing)"
while True:
    qiymat=input(savol)
    if qiymat=="exit" or qiymat=="quit":
        print("dastur tugadi")
        break

    yosh=int(qiymat)

    if yosh<7:
        narh=2000
    elif 7<=yosh<18:
        narh=3000
    elif 18<=yosh<65:
        narh=10000
    else:
        narh=0
    if narh==0:
        print("sizga chipta bepul")
    else:
        print(f"chipta {narh} so'm")



