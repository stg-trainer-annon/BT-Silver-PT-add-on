label boxdelievered:
    $ quest2start = False
    $ quest2start2 = True
    show blkfade with Dissolve(.3)
    show image "quest01/maslab01.png" at right behind blkfade
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
    pause.3
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch600 "Huh? *spit*"
    sch600 "What's this? A delivery? For me?"
    menu:
        sch600 "\"Who gave this box to you?\""
        "\"That's a secret.\"":
            sch600 "A secret, huh? *spit*"
            sch600 "Must be from Fat Lily then. This is from her isn't it?"
            sch600 "It's a tough job to love that woman, let me tell you..."
            sch600 "About time she started to show some appreciation."
            sch600 "Alright then, let's see what's inside!"
            hide image "quest01/maslab01.png" at right with Dissolve(.3)
            ">Maslabs grabs the box and opens it."
            ">You hear something click inside of it and then a soft cracking sound."
            ">Suddenly the box spits out some sort of slimy liquid right into the inn keeper's face."
            ">Instinctively you take a step back, but Maslab doesn't even flinch."
            ">Casually he picks up a piece of cloth from the counter and wipes his face clean."
            show image "quest01/maslab01.png" at right with Dissolve(.3)
            sch600 "Do you smell this, my friend? *spit*"
            sch600 "Rotten eggs..."
            sch600 "Son of a jackal! He wanted to scare me with this?"
            sch600 "Oh, it's on now!"
        "\"Your brother.\"":
            sch600 "Balsam? *spit*"
            sch600 "Well, then this must be some sort of trick..."
            sch600 "Just put it on this table here... carefully..."
            hide image "quest01/maslab01.png" at right with Dissolve(.3)
            ">You put the box on the table and take a step back." 
            ">Maslab is looking at it suspiciously..."
            show image "quest01/maslab01.png" at right with Dissolve(.3)
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            sch600 "What do you wager is inside of this little beast?"
            menu:
                "\"Chocolate.\"":
                    sch600 "You think? Hm... that's unlikely..."
                "\"A bomb.\"":
                    sch600 "Ha-ha-ha! You think? Well, then there is only one way to find out for sure!"
                "\"It's empty.\"":
                    sch600 "Hm... *spit* Why go through the trouble of delivering it all the way here then?"
                    sch600 "No, there's gotta be something inside..."
                    sch600 "A couple of black scorpions... Or a poisonous snake."
                "\"Rotten eggs.\"":
                    sch600 "Well of course! This is a trick-box!"
                    sch600 "*spit* How predictable... And boring..."
                "\"A Playstation VITA.\"":
                    sch600 "You think? You think?!"
                    sch600 "Nah... That would be too good to be true..."
                "\"I don't know...\"":
                    sch600 "Well, let's see then, shall we?"
            hide image "quest01/maslab01.png" at right with Dissolve(.3)
            ">Maslab flips the top of the box open with his dagger."
            ">You hear something click and then a soft cracking sound."
            ">Suddenly the box squirts out some sort of slimy liquid towards the ceiling."
            show image "quest01/maslab01.png" at right with Dissolve(.3)
            sch600 "*Spit!* Is this all you got, brother?"
            sch600 "Ha-ha-ha! This is not even enough to make me flinch!"
            sch600 "But I accept your challenge!"
   
    show image im.Flip ("04_pt/iris/q1/iris02.png", horizontal=True) at left with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Father? What is this godawful smell?"
    show image "quest01/maslab02.png" at right with Dissolve(.2)
    hide image "quest01/maslab01.png"
    sch600 "Whadda you think, girl?"
    sch600 "A present, from my dear brother. *spit*"
    hide image "quest01/maslab02.png" at right with Dissolve(.2)
    hide image im.Flip ("04_pt/iris/q1/iris02.png", horizontal=True) at left with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris03.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "From uncle Balsam?"
    sch1100 "But this means--"
    hide image im.Flip ("04_pt/iris/q1/iris03.png", horizontal=True) at center with Dissolve(.2)
    show image "quest01/maslab02.png" at right with Dissolve(.2)
    sch600 "Absolutely! That son of a jackal is gonna pay!"
    hide image "quest01/maslab02.png" at right with Dissolve(.2)
    show image im.Flip ("04_pt/iris/q1/iris04.png", horizontal=True) at center with Dissolve(.2)
    sch1100 "Great! I will go fetch your cutlass and my throwing knifes."
    hide image im.Flip ("04_pt/iris/q1/iris04.png", horizontal=True) at center with Dissolve(.2)
    show image "quest01/maslab02.png" at right with Dissolve(.2)
    sch600 "My cutlass and your--"
    sch600 "Have you gone mad, girl? The man is family!"
    sch600 "Plus I've retired. Just a humble inn keeper now, remember?"
    hide image "quest01/maslab02.png" at right with Dissolve(.2)
    show image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) at center with Dissolve(.2) 
    sch1100 "Yes, father, I remember..."
    hide image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) at center with Dissolve(.2)
    show image "quest01/maslab02.png" at right with Dissolve(.2)
    sch600 "Then stop saying nonsense and get back to work..."
    hide image "quest01/maslab02.png" at right with Dissolve(.2)
    show image im.Flip ("04_pt/iris/q1/iris05.png", horizontal=True) at center with Dissolve(.2)
    sch1100 "Tsk..."
    hide image im.Flip ("04_pt/iris/q1/iris05.png", horizontal=True) at center with Dissolve(.3)
    show image "quest01/maslab02.png" at right with Dissolve(.2)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show image "quest01/maslab01.png" at right with Dissolve(.3)
    hide image "quest01/maslab02.png" 
    sch600 "Listen, friend, do you want to have some fun?"
    menu:
        "\"I don't like you {size=+5}THAT MUCH{/size}, Maslab.\"":
            sch600 "*spit* Nor do I fancy you one little bit! Ha-ha-ha!"
        "\"Yes I do! Absolutely!\"":
            sch600 "Great! I expected you to say that!"
        "\"Depends on what you mean by \"fun\".\"":
            sch600 "*spit* Just trust me. It's gonna be a lot of fun."
        "\"You mean with your daughter?\"":
            sch600 "Yes, of course. This is a family matter, so she will be taking part in this as well."
            sch600 "And you did deliver me the damn trick box so you have some making up to do."
    sch600 "Listen, I need to take a bath now, before I scare off the few customers I have, with this stench."
    sch600 "But you, my friend, make sure to come by tonight. I will need your assistance with something."
    sch600 "See you tonight then."
    show blkfade with Dissolve(.3)
    hide image "quest01/maslab01.png" 
    ">You leave the tavern."
    $ renpy.play('sounds/door2.mp3')
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    hide blkfade with Dissolve(.5)
    ">It's getting late. You decide to head home."
    jump dayends
