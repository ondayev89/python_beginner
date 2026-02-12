""""
Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
"""
buyurma=[]
n=1
while True:
    kirit=f"{n}-buyurtmani bering:  "
    ol=input(kirit)
    buyurma.append(ol)
    takrorlash=input("yana buyurma berasizmi (ha/yo'q)  ")
    n+=1
    if takrorlash!="ha":
        break
#----------------------------------------------
print("buyurtmalaringiz ")
for ol in buyurma:
    print(ol)