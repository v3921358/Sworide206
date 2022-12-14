# id 64036 ([MONAD: The First Omen] Leader of the Dispatch), field 867200800
sm.lockInGameUI(True, False)
sm.startQuest(parentID)
sm.moveNpcByTemplateId(9400581, True, 50, 50)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face0##h0#... ")
sm.setParam(57)
sm.sendSay("#bYes? ")
sm.setParam(37)
sm.sendSay("#face0#I know that you are a capable and brave warrior. But you lack the experience needed to command. ")
sm.sendSay("#face0#It's not your fault, of course. You just need a trusted advisor, just as Peytour is to Chief Kan. ")
sm.sendSay("#face0#Now, then... Do you really think it wise to spend time resting before we move out? ")
sm.sendDelay(2000)
sm.setParam(57)
sm.sendNext("#bI'm aware that the snowstorm is approaching, and also that we are vulnerable to monsters. There are certainly risks. ")
sm.sendSay("#bBut as Alika said, if we push on without rest, there are those who will not be able to keep up. We're sure to lose people. ")
sm.setParam(37)
sm.sendSay("#face1#You're allowing your emotions to cloud your judgment. The correct decision is clearly to push onward. ")
sm.sendSay("#face1#You want to give people time to think, when they're already tired and disappointed? That can only lead to further despair. ")
sm.sendSay("#face1#Give them a goal. Push them to keep moving forward. If they're too busy to think, they're too busy to complain. ")
sm.setParam(57)
sm.sendSay("#bThat may work for trained knights, but these are ordinary people. ")
sm.sendDelay(2000)
sm.setParam(37)
sm.sendNext("#face0#Before I became a knight, I was a wandering mercenary for years. Just like you. ")
sm.sendSay("#face0#I've spent more of my life with the commoners than with trained knights. I know how they think, and what they're capable of. Do not dismiss the wisdom I've gained. ")
sm.sendSay("#face0#You will soon see that your decision was wrong. I only hope you'll have the chance to recover from it. ")
sm.setParam(57)
sm.sendSay("#b...Thank you for the advice. ")
sm.setParam(37)
sm.sendSay("#face0#Remember well who gives you the advice and counsel you need. ")
sm.sendDelay(500)
sm.flipNpcByTemplateId(9400581, False)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400581, False, 70, 100)
sm.sendDelay(2500)
sm.flipNpcByTemplateId(9400581, True)
sm.sendDelay(500)
sm.sendNext("#face0#Ah, and just as a reminder... if the pressures of leadership are too much for you, I'd be happy to take over at any time. ")
sm.sendDelay(250)
sm.flipNpcByTemplateId(9400581, False)
sm.sendDelay(250)
sm.sendDelay(1500)
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(parentID)
