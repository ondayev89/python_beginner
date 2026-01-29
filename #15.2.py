""""
Davlatlar va ularning poytaxtlari lug'atini tuzing.
Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida,
alifbo ketma-ketligida konsolga chiqaring.
"""
dav_poy={
    'amerika':'vashington',
    'rossiya':'moskva',
    'germaniya':'berlin',
    'fransiya':'parij',
    'ispaniya':'madrid',
    'angliya':'london',
    'yaponiya':'tokio',
    'xitoy':'pekin',
    'misr':'qohira'
}
#1-usul quyidagi
#------------------------------------------
#dav_poy_1=sorted(dav_poy.keys())
#print(dav_poy_1)
#------------------------------------------
# 2 - usul quyidagi
print("DUNYO DAVLATLARI")
for dav_1 in sorted(dav_poy.keys()):
    print(dav_1)
#-------------------------------------------
print("DUNYO poytaxtlari")
for dav_2 in sorted(dav_poy.values()):
    print(dav_2)
#------------------------------------------
for dav_kalit, day_qiymat  in sorted(dav_poy.items()):
    print(dav_kalit,'',day_qiymat)
