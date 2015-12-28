####NIGHT WALK#######

##########################

    

##########################################
label nightwalk:
$ select = renpy.imagemap("04_pt/slavem/mainbg03.png", "04_pt/slavem/mainbg04.png", [
                                           (39, 325, 140, 412, "cheap"),
                                           (93, 446, 236, 552, "home"),
                                           (155, 368, 247, 444, "brothel"),
                                           (309, 371, 400, 512, "shop"),
                                           (407, 316, 519, 396, "market"),
                                           (531, 368, 621, 487, "tavern"),
                                           (693, 357, 774, 441, "school"),
                                           (532, 187, 594, 307, "jpalace"),
                                           ])
    
if select == "cheap":
        ">You have no business at the Cheapside."
        jump nightwalk
######HOME#####
if select == "home":
    menu:    
        "Do you want to call it a night?"
        "-Yes-":
            ">You return home and go to sleep."
            show image "interface/blackfade.png" with Dissolve(.3)
            pause 1
            jump dayone
        "-Not yet-":
            jump nightwalk
######BROTHEL#######
if select == "brothel":
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    label brothelnight:
        if quest4complete: 
            $ brothelnight = True
            $ renpy.play('sounds/door.mp3')
            jump brothelreopned
        else:
            jump quest4
            
if select == "shop":
        ">The shop is closed for the night."
        jump nightwalk
####MARKET#######
if select == "market":
    label nightmarket:
        show image "04_pt/slavem/bld.png" with Dissolve(.3)
    menu:
        "Market square is silent during the night. Once in a while a city guard passes by but other than that there is not a soul in sight."
        "-Test your strength-":
            menu:
                "-Pick up a big rock (easy)-":
                    ">You spot a big boulder near one of the empty fruit stands."
                    ">You grab the boulder with both of your hands and do your best to lift it off the ground..."
                    if strength >= 0 and strength < 2:
                        ">Unfortunately all you were able to do is shift it a little..."
                    elif strength == 2:
                        ">You were able to lift the boulder off the ground and hold it for a few moments before dropping it down."
                    elif strength == 3: 
                        ">You were able to lift the boulder off the ground and hold it in your arms for quite a while before carefully putting it back down."
                    elif strength >= 4:
                        ">You easily pick up the boulder and hold it over your head. Your body is bulging with strength."
                    jump nightmarket
                "-Arm wrestle a city guard (hard)-":
                    if strength >= 0 and strength < 6:
                        ">You wait for the city guard to show up."
                        sch12_2 "Is everything alright here?"
                        m "Everything is fine..."
                        m "Care to arm wrestle with me?"
                        sch12 "Sure. Anything to keep me awake..."
                        ">You try to beat the city guard at arm-wrestling..... \n {w}.............."
                        ">You lost."
                        sch12_2 "I'm sorry but I almost fell asleep during our \"match\"..."
                        sch12_2 "You need some exercise, buddy..."
                        sch12_2 "Alright, I better get back on my way now..."
                        jump nightmarket
                    elif strength >= 6 and strength < 9:
                        ">You wait for the city guard to show up."
                        sch12_2 "Is everything alright here?"
                        m "Everything is fine..."
                        m "Care to arm wrestle with me?"
                        sch12 "Sure. Anything to keep me awake..."
                        ">You try to beat the city guard at arm-wrestling..... \n {w}..............{w}..............{w}..............."
                        ">You lost."
                        sch12 "This was intense! I don't even feel sleepy anymore!"
                        sch12 "I'm a military man, they make us undergo all sorts of special training, so I'm pretty strong..."
                        sch12 "But you almost beat me this time! Good job!"
                        sch12 "Alright, I better get back on my way now..."
                        jump nightmarket
                    elif strength >= 9:
                        ">You wait for the city guard to show up."
                        sch12_2 "Is everything alright here?"
                        m ">Everything is fine..."
                        m ">Care to arm wrestle with me?"
                        sch12 "Sure. Anything to keep me awake..."
                        ">You try to beat the city guard at arm-wrestling..... \n {w}..............{w}..............{w}...............{w}..............."
                        ">You won!!!"
                        sch12 "I can't believe this!"
                        sch12 "Great job! Seems like all those exercises paid off for you!"
                        sch12 "Thank you for chasing my sleepiness away and for motivating me to exercise even harder from now on!"
                        sch12_2 "Oops, I better get back to my duties now."
                        jump nightmarket
                "-Cancel-":
                    jump nightmarket

        
        "-Do some exercises-":
            if strength >= 11:
                ">You are in the best shape of your life. You can take a break from exercises for a few days."
                jump nightmarket
            else:
                if strength >= 0 and strength < 3:
                    play music "music/tiger.mp3" fadein 1 fadeout 1 #WORKOUT
                    ">You hang your cloak on one of the nearby fruit stands..."
                    ">You run a few circles around the market square to warm up..." 
                    ">You quickly feel out of breath, but you keep pushing..." 
                    ">You feel tired, but it's a good sort of tiredness..."
                    play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1
                    ">You decide to call it a night."
                    $ strength +=1
                    $ dayswithoutexercise = 0
                    ">You return home and go to sleep."
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
                elif strength >= 3 and strength < 5:
                    play music "music/tiger.mp3" fadein 1 fadeout 1 #WORKOUT
                    ">You hang your cloak on one of the nearby fruit stands..."
                    ">You run a few circles around the market square to warm up..." 
                    ">You feel good..."
                    ">You decide to do some push-ups as well..."
                    ">You feel tired, but it's a good sort of tiredness..."
                    play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1
                    ">You decide to call it a night."
                    $ strength +=1
                    $ dayswithoutexercise = 0
                    ">You return home and go to sleep."
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
                elif strength >= 5 and strength < 7:
                    play music "music/tiger.mp3" fadein 1 fadeout 1 #WORKOUT
                    ">You hang your cloak on one of the nearby fruit stands..."
                    ">You run a few circles around the market square to warm up..." 
                    ">You feel great..."
                    ">You decide to do some push-ups as well..."
                    ">You feel that you can push yourself even farther today..."
                    ">You do some pull ups and then some push ups again..."
                    ">You feel exhausted but satisfied..."
                    ">Your body is stronger than it's been yesterday..."
                    play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1
                    ">You decide to call it a night."
                    $ strength +=1
                    $ dayswithoutexercise = 0
                    ">You return home and go to sleep."
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
                elif strength >= 7 and strength < 9:
                    play music "music/tiger.mp3" fadein 1 fadeout 1 #WORKOUT
                    ">You hang your cloak on one of the nearby fruit stands..."
                    ">You run a few circles around the market square to warm up..." 
                    ">You feel great..."
                    ">You decide to do some pull-ups, then some push-ups..."
                    ">You feel that you can push yourself even farther today..."
                    ">You pick up a big rock and do some squats..."
                    ">You do some pull ups and then some push ups again..."
                    ">You feel exhausted but satisfied..."
                    ">Your body is stronger than it's been yesterday..."
                    play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1
                    ">You decide to call it a night."
                    $ strength +=1
                    $ dayswithoutexercise = 0
                    ">You return home and go to sleep."
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
                elif strength >= 9:
                    play music "music/tiger.mp3" fadein 1 fadeout 1 #WORKOUT
                    ">You hang your cloak on one of the nearby fruit stands..."
                    ">You run quite a few circles around the market square to warm up..." 
                    ">You don't feel tired at all..."
                    ">You decide to do some pull-ups, then some push-ups..."
                    ">You feel that you can push yourself even farther today..."
                    ">You pick up a big rock and do some squats..."
                    ">You do some pull ups and then some push ups again..."
                    ">Then you do some more pull ups..."
                    ">You run around the square one more time to cool down..."
                    ">You feel exhausted but satisfied..."
                    ">Your body is stronger than it's been yesterday..."
                    ">You are in the best shape of your life! Maybe you should take a break and let your body recover."
                    play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1
                    ">You decide to call it a night."
                    $ strength +=1
                    $ dayswithoutexercise = 0
                    ">You return home and go to sleep."
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
        "-Leave-":
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            jump nightwalk
            
            

        
###TAVERN##########
if select == "tavern":
    label nightytavern:
    if maslabfriendship >= 3 and awmaslab00:
        $ awmaslab = True
        $ awmaslab00 = False
        jump meetmdaughter
    else:
        show image "04_pt/slavem/bld.png" with Dissolve(.3)
        menu:
            sch6_3 "Welcome to the \"The Blue Bull\"."
            "-Pick up the dish-" if quest7maslab3 and not quest7notcooking:
                jump thedishready2
            "-Pick up the dish-" if quest7start and quest7maslab2:
                jump thedishready
            "-Arm-wrestle with Maslab-" if awmaslab:
                if awmaslabcomplete:
                    jump wrestlemaslab2
                else:
                    jump wrestlemaslab
            "-Play dice with Maslab-" if quest2complete:
                if gold >= 60:
                    jump playmdice
                else:
                    sch6 "Doesn't look like you have enough gold to bet."
                    jump nightytavern
            "-Order some wine-" if quest3complete:
                jump datedaughter
            "-leave-":                   
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump nightwalk
if select == "jpalace":
    ">The palace gates are closed shut."
    jump nightwalk
if select == "school":
    ">The school is closed."
    jump nightwalk




