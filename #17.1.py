""""
Dasturlash asoslari     #17-dars: WHILE     Muallif: Anvar Narzullaev
                        Web sahifa: https://python.sariq.dev
Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
Bajaruvchi: Jasur Ondayev 02/02/2026
"""
from operator import truediv

#kitob="yaxshi ko'rgan kitoblaringiz kiriting"
#kitob+="(dasturto'xtashi uchun stop deb yozing)\n"
#qiymat=''
#while qiymat!='stop':
#    qiymat=input(kitob)
#    if qiymat!='stop':
#        print(qiymat)
#print('dastur tugadi')
#--------------------------------------------
# 2 usul
kitob="yaxshi ko'rgan kitoblaringiz kiriting"
kitob+="(dasturto'xtashi uchun stop deb yozing)\n"
while True: #abadiy sikl
    qiymat=input(kitob)
    if qiymat=='stop':
        break
print('dastur tugadi')