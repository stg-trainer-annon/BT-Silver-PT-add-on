

label jasminsroom:
    $ renpy.play('sounds/door3.mp3')
    pause 1
    $ renpy.play('sounds/door.mp3')
    show blkfade with d3
    pause.5
    hide blkfade with d3
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    show screen jasmine_sprite_room
    
    if obedience >= 0 and obedience < 2:
        j "Tsk... What do you want of me, [myname]?"
    elif obedience == 2:
        j "Oh, it's you, [myname]."
    elif obedience == 3:
        j "What is it, [myname]?"
    elif obedience == 4:
        j "What is it that you want of your [jasname] this time, [myname]?"
    elif obedience == 5:
        j "Good evening, [myname]."
        j "What will it be this time?"
    elif obedience == 6:
        j "Tell your [jasname] what you want her to do, [myname]."
    elif obedience == 7:
        j "Tell your [jasname] what you want of her this time, [myname]."
        j "I will follow your every order..."
        j "Well, almost every order..."
    elif obedience == 8: 
        j "I'm your [jasname]."
        j "And I will do whatever you say, [myname]."
    elif obedience == 9: 
        j "[myname], thank you for taking your time to visit me."
        j "How can your [jasname] serve you tonight?"
    elif obedience >= 10:
        j "I will gladly do anything you want me to, [myname]."
        j "I am your [jasname] after all..."
            
label jasminesroom1:   
    menu:
        m "................"
        "\"Feed me fruits...\"":
            if tired >= 2:
                ">Jasmine is too tired to do this today."
                jump jasminesroom1
            else: 
                if obedience >= 6 and courage >= 3:  
                    jump fruit4
                elif obedience >= 4 and courage >= 1:  
                    jump fruit3
                elif obedience >= 2:  
                    jump fruit2
                else:
                    jump fruit1
                
                
                
                
                
                
#                if obedience >= 0 and obedience < 2:
#                    jump fruit1
#                elif obedience >= 2 and courage < 1:  
#                    jump fruit2
#                elif obedience >= 4 and obedience < 6 and courage >= 1:  
#                    jump fruit3
#                elif obedience >= 6 and courage >= 3:  
#                    jump fruit4
        
        
#                if obedience >= 0 and obedience < 2:
#                    jump fruit1
#                elif obedience >= 2 and obedience < 4:  
#                    jump fruit2
#                elif obedience >= 4 and obedience < 6:  
#                    jump fruit3
#                elif obedience >= 6:  
#                    jump fruit4
                    
        "\"Dance for me...\"":
            if tired >= 2:
                ">Jasmine is too tired to do this today."
                jump jasminesroom1
            else: 
                if dancer:
                    if obedience >= 9 and courage >= 5:
                        jump dance5
                    elif obedience >= 7 and courage >= 3:  
                        jump dance4
                    elif obedience >= 5 and courage >= 1:  
                        jump dance3
                    elif obedience >= 3:  
                        jump dance2
                    else:
                        jump dance1
                
                    
#                    if obedience >= 0 and obedience < 3:
#                        jump dance1
#                    elif obedience >= 3 and obedience < 5:  
#                        jump dance2
#                    elif obedience >= 5 and obedience < 7 and courage < 2:  
#                        jump dance3
#                    elif obedience >= 7 and obedience < 9 and courage < 4:  
#                        jump dance4
#                    elif obedience >= 9 and courage >= 5:
#                        jump dance5
                else:
                    jump wanttodance
                            
        "\"Have sex with me...\"":
            if tired >= 2:
                ">Jasmine is too tired to do this today."
                jump jasminesroom1
            else: 
                if obedience >= 7 and courage >= 9:
                    jump sexp4
                elif obedience >= 4 and courage >= 5:  
                    jump sexp3
                elif obedience >= 4 and courage >= 3:  
                    jump sexp2
                else:
                    jump sexp1
                 
                 
                 
