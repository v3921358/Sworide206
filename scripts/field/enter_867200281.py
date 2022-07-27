# id 867200281 (null), field 867200281
sm.lockInGameUI(True, False)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(100)
sm.blind(False, 0, 0, 0, 0, 250)
sm.sendDelay(300)
sm.spawnNpc(9400588, -20, 200)
sm.showNpcSpecialActionByTemplateId(9400588, "summon", 0)
sm.spawnNpc(9400596, 920, 330)
sm.showNpcSpecialActionByTemplateId(9400596, "summon", 0)
sm.spawnNpc(9400642, 960, 330)
sm.showNpcSpecialActionByTemplateId(9400642, "summon", 0)
sm.forcedFlip(True)
sm.flipNpcByTemplateId(9400588, False)
sm.moveNpcByTemplateId(9400596, True, 520, 250)
sm.moveNpcByTemplateId(9400642, True, 500, 220)
sm.sendDelay(900)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT1/archer", 128)
sm.sendDelay(600)
sm.speechBalloon(False, 0, 0, "#fs15##eAghh!", 2000, 1, 0, 0, 0, 4, 9400596, 4878499)
sm.sendDelay(1200)
sm.showNpcSpecialActionByTemplateId(9400642, "skill2", 2880)
sm.sendDelay(630)
sm.showEffect("Effect/OnUserEff.img/emotion/wolfgrab", 2200, 0, 0, 0, 15154938, 0, 0)
sm.sendDelay(500)
sm.avatarOriented("Effect/OnUserEff.img/emotionBalloon/exclamation")
sm.sendDelay(900)
sm.forcedMove(False, 170)
sm.sendDelay(300)
sm.forcedAction(5, 0)
sm.sendDelay(500)
sm.resetNpcSpecialActionByTemplateId(9400642)
sm.sendDelay(500)
sm.showNpcSpecialActionByTemplateId(9400642, "die1", 1300)
sm.moveNpcByTemplateId(9400596, True, 90, 200)
sm.sendDelay(1300)
sm.sendDelay(500)
sm.moveNpcByTemplateId(9400588, False, 100, 150)
sm.sendDelay(500)
sm.forcedFlip(True)
sm.flipNpcByTemplateId(9400596, False)
sm.resetNpcSpecialActionByTemplateId(9400588)
sm.sendDelay(500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400596) # Snowfield Archer
sm.sendNext("Gahh, t-thank you!")
sm.sendSay("F-Fembris in town! ")
sm.sendSay("The wolves of legend are here, burning our village to the ground!")
sm.sendSay("They're calling more monsters to help! We have to stop them somehow!")
sm.setParam(57)
sm.sendSay("#bFembris?")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400588) # Ullan
sm.sendSay("In our stories, Fembris is the massive wolf that devours the sky. The real ones aren't that big, but they're scary and breathe fire so... close enough, right?")
sm.sendSay("Someday, Fembris is supposed to end the world in flame and misery. We gotta make sure that isn't today!")
sm.sendDelay(500)
sm.sendDelay(1000)
sm.avatarOriented("Effect/OnUserEff.img/emotionBalloon/exclamation")
sm.setParam(57)
sm.sendNext("#bI'll do what I can. You stay right here!")
sm.forcedFlip(True)
sm.forcedMove(False, 500)
sm.sendDelay(1000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(64014)
sm.createQuestWithQRValue(64015, "map=0")
sm.warp(867200310)
