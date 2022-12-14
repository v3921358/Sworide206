# id 100051010 (Partem : Karuppa Forest Entrance), field 100051010
if not hasQuest(35906):
sm.createQuestWithQRValue(35948, "10=h0;11=h0;02=h0;12=h0;22=h1;13=h0;14=h0;15=h0;06=h2;07=h0;16=h0;08=h0;17=h0;09=h0;19=h0")
sm.createQuestWithQRValue(35948, "10=h0;11=h0;02=h0;12=h0;22=h1;13=h0;23=h1;14=h0;15=h0;06=h2;07=h0;16=h0;08=h0;17=h0;09=h0;19=h0")
sm.spawnNpc(1013306)
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.zoomCamera(0, 2000, 0, 220, 120)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(549)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendNext("#face3#There's something moving there, in the brush. Time to find out what we're dealing with.")
sm.forcedMove(False, 320)
sm.zoomCamera(2000, 1000, 2000, 110, -30)
sm.sendDelay(2500)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013353) # Mascarpo
sm.sendNext("#face1#Argh...S-save meeeee. My poor head... It's become stuck in the ground, you see...")
sm.setParam(549)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendSay("#face1#(I should proooobably help him. You never know which random person will have the clue that leads you on your next adventure, after all!)")
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.createQuestWithQRValue(35947, "2=1;6=1")
else:
