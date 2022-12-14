# id 867200401 (Abrup Basin : Kaptafel Ashes), field 867200401
sm.lockInGameUI(True, False)
sm.setMapTaggedObjectVisible("q64025Obj", False, 0, 0)
sm.blind(True, 255, 0, 0, 0, 0)
sm.startQuest(64166)
sm.forcedFlip(True)
sm.spawnNpc(9400580, 2850, 400)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400593, 2790, 400)
sm.showNpcSpecialActionByTemplateId(9400593, "summon", 0)
sm.spawnNpc(9400595, 3000, 400)
sm.showNpcSpecialActionByTemplateId(9400595, "summon", 0)
sm.spawnNpc(9400620, 2000, 350)
sm.showNpcSpecialActionByTemplateId(9400620, "summon", 0)
sm.spawnNpc(9400621, 1950, 350)
sm.showNpcSpecialActionByTemplateId(9400621, "summon", 0)
sm.spawnNpc(9400622, 1900, 350)
sm.showNpcSpecialActionByTemplateId(9400622, "summon", 0)
sm.spawnNpc(9400582, 2000, 350)
sm.showNpcSpecialActionByTemplateId(9400582, "summon", 0)
sm.spawnNpc(9400591, 2000, 350)
sm.showNpcSpecialActionByTemplateId(9400591, "summon", 0)
sm.spawnNpc(9400581, 2000, 350)
sm.showNpcSpecialActionByTemplateId(9400581, "summon", 0)
sm.spawnNpc(9400583, 1950, 350)
sm.showNpcSpecialActionByTemplateId(9400583, "summon", 0)
sm.spawnNpc(9400585, 1900, 350)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.moveNpcByTemplateId(9400620, False, 500, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400621, False, 500, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400622, False, 500, 100)
sm.sendDelay(250)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.sendDelay(500)
sm.sendDelay(1000)
sm.speechBalloon(False, 0, 0, "Ma'am!", 2000, 1, 0, 0, 0, 4, 9400620, 4878499)
sm.sendDelay(1000)
sm.speechBalloon(False, 0, 0, "Ma'am!!", 2000, 1, 0, 0, 0, 4, 9400621, 4878499)
sm.sendDelay(1000)
sm.speechBalloon(False, 0, 0, "Are you okay?", 2000, 1, 0, 0, 0, 4, 9400622, 4878499)
sm.moveNpcByTemplateId(9400582, False, 560, 200)
sm.sendDelay(500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendNext("#face0#Alika!!")
sm.sendDelay(1000)
sm.moveNpcByTemplateId(9400591, False, 650, 200)
sm.sendDelay(4000)
sm.speechBalloon(True, 0, 0, "Hawalu!", 2000, 1, 0, 0, 0, 4, 9400591, 4878499)
sm.sendDelay(500)
sm.speechBalloon(False, 0, 0, "You're okay... What a relief...", 2000, 1, 0, 0, 0, 4, 9400591, 4878499)
sm.startQuest(64166)
sm.moveNpcByTemplateId(9400593, True, 10, 50)
sm.sendDelay(1500)
sm.sendDelay(1500)
sm.speechBalloon(False, 0, 0, "Thank you, thank you, thank you...", 2000, 1, 0, 0, 0, 4, 9400591, 4878499)
sm.showNpcSpecialActionByTemplateId(9400591, "thankyou", 930)
sm.sendDelay(930)
sm.resetNpcSpecialActionByTemplateId(9400591)
sm.flipNpcByTemplateId(9400591, True)
sm.sendDelay(250)
sm.showNpcSpecialActionByTemplateId(9400591, "thankyou", 930)
sm.sendDelay(930)
sm.resetNpcSpecialActionByTemplateId(9400591)
sm.flipNpcByTemplateId(9400591, False)
sm.sendDelay(250)
sm.showNpcSpecialActionByTemplateId(9400591, "thankyou2", 930)
sm.sendDelay(930)
sm.resetNpcSpecialActionByTemplateId(9400591)
sm.flipNpcByTemplateId(9400591, True)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400591, True, 1000, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400593, True, 1000, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400595, True, 1300, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400581, False, 700, 150)
sm.sendDelay(500)
sm.moveNpcByTemplateId(9400583, False, 700, 150)
sm.sendDelay(500)
sm.moveNpcByTemplateId(9400585, False, 700, 150)
sm.sendDelay(7000)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face1#Alika! Explain yourself! What use is a scholar atop a burning tower?")
sm.sendDelay(1000)
sm.sendNext("#face1#I have told you countless times that you MUST remain safe. What were you thinking?!")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face4#Tell me, where can I go where I'll be safe here?")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face1#That's... Well, you could have found a safer place than a towering inferno! What will we do if you get injured? Or worse?")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face2#Hey, let's just focus on the good here, yeah? Alika pulled through just fine.")
sm.moveNpcByTemplateId(9400582, False, 10, 50)
sm.sendDelay(250)
sm.flipNpcByTemplateId(9400581, True)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face1#No thanks to you, Cayne! Alika might be better off alone than with a bodyguard as useless as you.")
sm.flipNpcByTemplateId(9400581, False)
sm.sendDelay(250)
sm.sendNext("#face1#Do not forget your purpose here. Your duty!")
sm.sendDelay(1000)
sm.flipNpcByTemplateId(9400581, True)
sm.sendNext("#face1#Our priority now is getting the town back in order.")
sm.sendSay("#face0#All knights, follow me. Not you, Cayne. Take some time to ponder your failure.")
sm.moveNpcByTemplateId(9400581, True, 1000, 150)
sm.sendDelay(1000)
sm.flipNpcByTemplateId(9400585, True)
sm.flipNpcByTemplateId(9400583, True)
sm.sendDelay(500)
sm.moveNpcByTemplateId(9400583, True, 1000, 150)
sm.sendDelay(1000)
sm.speechBalloon(True, 0, 0, "...Aw, cheer up! It's not so bad.", 2000, 1, 0, 0, 0, 4, 9400583, 4878499)
sm.moveNpcByTemplateId(9400585, True, 1000, 150)
sm.sendDelay(2000)
sm.flipNpcByTemplateId(9400620, True)
sm.flipNpcByTemplateId(9400621, True)
sm.flipNpcByTemplateId(9400622, True)
sm.moveNpcByTemplateId(9400622, True, 500, 150)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400621, True, 500, 150)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400620, True, 500, 150)
sm.sendDelay(2000)
sm.moveNpcByTemplateId(9400582, False, 50, 50)
sm.sendDelay(250)
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendNext("#face2#Alika... I thought you were inside the house... You promised me that you'd stay safe.")
sm.sendSay("#face2#I'm just... I'm sorry. It's all my fault. I shouldn't have left your side, not even for a second.")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face0#But it's what I asked of you. There's no need for you to apologize. It's okay.")
sm.sendSay("#face0#As for you... Thank you. For all your help.")
sm.setParam(57)
sm.sendSay("#bAh, it's nothing.")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Ah, that's right! You're the one that fought alongside us earlier. You're definitely not with Afinas. What's your name?")
sm.setParam(57)
sm.sendSay("#bI'm #h0#. And I should thank you for your part earlier, too. So... Thank you! ")
sm.setParam(37)
sm.sendSay("#face1#Nice to meet you, #h0#. I am Cayne, dashing knight extraordinaire of Afinas.")
sm.sendSay("#face1#And this is my muse, my goddess, Alika.")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face0#...Goodness Cayne, you're making me blush.")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Allow me to express my sincerest possible gratitude for saving Alika. I am in your debt.")
sm.setParam(57)
sm.sendSay("#bRelax, you already helped me out.")
sm.setParam(37)
sm.sendSay("#face1#...You do have a point there. Heh, you would have been slow-roasted if not for my timely intervention, eh?")
sm.sendSay("#face1#How remarkable, that we might do each other such a service in such dire circumstances! It's a good thing I was there for you, you know. ")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face5#Cayne...")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Huh? Alika, what's wrong? Have you been hiding a grievous injury from us?")
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendNext("#face5#Of course not. But this isn't the time for your bravado. Look around.")
sm.spawnNpc(9400591, 1180, 253)
sm.showNpcSpecialActionByTemplateId(9400591, "summon", 0)
sm.flipNpcByTemplateId(9400591, False)
sm.startQuest(64160)
sm.spawnNpc(9400593, 1055, 200)
sm.showNpcSpecialActionByTemplateId(9400593, "summon", 0)
sm.flipNpcByTemplateId(9400593, True)
sm.startQuest(64166)
sm.spawnNpc(9400596, 250, 280)
sm.showNpcSpecialActionByTemplateId(9400596, "summon", 0)
sm.showNpcSpecialActionByTemplateId(9400596, "rest", -1)
sm.spawnNpc(9400589, 150, 280)
sm.showNpcSpecialActionByTemplateId(9400589, "summon", 0)
sm.spawnNpc(9400587, -900, 330)
sm.showNpcSpecialActionByTemplateId(9400587, "summon", 0)
sm.spawnNpc(9400588, -510, 380)
sm.showNpcSpecialActionByTemplateId(9400588, "summon", 0)
sm.spawnNpc(9400585, -200, 370)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.showNpcSpecialActionByTemplateId(9400585, "rest", -1)
sm.spawnNpc(9400585, -1325, 350)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.showNpcSpecialActionByTemplateId(9400585, "rest", -1)
sm.spawnNpc(9400596, -1680, 350)
sm.showNpcSpecialActionByTemplateId(9400596, "summon", 0)
sm.showNpcSpecialActionByTemplateId(9400596, "rest", -1)
sm.sendDelay(1500)
sm.sendDelay(5000)
sm.sendDelay(1000)
sm.speechBalloon(True, 0, 0, "Where is...? I need to find... Where...", 2000, 1, 0, 0, 0, 4, 9400591, 4878499)
sm.sendDelay(2000)
sm.speechBalloon(False, 0, 0, "Waaah! Mommy...", 2000, 1, 0, 0, 0, 4, 9400593, 4878499)
sm.sendDelay(1000)
sm.speechBalloon(True, 0, 0, "Are you okay...?", 2000, 1, 0, 0, 0, 4, 9400589, 4878499)
sm.sendDelay(2000)
sm.speechBalloon(False, 0, 0, "Ugh...", 2000, 1, 0, 0, 0, 4, 9400596, 4878499)
sm.sendDelay(2000)
sm.speechBalloon(False, 0, 0, "Dad! Are you okay?!", 2000, 1, 0, 0, 0, 4, 9400588, 4878499)
sm.sendDelay(5000)
sm.speechBalloon(True, 0, 0, "...", 2000, 1, 0, 0, 0, 4, 9400587, 4878499)
sm.sendDelay(1000)
sm.sendNext("#face4#I need to help these people.")
sm.sendDelay(1000)
sm.moveNpcByTemplateId(9400580, True, 300, 100)
sm.sendDelay(1000)
sm.flipNpcByTemplateId(9400582, True)
sm.moveNpcByTemplateId(9400582, True, 200, 100)
sm.setParam(57)
res = sm.sendNext("#b(What should I do now?)\r\n#L0# I should look for the old lady. #l\r\n#L1# I need to help the villagers with Alika and Cayne.#l")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendNext("#face0##h0#? What are you doing? Aren't you coming? ")
sm.sendSay("#face0#I know you're exhausted, but every moment counts right now. Please, show us your noble spirit!")
sm.setParam(57)
res = sm.sendNext("#b(Of course, the letter that brought me here also mentioned helping the people of Abrup.) \r\n#L0# All right, lead on Cayne.#l\r\n#L1# But the old lady...#l")
sm.forcedMove(True, 200)
sm.sendDelay(1000)
sm.startQuest(64017)
sm.lockInGameUI(False, True)
sm.warp(867200400)
