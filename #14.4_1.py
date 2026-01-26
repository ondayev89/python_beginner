""""
Foydalanuvchidan biror so'z kiritishni so'rang
va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
"""
# get metodi yordamida
dicti_1={
    'remove':"ko'chirmoq",
    'employee':'xodim',
    'entrance':'kirish',
    'fiction':'fantastik',
    'frequent':'tez-tez',
    'peel':"po'chog'ini archmoq"
}
kirit_suz=input("inglizcha so'z kiriting")
kirit_suz=kirit_suz.lower()

tarjima=dicti_1.get(kirit_suz,"bunday so'z mavjus emas")
print(tarjima)

#if kirit_suz in dicti_1:
 #   print("tarjimasi ", dicti_1[kirit_suz])
#else:
 #   print("bunday so'z mavjud emas")