#############################################################################
label quest2night1:
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show blkfade with Dissolve(.3)
    hide image "04_pt/slavem/bld.png" 
    show image "04_pt/slavem/bld2.png" behind blkfade
    show image "04_pt/slavem/bld.png" behind blkfade
    show image "quest01/maslab01.png" at right behind blkfade
    $ renpy.play('sounds/door2.mp3')
    pause.3
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch600 "Welcome to the \"Blue Bull\" tavern..."
    sch600 "You're just in time. *Spit*."
    show image im.Flip ("04_pt/iris/q1/iris06.png", horizontal=True) at left with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "Hi there."
    show image "quest01/maslab02.png" at right with Dissolve(.3)
    hide image "quest01/maslab01.png"
    sch600 "Is everyone ready?"
    show image im.Flip ("04_pt/iris/q1/iris07.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris06.png", horizontal=True) at left 
    sch1100 "I'm ready!"
    menu:
        "\"As ready as I will ever be.\"":
            hide image im.Flip ("04_pt/iris/q1/iris07.png", horizontal=True) at left with Dissolve(.3)
            hide image "quest01/maslab02.png" at right with Dissolve(.2)
            pass
        "\"Ready for what?\"":
            hide image im.Flip ("04_pt/iris/q1/iris07.png", horizontal=True) at left with Dissolve(.3)
            show image "quest01/maslab01.png" at right with Dissolve(.3)
            hide image "quest01/maslab02.png"
            sch600 "Oh, right, I forgot to explain the plan to you."
            hide image "quest01/maslab01.png" at right with Dissolve(.2)
            show image im.Flip ("04_pt/iris/q1/iris06.png", horizontal=True) at left with Dissolve(.2)
            sch1100 "That's alright, I will fill your friend in, father."
            hide image im.Flip ("04_pt/iris/q1/iris06.png", horizontal=True) at left with Dissolve(.2)
            show image im.Flip ("04_pt/iris/q1/iris06.png", horizontal=True) at center with Dissolve(.2)
            sch1100 "Three of us will go to the market square, find my uncle's fruit stand and burn it down..."
            show image "quest01/maslab03.png" at right with Dissolve(.3)
            sch600 "No, I told you, girl, we are not going to burn down anything."
            show image "quest01/maslab02.png" at right with Dissolve(.2)
            hide image "quest01/maslab03.png" at right with Dissolve(.2)
            sch600 "We're not doing stuff like that anymore! Remember?"
            hide image im.Flip ("04_pt/iris/q1/iris06.png", horizontal=True) at center with Dissolve(.2)
            show image "04_pt/iris/q1/iris08.png" at left with Dissolve(.2)
            sch1100 "Yes, father..."
            hide image "04_pt/iris/q1/iris08.png" at left with Dissolve(.2)
            show image im.Flip ("04_pt/iris/q1/iris08.png", horizontal=True) at left with Dissolve(.2)
            sch1100 "We are just going to move it to a nearby alley and cover it with piles of garbage, I guess..."
            hide image im.Flip ("04_pt/iris/q1/iris08.png", horizontal=True) at left with Dissolve(.2)
            sch600 "Exactly."
            hide image "quest01/maslab02.png" at right with Dissolve(.2)
        "\".................\"":
            hide image im.Flip ("04_pt/iris/q1/iris07.png", horizontal=True) at left with Dissolve(.3)
            show image "quest01/maslab01.png" at right with Dissolve(.2)
            hide image "quest01/maslab02.png" 
            sch600 "Don't tell me you're having second thoughts, friend."
            show image im.Flip ("04_pt/iris/q1/iris07.png", horizontal=True) at left with Dissolve(.3)
            sch1100 "It's gonna be fun, come on!"
            hide image im.Flip ("04_pt/iris/q1/iris07.png", horizontal=True) at left with Dissolve(.2)
    show image "quest01/maslab01.png" at right with Dissolve(.2)
    sch600 "Let's go then."
    hide image "quest01/maslab01.png" at right with Dissolve(.2)
    ">You leave the tavern building with Maslab and his daughter."
    $ renpy.play('sounds/door.mp3')
    play music "music/tension2.MP3" fadein 1 fadeout 1
    show blkfade with Dissolve(.3)
    hide image "04_pt/slavem/bld2.png" with Dissolve(.2)
    hide image "04_pt/slavem/bld.png"  with Dissolve(.2)
    hide blkfade with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show image "04_pt/slavem/bld.png"  with Dissolve(.2)
    ">The market square is empty and silent..."
    show image "04_pt/slavem/bld2.png"  with Dissolve(.2)
    sch6_2 "Iris, you will be our lookout. If you see a guard coming make sure to warn us."
    show image im.Flip ("04_pt/iris/q1/iris08.png", horizontal=True) at center with Dissolve(.2)
    sch1100 "Of course, like always."
    hide image im.Flip ("04_pt/iris/q1/iris08.png", horizontal=True) at center with Dissolve(.2)
    sch6_2 "Alright, my friend, let's do this!"
    hide image "04_pt/slavem/bld2.png" with Dissolve(.2)
    ">You and Maslab find the fruit stand that belongs to his brother and move it to a nearby alley."
    ">After that you help Maslab cover it with garbage and some dirt."
    "...."
    "..."
    $ renpy.play('sounds/whistle.mp3')
    ">You hear a soft whistle."
    show image "04_pt/slavem/bld2.png" with Dissolve(.2)
    sch6_2 "That's Iris. The city guard must be coming. Time to go!"
    ">You and Maslab quickly bail." 
    show blkfade with Dissolve(.3)
    hide image "04_pt/slavem/bld2.png" with Dissolve(.2)
    hide image "04_pt/slavem/bld.png"  with Dissolve(.2)
    pause 1
    hide blkfade with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
    ">When you get back to the tavern Iris is already there."
    show image "04_pt/slavem/bld.png" with Dissolve(.2)
    $ renpy.play('sounds/door2.mp3')
    show image "04_pt/slavem/bld2.png"  with Dissolve(.2)
    show image im.Flip ("04_pt/iris/q1/iris09.png", horizontal=True) at center with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch1100 "There you are, guys. How did it go?"
    show image "quest01/maslab02.png" at right with Dissolve(.2)
    sch600 "Well enough..."
    sch600 "Did the city guard see you?"
    hide image im.Flip ("04_pt/iris/q1/iris09.png", horizontal=True) at left with Dissolve(.2)
    show image im.Flip ("04_pt/iris/q1/iris10.png", horizontal=True) at left with Dissolve(.2)
    sch1100 "Yes... He was going right towards you guys, and I didn't have enough time to warn you, so I had to improvise."
    show image "quest01/maslab03.png" at right with Dissolve(.2)
    hide image "quest01/maslab02.png" at right with Dissolve(.2)
    sch600 "Improvise how? Did you do something stupid again, girl?"
    hide image "quest01/maslab03.png" at right with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris10.png", horizontal=True) at left with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris11.png", horizontal=True) at center with Dissolve(.3)
    sch1100 "What? Oh, no, I didn't hurt him, I swear."
    hide image im.Flip ("04_pt/iris/q1/iris11.png", horizontal=True) at left with Dissolve(.3)
    show image "04_pt/iris/q1/iris12.png" at left with Dissolve(.3)
    sch1100 "All I did was show him my--"
    show image "quest01/maslab03.png" at right with Dissolve(.3)
    sch600 "Huh?"
    show image "04_pt/iris/q1/iris13.png" at left with Dissolve(.3)
    hide image "04_pt/iris/q1/iris12.png"
    sch1100 "...em... er... I mean, I showed him my... my rock throwing skills."
    hide image "04_pt/iris/q1/iris13.png" at left with Dissolve(.2)
    show image im.Flip ("04_pt/iris/q1/iris12.png", horizontal=True) at left with Dissolve(.2)
    sch1100 "Yes, that's what I did. I threw a rock at him and then I ran like hell.... And like that I had enough time to warn you, guys." 
    show image "quest01/maslab02.png" at right with Dissolve(.2)
    hide image "quest01/maslab03.png" 
    sch600 "Nicely done, girl."
    hide image im.Flip ("04_pt/iris/q1/iris12.png", horizontal=True) at left with Dissolve(.2)
    show image "quest01/maslab01.png" at right with Dissolve(.2)
    hide image "quest01/maslab02.png" 
    sch600 "Ha-ha-ha! *spit* \nI would give anything to see that dog's face tomorrow morning."
    sch600 "\"Where is my precious fruit stand? It disappeared! I can't sell my precious fruits anymore!\""
    sch600 "Ha-ha-ha! Silly old frog!"
    show image im.Flip ("04_pt/iris/q1/iris14.png", horizontal=True) at left with Dissolve(.2)
    sch1100 "........"
    show image "quest01/maslab03.png" at right with Dissolve(.2)
    hide image "quest01/maslab01.png" 
    sch600 "Stop daydreaming and get back to work, girl."
    show image im.Flip ("04_pt/iris/q1/iris15.png", horizontal=True) at left with Dissolve(.2)
    hide image im.Flip ("04_pt/iris/q1/iris14.png", horizontal=True)
    sch1100 "Yes, father..."
    hide image im.Flip ("04_pt/iris/q1/iris15.png", horizontal=True) with Dissolve(.4) 
    show image "quest01/maslab01.png" at right with Dissolve(.2)
    hide image "quest01/maslab03.png"
    sch600 "Thank you for your help, my friend."
    sch600 "Wine is on the house for you tonight."
    hide image "quest01/maslab01.png" at right with Dissolve(.2)
    hide image "04_pt/slavem/bld2.png"  with Dissolve(.2)
    ">You stay at the tavern for a bit longer, and enjoy some cheap wine on the house."
    ">After a while you decide that it is time to call it a night."
    hide image "04_pt/slavem/bld.png" with Dissolve(.2)
    $ renpy.play('sounds/door2.mp3')
    ">You return home. Jasmine is sound asleep. You decide to follow her example."
    $ quest2start2 = False
    $ quest2start3 = True
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayone
##########################################
label aboutlastnight:
    sch5 "Hi there, friend. You want to hear a funny story?"
    sch5 "I had to open a few hours late this morning."
    menu:
        sch5 "Do you know why?"
        "\"I have no idea.\"":
            sch5 "I couldn't find my fruit-stand!"
            sch5 "I'm pretty certain that my good-for-nothing... I mean my dear brother is the man responsible for this."
        "\"Couldn't find your fruit-stand?\"":
            sch5 "I couldn't find my... Oh, so you know."
            sch5 "Tell me one thing then: was it my good-for-nothing... I mean my favorite brother who did this to me?"
            sch5 "Well, of course it was him. Who else would it be?"
    sch5 "Well, now I have no choice but to retaliate."
    menu:
        sch5 "Don't you think he went too far this time?"
        "\"You started it.\"":
            sch5 "It may seem that way, yes, but the truth is that he was the one who started it, not me. Very long time ago when we were just kids."
        "\"Totally agree. Maslab, that dog.\"":
            sch5 "Exactly! Glad you agree with me, my friend."
        "\"What are you guys, 10 years old?\"":
            sch5 "Well actually that's exactly when this whole thing started... Back when we were kids..."
    sch5 "In any case, I already know what my next step will be."
    sch5 "But I will need your assistance."
    menu:
        sch5 "Can I count on your help?"
        "\"I'm your man!\"":
            sch5 "Great!"
        "\"I would rather not...\"":
            sch5 "But I need your help!"
            sch5 "Fine. Here is some gold for your trouble."
            $ gold +=25
            $ renpy.play('sounds/win2.mp3')
            ">You received 25 gold coins."
        "\"You promised a reward.\"":
            sch5 "What? Oh, yeah, sure."
            sch5 "Here, have an orange."
            "You received an orange."
    sch5 "Alright then. I need to make a few preparations first..."
    sch5 "Meet me here at midnight..."
    sch5 "Until then."
    $ quest2start3 = False
    $ quest2start4 = True
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    jump mainmenu
    