#                if obedience >= 0 and obedience < 4:
#                    jump sexp1
#                elif obedience >= 4 and obedience < 7 and courage > 3:  
#                    jump sexp2
#                elif obedience >= 7 and obedience < 10 and courage < 7:  
#                    jump sexp3
#                elif obedience >= 10 and courage >= 10:
#                    jump sexp4

        "\"Put on another outfit...\"":
            label jasmine_outfit_menu:
            menu:
                "Choose an outfit that you woul want jasmine to greet you in, every time you enter her room."
                "-Normal princess outfit-" if not normalw2:
                    ">Princess Jasmine agrees to wear that outfit in front of you."
                    call jas_change_clothes("normal")
                    jump jasmine_outfit_menu
                "-Peasant robe-" if peasant and not peasantw2:
                    if obedience >= 2:
                        ">Princess Jasmine agrees to wear this outfit in front of you."
                        call jas_change_clothes("peasant")
                        jump jasmine_outfit_menu
                    else:
                        ">Princess Jasmine refuses to wear this outfit in front of you."
                        jump jasminesroom1
                "-Tavern wench-" if taverngirl and not tavernw2:
                    if obedience >= 3:
                        ">Princess Jasmine agrees to wear this outfit in front of you."
                        call jas_change_clothes("tavern")
                        jump jasmine_outfit_menu
                    else:
                        ">Princess Jasmine refuses to wear this outfit in front of you."
                        jump jasminesroom1
                "-Dancer girl-" if dancer and not dancew2:
                    if obedience >= 3:
                        "Princess Jasmine agrees to wear this outfit in front of you."
                        call jas_change_clothes("dance")
                        jump jasmine_outfit_menu
                    else:
                        ">Princess Jasmine refuses to wear this outfit in front of you."
                        jump jasminesroom1
                "-Whore-" if whore and not whorew2:
                    if obedience >= 5:
                        ">Princess Jasmine agrees to wear this outfit in front of you."
                        call jas_change_clothes("whore")
                        jump jasmine_outfit_menu
                    else:
                        ">Princess Jasmine refuses to wear this outfit in front of you."
                        jump jasminesroom1
                "-Slave-girl-" if slavegirl and not slavew2:
                    if obedience >= 6:
                        ">Princess Jasmine agrees to wear this outfit in front of you."
                        call jas_change_clothes("slave")
                        jump jasmine_outfit_menu
                    else:
                        "the Princess refuses to wear this outfit in front of you."
                        jump jasminesroom1
                "-Fully naked-" if obedience >= 8 and not naked2:
                    ">Princess Jasmine agrees to wear this outfit in front of you."
                    call jas_change_clothes("naked")
                    jump jasmine_outfit_menu
                "{color=#858585}...(LOCKED)...{/color}" if not lolamovedin:
                    ">You need to complete a correlating quest to unlock this outfit."
                    jump jasmine_outfit_menu
                "-Fully naked lolita-" if lolamovedin and not naked_lolita:
                        ">Princess Jasmine agrees to wear this outfit in front of you."
                        call jas_change_clothes("naked_lolita")
                        jump jasmine_outfit_menu
                "-Return-":
                    jump jasminesroom1
        "\"Address me only as...\"": 
            menu:
                "Here you can choose the way you want jasmine to address you."
                "\"My lord\".":
                     if obedience >= 2:
                        $ myname = "My lord"
                        j "As you wish. From now on I shall dress you as \"[myname]\"."
                        jump jasminesroom1
                     else:
                        jump selftiteno
                "\"Filthy bum\".":
                    $ myname = "Filthy bum"
                    j "As you wish. From now on I shall dress you as \"[myname]\"."
                    jump jasminesroom1
                "\"Old man\".":
                    $ myname = "Old man"
                    j "As you wish. From now on I shall dress you as \"[myname]\"."
                    jump jasminesroom1
                "\"Master\".":
                    if obedience >= 3:
                        $ myname = "Master"
                        j "As you wish. From now on I shall dress you as \"[myname]\"."
                        jump jasminesroom1
                    else:
                        jump selftiteno
                "\"My king\".":
                    if obedience >= 4:
                        $ myname = "My king"
                        j "As you wish. From now on I shall dress you as \"[myname]\"."
                        jump jasminesroom1
                    else:
                        jump selftiteno
                "\"My owner\".":
                    if obedience >= 4:
                        $ myname = "My owner"
                        j "As you wish. From now on I shall dress you as \"[myname]\"."
                        jump jasminesroom1
                    else:
                        jump selftiteno
                "\"My husband\".":
                    if obedience >= 3:
                        $ myname = "My husband"
                        j "As you wish. From now on I shall dress you as \"[myname]\"."
                        jump jasminesroom1
                    else:
                        jump selftiteno
                "\"My tormentor\".":
                    if obedience >= 1:
                        $ myname = "My tormentor"
                        j "As you wish. From now on I shall dress you as \"[myname]\"."
                        jump jasminesroom1
                    else:
                        jump selftiteno
                "\"My beast\".":
                    if obedience >= 4:
                        $ myname = "My beast"
                        j "As you wish. From now on I shall dress you as \"[myname]\"."
                        jump jasminesroom1
                    else:
                        jump selftiteno
                "\"Pussy destroyer\".":
                    if obedience >= 6:
                        $ myname = "Pussy destroyer"
                        j "As you wish. From now on I shall dress you as \"[myname]\"."
                        jump jasminesroom1
                    else:
                        jump selftiteno
                "-Manual input-":
                     if obedience <= 6:
                        j "Tsk... I will never agree to that..."
                        jump jasminesroom1
                     else:
                        show image im.Alpha("interface/blackfade.png", 0.8) #MENU_CHOISE_BG
                        # The phrase in the brackets is the text that the game will display to prompt 
                        # the player to enter the name they've chosen.

                        $ myname = renpy.input("(Use keyboard to enter new title for yourself.)")

                        $ myname = myname.strip()
                        # The .strip() instruction removes any extra spaces the player may have typed by accident.

                        #  If the player can't be bothered to choose a name, then we
                        #  choose a suitable one for them:
                        if myname == "":
                            $ myname="old man"
                            hide image im.Alpha("interface/blackfade.png", 0.8) #MENU_CHOISE_BG
                            j "You didn't say anything...."
                            j "Does it mean you let me choose?"
                            j "As you wish. I shall address you as \"[myname]\" then."
                            jump jasminesroom1
                        hide image im.Alpha("interface/blackfade.png", 0.8) #MENU_CHOISE_BG
                        j "As you wish. From now on I shall address you as \"[myname]\"."
                        jump jasminesroom1
                         
                "-Cancel-":
                    jump jasminesroom1
        "\"Address yourself as...\"":
            menu:
                "Choose the way you want jasmine to address herself."
                "\"Princess\".":
                    $ jasname = "Princess"
                    j "As you wish. From now on I shall address you as \"[jasname]\"."
                    jump jasminesroom1
                "\"Bimbo\"":
                    if obedience >= 2 and courage >= 1:
                        $ jasname = "Bimbo"
                        j "As you wish. From now on I shall address myself as \"[jasname]\"."
                        jump jasminesroom1
                    else:
                        jump jasselfno
                "\"Pet\".":
                    if obedience >= 3:
                        $ jasname = "pet"
                        j "As you wish. From now on I shall address myself as \"[jasname]\"."
                        jump jasminesroom1
                    else:
                        jump jasselfno
                "\"Filthy Slut\".":
                    if obedience >= 5 and courage >= 3:
                        $ jasname = "Filthy Slut"
                        j "As you wish. From now on I shall address myself as \"[jasname]\"."
                        jump jasminesroom1
                    else:
                        jump jasselfno
                "\"Whore\".":
                    if obedience >= 5 and courage >= 2:
                        $ jasname = "Whore"
                        j "As you wish. From now on I shall address myself as \"[jasname]\"."
                        jump jasminesroom1
                    else:
                        jump jasselfno
                "\"Lover\".":
                    if obedience >= 6:
                        $ jasname = "Lover"
                        j "As you wish. From now on I shall address myself as \"[jasname]\"."
                        jump jasminesroom1
                    else:
                        jump jasselfno
                "\"Fuck-toy\".":
                    if obedience >= 7:
                        $ jasname = "Fuck-toy"
                        j "As you wish. From now on I shall address myself as \"[jasname]\"."
                        jump jasminesroom1
                    else:
                        jump jasselfno
                "\"Royal Bitch\"":
                    if obedience >= 8:
                        $ jasname = "Royal Bitch"
                        j "As you wish. From now on I shall address myself as \"[jasname]\"."
                        jump jasminesroom1
                    else:
                        jump jasselfno
                "\"Shameless slut\".":
                    if obedience >= 6:
                        $ jasname = "Shameless slut"
                        j "As you wish. From now on I shall address myself as \"[jasname]\"."
                        jump jasminesroom1
                    else:
                        jump jasselfno
                "\"Prostitute\".":
                    if obedience >= 7:
                        $ jasname = "Prostitute"
                        j "As you wish. From now on I shall address myself as \"[jasname]\"."
                        jump jasminesroom1
                    else:
                        jump jasselfno
                "-Manual input-":
                    if obedience <= 6:
                        j "Tsk... I will never agree to that..."
                        jump jasminesroom1
                    else:
                        show image im.Alpha("interface/blackfade.png", 0.8) #MENU_CHOISE_BG
                        # The phrase in the brackets is the text that the game will display to prompt 
                        # the player to enter the name they've chosen.

                        $ jasname = renpy.input("(Use keyboard to enter new title for your slave-girl.)")

                        $ jasname = jasname.strip()
                        # The .strip() instruction removes any extra spaces the player may have typed by accident.

                        #  If the player can't be bothered to choose a name, then we
                        #  choose a suitable one for them:
                        if jasname == "":
                            $ jasname="Princess"
                            hide image im.Alpha("interface/blackfade.png", 0.8) #MENU_CHOISE_BG
                            j "You didn't say anything...."
                            j "Does it mean you let me choose?"
                            j "As you wish. I shall address myself as \"[jasname]\" then."
                            jump jasminesroom1
                         
                        # Now the other characters in the game can greet the player.
  
    
    #Edit: If you are using the new version of ren'py, use the following line instead of the one above, since that changed:
    #e "Pleased to meet you, [player_name]!"
                   
