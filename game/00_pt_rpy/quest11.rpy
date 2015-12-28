label quest1100:
    if onquest:
        "You need to complete the current quest first in order to take on a new one."
        jump tavern2
    else:
        play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab BG
        show blkfade with d3
        pause.5
        hide blkfade with d3
        sch6_5 "You want to employ your Jasper girl as a dancer here?"
        sch6_6 "Well, I will be honest with you..."
        sch6_6 "As much as I would love to allow that..."
        menu:
            sch6_6 "I can't...*spit* I hope you understand."
            "\"What? Why not?\"":
                sch6_6 "Because I may be many things, my friend, but not stupid."
                sch6_6 "I notice things, you know..."
                sch6_6 "The way your Jasper girl talks, the way she keeps her posture..."
                sch6_4 "Not that I'm staring at her all the time or anything... khem..."
                sch6_6 "At first I just thought she is one of those \"Slave-Girl Academy\" graduates or something..."
                sch6_6 "But it is more than that, isn't it?"
                sch6_6 "I don't know who she really is, but she is most likely of high birth..."
                sch6_6 "A daughter of some rather rich nobleman, I would assume..."
                sch6_6 "I don't know how you came by this one, my friend, but let me give you a friendly advice..."
                sch6_6 "Get rid of her while you can. She will bring you nothing but trouble..."
                sch6 "I still don't mind her working here as a waitress of course."
                sch6 "There is nothing wrong with giving her an honest job..."
                sch6_6 "But making her dance for the customers is another story..."
                sch6_6 "I may lose my head for that..."
                sch6 "And I kinda like my head, you know..."
                sch6 "It's not too bright and the face is not exactly handsome..."
                sch6 "But it is still {size=+5}my{/size} head, you know what I mean? Ha-ha-ha!"
                sch6_6 "So, my answer is \"no\", my friend. As much as I love money, I love my head more..."
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                $ onquest = True
                $ quest11start = True
                $ quest1100 = False
                show image "04_pt/slavem/qstart.png" with Dissolve(.3)
                show image "04_pt/slavem/onaquest.png" with Dissolve(.3)
                show con1 at right
                show ctc7 at right
                pause 
                hide con1
                hide ctc7
                hide image "04_pt/slavem/qstart.png" with Dissolve(.3)
                show blkfade with d3
                pause.5
                hide blkfade with d3
                jump tavern2
            "\"I see.\"":
                sch6 "I knew you would understand..."
                show blkfade with d3
                pause.5
                hide blkfade with d3
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                jump tavern2

            
        

            
###MASLAB FRIENDSHIP LOW#####
label notafriendyet:
    sch6 "You want your wench to dance in my tavern?"
    sch6 "Nah... I don't think so, buddy."
    sch6 "I don't know you that well..."
    jump tavern2
#####AUDIENCE WITH JAFAR#######
label audijafar5:
    sch4 "I see... Follow me please..."
    show blkfade with d3
    pause.5
    play music "music/JafarsHour.mp3" fadein 1 fadeout 1
    hide blkfade with d3
    sch4 "Your majesty... Please, forgive my intrusion, but there is someone here to see you..."
    jaf[2] "Huh? Oh, it's you, old man..."            
    jaf[2] "What? What is it? Make it quick, I'm busy."
    jaf[2] "You want to make her dance for the peasants?"
    jaf[5] "(This is brilliant!)"
    jaf[2] "But you know she will never agree to that, right?"
    if jidle:
        sch13_2 "........................"
    jaf[2] "You want me to sign a permission? well, of course! Come back tomorrow, the papers will be waiting for you."
    jaf[4] "Now leave. I am a busy man."
    sch4 "I will take you to the exit. Follow me..."  
    $ quest11start = False
    $ quest11start2 = True
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    jump mainmenu
####PICKING UP THE PERMIT#############
label audijafar6:
    play music "music/JafarsHour.mp3" fadein 1 fadeout 1
    sch4 "Yes, I have your papers here."
    sch4 "That will be 100 gold coins."
    sch4 "What's wrong? That's the usual fee."
    menu:                            
        "You currently have [gold] gold. \nWould you like to pay 100 gold for the papers?"
        "-Pay 100 gold coins-":
            if gold >= 100:
                $ gold -=100
                sch4 "Here are your papers."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxdance.png" with moveinright
                ">You received a documented permission for princess Jasmine to dance in a tavern, signed by the Sultan."
                $ quest11start3 = True
                $ quest11start2 = False
                $ quest11days = 0
                hide image "04_pt/slavem/boxdance.png" with Dissolve(.4)
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