#########################
label quest2night2:
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    ">You go to meet with Balsam."
    play music "music/Ozone.ogg" fadein 1 fadeout 1
    ">You come to the market square and find the merchant in the company of one of the city guards."
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    sch5 "And then I said: \"show me your tits and you can have that orange for free!\""
    sch12 "He-he! Good one!"
    "Balsam notices your presence."
    sch5 "Oh, it seems like my business partner is finally here."
    sch12_2 "........"
    sch5 "Please don't let me keep you from performing your duty any longer then."
    sch12_2 "Yeah, time for me to get back to patrolling this darn city..."
    ">The guard gives you a stiff nod and leaves."
    sch5 "I'm glad to see you, my friend."
    sch5 "Everything is ready, it's all up to you now."
    sch5 "Here. Take this parchment."
    show image "04_pt/slavem/masteritem.png" with moveinleft
    $ renpy.play('sounds/win2.mp3')
    show image "04_pt/slavem/boxev.png" with moveinright
    ">You received \"The Eviction Notice\"."
    hide image "04_pt/slavem/boxev.png" with Dissolve(.4)
    hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
    sch5 "Now, all you need to do is go to the \"Blue Bull\" and stick this parchment on the front door."
    sch5 "In case you are curious, this is an official eviction notice signed by the sultan himself."
    sch5 "The document says that Maslab been found guilty of hosting illegal dice games in his tavern..."
    sch5 "And now has to vacate the building until noon tomorrow or be beheaded."
    sch5 "I'm hoping to give my dear brother a good scare before he realizes that the document is fake."
    sch5 "Yes. This will teach him not to mess with my business."
    menu:
        sch5 "Do you have any questions, my friend?"
        "\"Why can't you do it yourself?\"":
            sch5 "Huh? Oh, I would rather not go anywhere near that damn tavern..."
        "\"Will I get paid for this?\"":
            sch5 "You want to get paid? Em, yeah, sure, here is some gold."
            $ gold +=7
            $ renpy.play('sounds/win2.mp3')
            ">You received 7 gold coins."
        "\"No. I'm all set and ready to go.\"":
            sch5 "Good luck then."
    ">You leave the market square."
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    ">The city streets are deserted and quiet. On your way to the tavern you didn't see a soul."
    ">You reach your destination and take out the parchment Balsam gave you."
    ">You are hesitating... It seems no matter what you do, you will let down one of the brothers."
    ">Nevertheless the decision should be made..."
    menu:
        "Will you do what Balsam asked you to do, or would you rather enter the tavern and tell Balsam everything?"
        "-Stick parchment to the door and leave-":
            ">You decide to keep your word and do what you promised to Balsam."
            ">You unroll the parchment and stick it to the door."
            ">After the deed is done you leave..."
            ">You return home and go to sleep."
            $ quest2start4 = False
            $ quest2start5 = True
            show image "interface/blackfade.png" with Dissolve(.3)
            pause 1
            jump dayone
        "-Enter the tavern and confess-":
            ">You decide to tell Maslab everything."
            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
            $ renpy.play('sounds/door.mp3')
            show image "04_pt/slavem/bld.png" with Dissolve(.3)
            show image "04_pt/slavem/bld2.png" with Dissolve(.3)
            show image im.Flip ("04_pt/iris/q1/iris17.png", horizontal=True) at center with Dissolve(.3)
            sch1100 "Hello there, welcome to the--"
            show image im.Flip ("04_pt/iris/q1/iris16.png", horizontal=True) at center with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q1/iris17.png", horizontal=True) 
            sch1100 "Oh, it's you."
            sch1100 "Father is behind the counter."
            hide image im.Flip ("04_pt/iris/q1/iris16.png", horizontal=True) at center with Dissolve(.3)
            show image "quest01/maslab01.png" at right with Dissolve(.3)
            sch600 "Hello, friend. Should I pour you some wine?"
            sch600 "What is that piece of paper you're holding there?"
            hide image "quest01/maslab01.png" at right with Dissolve(.3)
            ">You show Maslab the parchment and tell him everything."
            show blkfade with Dissolve(.3)
            pause 1
            hide blkfade with Dissolve(.3)
            show image "quest01/maslab03.png" at right with Dissolve(.3)
            sch600 "That infidel dog! How on earth did he find out about the dice games?"
            sch600 "More than that, if someone were to see this sort of paper on the front door of my tavern..."
            sch600 "Fake or not, it would raise all sorts of suspicions..."
            show image "quest01/maslab01.png" at right with Dissolve(.3)
            hide image "quest01/maslab03.png" with Dissolve(.3)
            sch600 "You did the right thing by telling me this, my friend."
            hide image "quest01/maslab01.png" at right with Dissolve(.3)
            ">Maslab seem to be trusting you more now."
            ">You feel a faint bond forming between you two."
            play music "music/Power_of_the_Heart.mp3" fadein 1 fadeout 1
            with flashbulb
            show image "quest01/per01.png" with Dissolve(.5)
            pause.7
            show image "quest01/per02.png" with Dissolve(.5)
            pause 1
            show image "quest01/per03.png" with Dissolve(.5)
            pause 2
            show image "quest01/per04.png" with Dissolve(.5)
            pause 2
            show image "quest01/per05.png" with Dissolve(.5)
            pause 2
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            stop music 
            $ renpy.play('sounds/scratch.wav')
            a2 "Just kidding."
            a2 "Sorry, I couldn't resist."
            a1 "You relationship with Maslab did improve though..."
            ">Your relationship with Maslab the inn keeper has improved."
            $ maslabfriendship += 1
            a2 "Told ya!"
            show image "interface/blackfade.png" with Dissolve(.3)
            hide image "quest01/per01.png" 
            hide image "quest01/per02.png"
            hide image "quest01/per03.png"
            hide image "quest01/per04.png"
            hide image "quest01/per05.png"
            pause.3
            hide image "interface/blackfade.png" with Dissolve(.3)
            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
            show image "quest01/maslab03.png" at right with Dissolve(.3)
            sch600 "I can't believe my good-for-nothing brother would do something that stupid."
            sch600 "He finally crossed the line."
            show image "quest01/maslab04.png" at right with Dissolve(.3)
            hide image "quest01/maslab03.png" with Dissolve(.3)
            sch600 "I need to teach him a lesson and really hurt him with my next move..."
            show image im.Flip ("04_pt/iris/q1/iris04.png", horizontal=True) at left with Dissolve(.3)
            sch1100 "Great! I'll get your cutlass ready!"
            show image "quest01/maslab03.png" at right with Dissolve(.3)
            hide image "quest01/maslab04.png" with Dissolve(.3)
            sch600 "You know that's not what I mean, girl! Now get back to work!"
            show image im.Flip ("04_pt/iris/q1/iris02.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q1/iris04.png", horizontal=True) 
            sch1100 "Tsk..."
            hide image im.Flip ("04_pt/iris/q1/iris02.png", horizontal=True) at left with Dissolve(.3)
            sch600 "I have to make him pay.. But how?"
            show image "quest01/maslab04.png" at right with Dissolve(.3)
            hide image "quest01/maslab03.png" with Dissolve(.3)
            sch600 "I better come up with something really clever this time..."
            sch600 "I will probably require your assistance again, my friend."
            menu:
                sch600 "Can I count on your help?"
                "\"Absolutely! Balsam, that dirtbag! *spit*\"":
                    show image "quest01/maslab02.png"  at right with Dissolve(.3)
                    hide image "quest01/maslab04.png" with Dissolve(.3)
                    sch600 "Funny thing..."
                    sch600 "I loath that good-for-nothing bastard almost more than anyone..."
                    sch600 "And yet, can't help but feel a little bit insulted when I hear you badmouth him..." 
                    show image "quest01/maslab01.png"  at right with Dissolve(.3)
                    hide image "quest01/maslab02.png" with Dissolve(.3)
                    sch600 "You are not at fault here, the man is a dirtbag!"
                    sch600 "And I appreciate your help up until now, my friend, but..."
                "{size=-3}\"I would rather not get involved anymore.\"{/size}":
                    show image "quest01/maslab01.png"  at right with Dissolve(.3)
                    hide image "quest01/maslab04.png" with Dissolve(.3)
                    sch600 "Fair enough..."
            sch600 "Maybe I should stop dragging outsiders into family matters."
            menu:
                sch600 "Unless you want to marry my daughter that is..."
                "{size=-3}\"What? That's a bit sudden, don't you think?\"{/size}":
                    sch600 "Ha-ha-ha. Relax, my friend! That was a joke."
                    sch600 "I abandoned that hope long ago."
                    sch600 "No sober man would ever want to have that unruly thing as his wife."
                "\"Gladly!\"":
                    sch600 "Ah-ha-ha! That's a good one!"
                    sch600 "\"Gladly\" he says! Ha-ha-ha!"
                    sch600 "Heh... The truth is I abandoned that hope long time ago."
                    sch600 "No sober man would ever want to have that unruly thing as his wife." 
            show image im.Flip ("04_pt/iris/q1/iris09.png", horizontal=True) at left with Dissolve(.3)
            sch1100 "Are you talking about me, father?"
            show image "quest01/maslab03.png"  at right with Dissolve(.3)
            hide image "quest01/maslab01.png" with Dissolve(.3)
            sch600 "No, about some other unruly thing! Stop eavesdropping and get back to work, girl!"
            show image im.Flip ("04_pt/iris/q1/iris14.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q1/iris09.png", horizontal=True) 
            sch1100 "I'm on a break..."
            show image im.Flip ("04_pt/iris/q1/iris12.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q1/iris14.png", horizontal=True) 
            sch1100 "Can I dance on a table a little, with the other girls?"
            sch600 "Only if you want to get flogged!"
            show image im.Flip ("04_pt/iris/q1/iris15.png", horizontal=True) at left with Dissolve(.3)
            hide image im.Flip ("04_pt/iris/q1/iris12.png", horizontal=True) 
            sch1100 "Tsk..."
            hide image im.Flip ("04_pt/iris/q1/iris15.png", horizontal=True) at left with Dissolve(.3)
            show image "quest01/maslab01.png"  at right with Dissolve(.3)
            hide image "quest01/maslab03.png" with Dissolve(.3)
            sch600 "So me and Iris will handle this thing on our own from now."
            sch600 "Oh, and about those dice games..."
            sch600 "I would appreciate it if you could keep that information to yourself."
            sch600 "But if you feel like taking part in it, by all means, feel free to."
            hide image "quest01/maslab01.png"  at right with Dissolve(.3)
            ">You feel like you had enough excitement for one day and decide to call it a night."
            $ renpy.play('sounds/door.mp3')
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            hide image "04_pt/slavem/bld2.png" with Dissolve(.3)
            hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
            $ quest2start4 = False
            $ quest2complete = True
            $ onquest = False
            $ idlequest = True
            $ renpy.play('sounds/win2.mp3')   
            show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
            show con1 at right
            show ctc7 at right
            pause
            hide con1
            hide ctc7
            "Now you can also explore the city during nighttime."
            hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            ">You return home and go to sleep."
            show image "interface/blackfade.png" with Dissolve(.3)
            pause 1
            jump dayone
            pause
