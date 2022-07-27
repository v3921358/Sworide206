# id 450001370 (Hidden Street : Mirage Cliff), field 450001370
sm.createQuestWithQRValue(34125, "370=2;390=2;310=2;320=2")
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.spawnNpc(3003113, 70, 213)
sm.showNpcSpecialActionByTemplateId(3003113, "summon", 0)
sm.spawnNpc(3003112, 160, 213)
sm.showNpcSpecialActionByTemplateId(3003112, "summon", 0)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003112) # Rino
sm.sendNext("Blow with all your might on this hard shell...")
sm.playSound("Sound/SoundEff.img/ArcaneRiver/fireBird", 100)
sm.spawnNpc(3003124, 1000, 75)
sm.showNpcSpecialActionByTemplateId(3003124, "summon", 0)
sm.moveNpcByTemplateId(3003124, True, 400, 75)
sm.sendDelay(2000)
sm.playSound("Sound/SoundEff.img/ArcaneRiver/fireBird3", 100)
sm.sendNext("The Flame Bird answered your call. You should be able to reach the end of Vanishing Journey on its back.")
sm.sendSay("Oh, did Kao say that he's going back to where he came from?")
sm.sendSay("So you're heading to the end of the Vanishing Journey? We'll escort you, it's on our way.")
sm.sendSay("Here are those Solid Claws and Sticky Oils you gathered. If you try and ride a Flame Bird without them, you're gonna have a bad time.")
sm.sendDelay(500)
sm.blind(True, 255, 0, 0, 0, 250)
sm.sendDelay(250)
sm.lockInGameUI(False, True)
sm.warp(450001330)
