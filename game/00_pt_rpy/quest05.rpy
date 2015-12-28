label datedaughter:
        if gold >= 50:
            if daintavern == 1 or daintavern == 3:
                menu:
                    "You currently have [gold] gold. \nWould you like to spend the rest of the night in the tavern?"
                    "\"Yes.\"":
                        show image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
                        $ drinkingvine = renpy.random.randint(1, 10)    
                        if drinkingvine == 1: 
                            with fade
                            play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
                            ">One of the serving wenches brings you your wine."
                            ">Following everybody's example you reach out and grab her butt while she is pouring you your wine."
                            ">The girl gives you a timid smile and moves on to the next patron."
                        elif drinkingvine == 2:
                            play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
                            ">One of the serving wenches brings you your wine."
                            ">A few moments later she brings you another bottle. Unlike the one you ordered this bottle looks very expensive."
                            menu:
                                "You did not order this one..."
                                "-Tell the girl that you didn't order it-":
                                    ">You ask the girl where the wine came from."
                                    ">She smiles and points into the farthest corner of the tavern."
                                    ">You see a hooded figure sitting behind a table."
                                    a1 "Thank you for your support, my friend. The wine is on me."
                                    ">Somehow the stranger looks familiar to you, and yet you have no idea who he is."
                                    ">You thank him with a nod and open the bottle."
                                    ">The wine he sent is unbelievably delicious."
                                    ">Later you try to look for the stranger but he is nowhere to be found..."
                                    ">You can't get rid of the feeling that you are supposed to know who the stranger is... Why can't you remember?"
                                "-Count your blessing and enjoy the wine-":
                                    ">You open the bottle..."
                                    ">You guess was correct. The wine tastes a million times better than anything else served in \"the bull\" ever."
                                    ">You sip the delicious beverage slowly, savoring the taste..."
                        elif drinkingvine == 3:
                            with fade
                            play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
                            ">One of the serving wenches brings you your wine."
                            ">You enjoy the drink..."
                            ">You enjoy the drink right up until some local thug starts insulting you, looking for a fight."
                            if strength >= 0 and strength < 5:
                                "The guy looks scary, and you are not in a very good shape, so you decide to avoid the confrontation by offering to buy him a drink."
                            elif strength >= 5 and strength < 8:
                                ">The guy looks scary, but you decide to take your chances."
                                ">You reply with a bunch of insults yourself and get into a fight with him."
                                ">You emerge victorious although your nose is bleeding heavily." 
                                ">One of the serving wenches seem to be feeling very sympathetic towards you."
                                ">She tends to your wound and then gives you kiss on a cheek."
                            elif strength >= 8:
                                ">The guy looks scary, but you decide to take your chances."
                                ">You reply with a bunch of insults yourself and get into a fight with him."
                                ">Your opponent is bigger then you, but you are in a much better shape."
                                ">You practically mop the floor with the poor bastard."
                                ">Every single girl in the building cheers approvingly."
                                ">Maslab is looking at the broken table and a few dismantled chairs... The innkeeper is not pleased."
                        elif drinkingvine == 4:
                            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
                            ">One of the serving wenches brings you your wine."
                            ">You spend some time at the tavern..."
                        elif drinkingvine == 5:
                            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
                            ">You are slowly sipping your wine, patiently waiting for the \"Magical Time\"..."
                            ">After a while the bard finally starts to  play..."
                            ">As usual every woman at the building drops everything she was doing and mounts  nearest table."
                            ">You see that one or two of the girls treat the tradition as a chore, but most of them seem to be having a great time."
                        elif drinkingvine == 6:
                            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
                            ">One of the serving wenches brings you your wine."
                            ">Following everybody's example you reach out and grab her butt while she is pouring you your wine."
                            ">The girl gives you a timid smile and offers you to touch her tits for 1 gold coin."
                            menu:
                                "-Pay the girl-":
                                    if gold >= 1: 
                                        $ gold -=1
                                        play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
                                        ">You give the girl one gold coin."
                                        ">She pretends to keep pouring the wine while you play with her tits through the fabric of her dress..."
                                        ">The girl gives you an embarrassed look and makes you another offer..."
                                        ">She says that for 5 gold coins you can take her tits out."
                                        ">Or for 10 gold she could prepare a \"Royal Goblet\" for you."
                                        label thegoblet:
                                        menu:
                                            "-Play with her tits (5 gold)-":
                                                if gold >= 5: 
                                                    $ gold -=5
                                                    ">You pay the girl 5 gold coins."
                                                    ">She continues to pretend that she is pouring you your wine while you take her tits out of her dress one after another."
                                                    ">The girl keeps glancing towards Maslab nervously while you are admiring her shapely tits hanging out of her dress."
                                                    ">You notice that the girl is starting to pant lightly..."
                                                    ">She looks at you with and says that for another 10 gold coins she will touch your cock under the table."
                                                    ">And for 15 she will let you finger her. Or you can pay her 30 gold coins and she will dive under the table and put your cock in her mouth."
                                                    menu:
                                                        "The girl is panting heavily listing the services she is willing to provide..."
                                                        "\"Touch my cock.\" (10 gold)":
                                                            if gold >= 10: 
                                                                $ gold -=10
                                                                ">You pay her another 10 coins..."
                                                                ">The girl takes out a piece of cloth with her right hand and pretends to wipe the table."
                                                                ">Meanwhile she skillfully slides her left hand into your pants and grabs your dick with her slender fingers."
                                                                ">The girl keeps looking in Maslab's direction while making equally awkward motions with both of her hands..."
                                                                ">It goes on for a while before the inn keeper starts to pay close attention to your activity."
                                                                "The Waitress" "Oh, crap, sorry, I gotta go!"
                                                                ">The girl quickly releases your cock, turns around and starts chatting with another patron."  
                                                                ">You did enjoy the service she provided, but it wasn't nearly enough... You wonder if you should pay a visit to a whore in the near future..."
                                                            else: 
                                                                ">You reach for your purse, but realize that you don't have enough money... This is embarrassing..." 
                                                        "\"Let me finger you.\" (15 gold)":
                                                            if gold >= 15: 
                                                                $ gold -=15
                                                                ">You pay the girl 15 gold coins."
                                                                ">She takes out a piece of cloth, bends over a bit more and pretends to wipe the table..."
                                                                ">You slide your hand under her skirt and start to massage her already wet slit."
                                                                ">The girl is blushing furiously but keeps wiping the table over and over again..."
                                                                ">You stick two fingers in her pussy. The girl produces a muffled moan."
                                                                ">You start working your hand... The girl is panting heavily. She is staring at one spot and keeps wiping the table over and over and over..."
                                                                ">You wonder if other customers are starting to take notice of your activity..."
                                                                if strength >= 0 and strength < 5:
                                                                    ">You also wonder if you will be able to make the girl cum, but your arm is already tired... If only you had more strength..."
                                                                    ">You pull your fingers out of her... They are really wet..."
                                                                    ">The girl doesn't say anything. She just runs off and disappears behind the kitchen door."
                                                                    ">She forgot her wiping cloth and her tray..."
                                                                elif strength >= 5 and strength < 9:
                                                                    ">You also wonder if you will be able to make the girl cum by only your fingers..."
                                                                    ">You keep on fingering her furiously and can feel her drenching wet pussy trying to grab your fingers tighter..."
                                                                    ">The girl doesn't even bother with pretending to wipe your table anymore... She is just panting heavily and blushing..."
                                                                    ">You think she might be getting close, but your arm is too tired of those repetitive motions..."
                                                                    ">If you only had more strength..."
                                                                    ">You pull your fingers out of her... They are all wet..."
                                                                    ">The girl doesn't say anything. She just runs off and disappears behind the kitchen door."
                                                                    ">She forgot her wiping cloth and her tray..."
                                                                elif strength >= 10:
                                                                    ">You also wonder if you will be able to make the girl cum using only your fingers..."
                                                                    ">You keep on fingering her furiously and can feel her drenching wet pussy trying to grab your fingers..."
                                                                    ">The girl doesn't even bother with pretending to wipe your table anymore... She is just panting heavily and blushing furiously..."
                                                                    ">You think she might be getting close, and double the pace."
                                                                    ">You have enough strength in your arm to keep assaulting her pussy for as long as it takes..."
                                                                    ">The girl starts to move her hips a little and moans softly."
                                                                    ">You realize that nearby patrons are starting to notice your activity..."
                                                                    ">Finally Maslab takes notice of the event. You see him walking towards your table."
                                                                    ">You keep doing what you're doing, so when Maslab finally reaches your table the girl is starting to cum."
                                                                    ">You keep on working with your fingers under her dress..."
                                                                    ">When the inn keeper then asks her what she thinks she is doing, the only thing she can barely mouth out is..."
                                                                    "\"I'm cumming!\"."
                                                                    ">The patrons who are close enough to hear that are starting to laugh..."
                                                                    ">You pull your fingers out of her... They are all wet..."
                                                                    ">The girl doesn't say anything and just runs off stumbling and disappears behind the kitchen door."
                                                                    ">Maslab gives you a disapproving look."
                                                                    ">The rest of the inn, including most of the waitresses are starting to laugh as well."
                                                            else: 
                                                                ">You reach for your purse, but realize that you don't have enough money... This is embarrassing..." 
                                                        "\"Put my cock in your mouth.\" (30 gold)":
                                                            if gold >= 30: 
                                                                $ gold -=30
                                                                ">You pay the girl 30 gold coins..."
                                                                ">She takes a one last glance in the inn keeper's directions and then crawls under the table."
                                                                ">You can feel her taking your dick out with her fingers and then putting it in her little mouth..."
                                                                ">Her technique is a bit sloppy, but you can't blame her. The girl is obviously in a hurry and under all sorts of pressure..."
                                                                ">You slowly sip your wine while the young waitress is sliding her wet mouth up and down your cock."
                                                                ">Suddenly to your own surprise you feel that you are about to cum..."
                                                                ">You grab your table by the edges and do you best to keep a straight face while you shoot one load after another into the girl's throat..."
                                                                ">She emerges from under the table... You can see a few drops of cum on her hair and her chest."
                                                                ">But for the most part no one would dare to assume that your cock was balls-deep in her pretty little mouth just a second ago."
                                                                ">She doesn't say anything, just glances in Maslab's detection then gives you a timid smile and leaves..."
                                                            else: 
                                                                ">You reach for your purse, but realize that you don't have enough money... This is embarrassing..." 
                                                        "-Refuse her offer-":
                                                            ">You refuse the girl's offer. She laughs nervously and says that that was a joke."
                                                            ">She moves on to the next patron."
                                                else: 
                                                    ">You reach for your purse, but realize that you don't have enough money... This is embarrassing..." 
                                            "-Order the \"Royal Goblet\" (10 gold)-":
                                                if gold >= 10: 
                                                    $ gold -=10
                                                    ">You give the girl 10 gold coins."
                                                    ">She glances at Maslab... The inn keeper seems to be busy with something else..."
                                                    ">The girl takes one of her tits out of her dress... You can clearly see her red and erect nipple..."
                                                    ">She picks up your pint and clumsily dips her tit into your wine a few times. After that she quickly covers up again."
                                                    "\"Enjoy your drink, sir.\" - She is blushing furiously."
                                                    ">You take a few sips from the \"Royal Goblet\". Strangely enough you note that the wine doesn't taste nearly as bad as it did a moment ago..."
                                                    ">The girl glances at Maslab again. The inn keeper looks right at her and doesn't seem to be pleased. The girl quickly moves on to the next patron."
                                                    ">You enjoy the rest of the evening, while taking small sips from your \"Royal Goblet\"."
                                            "-Ask her what a \"Royal Goblet\" is-":
                                                ">The girl gives you a bewildered look... She seems to be surprised that you don't know what the \"Royal Goblet\" is."
                                                ">She explains that it's when the waitress takes one of her tits out and dips it into the patron's drink."
                                                jump thegoblet
                                            "-Refuse her offer-":
                                                ">You refuse the girl's offer. She laughs nervously and says that it was a joke."
                                                ">She moves on to the next patron."

                                        
                                    else: 
                                        ">You reach for your purse, but realize that you don't have enough money... This is embarrassing..." 
                                "-Refuse-":
                                    ">You refuse the girl's offer. She laughs nervously and says that it was a joke."
                                    ">She moves on to the next patron."
                        elif drinkingvine == 7:  
                            play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
                            ">One of the serving wenches brings you your wine."
                            ">It seems that Maslab is holding one of his underground dice games tonight as well..."
                            ">You watch a bunch of people arguing a particularly lucky roll of one of the players..."
                            ">A violent fight erupts."
                            ">You slowly enjoy the beverage watching a bunch of grown men beating the crap out of each other ..."
                        elif drinkingvine == 8:
                            play music "music/dice_game.MP3" fadein 1 fadeout 1
                            ">Maslab pours you a big pint of cheap wine..."
                            ">You chat with him for a while..."
                            ">You and Maslab passionately discuss things that don't matter much."
                            ">You are having a great time..."
                            ">Overall it was quiet and uneventful evening..."
                        elif drinkingvine == 9:
                            ">One of the serving wenches brings you your wine."
                            ">You slap her on her behind and she slaps your face in return."
                            ">A few nearby patrons are starting to laugh..."
                            ">You drink your wine as if nothing happened..."
                        elif drinkingvine == 10:
                            ">One of the serving wenches brings you your @vi..#ne.   .\n,."
                            show image "04_pt/slavem/bug.png"
                            "You ,3 try tona and... \n\nam ,,no"
                            stop music 
                            "ypos:34 x:445 show at right image"
                            "if mdaughterfriendship == 0: ypos:34 x:445 show at right image \">One of the serving wenches brings you your"
                            "2woujj2-21,3:3 xpos: 35" "show image \"04_pt/slavem/maslab01.png\" at right with Dissolve(.3) ;"
                            "hide blkfade with Dissolve(.5)" "show con1 at right show ctc7 at right"
                            with hpunch
                            a7 "{size=+5}Oh my god!!! You broke my fucking game!!!!{/size}"
                            hide image "04_pt/slavem/bug.png" with Dissolve(.5)
                            a2 "He-he-he... Gotcha!"
                        $ vine = renpy.random.randint(20, 35)
                        $ gold = gold - vine
                        ">Maslab's daughter is nowhere to be seen. Doesn't look like she is working today."
                        hide image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
                        ">You spent [vine] gold coins on wine tonight."
                        ">You decide to call it a night and leave the tavern."
                        ">You return home and go to sleep."
                        show image "interface/blackfade.png" with Dissolve(.3)
                        pause 1
                        jump dayone
                    "\"Maybe some other time.\"":
                        jump nightytavern
            if daintavern == 2:
                menu:
                    "You currently have [gold] gold. \nWould you like to spend the rest of the night in the tavern?"
                    "\"Yes.\"":
                        if mdaughterfriendship == 0:
                            jump mddate1
                        elif mdaughterfriendship == 1:
                            jump mddate2
                        elif mdaughterfriendship == 2:
                            jump mddate3
                        elif mdaughterfriendship == 3:
                            jump mddate4
                        elif mdaughterfriendship == 4:
                            jump mddate5
                        elif mdaughterfriendship == 5:
                            jump mddate6
                        elif mdaughterfriendship == 6:
                            jump mddate7
                        elif mdaughterfriendship == 7:
                            jump mddate8
                    "\"Maybe next time.\"":
                        jump nightytavern
        else: 
            "You don't have enough gold."
            jump nightytavern
