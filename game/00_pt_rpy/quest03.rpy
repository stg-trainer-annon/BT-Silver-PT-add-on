label quest3starts:
    if onquest:
        ">You need to complete your current quest first in order to take on a new one."
        jump tavern2
    else:
        show image "interface/blackfade.png"
        with Dissolve(.3)
        pause.5
        hide image "interface/blackfade.png"
        with Dissolve(.3)
        sch6 "Hello, friend."
        sch6 "Listen, you mentioned the other day that you own a slave-girl?"
        menu:
            sch6 "Say, is the wench cute?"
            "\"Hm... I guess...\"":
                sch6 "Hm... You didn't sound very confident..."
                sch6 "Is she that ugly?"
            "\"Not cute. Beautiful rather...\"":
                sch6 "Really? Even better!!"
            "\"Not so much... Why?\"":
                sch6 "Well, as long as she is not ugly it should be alright..."
        sch6 "You see, I have a problem..."
        sch6 "Another one of my waitresses got pregnant..."
        sch62 "Again!!"
        sch62 "I swear, at times it feels as if i'm not running a tavern but a full-fledged brothel."
        sch6 "So, if you are interested in employing your girl, there is an opening."
        menu:
            sch6 "Bring her by, later tonight, I will take a look at her."
            "\"Sure. Tonight then.\"":
                sch6 "Great! See you tonight!"
                $ quest300 = False
                $ quest3start = True
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
                hide image "04_pt/slavem/qstart.png" with Dissolve(.3)
                show image "interface/blackfade.png"
                with Dissolve(.3)
                pause.5
                hide image "interface/blackfade.png"
                with Dissolve(.3)
                jump mainmenu
            "\"Not interested.\"":
                sch6 "Well, sooner or later another one of those airheads will get pregnant, and then another one, I'm sure..."
                sch6 "So, if you change your mind you will have another chance..."
                show image "interface/blackfade.png"
                with Dissolve(.3)
                pause.5
                hide image "interface/blackfade.png"
                with Dissolve(.3)
                jump tavern2