#############################################################################
##############################################################################
##############################################################################
################LABELS########################################



####QUEST4#####################
                
###################################
###BROTHEL REOPENED#########
label brothelreopned:
    sch3 "Welcome to the \"Red Phoenix\" brothel, sweetheart ."
    label brothelmain:
    menu:                    
        sch3 "What can I do for you, love?"
        "-Give Lily the papers-" if quest12start3:
            jump quest12start3
        "-Make Jasmine work here as a whore-" if jidle and quest11complete and quest1200:
            jump fakewhorework
        
        "Quest: [quest8]." if quest8start00 and loladaytime:
                jump quest8start
        "-See lola (Night dates)-" if lolacomeatnight and brothelnight and gold >= 200:
                jump lolaoutnight
        "-Take lola out-" if quest7complete and loladaytime and loladates <= 3 and not lolacomeatnight:
            if quest7food and gold >= 100:
                if loladates == 3:
                    jump lolacomeatnight
                else:
                    jump lolaout
            else:
                sch3 "If you want to take my daughter out you will need two things..."
                sch3 "Enough money (more than 100 coins) and something delicious for me!"
                jump brothelmain
        "-Start the date with lily-" if brothelnight and quest7thing and quest7food:
            jump datewithlily
        "-Make Jasmine work here as a whore-" if jidle and quest12complete and not brothelnight:    
            ">Jasmine agrees to work in the \"Red Phoenix\" brothel as a whore..."
            show whore with Dissolve(.3)
            hide rest03
            $ jwhore = True
            $ jidle = False 
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)                        
            jump mainmenu  
        "-Ask for available whores-":
            menu:
                "You can choose any of the girls that are currently available. If you don't see the one you fancy, come back during the night time or tomorrow, she might become available."
                "-Talk to Lola-" if lolawaitsforroom and emptyroom and quest9complete:
                    jump lolawaitsforroom
                "Quest: \"Pleasing the mother\"." if loladaytime and quest7 == 1:
                    jump lolaquest
                "-Give the dress to Lola-" if quest8start3 and loladaytime:
                    jump quest8start3
                "-Dahlia-" if dahliaworks == 1:
                    jump dahliawhore
                "-Iris-" if daintavern == 3:
                    jump dawhore
                "-Jasmine-" if jwhore:
                    jump jasminewhore
                "-Lola-" if quest4complete and lolaworks == 2 and quest7 == 0:
                    jump lolawhore 
                "-Lola-" if quest8start4 and brothelnight:
                    jump quest8start4
                "-Both Dahlia and Iris-" if daintavern == 3 and dahliaworks == 1:
                    jump dahliaandda
                "-Both Jasmine and Iris-" if daintavern == 3 and jwhore:
                    jump jas_iris_sex
                "-Both Jasmine and Dahlia-" if dahliaworks == 1 and jwhore:
                    jump dah_jas_sex
                "-Jasmine, Dahlia and Iris all together-" if dahliaworks == 1 and jwhore and daintavern == 3:
                    jump foursome3
                "-Cancel-":
                    jump brothelmain
        "-Talk to lily-":
            sch3 "Welcome to the \"Red Phoenix\"."
            sch3 "one of the most popular brothels in Agarbah."
            sch3 "No matter how tired or distressed you are, you will be reborn from the ashes of your despair, when my girls are done with you."
            sch3 "And vice versa, every morning my girls are reborn anew from the ashes of humiliation and depravity they were the subject of the night before."
            jump brothelmain
        "-Leave-":
            $ renpy.play('sounds/door2.mp3')
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            if brothelnight:
                jump nightwalk
            else:            
                jump mainmenu
                


######TAVERN LABELS################
label thedishready2:
    sch6 "Your dish is ready. That will be 50 gold."
    menu:
        "You currently have [gold] gold. \nWould you like to pay for the dish 50 gold?"
        "\"Yes please.\"":
            if gold >= 50:
                sch6 "Here is your order. something delicious to go!"
                sch6 "Thank you for your purchase."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxdelicious.png" with moveinright
                ">You received something delicious."
                hide image "04_pt/slavem/boxdelicious.png" with Dissolve(.4)
                hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                $ gold -=50
                $ quest7food = True
                $ quest7notcooking = True
                jump nightytavern
            else:
                sch5 "Not enough gold? That's alright. Come back when you are ready. I'll put the dish aside for you."
                jump nightytavern
        "\"Changed my mind.\"":
            sch6 "Huh? Is it because of the smell? Your loss."
            jump nightytavern
