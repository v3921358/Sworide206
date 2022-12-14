# id 867202230 (Abrup Basin : Skuas Entrance), field 867202230
sm.lockInGameUI(True, False)
sm.blind(True, 255, 0, 0, 0, 0)
sm.forcedFlip(True)
sm.spawnNpc(9400582, 2930, 0)
sm.showNpcSpecialActionByTemplateId(9400582, "summon", 0)
sm.spawnNpc(9400602, 3000, 0)
sm.showNpcSpecialActionByTemplateId(9400602, "summon", 0)
sm.spawnNpc(9400580, 3170, -100)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400581, 2247, 108)
sm.showNpcSpecialActionByTemplateId(9400581, "summon", 0)
sm.spawnNpc(9400583, 2247, 108)
sm.showNpcSpecialActionByTemplateId(9400583, "summon", 0)
sm.spawnNpc(9400587, 2247, 108)
sm.showNpcSpecialActionByTemplateId(9400587, "summon", 0)
sm.spawnNpc(9400590, 2247, 108)
sm.showNpcSpecialActionByTemplateId(9400590, "summon", 0)
sm.spawnNpc(9400592, 2247, 108)
sm.showNpcSpecialActionByTemplateId(9400592, "summon", 0)
sm.spawnNpc(9400603, 2247, 108)
sm.showNpcSpecialActionByTemplateId(9400603, "summon", 0)
sm.spawnNpc(9400604, 2247, 108)
sm.showNpcSpecialActionByTemplateId(9400604, "summon", 0)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT3/horn2", 128)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400603) # Guard
sm.sendNext("T-they're here! We're under attack! ")
sm.sendSay("Monsters! ")
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.sendDelay(15000)
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendNext("#face0#...And so it begins. ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#Stand fast, everyone! D-don't let fear make you weak. ")
sm.setInnerOverrideSpeakerTemplateID(9400592) # Aruhi
sm.sendSay("#face0#Just like we practiced! Just like we practiced! ")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#So much for those reinforcements... I suppose we'll have to handle this ourselves. ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#...Alika, stay by my side. ")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face0#Stay safe, everyone... Please... ")
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendSay("#face2#Julieta... ")
sm.setParam(57)
sm.sendSay("#bLet's make this the last battle against these beasts! ")
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendNext("#bRemember, we have to protect the young and wounded taking shelter in the castle. ")
sm.sendSay("#bEveryone who can fight must rally outside the castle! ")
sm.sendSay("#bGillie, please lead the Snowfield Archers with Chief Kan. ")
sm.sendSay("#bVice Captain Butler, I'll leave the catapult to you. ")
sm.sendSay("#bAlika! I need you to help the miners plant those land mines along the flanks. ")
sm.sendSay("#bEveryone, fight hard and watch your backs! ")
sm.sendDelay(2000)
sm.setParam(37)
sm.sendNext("#face2##h0#, I promise I'll do my part to hold them back, no matter what it takes. Believe in me! ")
sm.completeQuestNoCheck(64138)
sm.startQuest(64139)
sm.lockInGameUI(False, True)
sm.createQuestWithQRValue(64001, "")
sm.createQuestWithQRValue(64002, "")
sm.createQuestWithQRValue(64003, "")
sm.createQuestWithQRValue(64004, "")
sm.createQuestWithQRValue(64001, "stage=0")
sm.createQuestWithQRValue(64001, "stage=0;enemy=000000")
sm.createQuestWithQRValue(64001, "stage=0;enemy=000000;companion=000000000")
sm.createQuestWithQRValue(64001, "man=720;stage=0;enemy=000000;companion=000000000")
sm.createQuestWithQRValue(64001, "man=720;stage=0;enemy=000000;seq=0;companion=000000000")
sm.createQuestWithQRValue(64001, "man=720;stage=0;enemy=000000;seq=0;mine=0;companion=000000000")
sm.createQuestWithQRValue(64002, "stage=0")
sm.createQuestWithQRValue(64002, "stage=0;enemy=0")
sm.createQuestWithQRValue(64002, "stage=0;enemy=0;companion=0")
sm.createQuestWithQRValue(64002, "man=0;stage=0;enemy=0;companion=0")
sm.createQuestWithQRValue(64003, "enemy0=0")
sm.createQuestWithQRValue(64003, "enemy0=0;companion0=0")
sm.createQuestWithQRValue(64003, "enemy0=0;enemy1=0;companion0=0")
sm.createQuestWithQRValue(64003, "enemy0=0;enemy1=0;companion0=0;companion1=0")
sm.createQuestWithQRValue(64002, "man=0;stage=0;enemy=0;man0=0;companion=0")
sm.createQuestWithQRValue(64002, "man=0;stage=0;enemy=0;man0=0;man1=0;companion=0")
sm.createQuestWithQRValue(64004, "0=1")
sm.createQuestWithQRValue(64004, "0=1;1=1")
sm.createQuestWithQRValue(64004, "0=1;1=1;2=1")
sm.createQuestWithQRValue(64004, "0=1;1=1;2=1;3=1")
sm.createQuestWithQRValue(64004, "0=1;1=1;2=1;3=1;4=1")
sm.createQuestWithQRValue(64004, "0=1;1=1;2=1;3=1;4=1;5=1")
sm.createQuestWithQRValue(64004, "0=1;1=1;2=1;3=1;4=1;5=1;6=1")
sm.createQuestWithQRValue(64001, "man=720;stage=0;enemy=000000;seq=0;mine=0;companion=708435216")
sm.createQuestWithQRValue(64001, "man=720;stage=0;enemy=104253;seq=0;mine=0;companion=708435216")
sm.warp(867233050)
