# id 64027 ([MONAD: The First Omen] Decisions, Decisions), field 867200400
sm.lockInGameUI(True, False)
sm.sendDelay(250)
sm.sendDelay(250)
sm.showEffect("Effect/OnUserEff.img/emotion/angry", 0, 0, 0, 0, 141098, 0, 0)
sm.sendDelay(3500)
sm.speechBalloon(True, 0, 0, "Geez, how can he just decide something like that himself? \r\nAnd how am I just hearing about it now?", 3000, 1, 0, 0, 0, 4, 9400629, 4878499)
sm.showEffect("Effect/OnUserEff.img/emotion/shade", 0, 0, 0, 0, 141102, 0, 0)
sm.sendDelay(3500)
sm.speechBalloon(True, 0, 0, "It's not just Kan making decisions, you know.\r\nAnd what else could they have done?", 3000, 1, 0, 0, 0, 4, 9400617, 4878499)
sm.sendDelay(3500)
sm.speechBalloon(True, 0, 0, "I'm not just talking about this time! \r\nIt feels like he's always pushing us around like this.", 3000, 1, 0, 0, 0, 4, 9400629, 4878499)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 141102, 0, 0)
sm.sendDelay(2500)
sm.speechBalloon(True, 0, 0, "Well... Kan has always been a decisive leader.", 2000, 1, 0, 0, 0, 4, 9400617, 4878499)
sm.showEffect("Effect/OnUserEff.img/emotion/angry", 0, 0, 0, 0, 141098, 0, 0)
sm.sendDelay(3000)
sm.speechBalloon(True, 0, 0, "There's a difference between being decisive and being a dictator, though.", 3000, 1, 0, 0, 0, 4, 9400629, 4878499)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bAre we all set to move out? I'm wondering if there's anything more I can do to help. ")
sm.showEffect("Effect/OnUserEff.img/emotionBalloon/noSpeak", 2000, 0, 0, 0, 141098, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotionBalloon/noSpeak", 2000, 0, 0, 0, 141102, 0, 0)
sm.sendDelay(2000)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400617) # Resident
sm.sendNext("I am... There is not much for me to pack... As you can see... ")
sm.setInnerOverrideSpeakerTemplateID(9400596) # Snowfield Archer
sm.sendSay("Tsk, what is Kan doing? Making you run around like this... ")
sm.setParam(57)
sm.sendSay("#bChief Kan is preparing a wagon to carry the injured. ")
sm.setParam(37)
sm.sendSay("I'm sure Peytour is preparing the wagon, not Kan. ")
sm.setParam(57)
sm.sendSay("#b... ")
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 141102, 0, 0)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400617) # Resident
sm.sendSay("Cut it out. He's still our chief. ")
sm.setInnerOverrideSpeakerTemplateID(9400596) # Snowfield Archer
sm.sendSay("...For how long, do you think? ")
sm.setParam(57)
sm.sendSay("#b(Seems like a lot of people have issues with Chief Kan...) ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400617) # Resident
sm.sendSay("There is nothing we need help with. You can go check on the other villagers.")
sm.completeQuestNoCheck(parentID)
sm.lockInGameUI(False, True)