label thedishready:
    sch6 "Yes, yes, your order is ready."
    sch6 "That will be 50 gold coins."
    menu:
        "You currently have [gold] gold. \nWould you like to pay 50 gold?"
        "\"Yes please\"":
            if gold >= 50: 
                $ gold -=50
                $ quest7maslab2 = False
                $ quest7food = True
                ">You paid Balsam 50 gold coins."
                sch6 "Here is your order. something delicious to go!"
                sch6 "Thank you for your purchase."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxdelicious.png" with moveinright
                ">You received something delicious."
                hide image "04_pt/slavem/boxdelicious.png" with Dissolve(.4)
                hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                jump nightytavern
            else:
                sch6 "Not enough gold? That's alright. Come back when you are ready. I'll put the dish aside for you."
                jump nightytavern
        "\"Nah... Changed my mind.\"":
            sch6 "Fine... I'll just take this one to the Fat Lily, she loves these..."
            jump nightytavern

    
label wrestlemaslab:
    sch6_3 "care to make it interesting?"
    menu:
        "You currently have [gold] gold. \nWould you like to bet 30 gold?"
        "-Yes please-":
            if gold >= 30: 
                if strength >= 0 and strength < 10:
                    sch6_3 "Great! Let's do it then!"
                    ">You try to beat maslab at arm-wrestling..... \n {w}..............{w}...............{w}..............."
                    ">You loose."
                    ">You lost your bet."
                    sch6_3 "Hey, don't beat yourself up, I'm stronger than I look."
                    sch6_3 "And I do look pretty strong! Ha-ha-ha!"
                    sch6_3 "Your gold please."
                    ">You give maslab 30 gold coins."
                    sch6_3 "Let me make it up to you."
                    sch6_3 "Tonight wine is on the house, how about that?!"
                    ">You spend rest of the night drinking wine in the tavern..."
                    $ gold -=30
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
                if strength >= 10:
                    "You try to beat maslab at arm-wrestling..... \n {w}..............{w}...............{w}..............."
                    "You won!"
                    sch62 "Argh! My arm!"
                    sch62 "You don't look like it, but your are freakishly strong, my friend!"
                    sch6_3 "Ha-ha-ha! It's been a while since I had a worthy opponent!"
                    sch6_3 "You won fair and square. Here is your gold."
                    m "Actually, I would rather have the brothel password..."
                    sch6_3 "Sure, if it means I will get to keep my money."
                    sch6_3 "The password is \"support akabur\", whatever the hell that means..."
                    sch6_3 "Oh, and don't let anyone know you got it from me, OK?"
                    sch6_3 "Some wine now? My treat."
                    sch6_3 "The girls are about to start dancing..."
                    sch6_4 "ah... Best part of my day..."
                    ">You drink wine and watch tavern wenches dance..."
                    ">You see one of them get's carried away and bares her tits..."
                    ">She immediately get's all the attention, so rest of the girls have a little choice but to follow her example..."
                    ">You look for Iris but don't see her anywhere..."
                    ">Finally you spot her standing in the corner, watching the girls and pouting..."
                    ">You are having a great time, but it's getting very late..."
                    ">You return home and go to sleep."
                    $ awmaslabcomplete = True
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
            else:
                "You don't have enough gold."
                jump nightytavern
        "-Maybe later-":
            sch6_3 "Come back when you're ready."
            jump nightytavern
label wrestlemaslab2: 
    sch6 "care to make it interesting?"
    if strength >= 10:
        sch6 "Nah... I kid. You look to strong to bet against! How about a frendly match?"
        "You try to beat maslab at arm-wrestling..... \n {w}..............{w}...............{w}..............."
        "You won!"
        sch6 "Ha-ha-ha. You won agagin! Are you trying to rub it in my face, you bastard!?"
        jump nightytavern
    if strength >= 0 and strength < 10:
        menu:
            "You currently have [gold] gold. \nWould you like to bet 30 gold?"
            "\"Yes please.\"":
                if gold >= 30: 
                    if strength >= 0 and strength < 7:
                        "You try to beat maslab at arm-wrestling..... \n {w}..............{w}...............{w}..............."
                        "You lose."
                        sch6_3"You got soft, my fried. You need some exersize!"
                        sch6_3 "Pay up!"
                        $ gold -=30
                        "You lost 30 gold."
                        jump nightytavern
                    else:
                        $ wrestling = renpy.random.randint(1, 2)    
                        if wrestling == 2:    
                            ">You try to beat maslab at arm-wrestling..... \n {w}..............{w}...............{w}..............."
                            ">You won!"
                            sch6 "Ha-ha-ha. You won agagin! Are you trying to rub it in my face, you bastard!?"
                            ">You recive 30 gold."
                            $ gold +=30
                            ">You spend rest of the night in the tavern..."
                            show image "interface/blackfade.png" with Dissolve(.3)
                            pause 1
                            jump dayone
                        elif wrestling == 1:
                            ">You try to beat maslab at arm-wrestling..... \n {w}..............{w}...............{w}..............."
                            ">You feel that someone is staring at you intently..."
                            ">You look up and see iris..."
                            ">She is not wearing her top!"
                            sch11_7 "....................."
                            ">You lost!"
                            sch6_3 "Hey, don't beat yourself up, there is no shame in loosing to me, I'm strong!"
                            $ gold -=30
                            ">You lost 30 gold."
                            jump nightytavern
                else:
                    "You don't have enough gold."
                    jump nightytavern
            "\"Maybe some other time.\"":
                sch6 "Come back when you are ready."
                jump nightytavern
        