##################DATES WITH MASLAB'S DAUGHTER############## 
label mddate1:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld2.png" behind blkfade
    show image "04_pt/iris/q5/iris01.png" at center behind blkfade
    pause.3
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Here is your wine..."
    show image "04_pt/iris/q5/iris02.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris01.png"
    sch1100 "Oh, it's you! Hi there."
    menu:
        "\"You look different...\"":
            hide image "04_pt/iris/q5/iris02.png" with Dissolve(.3)
            show image "04_pt/iris/q5/iris03.png" at center with Dissolve(.3)
            sch1100 "Yeah... I had a big fight with my father yesterday..."
            sch1100 "I hate that stupid veil thing he always forces me to wear!"
            sch1100 "I'm not some rich girl, you know. I can show my face to everyone if I want to."
            hide image "04_pt/iris/q5/iris03.png"  
        "\"Hello, Iris.\"":
            hide image "04_pt/iris/q5/iris02.png" with Dissolve(.3)
            show image "04_pt/iris/q5/iris04.png" at center with Dissolve(.3)
            sch1100 "What? You didn't notice?"
            sch1100 "I'm not wearing my veil today."
            hide image "04_pt/iris/q5/iris04.png" with Dissolve(.3)
            ">Iris is pouting a little..."
        "\"No veil today?\"":
            hide image "04_pt/iris/q5/iris02.png" with Dissolve(.3)
            show image "04_pt/iris/q5/iris05.png" at center with Dissolve(.3)
            sch1100 "Yeah... I took that silly thing off."
            show image "04_pt/iris/q5/iris06.png" at center with Dissolve(.2)
            hide image "04_pt/iris/q5/iris05.png" 
            sch1100 "My father was against it of course but I don't care."
            hide image "04_pt/iris/q5/iris06.png"
    show image im.Flip ("04_pt/iris/q5/iris07.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "Listen, about your slave-girl..."
    menu:
        sch1100 "Her real name is not Jasper, is it?"
        "\"Why do you think so?\"":
            show image im.Flip ("04_pt/iris/q5/iris08.png", horizontal=True) at center with Dissolve(.2)
            hide image im.Flip ("04_pt/iris/q5/iris07.png", horizontal=True)
            sch1100 "Well, for starters, that's a very silly name for a girl."
            sch1100 "And I can see that she hates to be called \"Jasper\"."
            hide image im.Flip ("04_pt/iris/q5/iris08.png", horizontal=True) at center with Dissolve(.2)
        "\"No, it's Jasmine.\"":
            show image im.Flip ("04_pt/iris/q5/iris08.png", horizontal=True) at center with Dissolve(.2)
            hide image im.Flip ("04_pt/iris/q5/iris07.png", horizontal=True)
            sch1100 "Jasmine, huh?"
            sch1100 "Yeah, it befits her..."
            show image im.Flip ("04_pt/iris/q5/iris09.png", horizontal=True) at center with Dissolve(.2)
            hide image im.Flip ("04_pt/iris/q5/iris08.png", horizontal=True)
            sch1100 "Jasmine.... Hm...."
            hide image im.Flip ("04_pt/iris/q5/iris09.png", horizontal=True) at center with Dissolve(.2)
        "\"It is. Her name is Jasper.\"":
            show image im.Flip ("04_pt/iris/q5/iris10.png", horizontal=True) at center with Dissolve(.2)
            hide image im.Flip ("04_pt/iris/q5/iris07.png", horizontal=True)
            sch1100 "I'm not stupid... I know it's not true..."
            show image im.Flip ("04_pt/iris/q5/iris09.png", horizontal=True) at center with Dissolve(.2)
            hide image im.Flip ("04_pt/iris/q5/iris10.png", horizontal=True)
            sch1100 "But whatever, if you don't want to tell me it's fine..."
            hide image im.Flip ("04_pt/iris/q5/iris09.png", horizontal=True) at center with Dissolve(.2)
    show image "04_pt/iris/q5/iris02.png" at right with Dissolve(.3)
    sch1100 "Oh, wait, let me pour you some more wine."
    hide image "04_pt/iris/q5/iris02.png" at right with Dissolve(.3)
    ">Iris pours more wine into your pint."
    show image "04_pt/iris/q5/iris11.png" at right with Dissolve(.3)
    hide image "04_pt/iris/q5/iris02.png" 
    sch1100 "Huh?"
    show image "04_pt/iris/q5/iris01.png" at right with Dissolve(.3)
    hide image "04_pt/iris/q5/iris11.png" 
    sch1100 "......?"
    menu:
        "\"What's the matter, Iris?\"":
            hide image "04_pt/iris/q5/iris01.png" with Dissolve(.3)
            show image "04_pt/iris/q5/iris09.png" at center with Dissolve(.3)
            sch1100 "Well, it's just..."
            show image "04_pt/iris/q5/iris12.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris09.png" with Dissolve(.3)
            sch1100 "......."
            show image "04_pt/iris/q5/iris06.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris12.png" with Dissolve(.3)
            sch1100 "Why didn't you touch my butt?"
            hide image "04_pt/iris/q5/iris06.png" at center with Dissolve(.3)
        "(Tip her 1 gold coin.)":
            hide image "04_pt/iris/q5/iris01.png" with Dissolve(.3)
            show image "04_pt/iris/q5/iris10.png" at center with Dissolve(.3)
            sch1100 "What is this? I didn't ask for your gold!"
            show image "04_pt/iris/q5/iris06.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris10.png" with Dissolve(.3)
            sch1100 "I'm just wondering why you didn't touch my butt when I was pouring you your wine?"
            hide image "04_pt/iris/q5/iris06.png" at center with Dissolve(.3)
        "\".................\"":
            hide image "04_pt/iris/q5/iris01.png" with Dissolve(.3)
            show image "04_pt/iris/q5/iris06.png" at center with Dissolve(.3)
            sch1100 "Tsk... Don't you wanna touch my butt?"
            hide image "04_pt/iris/q5/iris06.png" at center with Dissolve(.3)
    show image "04_pt/iris/q5/iris04.png" at center with Dissolve(.3)
    sch1100 "Is it because of my scar?"
    sch1100 "It is, isn't it?"
    show image "04_pt/iris/q5/iris06.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris04.png" 
    sch1100 "I knew it... Men don't find me attractive at all..."
    menu:
        "\"You are my friend's daughter!\"":
            sch1100 "So what?"
            show image "04_pt/iris/q5/iris10.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris06.png" 
            sch1100 "Are you afraid of my father?"
            hide image "04_pt/iris/q5/iris10.png" with Dissolve(.3)
        "\"Is Maslab OK with this?\"":
            show image "04_pt/iris/q5/iris05.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris06.png" 
            sch1100 "Teh-he-he... Father doesn't have to know... It will be our little secret."
            show image "04_pt/iris/q5/iris09.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris05.png" 
            sch1100 "My father..."
            hide image "04_pt/iris/q5/iris09.png" at center with Dissolve(.3)
        "\"Yup, that's because of your scar.\"":
            show image "04_pt/iris/q5/iris05.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris06.png" 
            sch1100 "Heh... You are just saying that."
            sch1100 "I know I'm pretty enough..."
            sch1100 "The actual reason is my father, am I right?"
            hide image "04_pt/iris/q5/iris05.png" at center with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q5/iris13.png", horizontal=True) at center with Dissolve(.2)
    sch1100 "It's bad enough that he doesn't allow me to dance for the patrons with other girls..."
    sch1100 "Can I at least get groped every once in a while like everyone else?"
    show image im.Flip ("04_pt/iris/q5/iris06.png", horizontal=True) at center with Dissolve(.2)
    hide image im.Flip ("04_pt/iris/q5/iris13.png", horizontal=True) at center with Dissolve(.2)
    sch1100 "I think I deserve that much! Don't I?"
    menu:
        "\"Next time I will grope you, I promise.\"":
            hide image im.Flip ("04_pt/iris/q5/iris06.png", horizontal=True) at center with Dissolve(.2)
            show image im.Flip ("04_pt/iris/q5/iris05.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Really?"
            sch1100 "You're probably saying this to all the girls..."
            sch1100 "Well, I will keep you to that promise!"
            hide image im.Flip ("04_pt/iris/q5/iris05.png", horizontal=True) at center with Dissolve(.3)
        "-(Say nothing and grope her butt)-":
            hide image im.Flip ("04_pt/iris/q5/iris06.png", horizontal=True) at center with Dissolve(.2)
            ">You reach out and squeeze the Iris' butt."
            show image im.Flip ("04_pt/iris/q5/iris14.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "!!!!!!!!!???"
            show image im.Flip ("04_pt/iris/q5/iris15.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris14.png", horizontal=True) 
            sch1100 "What are you doing, are you insane?"
            show image im.Flip ("04_pt/iris/q5/iris16.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris15.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Not like this... My father might see!"
            sch1100 "..........."
            show image im.Flip ("04_pt/iris/q5/iris05.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris16.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "But thank you... Thank you for making me feel like a normal girl for a change..."
            hide image im.Flip ("04_pt/iris/q5/iris05.png", horizontal=True) at center with Dissolve(.3)
        "\"Behave, girl! Or I will tell your father!\"":
            hide image im.Flip ("04_pt/iris/q5/iris06.png", horizontal=True) at center with Dissolve(.2)
            show image im.Flip ("04_pt/iris/q5/iris05.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "He-he... You're full of it!"
            sch1100 "I know you would never do that..."
            sch1100 "......................"
            show image im.Flip ("04_pt/iris/q5/iris07.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris05.png", horizontal=True) 
            sch1100 "R-right?"
            hide image im.Flip ("04_pt/iris/q5/iris07.png", horizontal=True) at center with Dissolve(.3)
    ">You spend the rest of the evening drinking wine and having a lively discussion with Iris."
    ">Your relationship with Iris has improved."
    show blkfade with Dissolve(.3)
    $ mdaughterfriendship += 1
    $ vine = renpy.random.randint(30, 50)
    $ gold = gold - vine
    ">You spent [vine] gold on wine tonight."
    ">You decide to call it a night and leave the tavern."
    $ renpy.play('sounds/door2.mp3')
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld2.png" with Dissolve(.3)
    hide blkfade with Dissolve(.5)
    ">You return home and go to sleep."
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayone
label mddate2:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld2.png" behind blkfade
    show image "04_pt/iris/q5/iris17.png" at center behind blkfade
    pause.3
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Oh, hi there!"
    sch1100 "Let me pour you some wine..."
    show image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris17.png" 
    sch1100 "..................."
    hide image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
    ">Iris pours wine into your pint."
    menu:
        "-Reach out and grope her butt-":
            ">You put your hand on one of  Iris's butt-cheeks and give it a good squeeze..."
            show image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
            sch1100 "......................."
            show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris19.png" 
            sch1100 "Enjoy your wine."
            hide image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
        "-Reach out and squeeze her tits-":
            ">You grab one of Iris's tits and squeeze it through the semi-transparent fabric of her top."
            show image "04_pt/iris/q5/iris21.png" at center with Dissolve(.3)
            sch1100 "!!!!!!!!!!!!!!!!!!!!!!!!!!"
            show image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris21.png" 
            sch1100 "What the hell are you doing?!"
            sch1100 "Touch me like this again and I will gut you like a pig!"
            play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
            hide image "04_pt/iris/q5/iris22.png" 
            show image im.Flip ("04_pt/iris/q5/iris22.png", horizontal=True) at left with Dissolve(.3)
            show image "quest01/maslab04.png" at right with dissolve
            sch600 "What is going on here?"
            menu:
                "\"Maslab, buddy. Everything is fine.\"":
                    sch600 "Is it?"
                    show image "quest01/maslab03.png" at right with dissolve
                    hide image "quest01/maslab04.png" at right with dissolve
                    sch600 "What happened, Iris?"
                    sch1100 "..................."
                    show image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at left with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris22.png", horizontal=True)
                    sch1100 "Ha-ha-ha! Father, it's nothing really."
                    hide image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at left with Dissolve(.3)
                    hide image "quest01/maslab03.png" at right with dissolve
                "\"I touched your daughter, sorry.\"":
                    with hpunch
                    sch600 "{size=+7}You did what?{/size}"
                    show image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at left with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris22.png", horizontal=True)
                    sch1100 "Ha-ha-ha! Your friend is so funny, father!"
                    sch1100 "That's not what happened at all!"
                    hide image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at left with Dissolve(.3)
                    hide image "quest01/maslab04.png" at right with dissolve
                "\"...........................\"":
                    sch1100 "Nothing, father..."
                    show image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at left with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris22.png", horizontal=True)
                    sch600 "Then why do you shout like that, girl?"
                    show image "quest01/maslab04.png" at right with dissolve
            show image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "I was just telling your friend here a story..."
            sch1100 "So the story goes like this..."
            sch1100 "The girl said: \"Touch me like this again and will I gut you like a pig!\"."
            sch1100 "And the guy said: \"Shut up, you bitch!\"."
            sch1100 "So... em... So then she stabbed him in his stomach three times and left him there to die..."
            sch1100 "The end."
            sch1100 "Such a funny story, don't you think?"
            sch1100 "Ha... ha... ha............"
            hide image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
            show image im.Flip ("04_pt/iris/q5/iris24.png", horizontal=True) at left with Dissolve(.3)
            show image "quest01/maslab04.png" at right with dissolve
            menu:
                "\"Ha-ha! So funny....\"":
                    show image "quest01/maslab03.png" at right with dissolve
                    hide image "quest01/maslab04.png" at right with dissolve
                    sch600 "Hm..."
                "\"That's awful...\"":
                    hide image im.Flip ("04_pt/iris/q5/iris24.png", horizontal=True) at center with Dissolve(.3)
                    show image im.Flip ("04_pt/iris/q5/iris25.png", horizontal=True) at left with Dissolve(.3)
                    sch1100 "{size=-5}(Pst! What are you doing? Play along!){/size}"
            sch600 "Well, I need to get back to work."
            hide image "quest01/maslab04.png" at right with dissolve
            hide image "quest01/maslab03.png" at right with dissolve
            show image "quest01/maslab03.png" at right with dissolve
            sch600 "Just keep your voice down when you tell people your weird stories, girl!"
            hide image im.Flip ("04_pt/iris/q5/iris25.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris24.png", horizontal=True) at left with Dissolve(.3)
            show image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at left with Dissolve(.3)
            sch1100 "Of course father! Sorry."
            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
            hide image "quest01/maslab03.png" at right with dissolve
            hide image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at left with Dissolve(.3)
            show image "04_pt/iris/q5/iris23.png" at center with Dissolve(.3)
            sch1100 "Phew, that was close."
            show image "04_pt/iris/q5/iris27.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris23.png" 
            sch1100 "{size=-5}(Have you lost your mind, grabbing my tit like this all of a sudden?){/size}"
            show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris27.png"
            sch1100 "Sorry for almost getting us both in trouble though."
            sch1100 "It's just that you startled me..."
            show image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris26.png"
            sch1100 "Crap... Let's forget this ever happened..."
            sch1100 "..............."
            hide image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
        "-Do nothing-":
            show image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
            sch1100 "Tsk....."
            show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris22.png" 
            sch1100 "{size=-5}(Whywon'thegropeme?){/size}"
            sch1100 "Whatever...."
            hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q5/iris29.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "......................"
    sch1100 "So how is Jasper doing?"
    sch1100 "Snobby as usual?..."
    hide image im.Flip ("04_pt/iris/q5/iris29.png", horizontal=True) at center with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q5/iris27.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "I have no idea how you put up with that girl!"
    show image im.Flip ("04_pt/iris/q5/iris22.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q5/iris27.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "I hope you punish her when she misbehaves!"
    show image im.Flip ("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q5/iris22.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "I bet you do punish her... punish her good...{image=textheart.png}"
    hide image im.Flip ("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "......."
    sch1100 "Some more wine?"
    menu:
        "\"You look different again...\"":
            hide image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
            show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            sch1100 "You mean my new top? Do you like it?"
        "\"I can almost see your nipples.\"":
            hide image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
            show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            sch1100 "Shut up, it's not {size=+5}that{/size} revealing..."
            sch1100 "Is it?"
        "\"Did Maslab approve of your new top?\"":
            hide image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
            show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
            sch1100 "Tsk... As if..."
            sch1100 "If father were to notice me wearing this he would probably get me flogged for real..."
            sch1100 "But you know what?"
            show image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
            sch1100 "Screw him! I don't care!"
            show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
            sch1100 ".........."
            sch1100 "So, you like my new top?"
    sch1100 "I actually made this top out of my old veil."
    show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
    sch1100 "Father said: \"you should wear your veil, girl!\"."
    show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
    sch1100 "Well, guess what, daddy. I do now!"
    hide image "04_pt/iris/q5/iris20.png" at center with Dissolve(.5)
    ">You spend the rest of the evening drinking wine and having a lively discussion with Iris."
    ">Your relationship with Iris has improved."
    show blkfade with Dissolve(.3)
    $ mdaughterfriendship += 1
    $ vine = renpy.random.randint(30, 50)
    $ gold = gold - vine
    ">You spent [vine] gold on wine tonight."
    ">You decide to call it a night and leave the tavern."
    $ renpy.play('sounds/door2.mp3')
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld2.png" with Dissolve(.3)
    hide blkfade with Dissolve(.5)
    ">You return home and go to sleep."
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayone
############################################
label mddate3:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld2.png" behind blkfade
    show image "04_pt/iris/q5/iris17.png" at center behind blkfade
    pause.3
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Hi there, I was hoping you would show up today!"
    show image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris17.png"
    sch1100 "Let me pour you some wine first..."
    hide image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
    ">Iris bends over the table a little to pour you your drink."
    menu:
        "-Grope her butt-":
            ">You put your hand on the girl's butt and give it a squeeze."
            show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
            sch1100 "Heh... I'm glad to see you too."
            hide image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
        "-Stare at her tits-":
            ">That see-through top Iris is wearing is very revealing. You stare at her tits intently."
            show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            sch1100 "I'm getting so much attention since I started to wear my old veil like this..."
            show image "04_pt/iris/q5/iris24.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            sch1100 "I only hope father will never notice..."
            hide image "04_pt/iris/q5/iris24.png" at center with Dissolve(.3)
        "-Do nothing...-":
            show image "04_pt/iris/q5/iris27.png" at center with Dissolve(.3)
            sch1100 "Tsk... Maybe I should just give up on you."
            show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris27.png" at center with Dissolve(.3)
            sch1100 "Are you into boys or something?"
            sch1100 "Well, in any case..."
            hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q5/iris29.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "Enjoy your wine now..."
    show image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q5/iris29.png", horizontal=True) 
    sch1100 "..............."
    show image im.Flip ("04_pt/iris/q5/iris19.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) 
    sch1100 "Hm......"
    show image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q5/iris19.png", horizontal=True) 
    sch1100 "Listen, how about we take a walk later tonight after I'm done working?"
    menu:
        "\"Are you asking me out?\"":
            show image im.Flip ("04_pt/iris/q5/iris21.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) 
            sch1100 "Huh? What is \"asking out\"?"
            sch1100 "I just want to take a walk, that's all..."
            hide image im.Flip ("04_pt/iris/q5/iris21.png", horizontal=True) at center with Dissolve(.3)
        "\"Sure, I'll wait for you.\"":
            sch1100 "Great!"
            hide image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) with Dissolve(.3)
        "\"Sorry, not interested.\"":
            show image im.Flip ("04_pt/iris/q5/iris27.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris20.png", horizontal=True) 
            sch1100 "Tsk..."
            sch1100 "Do this as a favor to me then!"
            hide image im.Flip ("04_pt/iris/q5/iris27.png", horizontal=True) at center with Dissolve(.3)
    show image "04_pt/iris/q5/iris29.png" at center with Dissolve(.3)
    sch1100 "I need to get back to work now."
    sch1100 "Wait for me outside of the tavern, OK?"
    show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris29.png" 
    sch1100 "See you then!"
    hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
    ">Iris leaves to serve other customers..."
    ">You enjoy your wine..."
    ">Time passes by slowly..."
    ">Finally you decide it's your cue..."
    show blkfade with Dissolve(.3)
    $ mdaughterfriendship += 1
    $ vine = renpy.random.randint(30, 50)
    $ gold = gold - vine
    ">You spent [vine] gold on wine tonight."
    play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
    $ renpy.play('sounds/door2.mp3')
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld2.png" with Dissolve(.3)
    hide blkfade with Dissolve(.5)
    ">You leave the tavern and wait for Iris in a nearby alley..."
    ">Nights are always very cold in Agrabah. You feel a chill running down your spine..."
    ">Finally Iris shows up..."
    show image "04_pt/iris/q5/iris30.png" at center with Dissolve(.3)
    sch1100 "Hi there. Thank you for waiting."
    sch1100 "Did you have to wait long?"
    menu:
        "\"Don't worry about it.\"":
            pass
        "\"Wearing a veil again?\"":
            sch1100 "Yes. Somehow I feel... naked tonight..."
    sch1100 "So, how about we take a walk?"
    sch1100 "I like taking night walks..."
    sch1100 "Usually I'm all by myself though..."
    show image "04_pt/iris/q5/iris32.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris30.png" 
    sch1100 "These streets can be dangerous for a girl at night, you know..."
    sch1100 "But I can take care of myself..."
    show image "04_pt/iris/q5/iris30.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris32.png"
    sch1100 "Not tonight though... Tonight is different... it's a bit scary... because..."
    show image "04_pt/iris/q5/iris33.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris30.png"
    sch1100 "Em...  never mind..."
    label yourhouse:
    show image "04_pt/iris/q5/iris35.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris33.png"
    label retreat:
    sch1100 "So, where do you want to go?"
    menu:
        "-Cheapside-":
            hide image "04_pt/iris/q5/iris35.png" at center with Dissolve(.3)
            ">You take Iris to the cheapside..."
            show blkfade with Dissolve(.3)
            show image "04_pt/slavem/bld.png" behind blkfade
            show image "04_pt/iris/q5/iris35.png" at center behind blkfade
            pause 1
            hide blkfade with Dissolve(.5)
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            sch1100 "Cheapside, huh?..."
            show image "04_pt/iris/q5/iris36.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris35.png" 
            sch1100 "I have so many memories here..."
            show image "04_pt/iris/q5/iris32.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris36.png" 
            sch1100 "This part of the town can be really dangerous at night, you know..."
            menu:
                "\"I will protect you.\"":
                    show image "04_pt/iris/q5/iris37.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris32.png"
                    sch1100 "To be honest, only a year ago I was the one who people would seek to be protected from..."
                    show image "04_pt/iris/q5/iris38.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris37.png"
                    sch1100 "Good old days..."
                    show image "04_pt/iris/q5/iris39.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris38.png"
                    sch1100 "But I'm starting to enjoy feeling like an normal girl every once in a while..."
                    show image "04_pt/iris/q5/iris40.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris39.png"
                    sch1100 "I'll tell you what: if we run into trouble I will just pretend to tremble with fear and let you protect me, how about that?"
                    hide image "04_pt/iris/q5/iris40.png" at center with Dissolve(.3)
                    ">Iris seems to be enjoying your company."
                "\"Danger is exciting!\"":
                    show image "04_pt/iris/q5/iris41.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris32.png"
                    sch1100 "I know, right!?"
                    show image "04_pt/iris/q5/iris42.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris41.png"
                    sch1100 "My life's been so boring lately though..."
                    show image "04_pt/iris/q5/iris37.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris42.png"
                    sch1100 "Let's hope we will get into some sort of trouble here!"
                    hide image "04_pt/iris/q5/iris37.png" at center with Dissolve(.3)
                    ">Iris is excited with anticipation."
                "\"Will you protect me?\"":
                    show image "04_pt/iris/q5/iris37.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris32.png"
                    sch1100 "Heh... You're funny!"
                    hide image "04_pt/iris/q5/iris37.png" at center with Dissolve(.3)
            ">You and Iris take a slow walk around the cheapside trying not to step into too many waste puddles..."
            who2 "Coin for the poor?"
            ">That voice... It sounds familiar..."
            sch8 "Is someone there? Coin for the poor?"
            show image im.Flip ("04_pt/iris/q5/iris38.png", horizontal=True) at left with Dissolve(.3)
            sch1100 "Hello there, Crocus, you old crow."
            sch7 "Is that really you, Iris? \nInfamous Iris \"one slice\"?"
            show image im.Flip ("04_pt/iris/q5/iris40.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris38.png", horizontal=True) 
            sch1100 "He-he. I haven't been called that in a while..."
            sch1100 "Just Iris now..."
            sch7 "My dear girl, did you come to keep this poor old man company...?"
            show image im.Flip ("04_pt/iris/q5/iris43.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris40.png", horizontal=True) 
            sch1100 "Huh?"
            sch7 "Maybe to keep Crocus warm also? Chilly night winds are bad for my bones..."
            sch1100 "You behave now, you old pervert..."
            sch7 "Crocus doesn't ask for much... Just show him a tit and he will be happy."
            show image im.Flip ("04_pt/iris/q5/iris44.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris43.png", horizontal=True) 
            sch1100 "Now you're testing my patience old man..."
            show image im.Flip ("04_pt/iris/q5/iris37.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris44.png", horizontal=True)
            sch1100 "And you're embarrassing me in front of my friend..."
            sch8 "Your friend? My eyes are not good in the dark..." 
            label noforcrocus:
            menu:
                sch8 "Who else is there?"
                "\"Hello, you old crow.\"":
                    sch7 "That voice...."
                    sch8 "Generous master? Is it you?"
                "\"Hello, Crocus.\"":
                    sch7 "Hello, kind sir."
                    sch8 "Yes, I know you..."
                "-(Give crocus a few coins)-":
                    if gold >= 5: 
                        $ gold -=5
                        $ renpy.play('sounds/coins.mp3')
                        ">You toss a few (5) gold coins into the beggar's cup."
                        sch7 "!!!!!!"
                        sch8 "Thank you, kind master!"
                    else:
                        ">You reach for your purse, but realize that you don't have enough money... This is embarrassing..."
                        jump noforcrocus
            sch8 "Kind master, how is your beautiful slave-girl doing?"
            sch8 "Is our Iris your new slave-girl?"
            sch1100 "What? I'm a no man's slave-girl!"
            sch7 "Just a girl for a night then?"
            show image im.Flip ("04_pt/iris/q5/iris44.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris37.png", horizontal=True)
            sch1100 "What?"
            sch7 "You're lucky girl, iris. I hear a lot of good things about our kind master here..."
            show image im.Flip ("04_pt/iris/q5/iris46.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris44.png", horizontal=True)
            sch1100 "What? I... er...."
            show image im.Flip ("04_pt/iris/q5/iris45.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris46.png", horizontal=True)
            sch1100 "Yeah, whatever..."
            show image im.Flip ("04_pt/iris/q5/iris48.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris46.png", horizontal=True)
            sch1100 "You know what, maybe we should just go..."
            show image im.Flip ("04_pt/iris/q5/iris49.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris48.png", horizontal=True)
            sch1100 "You take care, old crow..."
            sch7 "Leaving already?"
            sch8 "What about the tit you promised poor crocus to have a glimpse of?"
            show image im.Flip ("04_pt/iris/q5/iris47.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris49.png", horizontal=True)
            sch1100 "Tsk... Sure... I just showed it to you. Did you see it?"
            sch7 "No... My eyes are no good at night... But just knowing that you did will keep me warm tonight..."
            show image im.Flip ("04_pt/iris/q5/iris45.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris47.png", horizontal=True)
            sch1100 "Tsk, more like keeping you hard, you old perv..."
            sch8 "You take care now, girl. And you too, kind master."
            hide image im.Flip ("04_pt/iris/q5/iris45.png", horizontal=True) at left with Dissolve(.3)
            ">You leave the cheapside."
        "-My house-":
            show image "04_pt/iris/q5/iris34.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris35.png"
            sch1100 "Your house?"
            sch1100 "Why? I told you I want to take a walk outside..."
            hide image "04_pt/iris/q5/iris34.png" with Dissolve(.3)
            jump yourhouse
        "-The palace-":
            hide image "04_pt/iris/q5/iris35.png" at center with Dissolve(.3)
            ">You take Iris to the palace gates..."
            show blkfade with Dissolve(.3)
            show image "04_pt/slavem/bld.png" behind blkfade
            show image im.Flip ("04_pt/iris/q5/iris35.png", horizontal=True) at center behind blkfade
            pause 1
            hide blkfade with Dissolve(.5)
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            sch1100 "The palace is so big and beautiful..."
            sch1100 "Can you imagine how much gold and precious gems are hidden behind these walls?"
            play music "music/Vision2.mp3" fadein 1 fadeout 1 #TENSION
            sch4 "Who goes there?!"
            show image im.Flip ("04_pt/iris/q5/iris53.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris35.png", horizontal=True) at center behind blkfade
            sch1100 "Oh, crap! That the palace guard! Let's run!"
            menu:
                "-(Run away)-":
                    hide image im.Flip ("04_pt/iris/q5/iris53.png", horizontal=True) at center with Dissolve(.3)
                    ">You quickly bail."
                    play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                    jump runfromrasul
                "\"Hello, Rasul.\"":
                    play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                    sch4 "Oh, I didn't recognize you there... My apologies."
                    sch4 "Good evening princess Jasmine..."
                    hide image im.Flip ("04_pt/iris/q5/iris53.png", horizontal=True) 
                    show image im.Flip ("04_pt/iris/q5/iris54.png", horizontal=True) at left with Dissolve(.3)
                    sch1100 "Huh?"
                    sch4 "Oh, I'm sorry, I thought..."
                    sch4 "Never mind..."
                    sch4 "....em..........."
                    sch4 "I will continue on my route then..."
                    hide image im.Flip ("04_pt/iris/q5/iris54.png", horizontal=True) with Dissolve(.3)
                    ">Rasul leaves..."
                    show image im.Flip ("04_pt/iris/q5/iris32.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "This was so bizzare..."
                    sch1100 "He was acting as if he knows you..."
                    show image im.Flip ("04_pt/iris/q5/iris36.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris32.png", horizontal=True) 
                    sch1100 "And he called me a princess?"
                    menu:
                        "\"He is drunk.\"":
                            show image im.Flip ("04_pt/iris/q5/iris37.png", horizontal=True) at center with Dissolve(.3)
                            hide image im.Flip ("04_pt/iris/q5/iris36.png", horizontal=True) 
                            sch1100 "Yes, obviously..."
                            hide image im.Flip ("04_pt/iris/q5/iris37.png", horizontal=True) at center with Dissolve(.3)
                        "\"I do know him.\"":
                            show image im.Flip ("04_pt/iris/q5/iris54.png", horizontal=True) at center with Dissolve(.3)
                            hide image im.Flip ("04_pt/iris/q5/iris36.png", horizontal=True) 
                            sch1100 "You do?"
                            sch1100 "What kind of business could you possibly have with the royal guard?"
                            show image im.Flip ("04_pt/iris/q5/iris37.png", horizontal=True) at center with Dissolve(.3)
                            hide image im.Flip ("04_pt/iris/q5/iris54.png", horizontal=True)
                            sch1100 "No, wait, don't tell me. That's non of my business..."
                            hide image im.Flip ("04_pt/iris/q5/iris37.png", horizontal=True) at center with Dissolve(.3)
                        "\"You are a princess!\"":
                            show image im.Flip ("04_pt/iris/q5/iris54.png", horizontal=True) at center with Dissolve(.3)
                            hide image im.Flip ("04_pt/iris/q5/iris36.png", horizontal=True) 
                            sch1100 "What?"
                            show image im.Flip ("04_pt/iris/q5/iris32.png", horizontal=True) at center with Dissolve(.3)
                            hide image im.Flip ("04_pt/iris/q5/iris54.png", horizontal=True) 
                            sch1100 "Yeah, right! I am Iris the princess!"
                            sch1100 "Bow before me, you filthy commoners..."
                            show image im.Flip ("04_pt/iris/q5/iris36.png", horizontal=True) at center with Dissolve(.3)
                            hide image im.Flip ("04_pt/iris/q5/iris32.png", horizontal=True)
                            sch1100 "Hm... These words sound strangely familiar..."
                            hide image im.Flip ("04_pt/iris/q5/iris36.png", horizontal=True) at center with Dissolve(.3)
    label runfromrasul:
    show blkfade with Dissolve(.3)
    show image "04_pt/iris/q5/iris40.png" at center behind blkfade
    pause 1
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "That was fun..."
    show image "04_pt/iris/q5/iris33.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris40.png" 
    sch1100 "Er... Em...."
    show image "04_pt/iris/q5/iris34.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris33.png" 
    sch1100 ".............."
    show image "04_pt/iris/q5/iris33.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris34.png" 
    stop music fadeout 3
    sch1100 "Today is such a warm night, don't you think?"
    menu:
        "\"What? It's freezing!\"":
            show image "04_pt/iris/q5/iris39.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris33.png" 
            sch1100 "No... I'm hot..."
            hide image "04_pt/iris/q5/iris39.png" at center with Dissolve(.3)
        "\"Yeah, I'm burning up!\"":
            show image "04_pt/iris/q5/iris39.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris33.png" 
            sch1100 "Yes, me too..."
            hide image "04_pt/iris/q5/iris39.png" at center with Dissolve(.3)
    show image "04_pt/iris/q5/iris33.png" at center with Dissolve(.3)
    play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
    sch1100 "I think I need to undo my cloak a little..."
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris33.png" at center with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "There..."
    sch1100 "Much better..."
    show image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
    sch1100 "So, where to now?"
    menu:
        "\"Let's just keep walking...\"":
            sch1100 "Sure... Em..."
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
        "\"My house!\"":
            sch1100 "Em... No, I would rather walk outside some more..."
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
        "\"Are you... naked under that thing?\"":
            show image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)            
            sch1100 "What? What are you talking about?"
            sch1100 "Let's just keep walking..."
            hide image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
    show image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
    sch1100 "So... What do you think of my father?"
    menu:
        "\"He is a standup guy.\"":
            show image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            sch1100 "Yes... I guess he is..."
        "\"He scares me.\"":
            show image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            sch1100 "Really...?"
            sch1100 "You get scared easily then..."
            show image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
            sch1100 "I myself am afraid of him sometimes, but I'm a girl and his daughter..."
            show image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            sch1100 "I always thought you guys were good friends..."
        "\"Me and him are alike.\"":
            sch1100 "Hm... Yeah, I think you are..."
            show image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            sch1100 "Although you do not scare me nearly as much..."
    sch1100 "Whew... It's so hot in here, I'm burning up..."
    menu:
        "\"Just undo your cloak a bit more...\"":
            show image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris52.png" at center with Dissolve(.3)
            sch1100 "....I..... em...."
            show image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            sch1100 "Could you do it for me?"
            sch1100 "Undo my cloak a little more..."
        "\"And I'm feezing. Hug me.\"":
            show image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris52.png" at center with Dissolve(.3)
            sch1100 "What? You want me to keep {size=+5}you{/size} warm?"
            show image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            sch1100 "It supposed to be the other way around, don't you think?"
            show image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris52.png" at center with Dissolve(.3)
            sch1100 "I want to, I mean I need to undo my cloak some more..."
            sch1100 "Could you do it for me?"
            show image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris51.png" at center with Dissolve(.3)
            sch1100 "Undo my cloak a little more..."
        "\"Actually it's really, really cold.\"":
            sch1100 "No, no... It's hot here... I want to, I mean I need to undo my cloak some more..."
            sch1100 "Could you do it for me?"
            sch1100 "Undo my cloak a little more..."
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris50.png" at center with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Ah...{image=textheart.png}"
    sch1100 "Aha.... aha....{image=textheart.png} Thank you...*panting*"
    menu:
        "\"You {size=+5}are{/size} naked...\"":
            show image "04_pt/iris/q5/iris56.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
            sch1100 "Aha...{image=textheart.png} What...? Yes... I know..."
            sch1100 "Let's keep walking please..."
            show image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris56.png" at center with Dissolve(.3)
        "-(Stare at her tits.)-":
            hide image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
            "You can't look away from Iris's tits... You can almost see her nipples..."
            show image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
            sch1100 "Aha...*breathing heavily*"
            hide image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
        "-(Stare at her pussy.)-":
            hide image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
            ">You can't help but stare at Iris's pussy..."
            ">The girl is completely naked under that cloak... What game is she playing?"
        "-(Just act normal.)-":
            hide image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
            ">You keep walking as if you didn't even notice that Iris is practically naked now..."
    label runfromtavern:
    show image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris56.png" at center with Dissolve(.3)
    sch1100 "So.... em..."
    sch1100 "Where to now?"
    label muggingpeople:
    menu:
        "-Take her for a walk around the Tavern-":
            show blkfade with Dissolve(.3)
            hide image "04_pt/iris/q5/iris55.png"
            show image "04_pt/iris/q5/iris59.png" at center behind blkfade
            pause.8
            hide blkfade with Dissolve(.3)
            sch1100 "We are back?"
            sch1100 "What are you doing? What if somebody of the patrons sees me like this?"
            show image "04_pt/iris/q5/iris58.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris59.png" at center with Dissolve(.3)
            sch1100 "Or even worse, what if my Father does?"
            play music "music/tension2.mp3" fadein 1 fadeout 1 #TENSION
            sch1100 "He would kill us both on the spot!"
            menu:
                "-Undo your cloak some more-":
                    show image "04_pt/iris/q5/iris59.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris58.png" at center with Dissolve(.3)
                    sch1100 "..........."
                    show image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris59.png" at center with Dissolve(.3)
                    sch1100 "Well, do it yourslef then..."
                "-Take of your cloak completely-":
                    show image "04_pt/iris/q5/iris59.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris58.png" at center with Dissolve(.3)
                    sch1100 "What?! Have you lost your mind?!"
                    show image "04_pt/iris/q5/iris58.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris59.png" at center with Dissolve(.3)
                    sch1100 "My heart is already racing like crazy..."
                    sch1100 "If I take my cloak off here I think I might die of shame and embarrassment..."
                    show image "04_pt/iris/q5/iris60.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris58.png" at center with Dissolve(.3)
                    sch1100 "Embarrassment and excitement..."
                    sch1100 "Maybe I should at least undo it some more..."
                    sch1100 "..........."
                    show image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
                    hide image "04_pt/iris/q5/iris60.png" at center with Dissolve(.3)
                    sch1100 "You do it..."
                "-You're right. Let's leave-":
                    hide image "04_pt/iris/q5/iris58.png" at center with Dissolve(.3)
                    play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
                    jump runfromtavern
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            show image "04_pt/iris/q5/iris61.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris55.png" at center with Dissolve(.3)
            sch1100 "Oh my god... I don't think I ever been this terrified in my entire life..."
            show image "04_pt/iris/q5/iris62.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris61.png" at center with Dissolve(.3)
            sch1100 "Terrified and excited ..."
            sch1100 "This is amazing... This feels a million times better then I thought it would..."
            sch1100 "It's almost as exiting as mugging or kidnapping people..."
            show image "04_pt/iris/q5/iris63.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris62.png" at center with Dissolve(.3)
            sch1100 "He... he... he..."
            show image "04_pt/iris/q5/iris33.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris63.png" at center with Dissolve(.3)
            sch1100 "You know what? I think I better leave now..."
            show image "04_pt/iris/q5/iris34.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris33.png" at center with Dissolve(.3)
            sch1100 "Thank you for taking a walk with me tonight..."
            sch1100 "Have a good night..."
        "-Take her to your house-":
            sch1100 "Em..."
            sch1100 "No... I don't think that's a good idea..."
            jump muggingpeople
        "-Take her to the market square-":
            show blkfade with Dissolve(.3)
            hide image "04_pt/iris/q5/iris55.png" 
            show image im.Flip ("04_pt/iris/q5/iris56.png", horizontal=True) at center behind blkfade
            pause.3
            hide blkfade with Dissolve(.3)
            sch1100 "Market square, huh?"
            sch1100 "This place is so lively and full of people during the day..."
            sch1100 "And during the night hours it's the complete opposite..."
            show image im.Flip ("04_pt/iris/q5/iris60.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris56.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Not a soul here..."
            menu:
                "\"Undo your cloak some more.\"":
                    sch1100 "You think I should?"
                    sch1100 "I think I will do it!"
                    sch1100 "Here it comes..."
                    sch1100 "Don't look at me like that... That's I... Em..."
                    sch1100 "Well, I might as well take the whole thing of now..."
                    jump taking_cloack_off
                "\"Take off your cloak completely.\"":
                    show image im.Flip ("04_pt/iris/q5/iris58.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris60.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Are you serious?"
                    show image im.Flip ("04_pt/iris/q5/iris60.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris58.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Well, there is not a soul here..."
                    sch1100 "Alright, I will take it off..."
                    label taking_cloack_off:
                    sch1100 "........................"
                    hide image im.Flip ("04_pt/iris/q5/iris60.png", horizontal=True) at center with Dissolve(.3)
                    show image "04_pt/iris/q5/iris60.png" at center with Dissolve(.3)
                    sch1100 "......................."
                    hide image "04_pt/iris/q5/iris60.png" at center with Dissolve(.3)
                    show image im.Flip ("04_pt/iris/q5/iris60.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 ".........................."
                    show image im.Flip ("04_pt/iris/q5/iris56.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris60.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "This is silly... What is going on with me today?"
                    sch1100 "I'm pretty brave, you know... And it's nearly impossible to embarrass me..."
                    sch1100 "But... I just can't bring myself to taking this silly cloak off..."
                    sch1100 "You need to do it for me!"
                    show image im.Flip ("04_pt/iris/q5/iris60.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris56.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Come on... Before I change my mind."
                    show con1 at right
                    show ctc7 at right
                    pause 
                    hide con1
                    hide ctc7
                    hide image im.Flip ("04_pt/iris/q5/iris60.png", horizontal=True) at center with Dissolve(.3)
                    show image im.Flip ("04_pt/iris/q5/iris66.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "!!!!!!!!!!!!!!"
                    show image im.Flip ("04_pt/iris/q5/iris69.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris66.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "It's so cold..."
                    show image im.Flip ("04_pt/iris/q5/iris70.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris69.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "..........."
                    show image im.Flip ("04_pt/iris/q5/iris71.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris70.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "..........."
                    show image im.Flip ("04_pt/iris/q5/iris72.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris71.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "..........."
                    hide image im.Flip ("04_pt/iris/q5/iris72.png", horizontal=True) at center with Dissolve(.3)
                    show image im.Flip ("04_pt/iris/q5/iris68.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Alright, that's enough for the first time!"
                    show image im.Flip ("04_pt/iris/q5/iris74.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris68.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Oh my god! I always wanted to do this!"
                    show image im.Flip ("04_pt/iris/q5/iris73.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris74.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "This felt so... liberating!" 
                    show image im.Flip ("04_pt/iris/q5/iris43.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris73.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "And almost as exiting as mugging people..."
                    show image im.Flip ("04_pt/iris/q5/iris44.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris43.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "My life's been so boring since father decided to retire..."
                    show image im.Flip ("04_pt/iris/q5/iris39.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris44.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "But I had so much fun today! Thank you for accompanying me, I would not dare to do this on my own..."
                    show image im.Flip ("04_pt/iris/q5/iris36.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip ("04_pt/iris/q5/iris39.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Well, it's getting pretty late. I think I better head home now..."
                    hide image im.Flip ("04_pt/iris/q5/iris36.png", horizontal=True) at center with Dissolve(.3)
                "\"Let's go somewhere else...\"":
                    hide image im.Flip ("04_pt/iris/q5/iris60.png", horizontal=True) at center with Dissolve(.3)
                    jump runfromtavern
    play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
    menu:
        "\"What? You can't be serious!??\"":
            hide image "04_pt/iris/q5/iris34.png" at center with Dissolve(.3)
            show image im.Flip ("04_pt/iris/q5/iris39.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Huh? What did you expect?"
            sch1100 "Sorry, I'm not very good at this man and woman communication thing..."
            sch1100 "I had an amazing evening, and learned some new things about myself today..."
            sch1100 "And I'm sorry if I gave you the wrong idea..."
            sch1100 "You have a good night now..." 
            show blkfade with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris39.png", horizontal=True) at center with Dissolve(.3)
            ">Iris leaves."
            ">Your relationship with Iris has improved."
        "\"Goodnight, Iris.\"":
            hide image "04_pt/iris/q5/iris34.png" at center with Dissolve(.3)
            show image im.Flip ("04_pt/iris/q5/iris39.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "I'll see you again soon, right?"
            show blkfade with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris39.png", horizontal=True) at center with Dissolve(.3)
            ">Iris leaves."
            ">Your relationship with Iris has improved."
        "\"You have a beautiful body.\"":
            hide image "04_pt/iris/q5/iris34.png" at center with Dissolve(.3)
            show image im.Flip ("04_pt/iris/q5/iris45.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Huh?... You mean my body is beautiful, but my face is not?"
            sch1100 "Because I have this scar?"
            show image im.Flip ("04_pt/iris/q5/iris42.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris45.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "That's mean..."
            show image im.Flip ("04_pt/iris/q5/iris47.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris42.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "I'm going home now!"
            show blkfade with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris47.png", horizontal=True) at center with Dissolve(.3)
            ">Iris leaves."
            ">Your relationship with Iris stuck in a rut."
    
    ">You return home and go to sleep."
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayone
#################################################################################################################
label mddate4:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld2.png" behind blkfade
    show image "04_pt/iris/q5/iris17.png" at center behind blkfade
    pause.3
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Good evening, welcome to \"The Blue Bull\"."
    show image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris17.png" at center with Dissolve(.3)
    sch1100 "Let me pour you some wine..."
    hide image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
    ">Iris sticks her butt out and bends over almost to the point where she is practically lying on the table..."
    menu:
        "-Give her butt a squeeze-":
            ">You reach out, put your hand on one of Iris's butt cheeks and give it a good squeeze."
            show image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
            sch1100 "Anything else, sir?"
            hide image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
        "-Give her butt a slap-":
            $ renpy.play('sounds/slap.mp3')
            show image "04_pt/iris/q5/iris21.png" at center with Dissolve(.3)
            with hpunch
            sch1100 "!!!!!!!!!!!!?"
            show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris21.png" at center with Dissolve(.3)
            sch1100 "What are you doing, stupid?"
            sch1100 "..................."
            hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
        "-Grope her tits-":
            ">You reach out and grab one of Iris's tits... The girl keep pouring you your wine... Very slowly..."
            ">You start massaging her breast through the transparent fabric of her top..."
            ">You feel her hard nipple poking your palm..."
            sch11_62 "Ok, that's enough, stop it."
            sch11_62 "This is not allowed. Somebody will notice..."
            ">Reluctantly, you let go of her breast..."
        "-Do nothing-":
            ">You patiently wait for Iris to finish filling your cup."
            show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
            sch1100 "(Tsk... Whatever...)"
            hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "Em... listen, about our little adventure the other day..."
    show image im.Flip ("04_pt/iris/q5/iris24.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "You didn't tell anyone about it, did you?"
    show image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q5/iris24.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "It all seems so silly now... Why did I do that?"
    sch1100 "If someone were to find out and tell my father - I'd be dead..."
    hide image im.Flip ("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
    menu:
        "\"I did tell your father.\"":
            show image im.Flip ("04_pt/iris/q5/iris22.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "{size=+5}YOU DID WHAT?!{/size}"
            show image im.Flip ("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris22.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "No you didn't! Don't scare me like that!"
            hide image im.Flip ("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
        "\"It will be our secret.\"":
            show image im.Flip ("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "I like that."
            hide image im.Flip ("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
            ">Iris feels a bit closer to you now."
        "\"What adventure?\"":
            show image im.Flip ("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Well, you know... The other day, when you took me for a walk and I..."
            show image im.Flip ("04_pt/iris/q5/iris24.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Oh, I see what you did there..."
            show image im.Flip ("04_pt/iris/q5/iris19.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q5/iris24.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Yes, exactly! \"What adventure\"?"
            hide image im.Flip ("04_pt/iris/q5/iris19.png", horizontal=True) at center with Dissolve(.3)
    show image "04_pt/iris/q5/iris17.png" at center with Dissolve(.3)
    sch1100 "I need to take care of other customers, but it will not take long."
    sch1100 "Wait for me, alright? I have something I want to discuss with you..."
    hide image "04_pt/iris/q5/iris17.png" at center with Dissolve(.3)
    ">You slowly sip on your wine and wait for Iris to return..."
    show blkfade with Dissolve(.3)
    pause.8
    hide blkfade with Dissolve(.3)
    ">It's been a while but Iris has yet to show up..."
    ">It's getting pretty late..."
    ">You look around the tavern but don't see Iris anywhere..."
    show blkfade with d5
    pause.3
    hide blkfade with d5
    #play music "music/Bushwick Tarantella Loop.MP3" fadein 1 fadeout 1  #DICE GAME
    play music "music/India's Different (Dancing).MP3" fadein 1 fadeout 1 #DANCING
    ">The music is starting to play and you see all the waitresses abandoning whatever they were doing and climbing the tables..."
    ">Iris appears from the kitchen door... She looks very determined..."
    ">To your surprise you see Iris jumping on top of the nearest table and starting to dance rather awkwardly..."
    ">Just a few moments later her father forcefully pulls her down to the floor."
    ">They have a heated argument and Iris storms out the back to the kitchen... Maslab looks very angry..."
    ">You take another sip from you pint..."
    show blkfade with Dissolve(.3)
    stop music fadeout 7
    #play music "music/Bushwick Tarantella Loop.MP3" fadein 1 fadeout 1  #DICE GAME
    #play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show image "04_pt/iris/q5/iris22.png" at center behind blkfade
    pause.8
    hide blkfade with Dissolve(.3)
    sch1100 "{size=+5}I hate him!{/size}"
    with hpunch
    sch1100 "I hate him, I hate him, I hate him!"
    show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
    sch1100 "My father is such an idiot! When will he understand....?"
    play music "music/dice_game.MP3" fadein 3 fadeout 2  #DICE GAME2
    show image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
    sch1100 "Grab my ass! Do it now!"
    hide image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
    menu:
        "-(Grab her ass)-":
            ">You reach out and grab Iris' ass..."
            ">You start massaging her buttocks."
            show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
            sch1100 "Yes, like that! Let that old fool see!!"
        "\"I would rather not.\"":
            show image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
            sch1100 "Not you too?! I thought you were on my side?!"
    show image "04_pt/iris/q5/iris65.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
    sch1100 "I'm so sick of all this..."
    sch1100 "So sick of it all..."
    sch1100 ".............."
    sch1100 "............."
    sch1100 "............."
    show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris65.png" at center with Dissolve(.3)
    sch1100 "Fine! I made my decision!"
    sch1100 "I will go to Fat Lily and ask her for a job!"
    show image "04_pt/iris/q5/iris65.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
    sch1100 "I'm \"not old enough to dance\" like all the other girls, huh?"
    show image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris65.png" at center with Dissolve(.3)
    sch1100 "Well, I will be a whore then!"
    sch1100 "Yeah! That'll teach that old fool a lesson!"
    menu:
        "\"Have you lost your mind?!\"":
            show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
            sch1100 "No, I did not! I'm thinking clearly for the first time in a while!"
        "\"What a marvelous idea!\"":
            show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris22.png" at center with Dissolve(.3)
            sch1100 "I know, right!?"
    show image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris20.png" 
    hide image "04_pt/iris/q5/iris28.png" 
    sch1100 "I've been thinking about this for quite some time now, to be honest..."
    sch1100 "I even had a dress sketched out..."
    show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
    hide image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
    sch1100 "I need to order the dress from Azalea's store first... Then negotiate the details with Lily..."
    sch1100 "I will need your help... Can I count on you?"
    hide image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
    menu:
        "Quest: [quest5].":
            if onquest:
                    ">You need to complete your current quest first in order to take on a new one."
                    show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
                    sch1100 "Oh, I see..."
                    hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
                    "Your relationship with Iris is stuck in a rut."
                    $ vine = renpy.random.randint(30, 50)
                    $ gold = gold - vine
                    ">You spent [vine] gold on wine tonight."
                    ">You return home and go to sleep."
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
            else:
                if quest4complete:
                    show image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "I knew I could count on you!!!"
                    show image im.Flip("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Here is the dress design I mentioned earlier..."
                    hide image im.Flip("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
                    show image "04_pt/slavem/masteritem.png" with moveinleft
                    $ renpy.play('sounds/win2.mp3')
                    show image "04_pt/slavem/boxirissketch.png" with moveinright
                    "You received a rough sketch of a very skimpy dress."
                    hide image "04_pt/slavem/boxirissketch.png" with Dissolve(.4)
                    hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                    show image im.Flip("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Could you take this to Azalea and order that dress for me?"
                    show image im.Flip("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "This kind of dress won't come cheap, but you have money, right?"
                    show image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Alright, let me know when you will have the dress!"
                    show image im.Flip("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
                    hide image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "This is so exciting! Thank you so much for helping me out!"
                    sch1100 "Now I need to get back to work..."
                    hide image im.Flip("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
                    $ quest5start = True
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
                    $ mdaughterfriendship += 1
                    $ vine = renpy.random.randint(30, 50)
                    $ gold = gold - vine
                    ">You took an errand from Iris. Your relationship with her has moved to another level."
                    ">You spent [vine] gold on wine tonight."
                    ">You return home and go to sleep."
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
                else:
                    show image im.Flip("04_pt/iris/q5/iris65.png", horizontal=True) at center with Dissolve(.3)
                    sch1100 "Oh, shoot! I forgot! The Brothel has been closed for quite some time now...."
                    sch1100 "There will be no point in this dress unless \"Phoenix\" reopens."
                    sch1100 "Let us get back to drinking then...."
                    hide image im.Flip("04_pt/iris/q5/iris65.png", horizontal=True) at center with Dissolve(.3)
                    ">Your relationship with Iris is stuck in a rut. (For now.)"
                    $ vine = renpy.random.randint(30, 50)
                    $ gold = gold - vine
                    "You spent [vine] gold."
                    "You return home and go to sleep."
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
        "\"Maybe some other time...\"":
            show image im.Flip("04_pt/iris/q5/iris21.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "What? Are you serious...?"
            show image im.Flip("04_pt/iris/q5/iris22.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip("04_pt/iris/q5/iris21.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "But I need your help..."
            show image im.Flip("04_pt/iris/q5/iris65.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip("04_pt/iris/q5/iris22.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Tsk! Whatever! Fine, I don't care!"
            sch1100 "I will get back to my work then..."
            hide image im.Flip("04_pt/iris/q5/iris65.png", horizontal=True) at center with Dissolve(.3)
            ">You spend the rest of the night watching the girls dance..."
            ">Your relationship with is Iris stuck in a rut."
            $ vine = renpy.random.randint(30, 50)
            $ gold = gold - vine
            ">You spent [vine] gold on wine tonight."
            ">You return home and go to sleep."
            show image "interface/blackfade.png" with Dissolve(.3)
            pause 1
            jump dayone

        
label mddate5:
    if quest5start7:
        play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
        hide blkfade
        show blkfade with Dissolve(.3)
        show image "04_pt/slavem/bld2.png" behind blkfade
        show image "04_pt/iris/q5/iris17.png" at center behind blkfade
        pause.3
        hide blkfade with Dissolve(.5)
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        show image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris17.png" at center with Dissolve(.3)
        sch1100 "Good evening, welcome to \"The Blue Bull\"."
        sch1100 "Let me pour you some wine..."
        hide image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
        ">Iris sticks her butt out and bends over almost to the point where she is practically lying on the table..."
        menu:
            "-Give her butt a squeeze-":
                ">You reach out, put your hand on one of Iris's butt cheeks and give it a good squeeze."
                show image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
                sch1100 "Ah...{image=textheart.png}"
                hide image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
            "-Give her butt a slap-":
                $ renpy.play('sounds/slap.mp3')
                show image "04_pt/iris/q5/iris21.png" at center with Dissolve(.3)
                sch1100 "Ah...{image=textheart.png}"
                show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
                hide image "04_pt/iris/q5/iris21.png" at center with Dissolve(.3)
                sch1100 "T-thank you..."
                sch1100 "..................."
                hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            "-Grope her tits-":
                ">You reach out and grab one of Iris' tits... The girl keeps pouring you your wine... Very slowly..."
                ">You start massaging her breast through the transparent fabric of her old veil..."
                ">Her hard nipples poke into your palm..."
                sch11_62 "Ah...{image=textheart.png}"
                ">You keep massaging her breast... and give it a few good squeezes and then a firm pull."
                sch11_62 "Ah...{image=textheart.png} No, you have to stop now..."
                sch11_62 "I told you, this sort of behavior is frowned upon..."
                ">Reluctantly you let go of her breast..."
            "-Do nothing-":
                ">You patiently wait for Iris to finish filling your cup."
                show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
                sch1100 "(Tsk... Whatever...)"
                hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
        show image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
        sch1100 "So, is it ready? Do you have it?"
        show image im.Flip("04_pt/iris/q5/iris29.png", horizontal=True) at center with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
        sch1100 "No, wait, don't give it to me here, somebody might notice..."
        sch1100 "Let's meet outside... Wait for me near the backdoor."
        show image im.Flip("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris29.png", horizontal=True) at center with Dissolve(.3)
        sch1100 "Alright, see you in a few minutes then."
        hide image im.Flip("04_pt/iris/q5/iris26.png", horizontal=True) at center with Dissolve(.3)
        ">You finish your wine with a couple of big gulps and leave the building."
        play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
        $ renpy.play('sounds/door.mp3')
        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
        hide image "04_pt/slavem/bld2.png" with Dissolve(.3)
        ">You wait for Iris outside..."
        show image "04_pt/slavem/bld.png" with Dissolve(.3)
        show image "04_pt/slavem/bld2.png" with Dissolve(.3)
        show image "04_pt/iris/q5/iris39.png" at center with Dissolve(.3)
        sch1100 "So where is it?"
        show image "04_pt/iris/q5/iris41.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris39.png" at center with Dissolve(.3)
        sch1100 "Give it to me!"
        hide image "04_pt/iris/q5/iris41.png" at center with Dissolve(.3)
        show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
        show image "04_pt/slavem/boxdress.png" with moveinleft
        ">You hand over the dress to Iris."
        hide image "04_pt/slavem/boxdress.png" with moveoutright
        hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
        show image "04_pt/iris/q5/iris31.png" at center with Dissolve(.3)
        sch1100 "I can't wait to try this one on!"
        show image "04_pt/iris/q5/iris34.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris31.png" at center with Dissolve(.3)
        sch1100 "Thank you for your help!"
        sch1100 "I need to get back to work now before father notices my absence..."
        sch1100 "I hope I will see you again soon."
        hide image "04_pt/iris/q5/iris34.png" at center with Dissolve(.3)
        ">Iris disappears in the tavern building."
        hide image "04_pt/slavem/bld2.png" with Dissolve(.3)
        ">You decide to call it a night."
        $ mdaughterfriendship += 1
        $ quest5start7 = False
        $ quest5complete = True
        $ onquest = False
        $ renpy.play('sounds/win2.mp3')
        hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
        show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
        show con1 at right
        show ctc7 at right
        pause
        ">You completed an errand for Iris. Now she feels indebted to you."
        ">Your relationship with Iris has improved greatly." 

        hide con1
        hide ctc7
        hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
        ">You return home and go to sleep."
        show image "interface/blackfade.png" with Dissolve(.3)
        pause 1
        jump dayone

    else:
        play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
        show blkfade with Dissolve(.3)
        show image "04_pt/slavem/bld2.png" behind blkfade
        show image "04_pt/iris/q5/iris17.png" at center behind blkfade
        pause.3
        hide blkfade with Dissolve(.5)
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        sch1100 "Good evening, welcome to \"The Blue Bull\"."
        show image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris17.png" at center with Dissolve(.3)
        sch1100 "Let me pour you some wine..."
        hide image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
        ">Iris sticks her butt out and bends over almost to the point where she is practically lying on the table..."
        menu:
            "-Give her butt a squeeze-":
                ">You reach out, put your hand on one of Iris's butt cheeks and give it a good squeeze."
                show image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
                sch1100 ".................."
                hide image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
            "-Give her butt a slap-":
                $ renpy.play('sounds/slap.mp3')
                show image "04_pt/iris/q5/iris21.png" at center with Dissolve(.3)
                sch1100 "!!!!!!!!!!!!?"
                show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
                hide image "04_pt/iris/q5/iris21.png" at center with Dissolve(.3)
                sch1100 "What are you doing, stupid?"
                sch1100 "..................."
                hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            "-Grope her tits-":
                ">You reach out and grab one of Iris' tits... The girl keeps on pouring you your wine... Very slowly..."
                ">You start massaging her breast through the transparent fabric of her old veil..."
                ">her hard nipple pokes your palm..."
                sch11_62 "Ok, that's enough, stop it."
                sch11_62 "This is not allowed. Somebody will notice..."
                "Reluctantly you let go of her breast..."
            "-Do nothing-":
                ">You patiently wait for Iris to finish filling your cup."
                show image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
                sch1100 "(Tsk... Whatever...)"
                hide image "04_pt/iris/q5/iris28.png" at center with Dissolve(.3)
        show image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
        sch1100 "So... Do you have the dress?"
        show image im.Flip("04_pt/iris/q5/iris65.png", horizontal=True) at center with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
        sch1100 "Not yet?"
        sch1100 "I see..."
        sch1100 "Oh, well..."
        show image im.Flip("04_pt/iris/q5/iris29.png", horizontal=True) at center with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris65.png", horizontal=True) at center with Dissolve(.3)
        sch1100 "So, what's new with you?"
        hide image im.Flip("04_pt/iris/q5/iris29.png", horizontal=True) at center with Dissolve(.3)
        ">You spend the rest of the night drinking wine and discussing all sorts of things with Iris..."
        hide image "04_pt/slavem/bld2.png" with Dissolve(.3)
        ">Your relationship with Iris didn't change much though..."
        $ vine = renpy.random.randint(30, 50)
        $ gold = gold - vine
        ">You spent [vine] gold on wine tonight."
        ">You return home and go to sleep."
        show image "interface/blackfade.png" with Dissolve(.3)
        pause 1
        jump dayone
label mddate6:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld2.png" behind blkfade
    show image "04_pt/iris/q5/iris75.png" at center behind blkfade
    pause.3
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Er... Good evening, welcome to \"The Blue Bull\"."
    sch1100 "Some wine?..."
    hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
    ">Iris bends over a little and starts to pour wine into your cup rather awkwardly..."
    menu:
        "-Give her butt a squeeze-":
            ">You reach out, put your hand on one of Iris's butt cheeks and give it a good squeeze."
            show image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
            sch1100 ".................."
            hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
        "-Give her butt a slap-":
            $ renpy.play('sounds/slap.mp3')
            show image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
            sch1100 "..................."
            hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
        "-Do nothing-":
            ">You wait for Iris to finish filling your cup."
            show image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
            sch1100 "................."
            hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
    show image im.Flip("04_pt/iris/q5/iris29.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "Thank you again for your help the other day..."
    show image im.Flip("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip("04_pt/iris/q5/iris29.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "Sorry, it's hard for me to concentrate on anything today..."
    show image im.Flip("04_pt/iris/q5/iris24.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip("04_pt/iris/q5/iris23.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "All I can think about is going to see Fat Lily... I'm so nervous...."
    hide image im.Flip("04_pt/iris/q5/iris24.png", horizontal=True) at center with Dissolve(.3)
    menu:
        "\"Did you try the dress on?\"":
            show image im.Flip("04_pt/iris/q5/iris19.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Yes, I did... It's very...  revealing..."
            show image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip("04_pt/iris/q5/iris19.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "It's perfect..."
            hide image im.Flip("04_pt/iris/q5/iris20.png", horizontal=True) at center with Dissolve(.3)
        "\"Did you talk with Lily already?\"":
            show image im.Flip("04_pt/iris/q5/iris75.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "No, not yet..."
            hide image im.Flip("04_pt/iris/q5/iris75.png", horizontal=True) at center with Dissolve(.3)
        "\"Did you talk to your father yet?\"":
            show image im.Flip("04_pt/iris/q5/iris21.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "My father? What are you talking about?"
            show image im.Flip("04_pt/iris/q5/iris22.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip("04_pt/iris/q5/iris21.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "My father must be the last one to find out about all of this."
            hide image im.Flip("04_pt/iris/q5/iris22.png", horizontal=True) at center with Dissolve(.3)
    show image "04_pt/iris/q5/iris77.png" at center with Dissolve(.3)
    sch1100 "I want to go talk with Fat Lily tonight..."
    sch1100 "Discuss all the details of my future employment..."
    hide image "04_pt/iris/q5/iris77.png" at center with Dissolve(.3)
    show image "04_pt/iris/q5/iris26.png" at right with Dissolve(.3)
    menu:
        sch1100 "Care to accompany me?"
        "Quest: \"The dream job\"":
            if onquest:
                    "You need to complete the current quest first in order to take on a new one."
                    sch1100 "Oh, I see..."
                    hide image "04_pt/iris/q5/iris26.png" at right with Dissolve(.3)
                    "Your relationship with Iris is stuck in a rut."
                    $ vine = renpy.random.randint(30, 50)
                    $ gold = gold - vine
                    "You spent [vine] gold on wine tonight."
                    "You return home and go to sleep."
                    show image "interface/blackfade.png" with Dissolve(.3)
                    pause 1
                    jump dayone
            else:
                hide image "04_pt/iris/q5/iris26.png" at right with Dissolve(.3)
                show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
                sch1100 "Great, meet me at our usual spot."
                sch1100 "I need to get back to work now..."
                sch1100 "I will see you later, ok?"
                hide image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
                show image "04_pt/slavem/qstart.png" with Dissolve(.3)
                show image "04_pt/slavem/onaquest.png" with Dissolve(.3)
                show con1 at right
                show ctc7 at right
                pause 
                hide con1
                hide ctc7
                hide image "04_pt/slavem/qstart.png" with Dissolve(.3)
                ">You spend the rest of the night drinking wine in the tavern..."
                $ mdaughterfriendship += 1
                $ vine = renpy.random.randint(30, 50)
                $ gold = gold - vine
                $ onquest = True
                ">You spent [vine] gold on wine tonight."
                ">You leave the tavern."
                play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                $ renpy.play('sounds/door2.mp3')
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                show blkfade with Dissolve(.3)
                pause.7
                hide blkfade with Dissolve(.3)
                show image "04_pt/slavem/bld2.png" with Dissolve(.3)
                show image "04_pt/iris/q5/iris78.png" at center with Dissolve(.3)
                sch1100 "Did I keep you waiting? Sorry about that."
                show image "04_pt/iris/q5/iris79.png" at center with Dissolve(.3)
                hide image "04_pt/iris/q5/iris78.png" at center with Dissolve(.3)
                sch1100 "I had to make sure father didn't notice me sneaking out..."
                show image "04_pt/iris/q5/iris78.png" at center with Dissolve(.3)
                hide image "04_pt/iris/q5/iris79.png" at center with Dissolve(.3)
                sch1100 "Let's go?"
                show blkfade with Dissolve(.3)
                hide image "04_pt/slavem/bld2.png" 
                hide image "04_pt/iris/q5/iris78.png" 
                pause.7
                hide blkfade with Dissolve(.3)
                show con1 at right
                show ctc7 at right
                pause 
                hide con1
                hide ctc7
                play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
                $ renpy.play('sounds/door.mp3')
                show image "04_pt/slavem/bld.png" with Dissolve(.3)
                show image "04_pt/slavem/bld2.png" with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "Good evening and welcome to \"the red phoenix\"."
                show image im.Flip("04_pt/iris/q5/iris80.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "Good evening..."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "Iris? What are you doing here my girl?"
                show image im.Flip("04_pt/iris/q5/iris81.png", horizontal=True) at left with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris80.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "I... ehm... well.... I......."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "Did your father do something stupid again?"
                sch300 "Please, please come on in. Take off your cloak and tell aunt Lily what happened..."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris81.png", horizontal=True) at left with Dissolve(.3)
                show image im.Flip("04_pt/iris/q5/iris81.png", horizontal=True) at center with Dissolve(.3)
                sch1100 "....................."
                hide image im.Flip("04_pt/iris/q5/iris81.png", horizontal=True) at center with Dissolve(.3)
                show image im.Flip("04_pt/iris/q5/iris82.png", horizontal=True) at center with Dissolve(.3)
                show con1 at right
                show ctc7 at right
                pause 
                hide con1
                hide ctc7
                sch1100 "....................."
                show image "04_pt/lola/q5/lola01.png" at right with Dissolve(.3)
                sch1000 "Wow, Iris, you look beautiful!!!"
                hide image im.Flip("04_pt/iris/q5/iris82.png", horizontal=True) at center with Dissolve(.3)
                show image im.Flip("04_pt/iris/q5/iris83.png", horizontal=True) at left with Dissolve(.3)
                sch1000 "You really think so, Lola?"
                show image "04_pt/lola/q5/lola02.png" at right with Dissolve(.3)
                hide image "04_pt/lola/q5/lola01.png" at right with Dissolve(.3)
                sch1000 "Mom, is Iris gonna work here now?"
                hide image "04_pt/lola/q5/lola02.png" at right with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "I should hope so..."
                sch300 "Iris, my girl, I always knew you were pretty..."
                sch300 "But in this dress you're simply stunning..."
                show image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at left with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris83.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "Thank you..."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "If only I were at least 30 years younger..."
                sch300 "And had a cock!"
                sch300 "I would mount you and ride you so hard that you wouldn't be able to sit on your tiny little butt for a week!"
                show image im.Flip("04_pt/iris/q5/iris85.png", horizontal=True) at left with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "Err... Thank you... I guess..."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "quest05/lily02.png" at right with Dissolve(.3)
                sch300 "What do you say, old man?"
                sch300 "How much would you be willing to pay to dip your cock into this wild kitty?"
                show image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris85.png", horizontal=True) at left with Dissolve(.3)
                sch1100 ".................."
                hide image "quest05/lily02.png" at right with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
                menu:
                    "\"One gold coin.\"":
                        show image im.Flip("04_pt/iris/q5/iris87.png", horizontal=True) at left with Dissolve(.3)
                        sch1100 "What? Only one coin?"
                        show image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "That's alright darling..."
                        sch300 "He means that you look like a cheap whore..."
                        sch300 "And in this business \"cheap whores\" are not cheap at all and make the most money."
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        show image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
                        sch1000 "Yes, everyone knows that."
                        show image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris87.png", horizontal=True) at left with Dissolve(.3)
                        sch1100 "Really? I had no idea..."
                        hide image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                        hide image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
                    "\"50 gold coins.\"":
                        show image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                        sch1100 "That's not very much..."
                        show image "04_pt/lola/q5/lola05.png" at right with Dissolve(.3)
                        sch1000 "Cheapo!" 
                        hide image "04_pt/lola/q5/lola05.png" at right with Dissolve(.3)
                        show image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "Don't listen to him darling. He obviously doesn't know what he is talking about..."
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                    "\"1000 gold coins.\"":
                        show image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                        sch1100 "Really? Are you serious?"
                        show image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
                        sch1000 "Yes, yes, big money!"
                        hide image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
                        show image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "You see, darling? You will be very popular, I promise you that."
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                    "\"All of my money.\"":
                        show image im.Flip("04_pt/iris/q5/iris87.png", horizontal=True) at left with Dissolve(.3)
                        sch1100 "Hey, are you making fun of me?"
                        show image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
                        sch1000 "I don't think so, Iris. You are very pretty!"
                        show image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris87.png", horizontal=True) at left with Dissolve(.3)
                        sch1100 ".....................really?"
                        hide image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
                        show image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "Indeed... Many, many men will gladly part with their gold to spend a night with you..."
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
                                        
                    
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "Alright, girl, now I need to see what you are hiding under that dress."
                show image im.Flip("04_pt/iris/q5/iris83.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "Em..... Of course...."
                show image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris83.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "......................................."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "quest05/lily02.png" at right with Dissolve(.3)
                sch300 "What are you waiting for old man? Give us some privacy, would you?"
                menu:
                    "-(Turn around.)-":
                        ">You turn around and close your eyes."
                        show blkfade with Dissolve(.7)
                        hide image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
                        hide image "quest05/lily02.png" at right 
                        sch1100 "............."
                        sch1100 "............."
                        sch300 "Yes, yes! Look at those tits! You will be very popular for sure!"
                        sch1000 "I love your little tattoo down there, Iris..."
                        sch1000 "I want one like that, mom..."
                        sch300 "I don't think so, darling..."
                        sch1000 "..............."
                        sch300 "You can put your dress back on now, Iris dear."
                        hide blkfade with Dissolve(.7)
                    "-(Keep watching.)-":
                        hide image "quest05/lily02.png" at right with Dissolve(.3)
                        show image "quest05/lily02.png" at right with Dissolve(.3)
                        sch300 "Didn't you hear what I said, dear?"
                        show image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at left with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
                        sch1100 "That's OK, he can watch..."
                        hide image "quest05/lily02.png" at right with Dissolve(.3)
                        show image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "As you wish..."
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at left with Dissolve(.3)
                        show image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at center with Dissolve(.3)
                        sch1100 "............."
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        show image im.Flip("04_pt/iris/q5/iris90.png", horizontal=True) at center 
                        hide image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at center
                        show image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at center
                        hide image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at center with Dissolve(.3)
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        show image im.Flip("04_pt/iris/q5/iris91.png", horizontal=True) at center 
                        hide image im.Flip("04_pt/iris/q5/iris90.png", horizontal=True) at center 
                        show image im.Flip("04_pt/iris/q5/iris90.png", horizontal=True) at center 
                        hide image im.Flip("04_pt/iris/q5/iris90.png", horizontal=True) at center with Dissolve(.5)
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        hide image im.Flip("04_pt/iris/q5/iris91.png", horizontal=True) at center with Dissolve(.3)
                        show image im.Flip("04_pt/iris/q5/iris91.png", horizontal=True) at left with Dissolve(.3)
                        sch1100 "............."
                        show image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "Would you look at those tits! You will be very popular for sure!"
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        show image "04_pt/lola/q5/lola06.png" at right with Dissolve(.3)
                        sch1000 "I love your little tattoo down there, Iris..."
                        show image "04_pt/lola/q5/lola02.png" at right with Dissolve(.3)
                        hide image "04_pt/lola/q5/lola06.png" at right with Dissolve(.3)
                        sch1000 "I want one like that, mom..."
                        hide image "04_pt/lola/q5/lola02.png" at right with Dissolve(.3)
                        show image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "I don't think so, darling..."
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        show image "04_pt/lola/q5/lola07.png" at right with Dissolve(.3)
                        sch1000 "..............."
                        hide image "04_pt/lola/q5/lola07.png" at right with Dissolve(.3)
                        show image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "You can put your dress back on now, Iris dear."
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris91.png", horizontal=True) at left with Dissolve(.3)

                
                
                
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "This is great... You will make me a fortune, girl..."
                show image im.Flip("04_pt/iris/q5/iris83.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "........................."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "So, tell me, how did your father react when you told him you will be working for me now..."
                show image im.Flip("04_pt/iris/q5/iris85.png", horizontal=True) at left with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris83.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "Well, actually I didn't tell him yet..."
                sch1100 "I'm kinda keeping this a secret from him..."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
                sch1000 "Niiiiiiice!!!"
                hide image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "No, no, no, no, my girl. It does not work like that..."
                sch300 "Your father is a dangerous man... If I don't get his approval for this I can't let you work here, no matter how much I would want to..."
                show image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris85.png", horizontal=True) at left with Dissolve(.3)
                menu:
                    "\"Actually Maslab said it's OK.\"":
                        show image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                        show image "quest05/lily02.png" at right with Dissolve(.3)
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "Did he now....?"
                        hide image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                        hide image "quest05/lily02.png" at right with Dissolve(.3)
                    "\"I'm in charge of her. I say it's OK.\"":
                        show image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                        show image "quest05/lily02.png" at right with Dissolve(.3)
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "You are... in charge of Iris now?"
                        sch300 "Aren't you a slave trainer?"
                        sch300 "So what then, Maslab sold his precious daughter to you?"
                        sch300 "I know that man, he would never do that..."
                        hide image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                        hide image "quest05/lily02.png" at right with Dissolve(.3)
                    "\"I will pay you to employ her.\"":
                        show image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                        hide image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                        show image "quest05/lily02.png" at right with Dissolve(.3)
                        hide image "quest05/lily01.png" at right with Dissolve(.3)
                        sch300 "I bet you would... But no amount of gold is worth dying for, and if I do this behind her old man's back he might actually kill me..." 
                        hide image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
                        hide image "quest05/lily02.png" at right with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "Well, even if your father were to approve of your new career choice I will need some evidence for that..."
                sch300 "I need to hear it from him personally, or at least in a written form..."
                show image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "My father would never approve... Is there nothing you could do?"
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "I'm afraid not, my dear. I can't allow you to work for me until I get the approval from someone of your family..."
                hide image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                show image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "I understand... I'm sorry to have bothered you..."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "quest05/lily01.png" at right with Dissolve(.3)
                sch300 "You never bother me, my dear... I'm sorry I couldn't help you..."
                hide image "quest05/lily01.png" at right with Dissolve(.3)
                show image "04_pt/lola/q5/lola08.png" at right with Dissolve(.3)
                sch1000 "Bye, Iris..."
                show image im.Flip("04_pt/iris/q5/iris82.png", horizontal=True) at left with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris89.png", horizontal=True) at left with Dissolve(.3)
                sch1100 "Goodnight, lola."
                show blkfade with Dissolve(.3)
                hide image "04_pt/lola/q5/lola08.png" at right with Dissolve(.3)
                hide image im.Flip("04_pt/iris/q5/iris82.png", horizontal=True) at left with Dissolve(.3)
                hide image "04_pt/slavem/bld.png" 
                pause.7
                hide blkfade with Dissolve(.3)
                stop music fadeout 1
                #play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                $ renpy.play('sounds/door2.mp3')
                show image "04_pt/slavem/bld2.png"
                show image "04_pt/iris/q5/iris92.png" at center with Dissolve(.3)
                sch1100 "So what am I supposed to do now....?"
                sch1100 "I made you get this silly dress for me, and it was all for nothing..."
                sch1100 "I feel so embarrassed."
                show image "04_pt/iris/q5/iris93.png" at center with Dissolve(.3)
                hide image "04_pt/iris/q5/iris92.png" at center with Dissolve(.3)
                sch1100 "Me and my stupid dreams... I should just give up..."
                hide image "04_pt/iris/q5/iris93.png" at center with Dissolve(.3)
                play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1 #SAD
                menu:
                    "\"It's alright to dream.\"":
                        show image "04_pt/iris/q5/iris94.png" at center with Dissolve(.3)
                        sch1100 "You think?"
                        sch1100 "And I think it's time for me to face reality..."
                        hide image "04_pt/iris/q5/iris93.png" at center with Dissolve(.3)
                    "\"Yeah, you should give up.\"":
                        show image "04_pt/iris/q5/iris92.png" at center with Dissolve(.3)
                        sch1100 "Yes, I think so too..."
                        sch1100 "I think it's time for me to face reality..."
                        hide image "04_pt/iris/q5/iris94.png" at center with Dissolve(.3)
                    "\"Be my personal whore?\"":
                        show image "04_pt/iris/q5/iris93.png" at center with Dissolve(.3)
                        sch1100 "You are sweet.... Thank you..."
                        show image "04_pt/iris/q5/iris94.png" at center with Dissolve(.3)
                        hide image "04_pt/iris/q5/iris93.png" at center with Dissolve(.3)
                        sch1100 "But I don't want your pity..."
                        sch1100 "It is time for me to face reality..."
                        hide image "04_pt/iris/q5/iris94.png" at center with Dissolve(.3)
                
                show image "04_pt/iris/q5/iris92.png" at center with Dissolve(.3)
                sch1100 "I thought I could be a whore... Live a life of luxury and excitement..."
                sch1100 "But all I will ever be is a waitress..."
                show image "04_pt/iris/q5/iris96.png" at center with Dissolve(.3)
                hide image "04_pt/iris/q5/iris92.png" at center with Dissolve(.3)
                sch1100 "How could I even think for a minute that this could actually happen...*sob*"
                sch1100 "I'm an ex-criminal, what do I know about being a man-pleaser? *sob*"
                sch1100 "And my scar... *sob* Who would ever want to sleep with me?"
                show image "04_pt/iris/q5/iris95.png" at center with Dissolve(.3)
                hide image "04_pt/iris/q5/iris96.png" at center with Dissolve(.3)
                sch1100 "Sorry, I need to go now, I want to take this stupid dress off and burn it!"
                hide image "04_pt/iris/q5/iris94.png" 
                sch1100 "Thank you for your help, and sorry..."
                hide image "04_pt/iris/q5/iris95.png" at center with Dissolve(.3)
                $ renpy.play('sounds/iris_run.mp3')
                show con1 at right
                show ctc7 at right
                pause 
                hide con1
                hide ctc7
                ">You feel bad for Iris, but there is nothing you can do..."
                show blkfade with Dissolve(.3)
                hide image "04_pt/slavem/bld2.png" 
                pause.7
                
                ">You decide to call it a night."
                $ quest6 += 1
                pause 1
                jump dayone
                
        "\"Maybe next time.\"":
            hide image "04_pt/iris/q5/iris26.png" at right with Dissolve(.3)
            show image "04_pt/iris/q5/iris27.png" at right with Dissolve(.3)
            sch1100 "Oh, I see..."
            hide image "04_pt/iris/q5/iris27.png" at right with Dissolve(.3)
            ">Your relationship with Iris is stuck in a rut."
            $ vine = renpy.random.randint(30, 50)
            $ gold = gold - vine
            ">You spent [vine] gold on wine tonight."
            ">You return home and go to sleep."
            show image "interface/blackfade.png" with Dissolve(.3)
            pause 1
            jump dayone
label mddate7:
    if quest6 == 2:
        play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
        show blkfade with Dissolve(.3)
        show image "04_pt/slavem/bld2.png" behind blkfade
        show image "04_pt/iris/q5/iris75.png" at center behind blkfade
        pause.3
        hide blkfade with Dissolve(.5)
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        sch1100 "Good evening, welcome to \"The Blue Bull\"."
        sch1100 "Wine?..."
        hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
        menu:
            "-Give her butt a squeeze-":
                show image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
                sch1100 "Even being groped like that doesn't make me feel better anymore..."
                sch1100 "What has become of me..."
                hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
                show image "04_pt/iris/q5/iris29.png" at center with Dissolve(.3)
                sch1100 "Huh? What is that piece of parchment in your hand?"
                hide image "04_pt/iris/q5/iris29.png" at center with Dissolve(.3)
            "-Give her butt a slap-":
                $ renpy.play('sounds/slap.mp3')
                show image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
                with hpunch
                sch1100 "You spanking my butt like this in front of everyone... Normally that would excite me so much..."
                sch1100 "But lately I just feel like I don't care..."
                hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
                show image "04_pt/iris/q5/iris29.png" at center with Dissolve(.3)
                sch1100 "Huh? What is that piece of parchment in your hand?"
                hide image "04_pt/iris/q5/iris29.png" at center with Dissolve(.3)
            "-Give her the signed permission-":
                show image "04_pt/iris/q5/iris29.png" at center with Dissolve(.3)
                sch1100 "Huh? What is this piece of parchment?"
                hide image "04_pt/iris/q5/iris29.png" at center with Dissolve(.3)
        show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
        show image "04_pt/slavem/boxpermission.png" with moveinleft
        ">You give the permission signed by Balsam to Iris."
        hide image "04_pt/slavem/boxpermission.png" with moveoutright
        hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
        ">Iris is reading the paper intently..."
        show image "04_pt/iris/q5/iris14.png" at center with Dissolve(.3)
        sch1100 "Oh my god! I can't believe this!"
        show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris14.png" at center with Dissolve(.3)
        sch1100 "My uncle! Well of course! Why didn't I come up with that myself!?"
        sch1100 "You know what this means, don't you?!"
        show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
        sch1100 "We are going to see Fat Lily again tonight!"
        show image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
        sch1100 "With this paper in my hand she won't be able to refuse me!!!"
        sch1100 "Oh, my god! I'm so happy! I can't wait!!!"
        show image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris19.png" at center with Dissolve(.3)
        sch1100 "Let me pour you some more wine, and while I do that you grab my ass, OK?"
        hide image "04_pt/iris/q5/iris18.png" at center with Dissolve(.3)
        ">You reach out and start molesting Iris' butt, while she pours wine into your cup."
        show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
        sch1100 "This feels great! I can enjoy life again! Thank you so much!"
        show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
        sch1100 "Alright, now I will pretend to wipe your table and you grab my tits, and squeeze and pull on them and.... em, be rough with them OK?"
        hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
        ">Iris bends over again and pretends to wipe your table..."
        ">You grab both of her tits and squeeze them with force..."
        sch11_62 "Yes... Yes... Like this..."
        ">You spend the rest of the evening playing all sorts of exciting \"games\" with Iris right under everyone's noses..."
        show blkfade with Dissolve(.5)
        hide image "04_pt/slavem/bld2.png" 
        $ vine = renpy.random.randint(30, 50)
        $ gold = gold - vine
        ">You spent [vine] gold coins on wine tonight."
        play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
        pause 1
        hide blkfade with Dissolve(.5)
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        show image "04_pt/slavem/bld2.png" with Dissolve(.3)
        show image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)             
        sch1100 "Are you ready to go?"
        show image "04_pt/iris/q5/iris97.png" at center with Dissolve(.3)     
        hide image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)          
        sch1100 "Wait, how do I look?"
        hide image "04_pt/iris/q5/iris97.png" at center with Dissolve(.3)    
        menu:
            "\"You are beautiful.\"":
                show image "04_pt/iris/q5/iris98.png" at center with Dissolve(.3)  
                sch1100 "Yeah, right... whatever..."
                sch1100 "Let's go..."
                hide image "04_pt/iris/q5/iris98.png" at center with Dissolve(.3)  
            "\"Like a whore.\"":
                show image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)  
                sch1100 "Aw... You're so sweet!"
                sch1100 "Alright, let's go!"
                hide image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3) 
            "\"You look cute.\"":
                show image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)  
                sch1100 "Em... That's not the look I was going for, but thanks, I guess..."
                sch1100 "Let's go?"
                hide image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)
                hide image "04_pt/slavem/bld2.png" 
        show blkfade with Dissolve(.5)
        pause.5
        play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
        $ renpy.play('sounds/door.mp3')
        hide blkfade with Dissolve(.5)
        show image "04_pt/slavem/bld.png"
        show image "04_pt/slavem/bld2.png" 
        show image "quest05/lily01.png" at right with Dissolve(.3)
        sch300 "Good evening and welcome to \"the red phoenix\"."
        hide image "quest05/lily01.png" at right with Dissolve(.3)
        show image "04_pt/lola/q5/lola06.png" at right with Dissolve(.3)
        sch1000 "Hey Iris!"
        show image im.Flip("04_pt/iris/q5/iris85.png", horizontal=True) at left with Dissolve(.3)
        sch1100 "Hi there, Lola."
        hide image "04_pt/lola/q5/lola06.png" at right with Dissolve(.3)
        show image "quest05/lily01.png" at right with Dissolve(.3)
        sch300 "Iris, my girl, what are you doing here again wearing that dress?"
        sch300 "Wait, don't tell me... Your father finally came to his senses?"
        show image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris85.png", horizontal=True) at left with Dissolve(.3)
        sch1100 "Well... Not really... But I do have a written permission from a member of my family."
        hide image "quest05/lily01.png" at right with Dissolve(.3)
        show image "quest05/lily01.png" at right with Dissolve(.3)
        sch300 "What? Let me see?"
        hide image "quest05/lily01.png" at right with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
        show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
        show image "04_pt/slavem/boxpermission.png" with moveinleft
        ">Iris hands over the permission signed by Balsam to Lily."
        hide image "04_pt/slavem/boxpermission.png" with moveoutright
        hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
        show image "quest05/lily01.png" at right with Dissolve(.3)
        sch300 "Well I be damned..."
        sch300 "Your father might still kill me for this, but with this paper in my hands I'm at least not breaking any laws by giving you the job."
        show image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
        sch1100 "You mean I can work at your brothel now? Are you serious?"
        sch300 "Yes, my girl!"
        hide image "quest05/lily01.png" at right with Dissolve(.3)
        show image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
        sch1000 "Congrats, sister!"
        show image im.Flip("04_pt/iris/q5/iris83.png", horizontal=True) at left with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
        sch1100 "I cannot believe this! When can I start working?"
        hide image "04_pt/lola/q5/lola03.png" at right with Dissolve(.3)
        show image "quest05/lily01.png" at right with Dissolve(.3)
        sch300 "Whenever you want, dear. You can start right away if you want to."
        show image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris83.png", horizontal=True) at left with Dissolve(.3)
        sch1100 "Right now?"
        show image "quest05/lily02.png" at right with Dissolve(.3)
        hide image "quest05/lily01.png" at right with Dissolve(.3)
        sch300 "Why not? I'm sure your friend over there will gladly become your first client."
        show image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris83.png", horizontal=True) at left with Dissolve(.3)
        sch1100 "What...? B-but... Em..."
        sch1100 "er... I think this is enough excitement for for me today..."
        show image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at left with Dissolve(.3)
        hide image im.Flip("04_pt/iris/q5/iris86.png", horizontal=True) at left with Dissolve(.3)
        sch1100 "I need some time to process all of this..."
        show image "quest05/lily01.png" at right with Dissolve(.3)
        hide image "quest05/lily02.png" at right with Dissolve(.3)
        sch300 "Of course, take all the time you need..."
        show blkfade with Dissolve(.6)
        $ renpy.play('sounds/door2.mp3')
        hide image im.Flip("04_pt/iris/q5/iris84.png", horizontal=True) at left 
        hide image im.Flip("04_pt/iris/q5/iris88.png", horizontal=True) at left
        hide image "quest05/lily01.png" at right 
        pause 1
        hide image "04_pt/slavem/bld.png" 
        hide image "04_pt/slavem/bld2.png" 
        hide blkfade with Dissolve(.6)
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        show image "04_pt/slavem/bld2.png" with Dissolve(.3)
        show image "04_pt/iris/q5/iris97.png" at center with Dissolve(.3)
        play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
        sch1100 "I can't believe this is actually happening..."
        sch1100 "I'm so scared for some reason..."
        show image "04_pt/iris/q5/iris98.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris97.png" at center with Dissolve(.3)
        sch1100 "So silly... I always say that i'm pretty much fearless, and now I'm scared..."
        sch1100 "What a silly girl I am..."
        show image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris98.png" at center with Dissolve(.3)
        sch1100 "Wait a second, this is what it is... I feel like an ordinary girl..."
        sch1100 "A bit insecure, a bit uncertain about everything... And yet so wonderful..."
        show image "04_pt/iris/q5/iris97.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)
        sch1100 "Thank you for everything... I need to go home now..."
        show image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)
        hide image "04_pt/iris/q5/iris97.png" at center with Dissolve(.3)
        sch1100 "But before I do...."
        hide image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)
        pause.5
        $ renpy.play('sounds/kiss.mp3')
        with kissiris
        ">Iris gives you a kiss..."
        show image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)
        sch1100 "See you soon?"
        hide image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)
        $ mdaughterfriendship += 1
        $ onquest = False
        $ renpy.play('sounds/win2.mp3')
        show image "04_pt/slavem/bld.png" 
        hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
        show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
        show con1 at right
        show ctc7 at right
        pause
        hide con1
        hide ctc7
        ">Your relationship with Iris reached its maximum level."
        ">Starting tomorrow, if she is not taking a day off Iris will be working at her father's tavern..."
        ">But sometimes she will also be working as a whore in \"The Red Phoenix\"."
        hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
        ">You return home and go to sleep."
        show image "interface/blackfade.png" with Dissolve(.3)
        $ quest6 += 1
        $ quest6complete = True
        pause 1
        jump dayone
    else:
        play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
        show blkfade with Dissolve(.3)
        show image "04_pt/slavem/bld2.png" behind blkfade
        show image "04_pt/iris/q5/iris75.png" at center behind blkfade
        pause.3
        hide blkfade with Dissolve(.5)
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        sch1100 "Good evening, welcome to \"The Blue Bull\"."
        sch1100 "Wine?..."
        hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
        "Iris pours you some wine..."
        menu:
            "(Give her butt a squeeze.)":
                "You reach out, put your hand on one of Iris's butt cheeks and give it a good squeeze."
                show image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
                sch1100 "I appreciate you trying to make me feel better, but it won't work, sorry..."
                hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
            "(Give her butt a slap.)":
                $ renpy.play('sounds/slap.mp3')
                show image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
                sch1100 "Hey, don't... I feel awful today..."
                hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
            "Are you alright?":
                show image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
                sch1100 "What do you think?"
                sch1100 "I feel awful, but I will get better, just give me some time..."
                hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
            "(Do nothing.)":
                show image "04_pt/iris/q5/iris76.png" at center with Dissolve(.3)
                sch1100".............................."
                show image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
                hide image "04_pt/iris/q5/iris76.png" at center with Dissolve(.3)
                sch1100 "................."
                hide image "04_pt/iris/q5/iris75.png" at center with Dissolve(.3)
        show image "04_pt/iris/q5/iris07.png" at center with Dissolve(.3)
        sch1100 "So, what's new with you...?"
        show blkfade with Dissolve(.3)
        ">You spend the rest of the evening drinking wine and talking with Iris."
        ">She were doing her best to act normal, but you could see that she is still very upset..."

        ">Your relationship with Iris didn't change much."
        $ vine = renpy.random.randint(30, 50)
        $ gold = gold - vine
        ">You spent [vine] gold on wine tonight."
        pause 1
        jump dayone
label mddate8:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld2.png" behind blkfade
    show image "04_pt/iris/q5/iris17.png" at center behind blkfade
    pause.3
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Good evening, welcome to \"The Blue Bull\"."
    hide image "04_pt/iris/q5/iris17.png" at center with Dissolve(.3)
    ">Iris bends over a little and pours wine into your cup..."
    menu:
        "-Give her butt a squeeze-":
            show image "04_pt/iris/q5/iris24.png" at center with Dissolve(.3)
            sch1100 "I gotta thank you..."
            sch1100 "By grabbing my butt in front of everyone like that, you set an example..."
            show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris24.png" at center with Dissolve(.3)
            sch1100 "Now everyone is doing it to me, and father doesn't even bother to stop this..."
            show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            sch1100 "And it feels so great..."
            sch1100 "It's like as soon as my shift starts my little butt get's a non-stop massage..."
            hide image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
        "-Give her butt a slap-":
            $ renpy.play('sounds/slap.mp3')
            with hpunch
            show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
            sch1100 "Hey, listen, I would appreciate it if you could stop doing this every time you come here..."
            show image "04_pt/iris/q5/iris23.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
            sch1100 "Don't get me wrong, I do enjoy it..."
            show image "04_pt/iris/q5/iris24.png" at center with Dissolve(.3)
            hide image "04_pt/iris/q5/iris23.png" at center with Dissolve(.3)
            sch1100 "But since I'm also working in a brothel now, I want to be on my best behavior when I'm around my father..."
            hide image "04_pt/iris/q5/iris24.png" at center with Dissolve(.3)
        "-Do nothing-":
            show image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
            sch1100 "Yes, good. I don't want to attract unnecessary attention from my father..."
            hide image "04_pt/iris/q5/iris26.png" at center with Dissolve(.3)
    show image "04_pt/iris/q5/iris20.png" at center with Dissolve(.3)
    sch1100 "So, anyways, what's new with you?"
    show blkfade with Dissolve(.5)
    ">You spend the rest of the night drinking wine and having a lively discussion with Iris."
    ">Iris seems to be in exceptionally good mood."
    ">Your relationship with Iris is at a maximum level."
    $ vine = renpy.random.randint(30, 50)
    $ gold = gold - vine
    ">You spent [vine] gold on wine tonight."
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayone    