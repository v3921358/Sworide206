# id 867201001 (Abrup Basin : Svarti Entrance), field 867201001
sm.lockInGameUI(True, False)
sm.setMapTaggedObjectVisible("open", False, 0, 0)
sm.spawnNpc(9400587, 600, 0)
sm.showNpcSpecialActionByTemplateId(9400587, "summon", 0)
sm.spawnNpc(9400582, 360, 0)
sm.showNpcSpecialActionByTemplateId(9400582, "summon", 0)
sm.startQuest(64164)
sm.spawnNpc(9400581, 550, 0)
sm.showNpcSpecialActionByTemplateId(9400581, "summon", 0)
sm.spawnNpc(9400580, 420, 0)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400584, 250, 0)
sm.showNpcSpecialActionByTemplateId(9400584, "summon", 0)
sm.spawnNpc(9400583, 200, 0)
sm.showNpcSpecialActionByTemplateId(9400583, "summon", 0)
sm.spawnNpc(9400588, 150, 0)
sm.showNpcSpecialActionByTemplateId(9400588, "summon", 0)
sm.spawnNpc(9400593, 80, 0)
sm.showNpcSpecialActionByTemplateId(9400593, "summon", 0)
sm.spawnNpc(9400591, 35, 0)
sm.showNpcSpecialActionByTemplateId(9400591, "summon", 0)
sm.spawnNpc(9400589, -40, 0)
sm.showNpcSpecialActionByTemplateId(9400589, "summon", 0)
sm.spawnNpc(9400585, -180, 0)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.spawnNpc(9400585, -240, 0)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.sendDelay(1000)
sm.moveNpcByTemplateId(9400587, False, 100, 50)
sm.sendDelay(1000)
sm.sendDelay(3000)
sm.speechBalloon(True, 0, 0, "Is anyone there? ", 2000, 1, 0, 0, 0, 4, 9400587, 4878499)
sm.sendDelay(3000)
sm.speechBalloon(True, 0, 0, "Chief!", 2000, 1, 0, 0, 0, 4, 9400587, 4878499)
sm.moveNpcByTemplateId(9400581, False, 80, 50)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face0#The walls are intact... no sign of struggle... Did everyone just take shelter? ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#... ")
sm.setParam(57)
sm.sendSay("#bLet's wait and see. ")
sm.sendDelay(3000)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/open", 128)
sm.sendDelay(250)
sm.spawnNpc(9400597, 858, -45)
sm.showNpcSpecialActionByTemplateId(9400597, "summon", 0)
sm.sendDelay(1000)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendNext("#face0#Hmm, hmm. ")
sm.sendDelay(1000)
sm.moveNpcByTemplateId(9400587, False, 20, 50)
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendNext("#face0#Chief Gurnardson! ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#...Hmm. ")
sm.sendSay("#face0#So, Kaptafel was hit by the monsters as well. Am I right? ")
sm.sendSay("#face0#I've heard the chaos tearing through the valley, but I never expected Kaptafel to suffer so... ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#It's true. We've had to evacuate the entire village... ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#Wait, wait, wait. ")
sm.sendSay("#face0#Let me speak. ")
sm.sendSay("#face0#Chief Kan, I cannot take you or your people in to my village. It pains me to do this, but there is simply no way we can support that many refugees. ")
sm.sendSay("#face0#We don't have enough shelter or food for even part of your caravan. And frankly, I have concerns about the number of outsiders traveling with you. ")
sm.sendSay("#face0#From one chief to another I am sorry, but surely you understand that I must see to my own people first. ")
sm.sendSay("#face0#That is my final word on the matter. Farewell, Chief Kan. ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#...")
sm.sendDelay(250)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/close", 128)
sm.sendDelay(500)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face0#Hold a moment! I am Butler, leader of the Afinas Dispatch. ")
sm.moveNpcByTemplateId(9400581, False, 30, 50)
sm.sendSay("#face0#We have been deployed to provide aid to Abrup Basin. ")
sm.sendSay("#face0#If you will provide shelter for these people who have lost their town, we will assist in the defense of yours. ")
sm.sendDelay(1000)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/open", 128)
sm.sendDelay(250)
sm.spawnNpc(9400597, 858, -45)
sm.showNpcSpecialActionByTemplateId(9400597, "summon", 0)
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendNext("#face0#...Afinas, you say? Hmm, hmm. ")
sm.sendSay("#face0#I heard there were knights dispatched, of course... Isn't it rather late for your intervention? ")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#When souls are in need, there is no early or late. ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#... ")
sm.sendSay("#face0#You do not seem to appreciate how dire this situation is. If you expect me to consider so difficult a request, I expect you to abide by my rules. ")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face1#So be it. Don't be coy, man, let's hear it.")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#As you can see, we've barely enough supplies for our own people. With you lot coming in, our rations will be gone by morning. ")
sm.sendSay("#face0#You will be responsible for your own food. We will provide shelter and nothing else. Understood? ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#Understood. ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#I see some sour faces among your group. Well, my rule is law here. Those who complain are not welcome here, especially considering the sacrifices we're making. ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#... ")
sm.moveNpcByTemplateId(9400580, False, 170, 80)
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendNext("#face5#Chief, this is a lot to ask of our people! ")
sm.sendDelay(500)
sm.flipNpcByTemplateId(9400581, True)
sm.sendDelay(500)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face1#Alika! These negotiations do not concern you. Hold your tongue! ")
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendNext("#face4#Eh? ")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#... ")
sm.moveNpcByTemplateId(9400582, False, 270, 130)
sm.sendDelay(500)
sm.moveNpcByTemplateId(9400581, True, 140, 50)
sm.sendDelay(2000)
sm.sendNext("#face1#You all heard the situation. Our hunters should group up with the knights and depart as soon as possible. ")
sm.sendSay("#face0#Excluding those wounded, every able-bodied adult should step forward. ")
sm.sendDelay(1000)
sm.flipNpcByTemplateId(9400582, True)
sm.moveNpcByTemplateId(9400583, False, 180, 150)
sm.moveNpcByTemplateId(9400585, False, 480, 150)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400585, False, 480, 150)
sm.sendDelay(1000)
sm.flipNpcByTemplateId(9400584, True)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400584, True, 50, 50)
sm.sendDelay(1000)
sm.flipNpcByTemplateId(9400584, False)
sm.sendDelay(3000)
sm.flipNpcByTemplateId(9400581, False)
sm.sendDelay(250)
sm.sendNext("#face0#Cayne, you're coming too. ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Vice Captain! I will remain to protect Alika. ")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#No exceptions. I will personally guarantee Alika's safety. ")
sm.flipNpcByTemplateId(9400580, True)
sm.sendSay("#face1#Additionally, I will brook no insubordination. The next time you attempt to undermine my authority, you will be punished. ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#...Understood, sir. ")
sm.setParam(57)
sm.sendSay("#bI will go as well. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#Do as you wish. ")
sm.sendSay("#face0#I expect everyone to contribute 50 pieces of edible meat immediately. ")
sm.sendDelay(500)
sm.flipNpcByTemplateId(9400583, True)
sm.sendDelay(250)
sm.flipNpcByTemplateId(9400585, True)
sm.flipNpcByTemplateId(9400585, True)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400585, True, 1000, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400585, True, 1000, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400583, True, 1000, 100)
sm.sendDelay(250)
sm.forcedFlip(True)
sm.sendDelay(250)
sm.forcedMove(True, 1000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(64043)
sm.startQuest(64044)
sm.warp(867201110)