label meetmdaughter:
        show image "04_pt/slavem/bld.png" with Dissolve(.3)
        $ renpy.play('sounds/door.mp3')
        sch62 "No, no, no, absolutely not!"
        sch3 "I don't see what the big deal is..."
        sch3 "As her father you must have the final say, of course..." 
        sch3 "But personally I think that she would be very popular..."
        sch6 ".........."
        sch6 "{size=-9}Very popular......{/size}"
        sch6 "{size=-7}Very popular......{/size}"
        sch6 "{size=-3}Very popular......{/size}"
        with hpunch
        sch62 "Very popular {size=+8}whore!?{/size}"
        sch62 "{size=+3}Get out of my establishment, you fat pig!{/size}"
        sch3 "How rude..."
        sch3 "Rude customers are not welcome in my brothel, you know..."
        sch6 "What? Wait, I didn't mean it..."
        sch3 "Bye now..."
        sch62 "Crap...."
        sch62 ".............."
        sch6_3 "Oh, it's you, my friend... Hi there..."
        sch62 "Can you believe that woman? She came to recruit my daughter for her brothel!" 
        sch11_4 "............................."
        sch62 "The audacity..."
        m "I thought the brothel was closed by the sultan's order?"
        sch6 "Not if you know the password."
        sch6 "Which, of course, I do."
        sch11_2 "..................."
        sch6_4 "Well, in any case... Welcome to my brothel... I mean my tavern!"
        sch62 "Crap..."
        jump nightytavern
######INTRO###########
label smintro:
show image "04_pt/slavem/mainbg00.jpg" with d5 
g4 "!!!!!!????"
m "Is this... Agrabah?"
jaf[1] "So, what do you think, old man? Will this work?"
with hpunch
g4 "Jafar?!!"
m "{size=-4}(That's Jafar! But...){/size}"
g4 "{size=-4}(H-how is this possible? And why is he dressed like the sultan?){/size}"
m "{size=-4}(Well of course....){/size}"
m "{size=-4}(Jafar has always been the sultan of Agrabah...){/size}"
m "{size=-4} (Right...?){/size}"
jaf[2] "What's the matter, old man, why are you so quiet  suddenly? Doubting your skills?"
m "{size=-4}(Seems like he doesn't know who I really am...){/size}"
m "{size=-4}(Good. Because... I am...........){/size}"
g4 "{size=-4} (My name is... it's... it starts with...){/size}"
m "{size=-4}(What's going on here? Something is not right!){/size}"
jaf[3] "Old man? I'm starting to lose my patience! Answer my question {size=+7}NOW!{/size}"
m "My apologies, your majesty."
menu:
    g4 "{size=-4}(Crap! What question? What is going on here?){/size}"
    "\"Sure. It will work.\"":
        m "Sure, I think it will work perfectly."
        jaf[1] "Ha-ha! I knew you would say that!"
    "\"Nah... It's not going to work.\"":
        m "Nah... That will never work."
        jaf[3] "What? But you said you can do it!"
        jaf[2] "Oh, I get it! That must be one of your jokes."
        jaf[3] "I am not amused, old man. You agreed to do the job."
    "\"Could you repeat the question?\"":
        m "Erm... Could you repeat the question please?"
        jaf[2] "What is it with you today, old man?"
        jaf[2] "You've always been my best man for training slaves."
        jaf[2] "So I am entrusting you with the most disobedient and yet most important one."
        jaf[2] "Princess Jasmine herself."
        jaf[2] "I want you to train her for me, so you can turn her into the perfect slave-girl and wife."
jaf[2] "Alright then, that house near the Cheapside is yours."
jaf[2] "And I'll also give you 20 gold coins."
$ renpy.play('sounds/win2.mp3')
$ gold +=20
">You received 20 gold coins."
menu:
    m "{size=-4}(That's not very much...){/size}"
    "\"That should suffice.\"":
        m "Yes... That should suffice."
        jaf[2] "Good."
    "\"I will need 30 gold coins.\"":
        m "Your majesty, I will need 30 gold coins, I'm afraid."
        jaf[2] "Fine... Here is another 10 coins."
        $ gold +=10
        $ renpy.play('sounds/win2.mp3')
        ">You received 10 gold coins."
    "\"I will need 100 gold coins.\"":
        m "Your majesty, I'm afraid, I will need 100 gold coins."
        jaf[3] "What? No, I told you that I don't want to pay for the wedding. The princess should work for it..."
