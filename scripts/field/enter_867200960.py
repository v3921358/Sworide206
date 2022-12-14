# id 867200960 (Abrup Basin : Frozen River Center), field 867200960
sm.lockInGameUI(True, False)
sm.spawnNpc(9400589, 272, 430)
sm.showNpcSpecialActionByTemplateId(9400589, "summon", 0)
sm.showNpcSpecialActionByTemplateId(9400589, "saveme", -1)
sm.spawnNpc(9400596, 440, 380)
sm.showNpcSpecialActionByTemplateId(9400596, "summon", 0)
sm.spawnNpc(9400591, 100, 380)
sm.showNpcSpecialActionByTemplateId(9400591, "summon", 0)
sm.startQuest(64160)
sm.spawnNpc(9400592, 1245, 380)
sm.showNpcSpecialActionByTemplateId(9400592, "summon", 0)
sm.forcedFlip(True)
sm.spawnNpc(9400620, 1400, 380)
sm.showNpcSpecialActionByTemplateId(9400620, "summon", 0)
sm.spawnNpc(9400621, 1450, 380)
sm.showNpcSpecialActionByTemplateId(9400621, "summon", 0)
sm.sendDelay(300)
sm.moveNpcByTemplateId(9400592, True, 590, 150)
sm.sendDelay(300)
sm.forcedMove(True, 700)
sm.sendDelay(300)
sm.moveNpcByTemplateId(9400620, True, 700, 150)
sm.sendDelay(300)
sm.moveNpcByTemplateId(9400621, True, 700, 150)
sm.sendDelay(3000)
sm.sendDelay(1000)
sm.avatarOriented("Effect/OnUserEff.img/emotionBalloon/exclamation")
sm.forcedMove(True, 200)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(1000)
sm.spawnNpc(9400589, 430, 380)
sm.showNpcSpecialActionByTemplateId(9400589, "summon", 0)
sm.spawnNpc(9400596, 490, 380)
sm.showNpcSpecialActionByTemplateId(9400596, "summon", 0)
sm.forcedFlip(True)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendNext("#face1#Gasp-! ")
sm.setInnerOverrideSpeakerTemplateID(9400596) # Snowfield Archer
sm.sendSay("It's all my fault! Are you okay, Peytour? ")
sm.lockInGameUI(False, True)
sm.createQuestWithQRValue(64006, "WC=7;k1=0;k2=0;k3=0;k4=0;k5=0;speed=20;k6=0;k7=0;man=239;prog=0;Pt=CaravanP2_chk15;Ec=16;max=20;weather=3;food=90")
sm.warp(867200550)