#                    python:
#                        jasname = renpy.input("What is your name?")
#                        jasname = jasname.strip()
#                        if jasname:
#                            jasname = "Jasmine"
                    hide image im.Alpha("interface/blackfade.png", 0.8) #MENU_CHOISE_BG
                    j "As you wish. From now on I shall address myself as \"[jasname]\"."
                    jump jasminesroom1
                "-Cancel-":
                    jump jasminesroom1
        "-Leave-":
            jump leavejroom
######PERSONAL REQUESTS######
label personalorders:
    if tired >= 2:
        "Jasmine is too tired for that."
        jump dayends
    else: 
        if obedience >= 0 and obedience < 3:
            j "Tsk..."
        elif obedience >= 3 and obedience < 6:
            j "What is it that you want of me this time, old man?"
        elif obedience >= 6 and obedience < 8:
            j "Tell me what you want me to do, I will follow your every order..."
            j "Well, almost every order..."
        elif obedience >= 8: 
            j "I will do whatever you say, master."
        
            menu:
                "Feed me fruits.":
                    if tired >= 2:
                        "Jasmine is too tired to do this today."
                        jump dayends
                    else: 
                        if obedience >= 2:  
                            show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
                            "Jasmine agrees to playfully feed you some fruits." 
                            show ffeed with Dissolve(.3)
                            show con1 at right
                            show ctc7 at right
                            pause 
                            hide con1
                            hide ctc7
                            "Jasmine obediently feeds you some grapes."
                            "Afterwards she leaves for her room."
                            show image "interface/blackfade.png" with Dissolve(.3)
                            pause 1
                            jump dayone
                        else:
                            "Jasmine refuses to obey your command and locks herself in her room."
                            jump dayone
                "Dance for me.":
                    if tired >= 2:
                        "Jasmine is too tired to do this today."
                    else:
                        if dancer:
                            if obedience >= 3:                                    
                                show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
                                "Jasmine agrees to dance for you."
                                show pdance with Dissolve(.3)
                                show con1 at right
                                show ctc7 at right
                                pause 
                                hide con1
                                hide ctc7
                                "She gives it all she's got and you have a lot of fun watching her dance around."
                                "Afterwards she leaves for her room."
                                show image "interface/blackfade.png" with Dissolve(.3)
                                pause 1
                                jump dayone
                            else:
                                "Jasmine refuses to obey your command and locks herself in her room."
                                jump dayone
                        else:
                            "Jasmine refuses to dance for you without a proper dancer outfit."
                            jump dayends
                        
                "Have sex with me.":
                    if tired >= 1:
                        "Jasmine is too tired to do this today."
                        jump dayends 
                         
                    else:
                        if obedience >= 7:
                            show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
                            "Jasmine agrees to spend the night with you."                           
                            show sex2 with Dissolve(.3)
                            show con1 at right
                            show ctc7 at right
                            pause 
                            hide con1
                            hide ctc7
                            "You have passionate and disrespectful sex with her."
                            "Afterwards she leaves for her room."
                            show image "interface/blackfade.png" with Dissolve(.3)
                            hide image "04_pt/slavem/night.jpg" 
                            hide image "04_pt/slavem/night2.jpg"
                            hide sex2
                            pause 1
                            jump dayone
                        else:
                            show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
                            "Jasmine refuses your order and locks herself in her room."
                            show image "interface/blackfade.png" with Dissolve(.3)
                            hide image "04_pt/slavem/night.jpg" 
                            hide image "04_pt/slavem/night2.jpg"
                            pause 1
                            jump dayone
                "Cancel.":
                    jump jasminesroom1
                    
                
        

