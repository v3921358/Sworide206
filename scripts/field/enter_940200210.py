# id 940200210 (Arcana : Heart of the Forest), field 940200210
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.spawnNpc(3003350, 1700, -170)
sm.showNpcSpecialActionByTemplateId(3003350, "summon", 0)
sm.spawnNpc(3003359, 1700, -170)
sm.showNpcSpecialActionByTemplateId(3003359, "summon", 0)
sm.spawnNpc(3003352, 900, -170)
sm.showNpcSpecialActionByTemplateId(3003352, "summon", 0)
sm.spawnNpc(3003353, 850, -170)
sm.showNpcSpecialActionByTemplateId(3003353, "summon", 0)
sm.spawnNpc(3003354, 800, -170)
sm.showNpcSpecialActionByTemplateId(3003354, "summon", 0)
sm.spawnNpc(3003355, 750, -170)
sm.showNpcSpecialActionByTemplateId(3003355, "summon", 0)
sm.spawnNpc(3003357, 750, 25)
sm.showNpcSpecialActionByTemplateId(3003357, "summon", 0)
sm.showNpcSpecialActionByTemplateId(3003350, "cry", -1)
sm.zoomCamera(0, 1000, 0, 970, 0)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.forcedInput(1)
sm.moveNpcByTemplateId(3003350, True, 50, 100)
sm.sendDelay(3500)
sm.forcedInput(0)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003309) # Tree Spirits
sm.sendNext("#face0#It's that spiritnapping stranger?! Everybody, get them...!")
sm.setInnerOverrideSpeakerTemplateID(3003301) # Small Spirit
sm.sendSay("#face4#Stop! There are more important things to worry about. Look at this poor spirit! If we don't do something quick...")
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 171268073, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 171268077, 0, 0)
sm.sendDelay(500)
sm.zoomCamera(500, 1000, 500, 1200, 0)
sm.sendDelay(500)
sm.moveNpcByTemplateId(3003352, False, 600, 150)
sm.moveNpcByTemplateId(3003353, False, 600, 150)
sm.moveNpcByTemplateId(3003354, False, 600, 150)
sm.moveNpcByTemplateId(3003355, False, 600, 150)
sm.moveNpcByTemplateId(3003357, False, 450, 110)
sm.sendDelay(3000)
sm.forcedInput(2)
sm.sendDelay(1500)
sm.forcedInput(0)
sm.sendDelay(1000)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.zoomCamera(0, 2000, 0, 1650, 100)
sm.moveNpcByTemplateId(3003357, False, 580, 200)
sm.sendDelay(5000)
sm.moveNpcByTemplateId(3003357, True, 30, 110)
sm.sendDelay(2500)
sm.showNpcSpecialActionByTemplateId(3003352, "jump", 2000)
sm.showNpcSpecialActionByTemplateId(3003353, "jump", 2000)
sm.showNpcSpecialActionByTemplateId(3003354, "jump", 2000)
sm.showNpcSpecialActionByTemplateId(3003355, "jump", 2000)
sm.showNpcSpecialActionByTemplateId(3003357, "jump", 2000)
sm.sendDelay(2000)
sm.setInnerOverrideSpeakerTemplateID(3003309) # Tree Spirits
sm.sendNext("#face0#Don't give up, friend! Take our strength...")
sm.resetNpcSpecialActionByTemplateId(3003359)
sm.showNpcSpecialActionByTemplateId(3003359, "refresh", 2400)
sm.sendDelay(2300)
sm.resetNpcSpecialActionByTemplateId(3003359)
sm.showNpcSpecialActionByTemplateId(3003359, "jump", -1)
sm.setInnerOverrideSpeakerTemplateID(3003310) # Lost Tree Spirit
sm.sendNext("#face0#Oogh...")
sm.resetNpcSpecialActionByTemplateId(3003350)
sm.setInnerOverrideSpeakerTemplateID(3003301) # Small Spirit
sm.sendSay("#face7#(Sniffs) That was a close one. But what was this spirit doing\r\nout there all alone?")
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.warp(450005200)
