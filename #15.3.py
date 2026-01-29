""""
Foydalanuvchidan istalgan davlatni kiritishni so'rang
va shu davlatning poytaxtini konsolga chiqaring.
Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
"Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
"""
dav_poy_1={
    'amerika':'vashington', 'rossiya':'moskva',
    'germaniya':'berlin','  fransiya':'parij',
    'ispaniya':'madrid',    'angliya':'london',
    'yaponiya':'tokio',     'xitoy':'pekin',
    'misr':'qohira',        'portugaliya':'lisabon'
}
# if operatori yordamida
#--------------------------------------------------
#kirit=input("qaysi davlat poytaxtini bilishni xohlaysan\n")
#if kirit in dav_poy_1.keys():
#    print(dav_poy_1[kirit])
#else:
#    print("bizda mavjud emas")
#-------------------------------------------------
# get metodi yordamida
#--------------------------------------------------
kirit=input("qaysi davlat poytaxtini bilishni xohlaysan\n")
kirit=kirit.lower()
natija=dav_poy_1.get(kirit,"bizda mavjud emas")
print(f" {kirit}ning poytaxti {natija} shahri")



