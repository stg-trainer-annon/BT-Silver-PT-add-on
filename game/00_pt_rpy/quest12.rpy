label fakewhorework:
    if whore:
        if obedience >= 8:
            if courage >= 8:
                show blkfade with d3
                pause.5
                hide blkfade with d3
                play music "music/India's Different (Dancing).MP3" fadein 1 fadeout 1 #DANCING
                sch3 "You want to employ your slave-girl at my establishment?"
                sch3 "Is she pretty...? Have any scars...?"
                sch3 "Oh, wait a second... Is it that Jasper girl?"
                sch3 "The one you send to work for that old dog Maslab sometimes?"
                sch3 "I'm sorry, darling, but I'm afraid I can't help you."
                menu:
                    "\"What? Why not?!\"":
                         if onquest:
                            ">You need to finish your current quest first, before you can take a new one."
                            jump brothelreopned
                         else:
                            sch3 "Because, although Maslab is not very bright..."
                            sch3 "Even he was able to notice that there is something off about your slave-girl..."
                            sch3 "I on the other hand am very clever, and I am pretty sure I know who that girl really is..."
                            sch3 "You call her \"Jasper\", but that's not her real name, is it?"
                            menu:
                                "\"It is. Her name is Jasper!\"":
                                    sch3 "Well, in any case, I want the same permission paper you gave that old dog, Maslab."
                                "\"No. It's actually Jasmine.\"":
                                    sch3 "Seriously!?"
                                    sch3 "You mean, the Princess?"
                                    sch3 "Oh, wow... This is huge..."
                                    sch3 "Having the princess herself working for me would be a total game changer!"
                                    sch3 "I could easily double or Maybe even triple my profits!"
                                    sch3 "And yet, my answer is \"no\"."
                                    sch3 "I want the same permission paper you acquired for that old dog, Maslab."
                            sch3 "Bring me the paper and then we'll talk."
                            $ onquest = True
                            $ quest12start = True
                            $ quest1200 = False
                            show image "04_pt/slavem/qstart.png" with Dissolve(.3)
                            show image "04_pt/slavem/onaquest.png" with Dissolve(.3)
                            show con1 at right
                            show ctc7 at right
                            pause 
                            hide con1
                            hide ctc7
                            hide image "04_pt/slavem/qstart.png" with Dissolve(.3)
                            $ renpy.play('sounds/door2.mp3')
                            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                            if brothelnight:
                                ">You return home and go to sleep."
                                show image "interface/blackfade.png" with Dissolve(.3)
                                pause 1
                                jump dayone
                            else:         
                                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                                jump mainmenu
                    "-Give up for now-":
                        show blkfade with d3
                        pause.5
                        hide blkfade with d3
                        play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                        jump brothelmain 
            else:
                "Jasmine agrees to work in the \"Red Phoenix\" brothel as a whore."
                "But her moral standards are still too high to actually do that..."
                jump brothelmain 
        else:
            show image "04_pt/jasmine/outfit/jas02.png" at right with Dissolve(.3)
            j "You want me to work here?!"
            show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
            hide image "04_pt/jasmine/outfit/jas02.png" 
            j "That's too much, old man. I will never agree to this!"
            hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
            ">Jasmine refuses to sell her body for money."
            jump brothelmain
           

    else:
        ">You need to buy a whore's outfit before Jasmine can work here."
        jump brothelmain
####AUDIENCE WITH JAFAR############
label audijafar7:
    play music "music/JafarsHour.mp3" fadein 1 fadeout 1
    sch4 "I see... Follow me please..."
    sch4 "Your majesty... Please, forgive my intrusion, but there is someone here to see you..."
    jaf[2] "Huh? Oh, it's you, old man..."            
    jaf[2] "What? What is it? Make it quick, I'm busy."
    jaf[2] "You want to make her to work in a brothel?"
    jaf[2] "Are you insane? She would never... Oh well, good luck."
    jaf[2] "You want me to sign the permission? well, of course! Come back in a few days, the papers will be waiting for you."
    jaf[4] "Now leave. I am a busy man."
    sch4 "I will take you to the exit. Follow me..."  
    $ quest12start = False
    $ quest12start2 = True
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    jump mainmenu
#######PICKING UP THE PERMIT######
label audijafar8:
    play music "music/JafarsHour.mp3" fadein 1 fadeout 1
    sch4 "Yes, I have your papers here."
    sch4 "It will be 200 gold coins."
    menu:                            
        "You currently have [gold] gold. \nWould you like to pay 200 gold for the papers?"
        "-Pay 200 gold coins-":
            if gold >= 200:
                $ gold -=200
                sch4 "Here are your papers."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxbropernit.png" with moveinright
                ">You received a documented permission for princess jasmine to legally work as a whore."
                $ quest12start3 = True
                $ quest12start2 = False
                $ quest12days = 0
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

####QUEST COMPLETE#########
label quest12start3:
    show blkfade with d3
    pause.5
    hide blkfade with d3
    sch3 "You brought the permit? Splendid!"
    sch3 "Your girl will make me a very wealthy woman..."
    sch3 "She can start any time!"
    hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
    $ quest12complete = True
    $ quest12start3 = False
    $ onquest = False
    show blkfade with d3
    $ renpy.play('sounds/win2.mp3')                        
    show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    ">New job unlocked: Jasmine can work as a whore now."
    hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    pause.5
    hide blkfade with d3
    jump brothelmain