#####GIVING THE PERMIT##########
label quest11start3:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with d3
    pause.5
    hide blkfade with d3
    sch6 "Huh? What's this?"
    show image "04_pt/slavem/masteritem.png" with moveinright
    show image "04_pt/slavem/boxdance.png" with moveinleft
    ">You hand over the permit to Maslab."
    hide image "04_pt/slavem/boxdance.png" with moveoutright
    hide image "04_pt/slavem/masteritem.png" with moveoutleft
    sch6_5 "A permit? Signed by the sultan himself?"
    sch6_5 "What...? But how...?"
    sch6_6 "Who the hell is that girl??"
    sch6 "Well, it doesn't matter, I suppose. If the sultan himself says it's OK for her to dance here, who am I to argue?"
    sch6 "So, yeah, sure, she can start anytime."
    sch6 "Bring her here, but make sure you get her a proper dress."
    sch6 "Did I say proper? I meant inappropriate! ha-ha-ha! This just doesn't get old!"
    $ quest11start4 = True
    $ quest11start3 = False
    show blkfade with d3
    pause.5
    $ renpy.play('sounds/door2.mp3')
    hide image "04_pt/slavem/bld.png"
    hide blkfade with d3
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
    jump mainmenu
######FINAL EXAMINATION IN THE DRESS############
label quest11start4:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with d3
    pause.5
    show bld2
    hide blkfade with d3
    show maslab 1 at right with d3
    sch600 "My friend, it is always nice to see you..."
    sch600 "And you, Jasper, my girl, look simply stunning."
    show jas 17 at left with d3
    j "Thank you... I suppose..."
    show iris 75 with d3
    sch1100 "Hello guys..."
    hide iris with d3
    show iris 28 with d3
    sch1100 "Huh?"
    sch1100 "Father, why is she dressed like that?"
    hide jas with d3
    hide iris with d3
    show iris_f 28 at left with d3
    hide maslab with d3
    show maslab 5 at right with d3
    sch600 "Irirs, from now on Jasper will be working here as a dancer."
    hide iris with d3
    show iris_f 21 at left with d3
    sch1100 "What?!"
    hide iris with d3
    show iris_f 28 at left with d3
    sch1100 "Father, you can't be serious!"
    sch1100 "You won't let {size=+5}me{/size} dance, but you hire {size=+5}her{/size}?"
    hide maslab with d3
    hide iris with d3
    show iris_f 22 at right with d3
    show jas 19 at left with d3
    j ".........................................."
    hide jas with d3
    show iris_f 28 at left
    show maslab 7 at right
    with d3
    sch600 "No, not this again, girl..."
    hide iris with d3
    show iris_f 22 at left with d3
    sch1100 "But father, she is an awful waitress, and she will be an even worse, dancer!"
    hide maslab with d3
    show maslab 6 at right with d3
    sch600 "That's enough, girl! Stop saying nonsense and get back to work."
    hide maslab with d3
    hide iris with d3
    show jas 20 at left with d3
    j "Yes, girl, get back to work."
    show iris 28 at center with d3
    sch1100 "You spoiled little bitch..."
    hide iris
    hide jas
    with d3
    show maslab 3 at right with d3
    with hpunch
    sch600 "{size=+7}Iris!{/size}"
    show iris_f 28 at left with d3
    sch1100 "Tsk! Fine, whatever, I don't care..."
    hide iris with d3
    hide maslab with d3
    show maslab 1 at right with d3
    sch600 "Well, it's decided then."
    show maslab 5 with d3
    sch600 "Leave jasper here with me, I will show her the basics and explain what will be required of her..."
    show maslab 1 with d3
    sch600 "And starting tomorrow she could start working..."
    show blkfade with d3
    hide bld2
    hide maslab
    show quest behind blkfade with Dissolve(.3) 
    hide rest03
    $ onquest = False
    $ jonquest = True
    $ jidle = False   
    $ quest11start4 = False
    $ quest11complete = True
    hide image "04_pt/slavem/onaquest.png" with Dissolve(.3)
    $ renpy.play('sounds/win2.mp3')                        
    show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
    "Jasmine can work as a dancer starting tomorrow."
    hide blkfade with d3
    hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    jump tavern2
    
    
    
    
    

    
    
    
    
    
  
    
    
    