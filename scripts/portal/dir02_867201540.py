# id 3 (dir02), field 867201540
sm.lockInGameUI(True, False)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendNext("#face0#What do we do now? ")
sm.sendDelay(1000)
sm.forcedMove(True, 140)
sm.sendDelay(1000)
sm.setParam(57)
sm.sendNext("#bHold on tight! ")
sm.forcedInput(5)
sm.createQuestWithQRValue(64078, "chk1=3")
sm.sendDelay(1000)
sm.lockInGameUI(False, True)
sm.warp(867201550)
