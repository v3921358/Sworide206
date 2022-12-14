# id 940200253 (Arcana : Marimba Lagoon), field 940200253
sm.startQuest(34472)
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.spawnNpc(3003350, 607, 473)
sm.showNpcSpecialActionByTemplateId(3003350, "summon", 0)
sm.zoomCamera(0, 1500, 0, 480, 500)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#b(The rock breaks open with a resounding crash, revealing a passageway.)#k")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(3003301) # Small Spirit
sm.sendSay("#face1#Huh? A path under the lagoon?")
sm.sendSay("#face0#Breaking the rock didn't restore the flow of water, but if we follow this path, we might find the blockage.")
sm.moveNpcByTemplateId(3003350, False, 400, 120)
sm.sendDelay(300)
sm.forcedMove(False, 400)
sm.sendDelay(300)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.warp(450005400)