###JAS SELF NO####
label jasselfno:
    j "Tsk... that's preposterous! I will never agree to address myself in this manner."
    jump jasminesroom1
###SELF TITLE NO#####
label selftiteno:
    j "Tsk... that's laughable! \nI will never agree to address you that way."
    jump jasminesroom1
######LEAVING THE ROOM#####
label leavejroom:
    show image "interface/blackfade.png" with Dissolve(.2)
    hide screen jasmine_sprite_room
    with d3
    hide image "04_pt/slavem/bld.png" 
    $ renpy.play('sounds/door2.mp3')
    hide image "interface/blackfade.png" with Dissolve(.2)
    jump dayended
######################FRUITS########################
label fruit1:
    j "What?"
    j "You forgetting your place, old man."
    jump jasminesroom1

label fruit2:
    j "......................"
    j "........."
    j "Well, alright..."
    hide screen jasmine_sprite_room
    with d3
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
    
    ">Jasmine leaves for the pantry..."
    ">You sit down on one of the cushions in the main room and wait for her return..."
    ">A moment later the princess appears holding a tray of fruits..."
    ">She doesn't look too happy about her task..."
    jas[36] "{size=-5}(I can not believe I have to stoop this low...){/size}"
    menu:
        jas[36] "I'm not your servant, you know..."
        "\"That's exactly what you are.\"":
            m "Right now that's exactly what your are, your majesty..."
            jas[37] "Tsk..."
            jas[38] "Old fool..."
            jas[38] "My current predicament is merely temporary... Soon I will find a way to rise back to power..."
            m "Perhaps..."
            m "But until then we should both obey the sultan's order..."
            jas[38] "Tsk... whatever..."
        "\"No, you are my slave.\"":
            m "A servant? Of course not... Servants get paid... You are my slave."
            jas[38] "For now..."
            jas[38] "Never forget that I will eventually get my throne back..."
            m "Yes, that is a possibility I suppose..."
            jas[38] "Yes... Keep that in mind before you decide to mistreat me in any way..."
            m "Mistreat you, your majesty? I wouldn't dare..."
            m "I will only treat you in the way you deserve to be treated, you have my word..."
            jas[38] "......................"
        "\"No, you are a Princess...\"":
            m "Of course not... You are a princess, your majesty..."
            jas[38] "Y-yes.... I am..."
            jas[36] "Wait, are you making fun of me?"
            jas[37] "Nothing lasts, forever, you know..."
            jas[36] "Enjoy your position of power while you can..."
            m "Oh, I intend to..."

    m "Now, where are my fruits, I'm getting hungry..."
    show image "00_personal/fruit02.jpg" with d5
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    ">You spend the rest of the evening in Jasmine's company..."
    ">It is pretty obvious that she despises you, and yet she obeys your command..."
    ">At some point you put your hand on Jasmine's butt and give it a light squeeze..."
    ">Jasmine shoots you a glare full of contempt but keeps on with her task..."
    ">She keeps feeding you fruits while you caress her butt lightly with one hand and stroke your own cock with another..."
    ">Every bite of fruit you receive is accompanied by a glare from Jasmine full of repulsion..."
    ">Despite that you keep enjoying yourself swallowing while down succulent fruits and feeling Jasmine's firm and round butt..."
    ">Before you know it the fruit tray is empty..."
    ">Jasmine gets up and leaves in a hurry without saying a word..."
    show image "interface/blackfade.png" with Dissolve(.7)
    ">You hate to see her go, but it's probably enough for today..."
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide image "00_personal/fruit02.jpg" 
    pause 1
    hide image "04_pt/slavem/night2.jpg" 
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show sleeping with Dissolve(.3)
    ">Jasmine goes to bed ...."
    jump jasdreams
####
label fruit3:
    j "As you wish..."
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
    
    ">Jasmine leaves for the pantry..."
    ">You sit down on one of the cushions in the main room and wait for her return..."
    ">A moment later the princess appears holding a tray of fruits..."
    ">She looks very relaxed and casual..."
    ">It seems like she doesn't mind serving you food anymore."
    ">She probably just got used to it by now..."

    jas[39] "I bought some really delicious grapes this morning, wait till you try them..."
    ">She seats down by your side and starts feeding you the fruits..."
    ">The grapes really are quite delicious..."
    ">You put your hand on Jasmine's butt and give it a squeeze, as usual..."
    ">She doesn't seem to notice, (or care) and continues to feed you nonchalantly..."
    jas[38] "By the way, I was meaning to ask you something..."
    m "Yes...?"
    menu:
        jas[39] "Do I really have to call you \"[myname]\"?"

        "\"Yes. That's that's an order.\"":
            m "Yes... That's exactly how you must address me."
            m "And that's why I told you to call me that and nothing else."
            m "That's an order."
            ">Jasmine feeds you another grape."
            jas[38] "I see..."
        "\"What's wrong with \"[myname]\"?\"":
            m "What is wrong with \"[myname]\"? I like the sound of it."
            jas[41] "Nothing, nothing is wrong with it, [myname]...."
            ">Jasmine feeds you another grape."
            jas[41] "It just... I don't think it fits you..."
            m "Hm..."
            m "Alright... Let me sleep on it."
            jas[40] "As you say, [myname]..."

        "\"What would you want to call me?\"":
            m "Hm... What would you call me then?"
            jas[38] "Hm... Let me think..." 
            ">Jasmine puts another fruit in your mouth absentmindedly..."
            jas[39] "I don't know... anything but [myname] would do..."
            m "Hm... Well, maybe I could come up with something better..."
            m "I will let you know..."
            jas[40] "Of course, as you wish, [myname]."

    ">You open your mouth and princess puts another grape on your tongue."
    ">You squish the berry between your teeth while you keep caressing Jasmine's butt with one hand and stroke your own cock with another..."
    ">Jasmine doesn't seem to mind any of that..."
    ">It doesn't look like she might be enjoying it either though..."
    ">She is simply doing her job it seems..."
    show image "00_personal/fruit03.jpg" with d5
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    ">Jasmine keeps chatting casually while you keep groping her behind any way you like..."
    ">You give her butt a light squeeze then a good strong one and pat on it a few times..."
    ">Before you know it the fruit tray is empty..."
    ">Jasmine get's up and about to leave..."
    show image "interface/blackfade.png" with Dissolve(1)
    ">Jasmine seems pleased to finally be used to at least one aspect of her new life with you..." 
    ">You hate to see her go, but it's probably enough for today..."
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide image "00_personal/fruit03.jpg" 
    pause 1
    hide image "04_pt/slavem/night2.jpg" 
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show sleeping with Dissolve(.3)
    ">Jasmine goes to bed ...."
    jump jasdreams
