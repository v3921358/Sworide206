# id 867200501 (Abrup Basin : Kaptafel Ashes), field 867200501
sm.createQuestWithQRValue(64006, "WC=0;man=200;prog=0;Ec=0;weather=0;max=1;food=450")
sm.createQuestWithQRValue(64006, "WC=0;speed=40;man=200;prog=0;Ec=0;weather=0;max=1;food=450")
sm.lockInGameUI(True, False)
sm.closeUI(1888)
sm.closeUI(1890)
sm.spineScreen(True, True, False, 15000, "Map/Effect2.img/Blizzard/skeleton","normal2","")
sm.sendDelay(3000)
sm.onLayer(2000, "title", 0, 350, -80, "Map/EffectPL.img/MONAD1/title", 1, True, -1, False)
sm.sendDelay(10000)
sm.offLayer(3000, "title", False)
sm.spineScreen(True, True, False, 0, "Map/Effect2.img/Blizzard/skeleton","normal","")
sm.lockInGameUI(False, True)