###########################################################
label waitress01:
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld.png" behind blkfade
    show image "04_pt/slavem/bld2.png" behind blkfade
    $ renpy.play('sounds/door.mp3')
    hide blkfade with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris17.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "Hi there..."
    show image im.Flip ("04_pt/iris/q1/iris16.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris17.png", horizontal=True) 
    sch1100 "Oh, it's you!"
    sch1100 "Oh, hey, who is the wench?"
    hide image im.Flip ("04_pt/iris/q1/iris16.png", horizontal=True) with Dissolve(.3)
    show image "04_pt/iris/q1/iris16.png" at right with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/outfit/jas11.png", horizontal=True) at left with Dissolve(.3)
    j "\"the wench\"?.....{p}How dare you--"
    with hpunch
    g4 "She is nobody!"
    j "..............."
    hide image "04_pt/iris/q1/iris16.png" at right with Dissolve(.3)
    show image "04_pt/iris/q1/iris18.png" at center with Dissolve(.3)
    sch1100 "Nobody, huh?..."
    show image im.Flip ("04_pt/jasmine/outfit/jas15.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/outfit/jas11.png", horizontal=True) 
    j "........................."
    sch1100 "..........................."
    hide emom
    hide sal 
    hide image im.Flip ("04_pt/jasmine/outfit/jas15.png", horizontal=True) with Dissolve(.3)
    show image "04_pt/iris/q1/iris16.png" at center with Dissolve(.3) 
    hide image "04_pt/iris/q1/iris18.png" 
    sch1100 "Well, in any case, you came to see my father, right?{p}He is over there, at his usual spot."
    show blkfade with Dissolve(.3)
    hide image "04_pt/iris/q1/iris16.png" with Dissolve(.3)
    show image "quest01/maslab01.png" at right behind blkfade
    hide blkfade with Dissolve(.3)
    sch600 "Good evening, my friend."
    sch600 "This is the girl, I presume?"
    show image im.Flip ("04_pt/jasmine/outfit/jas15.png", horizontal=True) at left with Dissolve(.3)
    j "............"
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Hm..."
    sch600 "I need to see what she is hiding under those robes... {p}Disrobe, girl."
    show image im.Flip ("04_pt/jasmine/outfit/jas11.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/outfit/jas15.png", horizontal=True) at left with Dissolve(.3)
    j "What?!"
    hide sur 
    hide image "emotions/emo01.png" 
    m "Do as he says."
    j ".................{p}.......Fine."
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/outfit/jas11.png", horizontal=True) with Dissolve(.5)
    pause 1
    show image im.Flip ("04_pt/jasmine/outfit/jas01.png", horizontal=True) at center with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide sal
    hide image "emotions/emo01.png"
    hide image im.Flip ("04_pt/jasmine/outfit/jas01.png", horizontal=True) at center with Dissolve(.3)
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    sch600 "By the havens, she is a beauty, isn't she?"
    sch600 "What is your name, girl?"
    show image "04_pt/jasmine/q1/jas02.png" at left with Dissolve(.3)
    j "\"Girl\"??!"
    j "My name is Ja--"
    with hpunch
    g4 "{size=+7}--sper!{/size}"
    show image "04_pt/jasmine/q1/jas03.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas02.png" 
    j "What?"
    m "Yes, her name is Jasper. Isn't that right girl?"
    m "Jasper wants to be a tavern wench, don't you Jasper?"
    hide sur 
    hide image "emotions/emo01.png" 
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas03.png" at left with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/q1/jas03.png", horizontal=True) at center with Dissolve(.5)
    j "But... I...?"
    g4 "Think about it, Jasper!"
    g4 "Only a peasant girl would agree to work here. And this particular peasant girl's name is Jasper!"
    hide image im.Flip ("04_pt/jasmine/q1/jas03.png", horizontal=True) at center with Dissolve(.5)
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    sch600 "Hm...?"
    show image "04_pt/jasmine/q1/jas03.png" at left with Dissolve(.3)
    j "......"
    show image "04_pt/jasmine/q1/jas04.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas03.png" 
    j "That's right master. My name is Jasper."
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Heh... Well, here in my tavern you can be called anything you want, girl."
    sch600 "You can be \"Cristal\", or \"Dew\" or \"Velvet Sky\" or \"Sunshine\"..."
    show image "04_pt/jasmine/q1/jas05.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas04.png"
    j "Very tempting..."
    show image "04_pt/jasmine/q1/jas04.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas05.png"
    j "(Although anything would be better than \"Jasper\"...)"
    sch600 "Do you know how to serve drinks, girl?"
    show image "04_pt/jasmine/q1/jas05.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas04.png"
    j "I'm not sure...."
    sch600 "Well, let's see then."
    hide image "04_pt/jasmine/q1/jas05.png" at left with Dissolve(.5)
    sch600 "Iris! Iris, where are you, my ungrateful daughter."
    show image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) at left with Dissolve(.5)
    sch1100 "I'm here, father."
    sch600 "Iris, this girl's name is Jasper."
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    sch1100 "Hello again..."
    show image im.Flip ("04_pt/jasmine/q1/jas05.png", horizontal=True) at right with Dissolve(.3)
    j "{size=-3}.........................{/size}"
    hide image im.Flip ("04_pt/jasmine/q1/jas05.png", horizontal=True) at right with Dissolve(.3)
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    sch600 "If all goes well Jasper will be replacing that whore, Fatima, as our new waitress."
    sch1100 "I see..."
    sch600 "I want you, Iris to train Jasper. Show her how to take orders and serve drinks..."
    show image im.Flip ("04_pt/iris/q1/iris04.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True)
    sch1100 "(and how to get groped)."
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    sch600 "What did you say?"
    show image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris04.png", horizontal=True)
    sch1100 "I said I will show her the ropes, father."
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "Exactly! You do that, girl."
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/q1/jas05.png", horizontal=True) at right with Dissolve(.5)
    j ".........................."
    hide image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) with Dissolve(.3)
    show image "04_pt/iris/q1/iris01.png" at left with Dissolve(.3)
    sch1100 "Well, come on... Jasper."
    j ".........."
    j "You can just call me jas."
    sch1100 "Yeah, whatever..."
    hide image "04_pt/iris/q1/iris01.png" at left with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/q1/jas05.png", horizontal=True) at right with Dissolve(.3)
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "So, how about some wine now, my friend?"
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    ">You spend some time at the tavern drinking cheap wine and watching Jasmine work..."
    ">Surprisingly enough she does a terrible job of it... \nJasmine seems very uncomfortable and clumsy."
    ">A few times she gets into an argument with customers who try to grope her butt."
    ">She also drops and breaks a few bottles and even spills the wine on one of the customers once..."
    show image "04_pt/iris/q1/iris02.png" at center with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Father! I don't think you should hire this one! This girl is a menace!"
    hide image "04_pt/iris/q1/iris02.png" at center with Dissolve(.3)
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "What are you talking about, woman?"
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "Look at her? She is a beauty!"
    show image im.Flip ("04_pt/iris/q1/iris02.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "Well, I hate to break it to you, pops, but good looks aren't everything! She is clumsy, unruly and spiteful!"
    sch600 "\"Good looks aren't everything\"? Don't be silly, girl!"
    sch600 "This woman, jasper, will make me rich, I'm telling you! But you need to teach her how to be a proper waitress!"
    $ renpy.play('sounds/drop.mp3')
    with hpunch
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
    ">You hear a loud argument erupt between Jasmine and one of the patrons."
    hide image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris02.png", horizontal=True) at left 
    show image "04_pt/iris/q1/iris02.png" at left with Dissolve(.3)
    sch1100 "You see what I mean?"
    sch600 "Go, take care of that. Offer him some wine on the house if necessary..."
    show image "04_pt/iris/q1/iris05.png" at left with Dissolve(.3)
    hide image "04_pt/iris/q1/iris02.png" at left with Dissolve(.3)
    sch1100 "Tsk... Fine, I will!"
    hide image "04_pt/iris/q1/iris05.png" at left with Dissolve(.3)
    pause.5
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "So.... I do like your girl, but Iris has a point."
    sch600 "If you want her to work as a waitress here, she needs to be properly trained first..."
    sch600 "Iris will train her. Just make sure to bring jasper here during daytime, when there are not so many customers."
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Hey, Jasper, come here, girl."
    show image "04_pt/jasmine/q1/jas05.png" at left with Dissolve(.3)
    j "...................."
    sch600 "So, Jasper, this was your first night as a waitress. What do you make of it?"
    hide image "quest01/maslab02.png" with Dissolve(.3) 
    hide image "04_pt/jasmine/q1/jas05.png" with Dissolve(.3)
    show image "04_pt/jasmine/q1/jas04.png" at center with Dissolve(.3)
    j "Tsk......"
    j "Apparently most of the people in here are incredibly stupid or too drunk to distinguish between a bottle of wine and a woman's buttocks."
    j "Every time one of those filthy peasants try to reach out for the bottle they end up grabbing my butt! This is unacceptable!"
    show image "04_pt/jasmine/q1/jas06.png" at center with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas04.png" at center with Dissolve(.3)
    j "Is it always like this?"
    show image im.Flip ("04_pt/iris/q1/iris18.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "Not always. Sometimes they try to grab your tits too."
    show image "04_pt/jasmine/q1/jas03.png" at center with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas06.png" 
    j "What? It this how all taverns in the city are? I had no idea..."
    hide image "04_pt/jasmine/q1/jas03.png" at center with Dissolve(.3)
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "Iris, bite your tongue! My tavern is a respectable establishment."
    sch1100 "Of course it is, father..."
    show image im.Flip ("04_pt/iris/q1/iris17.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris18.png", horizontal=True) 
    sch1100 "Right until the girls climb the tables and start dancing..."
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "A little dancing never hurt anybody..."
    sch1100 "Oh, really, father? Then why don't you ever let me join them?"
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Are you talking back to me again girl?"
    sch1100 "No, of course not, father."
    sch600 "Good... Now stop saying nonsense and get back to work!"
    sch1100 "Of course, father."
    hide image im.Flip ("04_pt/iris/q1/iris17.png", horizontal=True) 
    show image "04_pt/iris/q1/iris05.png" at left with Dissolve(.3)
    sch1100 "(Right after I finish cleaning up after a clumsy and spoiled cow...)"
    sch1100 "(Who spilled the wine all over the floor because she is too good to stay still while being groped)."
    hide image "quest01/maslab03.png" 
    hide image "04_pt/iris/q1/iris05.png" with Dissolve(.3)
    show image "04_pt/iris/q1/iris05.png" at right with Dissolve(.3)
    show image "04_pt/jasmine/q1/jas07.png" at left with Dissolve(.3)
    j "Huh?"
    hide image "04_pt/iris/q1/iris05.png" at right 
    show image "04_pt/iris/q1/iris19.png" at right with Dissolve(.3)
    sch1100 "Yes, I'm talking about you."
    sch1100 "You act like your are better than the rest of us or something..."
    show image "04_pt/jasmine/q1/jas08.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas07.png" at left 
    play music "music/fight.mp3" fadein 1 fadeout 1 #FIGHT
    j "Well maybe that's because I am, you dirty wench."
    show image "04_pt/iris/q1/iris20.png" at right with Dissolve(.3)
    hide image "04_pt/iris/q1/iris19.png" 
    sch1100 "WHAT?!"
    sch1100 "Who are you calling a dirty wench, you spoiled, little bitch?"
    show image "04_pt/jasmine/q1/jas09.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas08.png" at left
    j "What?!!"
    show image "04_pt/jasmine/q1/jas08.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas09.png" at left
    j "{size=+5}H-how dare you!? I will have you beheaded for this!{/size}"
    g4 "Jasper, you forget--"
    j "{size=+7}You are a bitch! A dirty and filthy peasant whore!{/size}"
    hide image "04_pt/iris/q1/iris20.png" 
    $ renpy.play('sounds/drop.mp3')
    with hpunch
    show image "04_pt/iris/q1/iris21.png" at Position(xpos=150, ypos=0, xanchor=0, yanchor=0) with Dissolve(.3)
    sch1100 "Call me a whore one more time and I will gut you like a pig!"
    hide image "04_pt/jasmine/q1/jas08.png" at left
    show image "04_pt/jasmine/q1/jas05.png" at Position(xpos=-80, ypos=0, xanchor=0, yanchor=0) with Dissolve(.3)
    j "I'm... not afraid of you!"
    stop music fadeout 1
    with vpunch
    with vpunch
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "{size=+7}Iris!{/size}"
    show image "04_pt/iris/q1/iris22.png" at Position(xpos=150, ypos=0, xanchor=0, yanchor=0) with Dissolve(.3)
    hide image "04_pt/iris/q1/iris21.png"
    sch1100 "!!!!!!!!!!!!"
    sch600 "What are these silly talks about damaging the property of my friend here?"
    show image "04_pt/jasmine/q1/jas04.png" at Position(xpos=-80, ypos=0, xanchor=0, yanchor=0) with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas08.png" at left
    j "(Property?!)"
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab BG
    hide image "04_pt/iris/q1/iris22.png"
    show image im.Flip ("04_pt/iris/q1/iris23.png", horizontal=True) at Position(xpos=150, ypos=0, xanchor=0, yanchor=0) with Dissolve(.3)
    sch1100 "I.........."
    sch1100 "I forgot..."
    sch1100 "I'm sorry..."
    sch600 "How many times do I need to tell you: our old life is over! You can't go around harassing people anymore!"
    sch600 "You are embarrassing me infront of my guest, girl!"
    hide image "04_pt/jasmine/q1/jas05.png" 
    hide image "04_pt/jasmine/q1/jas04.png" with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris23.png", horizontal=True) with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris23.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "Oh, I..."
    sch1100 "I'm sorry, father, I didn't think... I....."
    with hpunch
    sch600 "{size=+5}Of course you didn't think! Because your head is full of air!{/size}"
    sch600 "Get back to work, girl. I will deal with you later..."
    hide image im.Flip ("04_pt/iris/q1/iris23.png", horizontal=True) 
    show image "04_pt/iris/q1/iris23.png" at Position(xpos=-80, ypos=0, xanchor=0, yanchor=0) with Dissolve(.3)
    sch1100 "Yes father..."
    sch1100 ".................."
    hide image "04_pt/iris/q1/iris23.png" at Position(xpos=-80, ypos=0, xanchor=0, yanchor=0) with Dissolve(.3)
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "Jasper, are you alright there, girl?"
    sch600 "Don't mind Iris, she would never actually hurt you..."
    show image "04_pt/jasmine/q1/jas07.png" at left with Dissolve(.3)
    j "................................"
    hide image "04_pt/jasmine/q1/jas07.png" with Dissolve(.3)
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    sch600 "So that's that then. Bring your girl here during daytime, and we will train her to be a proper waitress."
    sch600 "Now if you excuse me I need to have a talk with my daughter."
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    show image "04_pt/jasmine/outfit/jas11.png" at center with Dissolve(.3)
    j "I'm ready to go..."
    hide image "04_pt/jasmine/outfit/jas11.png" at center with Dissolve(.3)
    ">You leave the tavern."
    hide image "04_pt/slavem/bld2.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    $ renpy.play('sounds/door2.mp3')
    show con1 at right
    show ctc7 at right
    play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
    pause 
    hide con1
    hide ctc7
    show image im.Flip ("04_pt/jasmine/q1/jas01.png", horizontal=True) at center with Dissolve(.3)
    j "That was terrible! Every customer in this darn tavern is a swine! How dare they touch me?"
    m "........"
    hide image im.Flip ("04_pt/jasmine/q1/jas01.png", horizontal=True)
    show image "04_pt/jasmine/q1/jas01.png" at center with Dissolve(.3)
    j "And that commoner girl..."
    menu:
        j "How dare she to treat me this way? I'm royalty, and she is nothing but a dirty peasant."
        "\"She doesn't know who you are, that's all.\"":
            hide image "04_pt/jasmine/q1/jas01.png" 
            show image im.Flip ("04_pt/jasmine/outfit/jas11.png", horizontal=True) at center with Dissolve(.3)
            j "You're probably right..."
            j "Because if she knew she would tremble with fear and kneel before me, like all the rest of those dirty peasants..."
        "\"You're not royalty anymore, Princess.\"":
            hide image "04_pt/jasmine/q1/jas01.png" 
            show image im.Flip ("04_pt/jasmine/outfit/jas11.png", horizontal=True) at center with Dissolve(.3)
            j "Don't be silly. I might have lost my throne but I am of royal blood! Nothing can change that!"
        "\".......................................\"":
            hide image "04_pt/jasmine/q1/jas01.png" 
            show image im.Flip ("04_pt/jasmine/outfit/jas11.png", horizontal=True) at center with Dissolve(.3)
            j "And by the way, why didn't you say anything when that mad peasant girl threatened me?"
            j "Tsk... Your duty is to keep me from harm... "
            j "I despise Jafar, but I know that he will have you pay dearly, shall any harm come to me while I'm entrusted to your care..."
            j "You better keep that in mind..."
    hide image im.Flip ("04_pt/jasmine/outfit/jas11.png", horizontal=True) 
    show image "04_pt/jasmine/q1/jas01.png" at center with Dissolve(.3)
    j "Alright, I'm getting cold... Take me home now..."
    hide image "04_pt/jasmine/q1/jas01.png" at center with Dissolve(.5)
    $ renpy.play('sounds/door2.mp3')
    show image "04_pt/slavem/bld.png" behind blkfade
    ">You return home and go to sleep."
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayone
#####################################################################################
label waitressfinish:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld.png" behind blkfade
    show image "04_pt/slavem/bld2.png" behind blkfade
    hide rest03
    show image "quest01/maslab01.png" at right behind blkfade
    pause.8
    hide blkfade with Dissolve(.3)
    sch600 "Hello, my friend."
    sch600 "Hello, Jas."
    hide image "quest01/maslab01.png" with Dissolve(.3)
    show image "04_pt/iris/q1/iris27.png" at right with Dissolve(.3)
    sch1100 "Hello, Jas."
    show image "04_pt/jasmine/q1/jas15.png" at left with Dissolve(.3)
    j "Hello, Iris."
    stop music fadeout 2
    j "......................"
    sch1100 "...................."
    show image "04_pt/jasmine/q1/jas16.png" at left 
    j "{size=-5}(Peasant whore!){/size}"
    show image "04_pt/iris/q1/iris32.png" at right 
    sch1100 "{size=-5}(Spoiled slut!){/size}"
    show tension 
    hide image "04_pt/jasmine/q1/jas16.png" at left 
    show image "04_pt/jasmine/q1/jas16.png" at left 
    hide image "04_pt/iris/q1/iris32.png" at right 
    show image "04_pt/iris/q1/iris32.png" at right 
    $ renpy.play('sounds/tension.mp3')
    j "..................."
    sch1100 "................."
    hide tension
    hide image "04_pt/jasmine/q1/jas16.png" 
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab BG
    j "Teh-he-he... Girlfriend..."
    hide image "04_pt/iris/q1/iris32.png" 
    sch1100 "Teh-he-he, bestie..."
    hide image "04_pt/iris/q1/iris27.png" at right with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas15.png" at left with Dissolve(.3)
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "I'm glad you came today, my friend!"
    show image "quest01/maslab04.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Another one of my, not so bright waitresses got herself pregnant, and my tavern is understaffed now..." 
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    hide image "quest01/maslab04.png" at right with Dissolve(.3)
    sch600 "So I say, to hell with training! Your girl is ready!"
    show image "04_pt/jasmine/q1/jas09.png" at left with Dissolve(.3)
    j "What?!"
    show image im.Flip ("04_pt/iris/q1/iris30.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "What?!"
    hide image "04_pt/jasmine/q1/jas09.png" at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris30.png", horizontal=True) at center with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris21.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "Father, she is {size=+5}not ready!{/size}"
    sch1100 "She keeps spilling wine and she refuses to wipe the tables properly!"
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Quiet girl! I decide if she is ready or not, and I say she is!"
    show image im.Flip ("04_pt/iris/q1/iris32.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris21.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "But father!!?"
    show image "quest01/maslab06.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    with hpunch
    sch600 "{size=+7}Iris!{/size}"
    show image im.Flip ("04_pt/iris/q1/iris15.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris32.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "That's so unfair..."
    hide image "quest01/maslab06.png" at right with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris15.png", horizontal=True) at left with Dissolve(.3)
    show image "04_pt/iris/q1/iris15.png" at right with Dissolve(.3)
    sch1100 "Welcome to \"The Blue Bull\", Jas... "
    show image "04_pt/jasmine/q1/jas11.png" at left with Dissolve(.3)
    j "..............."
    show image "04_pt/iris/q1/iris23.png" at right with Dissolve(.3)
    hide image "04_pt/iris/q1/iris15.png" 
    sch1100 "I guess I'm not your mentor anymore then, huh?..."
    sch1100 "Starting today we will be equals..."
    hide image "04_pt/jasmine/q1/jas11.png" at left with Dissolve(.3)
    show image "04_pt/jasmine/q1/jas08.png" at left with Dissolve(.3)
    j "Equals? Me and you?! Don't make me laugh, you vulgar peasant!"
    hide image "04_pt/iris/q1/iris23.png" with Dissolve(.3)
    show image "04_pt/iris/q1/iris21.png" at right with Dissolve(.3)
    sch1100 "You, little!!!"
    hide image "04_pt/jasmine/q1/jas08.png" at left with Dissolve(.3)
    hide image "04_pt/iris/q1/iris21.png" at right with Dissolve(.3)
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "So, it's decided then..."
    sch600 "From now on Jas can work as waitress here."
    sch600 "Don't worry, I will look after her, to make sure she doesn't get pregnant or anything."
    sch600 "Although she will need a proper outfit for the job."
    sch600 "I hear that that Azalea girl has some good dresses in stock, maybe you should pay her visit."
    sch600 "Just let me know when jas will be ready to start, alright?"
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    show image "04_pt/jasmine/q1/jas08.png" at left with Dissolve(.3)
    j "See you soon, you peasant tramp!"
    show image "04_pt/iris/q1/iris21.png" at right with Dissolve(.3)
    sch1100 "(I can hardly wait...)"
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    show blkfade with Dissolve(.8)
    hide image "04_pt/iris/q1/iris21.png"
    hide image "04_pt/jasmine/q1/jas08.png" 
    hide image "04_pt/slavem/bld.png" behind blkfade
    hide image "04_pt/slavem/bld2.png" behind blkfade
    pause 1
    ">You leave the tavern."
    $ renpy.play('sounds/door2.mp3')
    hide blkfade with Dissolve(.3)
    hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
    $ quest3complete = True
    $ quest3start4 = False
    $ onquest = False
    $ idlequest = True
    $ renpy.play('sounds/win2.mp3')
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
    show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    "Now jasmine can work at the tavern as a tavern wench."
    "Also you can now spend your nights at the tavern drinking wine."
    hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    show rest03 with Dissolve(.3)
    jump mainmenu
label waitresstrain2:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld.png" behind blkfade
    show image "04_pt/slavem/bld2.png" behind blkfade
    hide rest03
    show image "quest01/maslab01.png" at right behind blkfade
    pause.8
    hide blkfade with Dissolve(.3)
    sch600 "Hello there, my friend."
    sch600 "And hello there, Jasper... or simply Jas, was it?"
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Iris, where are you, girl?"
    show image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) at left with Dissolve(.3)
    sch600 "I'm here father."
    hide image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris25.png", horizontal=True) at left with Dissolve(.3)
    sch600 "Hello, guys."
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/q1/jas08.png", horizontal=True) at right with Dissolve(.3)
    stop music fadeout 1
    j "Hello, whore!"
    show image im.Flip ("04_pt/iris/q1/iris20.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris25.png", horizontal=True) 
    sch1100 "!!!!!!!?"
    hide image im.Flip ("04_pt/jasmine/q1/jas08.png", horizontal=True) with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/q1/jas05.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "Are you going to teach me how to properly entice clients with my tits again?"
    play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "What.....?"
    hide image im.Flip ("04_pt/iris/q1/iris20.png", horizontal=True) with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris26.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "Jasper... I mean, Jas, what are you talking about, girlfriend?"
    show image im.Flip ("04_pt/jasmine/q1/jas14.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/q1/jas05.png", horizontal=True) 
    j "Yes, let's review what I've learned from you so far, shall we?"
    sch1100 "What are you--?"
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/q1/jas14.png", horizontal=True) with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/q1/jas14.png", horizontal=True) at right with Dissolve(.3)
    j "Let's see..."
    j "If a client is trying to grab my butt I should let him."
    j "If he want's to play with my tits, I should let him."
    j "And if he wants me to touch his... thing..."
    j "I should do it but charge him a little extra..."
    hide image im.Flip ("04_pt/jasmine/q1/jas14.png", horizontal=True) at right with Dissolve(.3)
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "What?!"
    show image im.Flip ("04_pt/jasmine/q1/jas02.png", horizontal=True) at center with Dissolve(.3)
    j "Oh, did I miss anything, Iris, dear?"
    show image im.Flip ("04_pt/iris/q1/iris21.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris26.png", horizontal=True) 
    sch1100 "(Why, you little...)"
    hide image im.Flip ("04_pt/jasmine/q1/jas02.png", horizontal=True) at center with Dissolve(.3)
    sch600 "Iris, is this true?"
    show image im.Flip ("04_pt/iris/q1/iris27.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris21.png", horizontal=True) 
    sch1100 "Of course not, father! She is making this up!"
    show image im.Flip ("04_pt/jasmine/q1/jas06.png", horizontal=True) at center with Dissolve(.3)
    j "Oh, right! I almost forgot! Iris also said that if a client is asking for something called the \"Royal Goblet\" I should immediately call for her."
    hide image im.Flip ("04_pt/jasmine/q1/jas06.png", horizontal=True) at center with Dissolve(.3)
    with vpunch
    sch600 "{size=+5}IRIS!!!?{/size}"
    show image im.Flip ("04_pt/iris/q1/iris28.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris27.png", horizontal=True)
    sch1100 "Father, please, don't listen to this rubbish!"
    sch1100 "She is making this up, I don't even know what a \"Royal Goblet\" is! I swear!"
    with vpunch
    sch600 "{size=+5}Like hell you don't, you lying brat!{/size}"
    sch600 "You know damn well that your mother used to serve the best \"Goblet\" in Agrabah!"
    show image "quest01/maslab05.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "Those were the days..."
    show image im.Flip ("04_pt/iris/q1/iris29.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris28.png", horizontal=True)
    sch1100 "Yes, father, I do know, I'm sorry... But..."
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab05.png" at right with Dissolve(.3)
    sch600 "{size=+5}Quiet, girl!{/size}"
    show image im.Flip ("04_pt/iris/q1/iris30.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris29.png", horizontal=True)
    sch1100 "{size=-5}(You will pay for this, bitch!){/size}"
    with vpunch
    sch600 "{size=+5}I said quiet! Do you want me to flog you in front of everyone?{/size}"
    show image im.Flip ("04_pt/iris/q1/iris28.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris30.png", horizontal=True)
    sch1100 "No, father, I'm sorry! I just--"
    sch600 "{size=+7}You're talking again!{/size}"
    show image im.Flip ("04_pt/iris/q1/iris15.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris28.png", horizontal=True)
    sch1100 ".............................."
    sch600 "..............................."
    show image im.Flip ("04_pt/jasmine/q1/jas06.png", horizontal=True) at center with Dissolve(.3)
    j "...................................."
    hide image im.Flip ("04_pt/iris/q1/iris15.png", horizontal=True)
    hide image im.Flip ("04_pt/jasmine/q1/jas06.png", horizontal=True) at center with Dissolve(.3)
    show image "04_pt/jasmine/q1/jas06.png" at left with Dissolve(.3)
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "So... Jasper... Are you ready for another day of training?"
    show image "04_pt/jasmine/q1/jas11.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas06.png" 
    j "Em... Yes, I am... I guess..."
    sch600 "Good... Good..."
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    sch600 "Iris, my dear..."
    show image im.Flip ("04_pt/iris/q1/iris31.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "Yes, father...."
    sch600 "Don't just stand there, girl. Start doing your job!"
    sch1100 "Yes, father."
    hide image "04_pt/jasmine/q1/jas11.png" at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris31.png", horizontal=True) at center with Dissolve(.3)
    show image "04_pt/iris/q1/iris31.png" at left with Dissolve(.3)
    sch1100 "Please follow me, Jasper."
    show image im.Flip ("04_pt/jasmine/q1/jas07.png", horizontal=True) at center with Dissolve(.3)
    j "Tsk... Didn't you mean to say \"Jas\"?"
    hide image "04_pt/iris/q1/iris31.png" at left with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris21.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "(Don't push it, Jasper)."
    hide image im.Flip ("04_pt/jasmine/q1/jas07.png", horizontal=True) at center with Dissolve(.3)
    show image "04_pt/jasmine/q1/jas02.png" at Position(xpos=100, ypos=0, xanchor=0, yanchor=0) with Dissolve(.3)
    j "Oh, sir, Maslab, if I may... There was one more thing Iris taught me last time..."
    hide image im.Flip ("04_pt/iris/q1/iris21.png", horizontal=True) at left with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris26.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "Jas, my dear, dear, Jas, please do not bother my poor father with such trivialities..."
    sch1100 "Please follow me, jas..."
    sch1100 "And I will continue to teach you, jas, how to wait tables, jas..."
    sch1100 "Because that's the only thing that I ever teach you here, Jas...."
    hide image "04_pt/jasmine/q1/jas02.png" with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/q1/jas06.png", horizontal=True) at left with Dissolve(.3)
    j "Of course, Iris, after you..."
    j "{size=-5}(Who's who's bitch now, you peasant wench?){/size}"
    hide image im.Flip ("04_pt/iris/q1/iris26.png", horizontal=True) at center with Dissolve(.3)
    show image "04_pt/iris/q1/iris21.png" at left with Dissolve(.3)
    sch1100 "{size=-5}(The day is not over yet.){/size}"
    hide image "04_pt/iris/q1/iris21.png" at left with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/q1/jas06.png", horizontal=True) at left with Dissolve(.3)
    sch600 "......................"
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab BG
    sch600 "So nice to see the girls getting along, is it not?"
    sch600 "I will look after yours, don't worry. And by the end of this day I will send her home to you like last time."
    sch600 "You have a nice day now."
    sch600 "........................"
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "*Spit*........"
    sch600 "{size=-5}(Iris is serving the \"Royal Goblet\" to the clients?){/size}"
    sch600 "{size=-5}(Like mother like daughter I suppose...){/size}"
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    show blkfade with Dissolve(.3)
    hide image "quest01/maslab03.png" 
    hide image "04_pt/slavem/bld.png" behind blkfade
    hide image "04_pt/slavem/bld2.png" behind blkfade
    ">You leave the tavern."
    $ renpy.play('sounds/door2.mp3')
    pause.5
    hide blkfade with Dissolve(.3)
    show quest with Dissolve(.3) 
    $ jonquest = True
    $ jidle = False   
    $ quest3start3 = False
    $ quest3start4 = True
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN THEME
    jump mainmenu 
#################################################
label waitresstrain:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab BG
    show blkfade with Dissolve(.3)
    show image "04_pt/slavem/bld.png" behind blkfade
    show image "04_pt/slavem/bld2.png" behind blkfade
    hide rest03
    show image "quest01/maslab01.png" at right behind blkfade
    pause.8
    hide blkfade with Dissolve(.3)
    sch600 "Hello, my friend."
    sch600 "And hello to you Jasper. How are you doing today, girl?"
    show image im.Flip ("04_pt/jasmine/q1/jas01_2.png", horizontal=True) at left with Dissolve(.3)
    j ".............................."
    j "I am doing well.... thank you..."
    hide image im.Flip ("04_pt/jasmine/q1/jas01_2.png", horizontal=True) at left with Dissolve(.3)
    sch600 "Well, you certainly look great! Jasper the beauty, huh?"
    sch600 "Your girl will make me rich, my friend."
    show image "04_pt/jasmine/q1/jas07.png" at left with Dissolve(.3)
    j "If you could just call me \"Jas\" I would appreciate it."
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Jas it is then. Beautiful and polite and I think very well educated as well, aren't you?"
    show image "04_pt/jasmine/q1/jas02.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas07.png" 
    j "Yes I am, thank you for noticing."
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    sch600 "Your slave-girl is starting to grow on me, my friend."
    hide image "04_pt/jasmine/q1/jas02.png" at left with Dissolve(.3)
    sch600 "Where did you get this one? She probably cost you a fortune, huh?" 
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Iris? Iris, where are you, silly girl?"
    show image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "I'm here, father..."
    sch600 "Iris, my friend is here."
    sch600 "He brought Jasper."
    sch600 "Today you will train her to be a proper waitress."
    hide image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris25.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "Of course."
    sch1100 "Hi there. And hello, jasper, it is very nice to see you..."
    hide image im.Flip ("04_pt/iris/q1/iris25.png", horizontal=True) with Dissolve(.3)
    show image "04_pt/jasmine/q1/jas10.png" at left with Dissolve(.3)
    j "Huh.......?"
    hide image "04_pt/jasmine/q1/jas10.png" at left with Dissolve(.3)
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "Yes, I had a little talk with my dear daughter..."
    sch600 "And she is very sorry about the way she behaved the other day..."
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Aren't you, dear?"
    show image im.Flip ("04_pt/iris/q1/iris25.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "Yes, father... I'm very sorry."
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris25.png", horizontal=True) at left with Dissolve(.5)
    pause.5
    show image "04_pt/iris/q1/iris25.png" at right with Dissolve(.5)
    sch1100 "So, Jasper, are you ready to begin, dear?"
    show image "04_pt/jasmine/q1/jas11.png" at left with Dissolve(.3)
    j "Em... Yes.... sure..."
    j "Although, could you just call me \"Jas\"?"
    hide image "04_pt/iris/q1/iris25.png" 
    show image "04_pt/iris/q1/iris25.png" at center with Dissolve(.5)
    sch1100 "Of course. anything you want, {size=+4}Jasper{/size}."
    hide image "04_pt/jasmine/q1/jas11.png" at left with Dissolve(.3)
    hide image "04_pt/iris/q1/iris25.png" with Dissolve(.3)
    show image "04_pt/iris/q1/iris25.png" at left with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/q1/jas11.png", horizontal=True) at center with Dissolve(.3)
    j "Em... It's \"Jas\"."
    sch1100 "Of course, {size=+4}Jasper{/size}..."
    hide image "04_pt/iris/q1/iris25.png" with Dissolve(.3)
    show image "04_pt/iris/q1/iris25.png" at Position(xpos=0, ypos=0, xanchor=270, yanchor=0) with Dissolve(.3)
    sch1100 "Now, follow me, please... {size=-7}(you spoiled bitch){/size}."
    hide image "04_pt/iris/q1/iris25.png" with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/q1/jas09.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/q1/jas11.png", horizontal=True) 
    j "What did you say?"
    show emo7 at Position(xpos=0, ypos=100, xanchor=0, yanchor=0) with Dissolve(.3)
    sch1100 "I said, please follow me now..."
    hide emo7 at Position(xpos=0, ypos=100, xanchor=0, yanchor=0) with Dissolve(.3)
    show image im.Flip ("04_pt/jasmine/q1/jas10.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/q1/jas09.png", horizontal=True) 
    j ".........."
    show image im.Flip ("04_pt/jasmine/q1/jas11.png", horizontal=True) at center with Dissolve(.3)
    hide image im.Flip ("04_pt/jasmine/q1/jas10.png", horizontal=True)
    j "..........."
    hide image im.Flip ("04_pt/jasmine/q1/jas11.png", horizontal=True) at center with Dissolve(.3)
    pause 1
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Don't you worry about Iris, my friend. She will be on her best behavior from now on, I promise you that."
    sch600 "And as for Jasper... "
    sch600 "She is a beautiful and graceful girl, but she doesn't know the first thing about being a waitress..."
    sch600 "So it might take a while..."
    sch600 "Just leave her here, and by the end of the day I will send her home..."
    show image "04_pt/jasmine/q1/jas10.png" at left with Dissolve(.3)
    j "Wait? Are you leaving?"
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png" at right with Dissolve(.3)
    sch600 "Don't you worry, girl, I will look after you..."
    hide image "quest01/maslab02.png" at right with Dissolve(.3)
    show emo7 at Position(xpos=0, ypos=100, xanchor=0, yanchor=0) with Dissolve(.3)
    show image "04_pt/jasmine/q1/jas13.png" at left with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas10.png" 
    sch1100 "{size=-7}(Your ass is mine now, bitch!){/size}"
    hide emo7 at Position(xpos=0, ypos=100, xanchor=0, yanchor=0) with Dissolve(.3)
    hide image "04_pt/jasmine/q1/jas13.png" at left with Dissolve(.3)
    show image "04_pt/jasmine/q1/jas12.png" at center with Dissolve(.3)
    j "(Master...?)"
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    show blkfade with Dissolve(.3)
    hide image "04_pt/slavem/bld.png" behind blkfade
    hide image "04_pt/slavem/bld2.png" behind blkfade
    hide image "04_pt/jasmine/q1/jas12.png" with Dissolve(.3)
    ">You leave the tavern."
    $ renpy.play('sounds/door2.mp3')
    pause.5
    hide blkfade with Dissolve(.3)
    show quest with Dissolve(.3) 
    $ jonquest = True
    $ jidle = False   
    $ quest3start2 = False
    $ quest3start3 = True
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN THEME
    jump mainmenu
 

        

        
        
        
        
