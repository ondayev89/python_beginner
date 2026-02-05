""""
Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi
ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang,
va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
"""
#------------------------------------------------------------
buxoriy={
    "name":"abu abdulloh Muhammad ib Ismoil",
    "date":810,
    "region":"Buxoro",
    "umr":60
    }
#------------------------------------------------------------
qodiriy={
    "name":"Abdulla Qodiriy",
    "date":"1894",
    "region":"Toshkent",
    "umr":"44"
}
#------------------------------------------------
e_vohidov={
    "name": "Erkin Vohidov",
    "date":"1936",
    "region":"Farg'ona",
    "umr":"80"
}
#---------------------------------------------
navoiy={
    "name": "Alisher Navoiy",
    "date":"1441",
    "region":"Xirot",
    "umr":"60"
}
#-------------------------------------------------------------------
famous=[buxoriy,qodiriy,e_vohidov,navoiy]
for famous_1 in famous:
    print(f"{famous_1['name'].title()} {famous_1['date']} yilda "
    f"{famous_1['region'].title()} tavallud topgan. "
          f"{famous_1['umr']} umr ko'rgan ")
#-----------------------------------------------------------------