jaf[2] "And here is the Princess herself, completely at your disposal."
show jas_f 7 at right with d3
j "Jafar..."
hide jas_f 7 at right with d3
show jas_f 8 at right with d3
j "You infidel dog! You will pay for this."
hide jas_f 8 at right with d3
show jas_f 7 at right with d3
jaf[4] "Yeah, yeah, spare me your empty threats, your highness."
jaf[3] "So, old man, do whatever you deem necessary, but whip this one into shape!"
jaf[3] "But keep the three conditions I want you to fullfil in mind:..."
jaf[4] "Number one: by the end of her training the Princess should be completely obedient to me."
hide jas_f 7 
show image "04_pt/jasmine/outfit/jas01.png" at right with Dissolve(.3)
j "That will never happen, you pig!"
hide image "04_pt/jasmine/outfit/jas01.png" with Dissolve(.3)
jaf[4] "*yawn* You bore me, princess."
jaf[2] "Number two: You should provide me with enough gold to pay for the wedding parade."
jaf[2] "And the last condition: the people of Agrabah should lose all of their affection towards their dear princess." 
jaf[2] "Use any trick you know, but make them turn on her."
jaf[2] "Make them hate and despise her even more than they hate and despise me."
show image "04_pt/jasmine/outfit/jas01.png" at right with Dissolve(.3)
j "Like that's even possible..."
jaf[4] "One more word from you, woman, and I will have you gagged..."
j "........."
hide image "04_pt/jasmine/outfit/jas01.png" with Dissolve(.3)
jaf[2] "Here is your money, here is your Princess and you know which house I was talking about."
jaf[4] "You can go now."
jaf[4] "Rasul, show them out."
sch4 "Yes, your majesty..."
show image "04_pt/jasmine/outfit/jas01.png" at right with Dissolve(.3)
j "{size=-4}(Rasul...){/size}"
hide image "04_pt/jasmine/outfit/jas01.png" with Dissolve(.3)
sch4 "{size=-4}(I'm sorry Princess...){/size}"
sch4 "Follow me please..."



show image "interface/blackfade.png" with Dissolve(.3)
pause 1
label starttutinfo:
    stop music fadeout 1
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1
    jump dayone
    
