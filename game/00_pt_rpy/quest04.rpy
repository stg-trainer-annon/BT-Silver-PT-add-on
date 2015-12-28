label quest4:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
    #play music "music/India's Different (Dancing).MP3" fadein 1 fadeout 1
    menu:
        "The front door is locked, but you hear quiet music and a woman's laughter coming from the inside."
        "-Knock on the door-":
            $ renpy.play('sounds/door3.mp3')
            ">You knock on the door."
            ">The music stops abruptly..."
            stop music 
            "........................"
            "..........."
            who2 "Who is it?"
            who2 "Is it you, my love?"
            who2 "If it is you, then tell me the password...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            menu:
                "\"Swordfish?\"":
                    who2 "Heh, Good try."
                    who2 "Now get lost before I call the cops..."
                    who2 "I mean, the city guard."
                    jump brothelnight
                "\"HentaiUnited?\"":
                    who2 ".........\""
                    jump brothelnight
                "\"Jasmine is a whore.\"":
                    who2 "Huh?"
                    who2 "What?  What are you talking about? Who are you...?"
                    jump brothelnight
                "\"Jafar sucks.\"":
                    who2 "......."
                    who2 "What is this? A loyalty test of some sort?"
                    who2 "I'm not a traitor! Long live the sultan!"
                    jump brothelnight
                "\"TARDIS\"":
                    who2" Er.... Ok..."
                    jump brothelnight
                "\"Jafar rules.\"":
                    who2 "that's not the password."
                    who2 "Go away! Just leave please."
                    jump brothelnight
                "\"...........\"":
                    who2 "Anyone there...?"
                    jump brothelnight
########################################################
                "\"Support Akabur.\"" if awmaslabcomplete:
                    if quest400:
                        who2 "Long live the king!"
                        who2 "Come on in. Welcome to \"The Red Phoenix\"!"
                        $ renpy.play('sounds/door.mp3')
                        show image "04_pt/slavem/bld.png" with Dissolve(.3)
                        play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
                        sch3 "Huh? Wait a second, who are you, dear? And how did you come by our password?"
                        sch3 "Did you come to see one of the girls?"
                        sch3 "I'm afraid I can't allow that."
                        sch3 "I can't run my brothel openly these days, not without a special permit signed by the sultan."
                        menu:
                            sch3 "So unless you can get me one of those I just can't let you stay, sorry love."
                            "Quest: [quest4].":
                                if onquest:
                                    "You need to finish your current quest first, before you can take a new one."
                                    jump brothelnight
                                else:
                                    sch3 "You think you can get the permit signed? Really?"
                                    sch3 "This won't be easy unless you know the sultan personally, which I doubt you do."
                                    sch3 "But if somehow you do manage to get the paper signed I will be very grateful..."
                                    $ quest400 = False
                                    $ quest4start = True
                                    $ onquest = True
                                    $ idlequest = False
                                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                                    show image "04_pt/slavem/qstart.png" with Dissolve(.3)
                                    show image "04_pt/slavem/onaquest.png" with Dissolve(.3)
                                    show con1 at right
                                    show ctc7 at right
                                    pause 
                                    hide con1
                                    hide ctc7
                                    $ renpy.play('sounds/door.mp3')
                                    hide image "04_pt/slavem/qstart.png" with Dissolve(.3)
                                    ">You leave the brothel..."
                                    ">You return home and go to sleep."
                                    show image "interface/blackfade.png" with Dissolve(.3)
                                    pause 1
                                    jump dayone
                            "\"Maybe later.\"":
                                sch3 "I can't open my brothel for the public without the permit."
                                sch3 "Now you have to leave, dear."
                                jump brothelnight
                    elif  quest4start:
                        who2 "Long live the king!"
                        who2 "Come on in. Welcome to \"The Red Phoenix\"!"
                        $ renpy.play('sounds/door.mp3')
                        show image "04_pt/slavem/bld.png" with Dissolve(.3)
                        sch3 "No luck with getting the permit signed so far, huh?"
                        sch3 "I told you, it won't be easy..."
                        jump brothelnight
                    elif  quest4start2:
                        who2 "Long live the king!"
                        who2 "Come on in. Welcome to \"The Red Phoenix\"!"
                        $ renpy.play('sounds/door.mp3')
                        show image "04_pt/slavem/bld.png" with Dissolve(.3)
                        sch3 "Oh, it's you..."
                        play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
                        sch3 "No luck with getting the permit signed so far, huh?"
                        sch3 "I told you, it won't be easy..."
                        jump brothelnight
                    elif quest4start3:
                        who2 "Long live the king!"
                        who2 "Come on in. Welcome to \"The Red Phoenix\"!"
                        $ renpy.play('sounds/door.mp3')
                        show image "04_pt/slavem/bld.png" with Dissolve(.3)
                        play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
                        sch3 "Oh, it's you again, dear..."
                        sch3 "What? You got the permit signed by sultan?"
                        sch3 "I don't believe you! Let me see!"
                        show image "04_pt/slavem/masteritem.png" with moveinright
                        show image "04_pt/slavem/boxbropernit.png" with moveinleft
                        "You hand over the permit."
                        hide image "04_pt/slavem/boxbropernit.png" with moveoutright
                        hide image "04_pt/slavem/masteritem.png" with moveoutleft
                        sch3 "Would you look at that?! It has the royal seal and everything!"
                        sch3 "Well darling, I don't know how you managed to pull this off..."
                        sch3 "But it seems that \”The Red Phoenix\” is about to rise from the ashes once more..."
                        sch3 "I owe you a big one, for this."
                        hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
                        $ quest4complete = True
                        $ quest4start3 = False
                        $ onquest = False
                        $ idlequest = True
                        $ renpy.play('sounds/win2.mp3')                        
                        show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
                        show con1 at right
                        show ctc7 at right
                        pause
                        hide con1
                        hide ctc7
                        "Thanks to you, the brothel has been reopened. You can now visit it both during daytime and at night."
                        $ renpy.play('sounds/door2.mp3')
                        hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
                        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                        ">You decide that you had enough excitement for one day..."
                        ">You return home and go to sleep."
                        show image "interface/blackfade.png" with Dissolve(.3)
                        pause 1
                        jump dayone
        "-Leave-":
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            play music "music/Ozone.ogg" fadein 1 fadeout 1
            jump nightwalk
############################################
label audijafar3:
    if jidle:
        play music "music/JafarsHour.mp3" fadein 1 fadeout 1
        sch4 "I see... Follow me please..."
        show blkfade with Dissolve(.3)
        pause.8
        hide rest03
        hide blkfade with Dissolve(.3)
        sch4 "Your majesty... Please, forgive my intrusion, but there is someone here to see you..."
        jaf[2] "Huh? Oh, it's you, old man..."            
        jaf[2] "What? What is it? Make it quick, I'm busy."
        jaf[7] "You want to do what? Reopen one of the brothels I have closed?"
        jaf[4] "Out of question! Those things suck the gold right out of my pocket!"
        jaf[4] "Brothel owners barely pay any taxes and they make enormous profits."
        jaf[4] "So my answer is \"no\"."
        jaf[7] "Huh? You want for princess Jasmine to work in one?"
        jaf[7] "Are you insane? She is a princess, not some peasant wench!"
        sch13 "Exactly! How could you even think that I would agree to this?"
        jaf[2] "My answer is \"no\"."
        jaf[4] "Now leave. I am a busy man."
        sch4 "I will take you to the exit. Follow me..."  
        play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
        show rest03 with Dissolve(.3)
        jump mainmenu
    else:
        play music "music/JafarsHour.mp3" fadein 1 fadeout 1
        sch4 "I see... Follow me please..."
        show blkfade with Dissolve(.3)
        pause.8
        hide blkfade with Dissolve(.3)
        sch4 "Your majesty... Please, forgive my intrusion, but there is someone here to see you..."
        jaf[2] "Huh? Oh, it's you, old man..."            
        jaf[2] "What? What is it? Make it quick, I'm busy."
        jaf[7] "You want to do what? Reopen one of the brothels I have closed?"
        jaf[4] "Out of question! Those things suck the gold right out of my pocket!"
        jaf[4] "Brothel owners barely pay any taxes and they make enormous profits."
        jaf[4] "So my answer is \"no\"."
        jaf[7] "Huh? You want for princess Jasmine to work in one?"
        jaf[7] "Are you insane? She is a princess, not some peasant wench!"
        jaf[2] "She will never agree to go anywhere near that place..."
        jaf[2] "Hm..."
        jaf[2] "Princess Jasmine – the whore..."
        jaf[6] "I gotta admit it does have a nice ring to it..."
        jaf[2] "Well, if you think you will be able to convince her to work there, then I will not stand in your way."
        jaf[3] "You want to turn our self-righteous princess into a whore? I say, good luck!"
        jaf[6] "Do me a favor, though. Make sure she doesn't get pregnant."
        jaf[2] "I will give the order. The permit shall be ready in two days."
        jaf[4] "Now leave. I am a busy man."
        sch4 "I will take you to the exit. Follow me..."  
        play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
        $ quest4start = False
        $ quest4start2 = True
        jump mainmenu
###############################################
label audijafar4:
    play music "music/JafarsHour.mp3" fadein 1 fadeout 1
    sch4 "Yes, I have your papers here."
    sch4 "It will be 100 gold coins."
    sch4 "What's wrong? That's a usual fee."
    menu:                            
        "You currently have [gold] gold. \nWould you like to pay 100 gold for the papers?"
        "-Pay 100 gold coins-":
            if gold >= 100:
                $ gold -=100
                sch4 "Here are your papers."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxbropernit.png" with moveinright
                "You received a documented permission to reopen \”The Red Phoenix\” brothel, signed by the Sultan."
                $ quest4start2 = False
                $ quest4start3 = True
                hide image "04_pt/slavem/boxbropernit.png" with Dissolve(.4)
                hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                sch4 "I will take you to the exit. Follow me..."  
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump mainmenu                            
            else:
                "You don't have enough gold to purchase this."
                sch4 "I will take you to the exit. Follow me..."  
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump mainmenu
        "-Do not pay-":
            sch4 "Oh, I see... Well, come back whenever you're ready."
            sch4 "Now, please leave."  
            play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            jump mainmenu
    