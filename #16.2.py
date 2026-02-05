""""
Yuqoridagi #16.1  lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
"""
#
famous={
    'buxoriy':{
    'name':"abu abdulloh Muhammad ib Ismoil",
    "date":810,
    "region":"Buxoro",
    "umr":60,
    'asarlar':[ "Al-Jome’ as-Sahih",
                "Al-Adab al-Mufrad",
                "At-Tarix al-Kabir",
                "Raf’ul yadayn fi-s-salat"
                ]
    },
#------------------------------------------------------------
"qodiriy":{
    "name":"Abdulla Qodiriy",
    "date":"1894",
    "region":"Toshkent",
    "umr":"44",
    'asarlari':["o'tkan kunlar",
                "mehrobdan chayon",
                "jinlar bazmi",
                "uloqda"
                ]
},
#------------------------------------------------
"e_vohidov":{
    "name": "Erkin Vohidov",
    "date":"1936",
    "region":"Farg'ona",
    "umr":"80",
    "asarlar":["Tong nafasi",
               "Nido",
               "Yurak va aql",
               "Ruhlar isyoni"
               ]
},
#---------------------------------------------
"navoiy":{
    "name": "Alisher Navoiy",
    "date":"1441",
    "region":"Xirot",
    "umr":"60",
    "asarlar":["hamsa",
               "lison ut-tayr",
               "mahbub ul - qulub",
               "Devoni Foniy"
               ]
}

}
#------------------------------
"""for key_1, value_1 in famous.items():
    print(f"\n {value_1['name']} ning asarlari)
    for asar in value_1['asarlar'}:
    print(f"{asar}")
"""
#--------------------------------------------------------------
for ism, info in famous.items():
    print(f"\n{ism.title()} {info['name'].title()} asalari ")
    for til in info['asarlar']:
        print(til.upper())