##################
##DREMAS########
####
label jasdreams:
    if courage >= 0 and courage < 4:
        $ whoring = renpy.random.randint(1, 15)
        if whoring == 1:
            ">Jasmine is talking in her Sleep..."
            j "Aladdin.....  Please save me..."
            j "zzzzzz......."
        elif whoring == 2:
            j "zzzzzz..........."
        elif whoring == 3:
            j "zzzzzz..........."
        elif whoring == 4: 
            j "zzzzzz..........."
        elif whoring == 5: 
            ">Jasmine is talking in her Sleep..."
            j "Father?......"
            j "No, no, Jafar, please...."
            j "zzzz......."
        elif whoring == 6: 
            ">Jasmine is talking in her Sleep..."
            j "Jafar, you will pay for this..."
            j "Zzzz....."
        elif whoring == 7: 
            ">Jasmine is talking in her Sleep..."
            j "Aka.... Aka...zzzzzz......\nSupport akabur..."
            j "Zzzz....."
        elif whoring == 8: 
            ">Jasmine is talking in her Sleep..."
            j "demons..... demons run....."
            j "demons run when a good man goes to war...."
            j "zzzzz......"
        elif whoring == 9: 
            ">Jasmine is talking in her Sleep..."
            j "No! I said no!..... How dare you?!...."
            j "zzzzz......"
        elif whoring == 10: 
            ">Jasmine is talking in her Sleep..."
            j "I am the princess of agrbah... I am... I..."
            j "Zzzzzz...."
        elif whoring == 11: 
            "Jasmine is talking in her Sleep..."
            j "Filthy commoners... You will pay... All of you..."
            j "Zzzzzz....."
        elif whoring == 12: 
            ">Jasmine is talking in her Sleep..."
            j "I will have you beheaded for this Jafar, I swear!"
            j "No... Don't touch me..."
            j "zzzzzz....."
        elif whoring == 13: 
            ">Jasmine is talking in her Sleep..."
            j "Who dares to enter my chambers?"
            j "Oh, it's you rasul... come on in... sweetie..."
            j "yes...."
            j "Zzzzz....."
        elif whoring == 14: 
            ">Jasmine is talking in her Sleep..."
            j "Aladdin.... my love... Forgive me...."
            j "Zzzzzz...."
        elif whoring == 15: 
            ">Jasmine is talking in her Sleep..."
            j "All of you will pay for this! All of you...."
            j "ZZZzzzz...."
        
    if courage >= 4 and courage < 7:
        $ whoring = renpy.random.randint(1, 12)
        if whoring == 1:
            ">Jasmine is talking in her Sleep..."
            j "I hate.... rose the teacher.... She is mean..."
            j "zzzzz....."
        elif whoring == 2:
            j "zzzzzz..........."
        elif whoring == 3:
            ">Jasmine is talking in her Sleep..."
            j "I'm a [jasname]... a [jasname]..."
            j "Zzzzz......"
        elif whoring == 4: 
            j "zzzzzz..........."
        elif whoring == 5: 
            ">Jasmine is talking in her sleep..."
            j "Father?......"
            j "No, no, Jafar, please...."
            j "zzzzz......"
        elif whoring == 6: 
            ">Jasmine is talking in her Sleep..."
            j "Maybe I....\n...should be more obedient...?"
            j "zzzzzz......"
        elif whoring == 7: 
            ">Jasmine is talking in her Sleep..."
            j "zzzzzz..........."
            j "No... no... I don't want to do that..."
            j "ah... yes, I understand, I will try, teacher..."
            j "zzzz......."
        elif whoring == 8: 
            ">Jasmine is talking in her Sleep..."
            j "No, please keep it a secret..."
            j "No one should know that I work here..."
            j "What?....  Alright, you can touch them..."
            j "Ah....{image=textheart.png}"
            j "zzzzzzzz......"
        elif whoring == 9: 
            ">Jasmine is talking in her Sleep..."
            j "Of course I'm not..."
            j "I just look like her..."
            j "My name is...em... er... Jasper..."
            j "zzzzz......."
        elif whoring == 10: 
            ">Jasmine is talking in her Sleep..."
            j "... i...  ..i need to expose my tits now...."
            j "But everyone is watching... This is so embarrassing..."
            j "zzzzz......"
        elif whoring == 11: 
            ">Jasmine is talking in her Sleep..."
            j "...I know... I am trying..."
            j "no, please... oh, alright..."
            j "zzzzzz......"
        elif whoring == 12: 
            j "zzzz......"
            
    if courage >= 7 and courage < 11:
        $ whoring = renpy.random.randint(1, 12)
        if whoring == 1:
            ">Jasmine is talking in her Sleep..."
            j "Yes, yes, I love it..."
            j "Do it faster now..."
            j "ah... yes,  yes... I am a [jasname]."
            j "zzzz...."
        elif whoring == 2:
            ">Jasmine is talking in her Sleep..."
            j "yes, [myname], as you wish...."
            j "Yes, please fuck me tonight.... fuck your [jasname]."
            j "Ah.... yes..."
            j "ZZZzzz...."
        elif whoring == 3:
            j "zzzzzz..........."
        elif whoring == 4: 
            j "zzzzzz..........."
        elif whoring == 5: 
            ">Jasmine is talking in her Sleep..."
            j "I don't care, I just want to suck it..."
            j "Put it in my mouth now.... *drool*"
            j "zzzzzzzz......"
        elif whoring == 6: 
            ">Jasmine is talking in her Sleep..."
            j "Yes, I love dancing for you, you filthy peasants!"
            j "I think I..... zzzzz.... \nwill show you my tits today..."
            j "Yes...zzzzz..... \n....look at me..."
            j "zzzz......"
        elif whoring == 7: 
            ">Jasmine is talking in her Sleep..."
            j "no, I am not princess jasmine.... zzzzz....."
            j "Yes, I am princess jasmine...\nkeep your voice down would you?"
            j "Come here I will let you touch my tits..."
            j "What? zzz..zzzz"
            j "Oh, alright, take it out..."
            j "Slurp, slurp, zzzzz....."
            j "Zzzzz....."
        elif whoring == 8: 
            ">Jasmine is talking in her Sleep..."
            j "I love my teacher Rose... zzzz.....\nShe is so smart...."
            j "zzzzzz....."
        elif whoring == 9: 
            ">Jasmine is talking in her Sleep..."
            j "What...? With all of you at once?...."
            j "Well, alright, but you will.... have to pay more...."
            j "I am a [jasname]."
            j "Zzzz....."
        elif whoring == 10: 
            ">Jasmine is talking in her Sleep..."
            j "No, I want all of you to cum in my mouth..."
            j "I want to be a true [jasname]."
            j "ZZzz...zz..."
            j "Gulp... Gulp...."
        elif whoring == 11: 
            j "zzzzzz..........."
        elif whoring == 12: 
            j "zzzzzz..........."


    if courage == 3:
        if not watched_dream_01:
            jump dream_01
        else:
            pass
            
    if courage == 5:
        if not watched_dream_02:
            jump dream_02
        else:
            pass
            
    if courage == 9:
        if not watched_dream_03:
            jump dream_03
        else:
            pass

    show image "interface/blackfade.png" with Dissolve(.3)
    hide image "04_pt/slavem/night.jpg"
    hide image "04_pt/slavem/night2.jpg"
    hide sleeping
    pause 1
    jump dayone