###
label fruit4: 
    j "Of course, [myname]. As you wish."
    hide screen jasmine_sprite_room
    with d3
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
    ">Jasmine leaves for the pantry..."
    ">You sit down on one of the cushions in the main room and wait for her to return..."
    ">A moment later the princess appears holding a tray of fruits..."
    ">She looks excited..." 
    ">Is she taking some sort of twisted pleasure from following your orders now?"
    jas[42] "Here you go, [myname]."
    ">As soon as Jasmine sits beside you, you put your hand on her butt as usual..."
    ">She glances at you and shifts her weight a little so that you can have easier access to her butt..."
    jas[42] "Thank you for giving me a chance to attend the \"Slave Girl Academy\", [myname]..."
    ">She puts a berry on your tongue..."
    jas[42] "I admit, at first I was very skeptical about the institution as a whole, but now..."
    ">Another piece of fruit finds its way into your mouth."
    jas[42] "Now, I think it was a great idea for me to attend it... They taught me so much..."
    ">As she says that, the princess moves her hips slightly to push them against your open palm even more..."
    ">You give her behind a few approving pats." 
    show image "00_personal/fruit04.jpg" with d5
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    j "So many ways to control the men... To bend them to my will..."
    g3 "What? I thought they teach you obedience there?"
    j "Oh, that too of course... Among other things..."
    ">Jasmines gives you a playful smile but her eyes remain serious..."
    ">That makes you feel uneasy for some reason..."
    ">As usual you also stroke your cock lightly..."
    ">You notice that the Princess can't help but glance at it with anger in her eyes every now and then..."
    ">Jasmine keeps feeding you while you keep groping her butt."
    ">She doesn't seem to mind it. If anything she looks like she is actually enjoying it quite a bit."
    ">Is this an act? Something they taught her at the academy?"
    ">The fruit tray empties before you know it, as usual."
    ">Jasmine gets up..."
    show image "interface/blackfade.png" with Dissolve(1)
    ">You hate to see her go, and yet you dismiss her with a nod..."
    ">Jasmine seems disappointed..."
    ">Did she expect something else... Is she trying to use one of those \"men-bending-techniques\" on you?"
    ">Jasmine leaves you alone with your thoughts..."
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide image "00_personal/fruit04.jpg" 
    pause 1
    hide image "04_pt/slavem/night2.jpg" 
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show sleeping with Dissolve(.3)
    ">Jasmine goes to bed ...."
    jump jasdreams
        
    
##################DANCE##############################
label dance1:
    j ">You want me to dance for you? Have you gone insane, old man?"
    j ">I am still a princess, you better not forget that."
    jump jasminesroom1
label dance2:
    j "To be honest I do enjoy dancing..."
    j "Hm..."
    j "Alright, I will do it... Not for you of course, but rather for my own entertainment..."
    j "You can watch if you want though..."
    hide screen jasmine_sprite_room
    with d3
    show image "interface/blackfade.png" with Dissolve(1)
    ">Princess Jasmine is dancing for you..."
    ">Despite of what she said you can see that she is very aware of your presence..."
    ">Her movements seem awkward and somewhat restricted..."
    ">She does look beautiful in that outfit though..."
    ">Unable to resist you take your cock out and start stroking it in front of her..."
    show image "00_personal/dance01.jpg" with Dissolve(1)
    hide image "interface/blackfade.png" 
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    ">Princess jasmine shoots you a look of deep and sincere disgust, but keeps on with her routine until the dance is over..." 
    ">After that she leaves the room in a fury slamming the door behind herself." 
    show image "interface/blackfade.png" with Dissolve(1)
    $ renpy.play('sounds/door2.mp3')
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide image "00_personal/fruit04.jpg" 
    pause 1
    hide image "04_pt/slavem/night2.jpg" 
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show sleeping with Dissolve(.3)
    ">Jasmine goes to bed ...."
    jump jasdreams
    
label dance3:
    j "I will dance for you on one condition..."
    m "I'm listening..."
    menu:
        j "You will have enough decency to keep your vile cock in your pants at all times..."

        "\"We have a deal.\"":
            j "Alright then..."
        "\"We'll see how it goes.\"":
            j "Tsk... Dirty, uneducated brute..."
        "\"Can't promise that.\"":
            j "Do you have no shame at all?"
            j "Fine, suit yourself, you dirty peasant..."
    hide screen jasmine_sprite_room
    with d3
    show image "interface/blackfade.png" with Dissolve(1)
    play music "music/India's Different (Dancing).MP3" fadein 1 fadeout 1 #DANCING
    ">Princess Jasmine is dancing for you..."
    ">Today her movements seem more fluid and confident..."
    ">She looks even more beautiful and elegant then usual..."
    ">You reach for your cock again and pull it out of your pants..."
    ">Princess Jasmine is taking bows left and right shaking her hips quite gracefully..."
    ">Her ample tits bonce up and down with every pirouette..."
    ">Jasmine notices that you are jerking your cock in front of her again..."
    show image "00_personal/dance02.jpg" with Dissolve(1)
    hide image "interface/blackfade.png" 
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    ">She shoots you an angry glance, but keeps dancing..."
    ">You see that she not nearly as repulsed by your actions as she used to..."
    ">When the dance is over she hesitates for a second in the middle of the room..."
    ">Then shoots another angry glance toward your fully erect manhood and storms out of the room flustered."
    show image "interface/blackfade.png" with Dissolve(1)
    $ renpy.play('sounds/door2.mp3')
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide image "00_personal/dance02.jpg" 
    pause 1
    hide image "04_pt/slavem/night2.jpg" 
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show sleeping with Dissolve(.3)
    ">Jasmine goes to bed ...."
    jump jasdreams

