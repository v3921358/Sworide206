import random

items = [1020000,1021000,1022015,1022014,1022013,1022012,1022011,1022010,1022009,1022008,1022007,1022006,1022005,1022004,1022003,1022002,1022001,1022000,1022031,1022030,1022029,
1022028,1022027,1022026,1022025,1022024,1022023,1022022,1022021,1022020,1022019,1022018,1022017,1022016,1022047,1022046,1022045,1022044,1022043,1022042,1022041,1022040,1022039,
1022038,1022037,1022036,1022035,1022034,1022033,1022032,1022063,1022062,1022061,1022059,1022057,1022056,1022055,1022054,1022053,1022052,1022051,1022050,1022049,1022048,1022079,
1022075,1022074,1022072,1022071,1022070,1022069,1022068,1022066,1022065,1022064,1022095,1022090,1022087,1022086,1022085,1022084,1022083,1022081,1022110,1022109,1022108,1022104,
1022102,1022122,1022121,1022142,1022158,1022174,1022173,1022188,1022187,1022184,1022183,1022177,1022176,1022207,1022201,1022196,1022194,1022223,1022230,1022229,1022227,1022250,
1022249,1022248,1022247,1022244,1022243,1022270,1022269,1022267,1022266,1022265,1022263,1022262,1022259,1022258,1022257,1022287,1022286,1022285,1022284,1022283,1022282,1022280,
1022279,1022276,1022275,1022274,1022297,1022296,1022295,1022292,1022288

]


question = sm.sendAskYesNo("#eWould you like to spend #r2k NX#n #efor a random #bEye Acessory?")
randitem = random.choice(items)
if question and sm.canHold(randitem) and chr.getUser().getNxPrepaid() >= 2000:
    sm.giveItem(randitem)
    sm.deductNX(-2000)
else:
    sm.sendNext("#e#dYour inventory is full or you don't have enough NX.")