########QUEST9#########
label quest8start6:
    sch7 "You want to remodel your house? Of course! I know a guy."
    menu:
        sch7 "Are you interested?"
        "\"I am.\"":
            if onquest:
                ">You need to finish your current quest first, before you can take a new one."
                jump cheapside
            else:
                sch7 "Give me a few days and I will provide you with more detailed info."
                $ quest900 = False
                $ quest9start = True
                $ onquest = True
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                show image "04_pt/slavem/qstart.png" with Dissolve(.3)
                show image "04_pt/slavem/onaquest.png" with Dissolve(.3)
                show con1 at right
                show ctc7 at right
                pause 
                hide con1
                hide ctc7
                hide image "04_pt/slavem/qstart.png" with Dissolve(.3)
                show image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump cheapside
        "\"Maybe later.\"":
            sch7 "I'm not going anywhere, so take your time."
            jump cheapside
################################################
label quest9start:
    sch7 "Yes, yes, I talked to the guy."
    sch7 "He said master will have to pay upfront 400 gold coins. I mean 500 gold coins. But that's not all..."
    sch7 "He will also require written permission from the owner of the house..."
    $ quest9start = False
    $ quest9start2 = True
    jump cheapside
#######################
label quest9start2:
    play music "music/JafarsHour.mp3" fadein 1 fadeout 1
    sch4 "I see... Follow me please..."
    sch4 "Your majesty... Please, forgive my intrusion, but there is someone here to see you..."
    jaf[2] "Huh? Oh, it's you, old man..."            
    jaf[2] "What? What is it? Make it quick, I'm busy."
    jaf[2] "What? You want to remodel the house?"
    jaf[2] "What for?"
    jaf[2] "Fine, I will prepare the papers. Come back in two days."
    jaf[4] "Now leave. I am a busy man."
    sch4 "I will take you to the exit. Follow me..."  
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    $ quest9start2 = False
    $ quest9start3 = True
    jump mainmenu
####################
label quest9start3:
    play music "music/JafarsHour.mp3" fadein 1 fadeout 1
    sch4 "Yes, I have your papers here."
    sch4 "That will be 100 gold coins."
    menu:                            
        "You currently have [gold] gold. \nWould you like to pay 100 gold for the papers?"
        "-Pay 100 gold coins-":
            if gold >= 100:
                $ gold -=100
                sch4 "Here are your papers."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxdance.png" with moveinright
                ">You received the house remodeling permit."
                $ quest9start3 = False
                $ quest9start4 = True
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
    



###############################################
label quest9start4:
    sch7 "The permit? Good. Crocus will pass it on to his guy."
    sch7 "Now the payment..."
    menu:                            
        "You currently have [gold] gold. \nWould you like to give 500 gold to Crocus?"
        "\"Yes\"":
            if gold >= 500:
                $ gold -=500
                sch7 "I will make sure he gets the money."
                ">You hand over 500 gold coins to the beggar."
                $ quest9start4 = False
                $ quest9complete = True
                hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
                $ onquest = False
                $ renpy.play('sounds/win2.mp3')                        
                show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
                show con1 at right
                show ctc7 at right
                pause
                hide con1
                hide ctc7
                ">Your house been remodeled. (Yes, {size=+5}that{/size} quick!)"
                ">Now you have one extra room to house one more resident appart form Jasmine and yourself."
                hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                ">It's getting late. You decide to head home."
                jump dayends 
            else:
                ">You don't have enough gold."
                jump cheapside
        "\"Not right now.\"":
            jump cheapside
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#################
label quest9complete:
    $ renpy.play('sounds/door.mp3')
    hide blkfade
    show blkfade with d5
    show image "04_pt/slavem/bld.png" behind blkfade
    pause.5
    hide blkfade with d5
    ">This room is currently unoccupied."
    show blkfade with d5
    hide image "04_pt/slavem/bld.png" behind blkfade
    $ renpy.play('sounds/door2.mp3')
    pause.5
    hide blkfade with d5
    jump dayended
    
    
    