label dance4:
    j "Of course... As you wish, [myname]."
    hide screen jasmine_sprite_room
    with d3
    show image "interface/blackfade.png" with Dissolve(1)
    ">Princess Jasmine enters the room, and to your surprise she is topless..."
    play music "music/India's Different (Dancing).MP3" fadein 1 fadeout 1 #DANCING
    ">She tries to proceed with her dancing routine as if nothing happened but you can see that she is very self-conscious of her naked tits..."
    ">She makes a few pirouettes... Her naked breasts bounce uncontrollably with her every movement..."
    ">For a moment you just sit there completely mesmerized by an unexpected spectacle..."
    ">You notice that Jasmine keeps glancing at her crotch..."  
    ">You take your cock out and start jerking it off as usual..."
    ">Jasmine keeps dancing but her eyes are locked on your erect cock..."
    show image "00_personal/dance03.jpg" with Dissolve(1)
    hide image "interface/blackfade.png" 
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    ">She makes a few awkward movements and takes a few provocative poses..."
    ">Her ample round tits are almost within your grasp, and she flaunts them in front of you so boldly..."
    ">It seems that that \"Slave Girl academy\" already did a great number on the woman."
    ">Suddenly the dance is over..."
    ">You see that Jasmine is starring at your cock with something almost like hunger in her eyes..."
    ">But before you can say anything she covers her tits with her arms, gives you an angry stare and storms out of the room..."
    show image "interface/blackfade.png" with Dissolve(1)
    $ renpy.play('sounds/door2.mp3')
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide image "00_personal/dance02.jpg" 
    pause 1
    hide image "04_pt/slavem/night2.jpg" 
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show sleeping with Dissolve(.3)
    ">Jasmine goes to bed ...."
    jump jasdreams

label dance5:
    j "With pleasure, [myname]."
    hide screen jasmine_sprite_room
    with d3
    show image "interface/blackfade.png" with Dissolve(1)
    ">Princess Jasmine enters the room... Her tits are completely naked and bounce a little with every step she takes..."
    ">Suddenly she breaks into a dance..."
    play music "music/India's Different (Dancing).MP3" fadein 1 fadeout 1 #DANCING
    ">And this is a level of performance you were yet to see form your slave-girl."
    ">The dance is full of energy, emotion and passion..."
    ">She shakes her hips then slides down on the floor like a snake, then she is on her feet again..."
    ">She is shaking her naked tits in front of your face... Makes a few graceful pirouettes, lands on all fours and sprints into motion again..."
    ">Despite her confident and precise movements you can't help but notice that many moves she makes seem a bit out of place..."
    ">It seems she is putting a lot of effort into adding some really awkward movements just to make sure her tits bounce and jiggle all over the place..."
    ">And she succeeds at that... Her tits are completely out of control..."
    ">Suddenly you realize that the wench mesmerized you so that you even forgot about your cock..."
    ">You fix that oversight right away..."
    show image "00_personal/dance04.jpg" with Dissolve(1)
    hide image "interface/blackfade.png" 
    hide image "interface/blackfade.png" 
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    ">Jasmine keeps dancing... Her routine get's more and more aggressive..."
    ">During all that she keeps staring at your cock, taunting you..."
    j "Come on, you filthy peasant... The princess of Agrabah is dancing for you like some common slave-girl!"
    j "What else do you need?"
    j "Don't you like my tits?"
    ">You feel that the excitement is too much to bear and start to jerk your cock faster..."
    ">You let out a groan and see that Jasmine's eyes lit up with excitement because she understands what's about to happen..."
    ">Thick streams of hot cum shot out of your cock towards the woman..."
    show image "00_personal/dance05.jpg" with flashbulb
    with hpunch
    ">Some of your semen gets on her body..."
    j "Ah{image=textheart.png}... Your cum is so hot..."
    ">But it doesn't stop Jasmine from dancing..."
    ">Jasmine keeps danicnig while you shower her with your cum..."
    ">She makes a few rather complex pirouettes... She keeps dancing while your are cumming on her..."
    ">You can clearly see a few stings of your cum on her pants and hips..."
    ">Jasmine finishes the dance... You both breathe heavily..."
    show image "00_personal/dance06.jpg" with flashbulb
    ">the Princess is looking at your cock for a second, then takes a step towards you..."
    ">Accidentally she lands her foot right in the middle of a cum puddle on the floor..."
    $ renpy.play('sounds/gltch.mp3')
    ">She looks down in bewilderment, and then back at you."
    j "I will clean this up later, [myname]."
    ">And then before you could react she covers her tits suddenly acting all coy and leaves the room..."
    show image "interface/blackfade.png" with Dissolve(1)
    $ renpy.play('sounds/door2.mp3')
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide image "00_personal/dance02.jpg" 
    pause 1
    hide image "04_pt/slavem/night2.jpg" 
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show sleeping with Dissolve(.3)
    ">Jasmine goes to bed ...."
    jump jasdreams


        

        

        
    
###
label wanttodance:
    j "You want me do dance wearing these clothes?"
    j "Out of question..."
    j "I demand a proper outfit."
    jump jasminesroom1
    
    
label sexp1:
    j "What? You can't possibly expect me to say \"yes\" to this?!"
    j "Are you insane? "
    j "I can't believe Jafar entrusted my so-called \"training\" to a madman?!"
    j "I can not believe you would even ask such a thing!"
    jump jasminesroom1

label sexp2:
    j "No! My answer will always be the same!"
    j "I don't care what Jafar says..."
    jump jasminesroom1
    