###################################################
label wasscared:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
    ">As you enter the tavern you bump into a city guard on his way out."
    sch12_2 "Excuse me..."
    show image "04_pt/slavem/bld2.png" with Dissolve(.3)
    show image "04_pt/iris/q1/iris17.png" at center with Dissolve(.3)
    sch1100 "Oh, hello there..."
    sch1100 "Father is in a foul mood today..."
    menu:
        "\"Do you know why?\"":
            sch1100 "Yes... Something my uncle did really pissed him off..."
        "\"I still need to talk to him.\"":
            sch1100 "Sure, his at his usual spot..."
        "\"What's the city guard doing here?\"":
            sch1100 "Not sure... You better talk to my father..."
    with hpunch
    sch600 "That good-for-nothing piece of shit of a brother of mine!"
    hide image "04_pt/iris/q1/iris17.png" at center with Dissolve(.2)
    show image im.Flip ("04_pt/iris/q1/iris17.png", horizontal=True) at left with Dissolve(.4)
    show image "quest01/maslab03.png"  at right with Dissolve(.3)
    sch600 "Back in the day I would've strangled that dog with my bare hands for this!"
    hide image im.Flip ("04_pt/iris/q1/iris17.png", horizontal=True) at left with Dissolve(.3)
    show image im.Flip ("04_pt/iris/q1/iris04.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "What's stopping you, father? You know I keep your cutlass in perfect condition!"
    sch600 "Don't tempt me girl! Not today!"
    sch600 "And--"
    show image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris04.png", horizontal=True) at left with Dissolve(.3)
    sch1100 "\"Get back to work\", I know..."
    sch600 "Tsk... Getting smart with me are you?"
    show image im.Flip ("04_pt/iris/q1/iris05.png", horizontal=True) at left with Dissolve(.3)
    hide image im.Flip ("04_pt/iris/q1/iris01.png", horizontal=True)
    sch1100 "No father, I'm sorry, I need to get back to work now."
    hide image im.Flip ("04_pt/iris/q1/iris05.png", horizontal=True) at left with Dissolve(.3)
    sch600 "Grrr.. #$@#$$!! Everyone is pissing me off today!"
    show image "quest01/maslab04.png"  at right with Dissolve(.3)
    hide image "quest01/maslab03.png"  at right with Dissolve(.3)
    menu:
        sch600 "Oh, it's you... Do you know what happened last night?"
        "\"I know. Actually I helped your brother.\"":
            show image "quest01/maslab08.png"  at right with Dissolve(.3)
            hide image "quest01/maslab04.png"  at right with Dissolve(.3)
            sch600 "Y-you... You h-helped him?"
            show image "quest01/maslab07.png"  at right with Dissolve(.3)
            hide image "quest01/maslab08.png"  at right with Dissolve(.3)
            sch600 "Although to be fair you did help me as well... And this was supposed to be a \"family only\" matter from the very begging..."
            sch600 "It always was..."
            sch600 "I should stop dragging outsiders into this mess..."
            sch600 "I will retaliate of course! Gonna really hurt him this time!"
            sch600 "But it's up to me and Iris now... We will handle this thing on our own from now."
            sch600 "That stupid fake parchment..."
            sch600 "The moment I saw it I knew it was fake..."
            sch600 "But it did rise all sort of questions... It may cause me trouble in the future..."
            sch600 "How the hell did he know about the dice games..."
            sch600 "That infidel dog of a brother..."
            sch600 "Oh, and as for the dice games..."
            sch600 "I would appreciate if you could keep that information to yourself."
            sch600 "But if you feel like taking a part in it, by all means, feel free."
        "\"What happened? I was sleeping.\"":
            sch600 "Last night he stack a stupid fake eviction notice on my door..."
            sch600 "The moment I saw it I knew it was fake..."
            sch600 "But it did rise all sort of questions... It may cause me trouble in the future..."
            sch600 "How the hell did he know about the dice games..."
            sch600 "That infidel dog of a brother..."
            sch600 "I will retaliate of course! Gonna really hurt him this time!"
            sch600 "But I think I should stop dragging outsiders into this mess..."
            sch600 "It's up to me and Iris now... We will handle this thing on our own from now."
            sch600 "Oh, and as for the dice games..."
            sch600 "I would appreciate if you could keep that information to yourself."
            sch600 "But if you feel like taking a part in it, by all means, feel free."
    hide image "quest01/maslab04.png"  at right with Dissolve(.3)
    hide image "quest01/maslab07.png"  at right with Dissolve(.3)
    hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
    $ quest2complete = True
    $ quest2start5 = False
    $ onquest = False
    $ idlequest = True
    $ renpy.play('sounds/win2.mp3')                        
    show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    "Now you can also explore the city during the night time."
    hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld2.png" with Dissolve(.3)
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    jump mainmenu
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide image "04_pt/slavem/bld.png"
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    "Here is the parchment. Take it to the blue bull."
    "You take the parchment to the blue bull."
    "You return home and go to sleep."
    $ quest2start4 = False
    $ quest2start5 = True
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayone
    
