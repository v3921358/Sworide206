# id 1 (pt_r), field 940203000
sm.completeQuestNoCheck(parentID)
sm.createQuestWithQRValue(parentID, "hunt1=1;exp=1")
sm.startQuest(11620)
sm.startQuest(11620)
sm.startQuest(11620)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3001300) # Ex
if sm.hasItem(4036162, 10):
    sm.sendNext("#face0#Perfect! Now, let's move on and gather more.")
    sm.createQuestWithQRValue(16700, "count=33;date=20190221")
    sm.createQuestWithQRValue(16700, "count=34;date=20190221")
    sm.createQuestWithQRValue(16700, "count=35;date=20190221")
    sm.createQuestWithQRValue(16700, "count=36;date=20190221")
    sm.createQuestWithQRValue(16700, "count=37;date=20190221")
    sm.createQuestWithQRValue(16700, "count=38;date=20190221")
    sm.createQuestWithQRValue(16700, "count=39;date=20190221")
    sm.createQuestWithQRValue(16700, "count=40;date=20190221")
    sm.lockInGameUI(False, True)
    sm.createQuestWithQRValue(16027, "ComboK=19")
    sm.lockInGameUI(False, True)
    sm.warp(940202019)
else:
    sm.sendNext("You're still missing some materials!")