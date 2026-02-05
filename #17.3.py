"""
Quyidagi dasturda bir nechta mantiqiy xatolar bor.
Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda.
Xatolarni to'g'rilay olasizmi?
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
"""
print("Kiritilgan sonning ildizini qaytaruvchi dastur")
savol="Musbat son kiriting "
savol+="(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat=input(savol)# savolni qiymat o'tkazding
    if qiymat=='exit':# agar qiymat exit bo'lsa jaroyoni to'xtat
        break
    elif float(qiymat)<0:# qiymatni str dan float ga o'tkaz va manfiy bo'lsa whilening birinchi qiymatiga qayt savolga
        continue
    else:   #aks holda quyidagi amallarni bajar
        ildiz = float(qiymat)**(0.5) # nima uchun qiymat floatda edi yana floatga o'tkazib hisoblayabmiz
        # sabab elif bajarilmasa, qiymat ham floatga o'tmaydi
        print(f"{qiymat} ning ildizi {ildiz} ga teng")