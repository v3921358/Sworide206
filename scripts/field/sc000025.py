# id 811000025 (Hieizan : West Tower Central Shrine Entrance), field 811000025
sm.lockInGameUI(True, True)
sm.sendDelay(500)
sm.spawnNpc(9130109, -36, 44)
sm.showNpcSpecialActionByTemplateId(9130109, "summon", 0)
sm.sendDelay(500)
sm.moveNpcByTemplateId(9130109, True, 300, 100)
sm.setSpeakerType(3)
sm.setParam(5)
sm.setInnerOverrideSpeakerTemplateID(9130109) # Mikagami
sm.sendNext("Hm? Who are you?  ")
sm.sendSay("You can't go in. I'm not supposed to let anyone in. ")
sm.sendNext("Hm? Who are you?  ")
sm.sendSay("You can't go in. I'm not supposed to let anyone in. ")
sm.lockInGameUI(False, True)
sm.closeUI(1128)
sm.startQuest(58938)
sm.createQuestWithQRValue(58973, "m035=clear;dr1=clear;m037=clear")