label sexp3:
    j "Em..."
    j "I know I'm supposed to obey your every command, [myname], but..."
    j "Well, so be it."
    j "But let's do this real quick, alright?"
    hide screen jasmine_sprite_room
    with d3
    show image "interface/blackfade.png" with Dissolve(1)
    ">Jasmine turns around, sticks her butt out a and pulls down her pants..."
    j "What are you waiting for, old man? Stick it in me and let's be done with this."
    ">You were caught completely off guard by such quick and unexpected development, so it takes you a few seconds to react..."
    j "What are you doing there? have you changed your mind?"
    ">Quickly, you take your erect cock out..."
    ">It seems your body responded to the situation appropriately much faster than your brain did..."
    ">You grab Jasmine by her ass and slide your cock deep in her..."
    play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
    show image "00_personal/sex01.jpg" with Dissolve(1)
    hide image "interface/blackfade.png" 
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    j "You... Y-you peasant, I mean [myname]..."
    j "Now just start moving... Come on, old man..."
    j "It's too late to turn back now. Just fuck me already."
    ">You follow her advice and start fucking her..."
    ">Abruptly Jasmine gets really quiet and all you can hear for a while are your heavy breathing and the thumping of flesh against flesh..." 
    ">You keep going at it for quite some time... It is hard to say what is going on through Jasmine's mind..."
    ">The only sound you hear from her is her panting..."
    ">You have a feeling that she doesn't enjoy this much..."
    ">She is just following your orders..."
    ">But you don't have time to concentrate on her emotions for too long..."
    ">Her pussy is amazing, so tight and despite her cold behavior, very wet."
    ">You feel that you are getting close..."
    ">Jasmine notices that as well..."
    show image "00_personal/sex02.jpg" with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    j "What? You're almost there, aren't you?"
    j "Took you long enough!"
    j "You of course understand that you are not under any circumstances allowed to cum inside of m--"
    ">Jasmine get's interrupted by your heavy groan!"
    show image "00_personal/sex07.jpg" with flashbulb
    with hpunch
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    ">With another low growl you start unloading into Jasmine's pussy..."
    j "Aaahah!{image=textheart.png} You asshole! Stupid, filthy brute!{image=textheart.png}"
    j "It's so hot! I can't believe you were stupid enough to cum inside... ah...{image=textheart.png}"
    j "I would expect this from strangers - people hate me..."
    j "But what did I ever do to you?!"
    j "(It feels so good...{image=textheart.png}{image=textheart.png}{image=textheart.png})"
    show image "interface/blackfade.png" with Dissolve(1)
    ">Suddenly Jasmine shoves you away and pulls her pants up."
    ">You can see tears in her eyes..."
    j "You jerk! Dirty, son of a jackal! I hate you! *sob* I hate you!"
    j "You will pay for this! *sob* When I will marry Jafar you will lose your head! You can have my word on that!"
    ">Before you could react..."
    $ renpy.play('sounds/slap.mp3')
    with hpunch
    ">She slaps you on your face and storms out of the room..."
    $ renpy.play('sounds/door2.mp3')
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide image "00_personal/dance02.jpg" 
    pause 1
    hide image "04_pt/slavem/night2.jpg" 
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show sleeping with Dissolve(.3)
    "Jasmine goes to bed ...."
    jump jasdreams
        
label sexp4:
    j "Yes, [myname]. I was hoping you would ask this of me tonight..."
    hide screen jasmine_sprite_room
    with d3
    show image "interface/blackfade.png" with Dissolve(1)
    play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
    ">Obediently Jasmine turns around and pulls her pants down."
    ">After that she also pulls down her top to liberate her breasts."
    j "Master? Did you change your mind?"
    j "Please, don't reject me...."
    ">You pull down your own pants and grab the girl by her ass."
    ">You start to move your hips slowly...."
    j "ah...{image=textheart.png} Yes...{image=textheart.png}"
    show image "00_personal/sex04.jpg" with Dissolve(1)
    hide image "interface/blackfade.png" 
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    j "[myname]{image=textheart.png}... Thank you... Thank you for not neglecting me...{image=textheart.png}"
    ">Naturaly, as a part of her new lifestyle Jasmine was getting fucked a lot lately, by all sorts of people..."
    ">But you gladly notice that her pussy is as tight as ever..."
    j "Yes...{image=textheart.png} Thank you... Thank you... Thank you...{image=textheart.png}"
    ">She thanks you every time your cock re-enters her wet pussy."
    ">You feel your excitement rising and speed up the pace..."
    j "ah...{image=textheart.png} Yes...{image=textheart.png} Your cock is so big, it's gonna tear me apart!"
    menu:
        "\"Shut up and take it like a whore!\"":
            g3 "Shut up and take it like a whore, you slut!"
            j "Ah!{image=textheart.png} Yes!{image=textheart.png} Yes!{image=textheart.png} I'm a whore! Fuck me, [myname]! Fuck me, I beg you!{image=textheart.png} Rip me apart with your enormous cock!"
        "\"What are you? Tell me what you are!\"":
            g3 "What are you?"
            j "Ah...{image=textheart.png} W-what?"
            g3 "Tell me what are you, slut!"
            j "I'm a [jasname]! I'm a [jasname]! I'm your [jasname], [myname]!"
            g3 "Yes you are!"

        "\"Sing for me!\"":
            g3 "Sing for me!"
            j "Ah...{image=textheart.png} W-what?"
            g3 "I said, thing for me, whore!"
            j "Right now? B-but... ah...{image=textheart.png}"
            g3 "Sing I said, or I will stop fucking you!"
            ">You make a pause in your movements for a second..."
            j "Oh, no please, don't stop!"
            g3 "Sing for me, I said!"
            show image "00_personal/sex05.jpg" with flashbulb
            j "{image=note.png}Oh I come... f-from a land... from a faraway p-place...{image=note.png}"
            ">You resume your movements..."
            j "Ah, yes...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            j "{image=note.png}W-where the caravan camels roam...{image=note.png}"
            ">You squeeze her ass tighter and thrust harder..."
            ">As you keep fucking her jasmine keeps signing... Naturally sometimes her voice breaks into a moan..."
            ">But she is doing her best, you can see that..."
            ">As a reward and an acknowledgment of her hard work you start to fuck her even harder..."
            j "{image=note.png}A-arabian nights... ah...{image=textheart.png} Like Arabian da-a-ays... ah, yes, yes...{image=textheart.png}{image=note.png}"
            j "{image=note.png}More often than not.... Are hotter than hot... {image=textheart.png}ahh{image=textheart.png}...{image=note.png}"
            j "{image=note.png}In a lotta good wa-a-ays...{image=note.png} I think I'm about to cum, [myname]...."
            ">Actually you found her performance quite arousing so you are about to cum yourself..."
            ">Without saying a word you squeeze Jasmine's ass tightly and let out a groan..."
            j "Ah?!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            show image "00_personal/sex06.jpg" with flashbulb
            with hpunch
            j "Aaaa-aah!{image=textheart.png} Yee-e-ess!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            j "{image=note.png}Come... on down...{image=note.png} *sob*"
            j "{image=note.png}Stop on by... Hop a carpet and fly... ah,{image=textheart.png} your cum is filling me{image=textheart.png}...{image=note.png}"
            j "{image=note.png}To another Aa-arabian night.... I'm cumming...{image=note.png}"
            
            ">You keep shooting your cum deep inside her pussy until the last drop..."
            ">You can see that Jasmine is struggling to keep singing but her voice betrays her as multiple orgasms taking over her buddy..."
            ">Princess is trying to stay on her feet but as soon as you pull out of her she collapses on the ground..." 
            show image "interface/blackfade.png" with Dissolve(1)
            jump aftersong


    ">You keep pounding her from behind. Jasmine's ample breasts jump up a little with every thrust."
    ">You turn your attention to her butt... It's so round and... perfect... She truly is a princess...."
    $ renpy.play('sounds/slap.mp3')
    j "ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    ">You give her buttocks another loud slap."
    $ renpy.play('sounds/slap.mp3')
    show image "00_personal/sex05.jpg" with flashbulb
    j "Thank you, [myname]."
    ">You pick up the pace and feel that you are getting close..."
    j "Yes! Yes! Thank you! Thank you! I'm almost... almost...{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    ">Jasmine did't get a chance to finish her sentence: the strong wave of an orgasm consumes you abruptly and fully..." 
    show image "00_personal/sex06.jpg" with flashbulb
    with hpunch
    ">You let out a hoarse roar and start cumming uncontrollably right into her pussy..."
    j "ahh!{image=textheart.png} Yes!{image=textheart.png} I'm...{image=textheart.png} ah...{image=textheart.png} it's so hot...{image=textheart.png}"
    j "Your cum is filling me up..."
    j "{size=-3}It's...{/size}{w} {size=-7}i...{/size}{w} {size=-9}I'm cumming...{image=textheart.png}{image=textheart.png}{image=textheart.png}{/size}"
    ">You keep shooting your cum deep inside her pussy until the last drop..."
    ">You can see that Jasmine is struggling to stay on her feet, but her legs betray her because of multiple orgasms taking over her body..."
    show image "interface/blackfade.png" with Dissolve(1)
    ">Princess is trying to stay on her feet but as soon as you pull out of her she collapses on the ground with a thump..." 

    label aftersong:
    ">You look down on her... Jasmine is breathing lightly... Looks like she passed out..."
    ">She looks so peaceful..."
    ">You shake your dick a few times and couple of a leftover cum drops land on her face..."
    ">Jasmine really has grown as a sex-slave..."
    ">This is all thanks to your hard work of course..."
    label nopee:
    menu:
        "You decide what to do now..."

        "-Carry her to her bed-":
            ">You lift the princess up carefully and take her to her bed..."
            ">Slowly you put the girl down on a big cushion..."
            ">She is breathing calmly..."
            ">Her tits and her cum splattered butt are still in plain view..."
            ">You give her body one final admiring look and then cover her with a blanket..."
            $ renpy.play('sounds/door2.mp3')
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            hide image "00_personal/dance02.jpg" 
            pause 1
            hide image "04_pt/slavem/night2.jpg" 
            show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
            show sleeping with Dissolve(.3)
            ">Jasmine is sleeping ...."
            ">Jasmine is talking in her sleep..."
            j "[myname]... I love you..."
            j "*sob*..."
            show image "interface/blackfade.png" with Dissolve(.3)
            hide image "04_pt/slavem/night.jpg"
            hide image "04_pt/slavem/night2.jpg"
            hide sleeping
            pause 1
            jump dayone
        "-Just leave her-":
            ">You grab part of her long hair and wipe your dick clean with it..."
            ">No matter how you feel about her, you must stay professional..."
            ">You can't allow attachments... You must be mean to your slave-girl for both of your sakes..." 
            ">You turn around and leave the room..."
            $ renpy.play('sounds/door2.mp3')
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            hide image "00_personal/dance02.jpg" 
            pause 1
            hide image "04_pt/slavem/night2.jpg" 
            show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
            show sleeping with Dissolve(.3)
            ">Jasmine is sleeping ...."
            ">Jasmine is talking in her sleep..."
            j "Why....? Zzzzzz....."
            j "Why does everyone hate me....?"
            j "Zzzzz.... zzz...."
            j "Please love me...."
            j "Cold... It's so cold here..."
            j "*sob-sob*..... Zzzzz.........."
            show image "interface/blackfade.png" with Dissolve(.3)
            hide image "04_pt/slavem/night.jpg"
            hide image "04_pt/slavem/night2.jpg"
            hide sleeping
            pause 1
            jump dayone
        "-Pee on her...-":
            ">An odd idea crosses your mind..."
            ">You picture yourself peeing on Princess Jasmine for some reason..."
            a7 "I'm not drawing that..."
            jump nopee

            

    

   

    
        
        
        
    
    
    
    
    
    
    
    
    
    
   