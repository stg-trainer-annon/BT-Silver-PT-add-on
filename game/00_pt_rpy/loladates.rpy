label loladatecheapside:
    $ quest7food = False
    $ loladates += 1
    $ ldatecheapside = False
    lola[11] "the Cheapside? How exiting! Let's go!"
    show blkfade with Dissolve(.3)
    $ renpy.play('sounds/door2.mp3')
    pause 1.5
    hide blkfade with Dissolve(.3)
    lola[3] "Hm........"
    lola[3] "What is this stink?!"
    lola[3] "And there is garbage everywhere, and everything is so dirty..."
    lola[0] "I love it!"
    lola[5] "Girls in the brothel always say that the cheapside is a very dangerous area..."
    lola[5] "You think we might get in some sort trouble today?"
    menu:
        "\"Very unlikely.\"":
            lola[3] "aw... Too bad."
        "\"I will protect you.\"":
            lola[9] "You? Really?"
            lola[9] "Aren't you a bit too old?"
            lola[8] "Well, I hope somebody attacks us today, and then we'll see!"
    lola[8] "So where to now? Do they have any stores here?"
    show blkfade with Dissolve(.3)
    pause 1
    hide blkfade with Dissolve(.3)
    lola[9] "Hm... People are looking at me funnily..."
    lola[9] "Is there something wrong with the way I look?"
    sch8 "There is nothing wrong with the way you look, darling..."
    with hpunch
    lola[5] "!?!?!?!"
    sch8 "People around these parts are mean, that's all."
    lola[0] "Hello mister."
    sch8 "And hello to you too, little lady."
    lola[5] "Wow! You have a wooden leg?!"
    lola[5] "Cool!"
    lola[5] "What happened to your actual leg?"
    sch8 "A dog ate it while crocus was sleeping..."
    lola[0] "Who's Crocus?"
    sch7 "I am, of course..."
    lola[5] "So a dog ate your leg while you were asleep?"
    lola[3] "I don't believe you..."
    sch8 "You are one smart little girl... "
    sch8 "The truth is Crocus got so hungry with nothing to eat in one winter that Crocus had to cook his own leg."
    lola[9] "Ew! That's nasty!"
    sch8 "It was very delicious though..."
    lola[6] "He-hee. You're funny."
    sch8 "You are too kind, young lady..."
    sch8 "Would you be also kind enough to give poor Crocus a coin or two?"
    lola[43] "What? Oh, I don't have any money, sorry."
    sch7 "I see... How about something else, then? Show Crocus your tits maybe?"
    lola[5] "What?"
    sch8 "Please, little lady. Crocus is old, feeble and homless..."
    sch8 "Crocus doesn't even remember how a woman's tit looks like anymore."
    sch8 "Is it shaped like a cube? Is it shaped like a pyramid? I don't remember..."
    lola[6] "Hee-hee... You are really funny!"
    lola[7] "Well, alright!"
    show blkfade with Dissolve(.3)
    pause.5
    hide blkfade with Dissolve(.3)
    lola[37] "There..."
    menu:
        lola[37] ".........................................................................................."
        "\"What do you think you're doing girl!?\"":
            lola[36] "What?"
            lola[42] "I'm just trying to be nice to the elderly..."
        "\"Nice! Now shake them for him.\"":
            lola[36] "What?"
            sch8 "Yes, yes, shake'em for me girl..."
            lola[36] "Are you making fun of me? I don't want to!"
        "\"Ok, that's enough. Cover up.\"":
            lola[37] "Alright, alright..."
    show blkfade with Dissolve(.3)
    pause.5
    hide blkfade with Dissolve(.3)
    sch8 "What a treat for these sore eyes it was. Thank you, kind girl!"
    stop music fadeout 1
    lola[6] "Any time, gramps!"
    lola[5] "Huh!?"
    with hpunch
    sch7 "Kind master, be careful! That man is a well-known cut-purse!"
    with flashbulb
    play music "music/Vision2.mp3" fadein 1 fadeout 1 #TENSION
    ">Someone cuts your purse with 100 gold coins in it off your belt."
    $ renpy.play('sounds/iris_run.mp3')
    $ gold -=100
    menu:
        lola[5] "Hey! He took your money! He's running away!"
        "-Chase after the thief-":
            ">You rush after the thief."
            lola[40] "Go get him, old man!"
            sch8 "Can I see your tits again?"
            lola[1] "Sure!"
            show blkfade with Dissolve(.3)
            pause.5
            show image im.Alpha("interface/blackfade.png", 0.5) behind blkfade
            hide blkfade with Dissolve(.3)
            if strength >= 0 and strength < 4:
                $ renpy.play('sounds/iris_run.mp3')
                "You are running through the narrow streets of the cheapside trying to keep up with the thief."
                "You push your body to the limit and very soon start to feel short of breath."
                "The thief got away... Maybe you could have caught up with him if you weren't in such a bad shape."
                show blkfade with Dissolve(.3)
                pause.5
                hide image im.Alpha("interface/blackfade.png", 0.5) behind blkfade
                hide blkfade with Dissolve(.3)
                lola[7] "So he stole your money, big deal..."
                lola[8] "You have tons more, right?"
                jump runningfromden
            elif strength >= 4 and strength < 7:
                "You're running through the narrow streets of the cheapside trying to keep up with the thief."
                "You push your body to the limit and very soon start to feel short of breath."
                "You can hardly breathe and the distance between you and the thief is starting to grow rapidly..."
                $ renpy.play('sounds/iris_run.mp3')
                "Suddenly the thief takes a sharp turn and disappears behind a door of one of the building..."
            elif strength >= 7:
                ">You are running through the narrow streets of the cheapside trying to keep up with the thief."
                ">You put all of your strength into it and the distance between you and the thief starts to shorten quite rapidly."
                $ renpy.play('sounds/iris_run.mp3')
                ">Suddenly the man takes a sharp turn and you have to slow down..."
                ">He makes a few more turns but every time you are right behind him and even manage to get closer..."
                ">The Thief takes a sharp turn again and disappears behind a door of one of the buildings..."
            ">You reach the door but it appears to be blocked from the inside..."
            if strength >= 0 and strength < 7:
                ">You struggle to catch your breath...."
                ">The door looks very sturdy but you don't have much choice but to try and take it down..."
                ">You rush the door with your shoulder over and over again..."
                ">You are about to give up on the whole thing, when to your own surprise the door finally budges."
                $ renpy.play('sounds/door.mp3')
                show blkfade with Dissolve(.3)
                pause.5
                hide blkfade with Dissolve(.3)
            elif strength >= 7:
                ">Instead of slowing down you pick up the speed and ram the door with your shoulder."
                $ renpy.play('sounds/door_down.mp3')
                with hpunch
                ">The door breaks in two and dozens of splinters of various caliber fly in every direction!"
            ">You are inside the building, that appears to be an outlaw's den of some sort."
            ">You identify your thief instantaneously, but there are at least five more men in the room, and all of them are looking ready to fight."
            ">They are definitely about to attack you."
            menu:
                "-Retreat through the door-":
                    ">You wisely decide that a few stinking gold coins are not worth risking your health over and beat a hasty retreat..."
                    ">You go back and find Lola."
                    ">Apparently she already alerted the city guard, but by the time they arrive the outlaws are long gone."
                    hide image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
                    play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
                    lola[0] "I've been worried about you, old man..."
                    lola[0] "Glad you're alright..."
                    jump runningfromden
                "-Try to take them on-":
                    show blkfade with Dissolve(.3)
                    pause.5
                    hide blkfade with Dissolve(.3)
                    if strength >= 0 and strength < 9:
                        ">You pick up a wooden plank and charge the thief and his buddies."
                        ">You try to fight them and even manage to knock one of them out and give another one a bloody nose before they overpower you..."
                        with flashblood
                        ">You take a hard kick into a knee and fall on the ground..."
                        hide image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
                        play music "music/JafarsHour.mp3" fadein 1 fadeout 1 #JAFAR
                        sch12_2 "What's going on here!"
                        show image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
                        ">The city guard charges the bandits and they scatter..."
                        hide image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
                        sch12_2 "Are you alright, buddy?!"
                        sch12_2 "Easy now... You took a good beating..."
                        sch12_2 "Your girl alerted the city guards so I was sent to investigate..."
                        sch12_2 "I would never notice this place if not for the broken door..."
                        sch12 "Did you do that? I told you those exercises will pay off eventually!"
                        play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
                        lola[10] "Old man, old man, are you alright?!"
                        lola[9] "Oh my good, you are bleeding!"
                        sch12_2 "He will be alright, girl..."
                        show blkfade with Dissolve(.3)
                        pause 1
                        hide blkfade with Dissolve(.3)
                        lola[8] "This was so exiting..."
                        lola[8] "I can't believe you just ran after that thief like that..."
                        lola[7] "Like \"how dears he to take yours from you\", right?"
                        lola[7] "You are one bad-ass old man ..."
                        lola[5] "Oh, wait, you are bleeding again, let me help you out..."
                        lola[7] "This is so cool..."
                        show blkfade with Dissolve(.7)
                        ">You take Lola back to the brothel. Your date with her is over."
                        ">You are missing 100 gold coins, but today Lola changed her opinion about you."
                        jump dayends
                    elif strength >= 9:
                        ">You pick up a broken wooden chair and charge the thief and his buddies."
                        ">You swing the chair like a club and manage to do a great deal of damage to your attackers before it breaks to pieces..."
                        ">As soon as you looe your \"weapon\" the bandits counter attack..."
                        with vpunch
                        with flashblood
                        ">You take a few heavy punches and start to retreat..."
                        ">One of the skinnier bandits lands a rather clumsy punch onto your chest, and you seize the opportunity!"
                        ">You grab his arm, yank him towards you and put him on your shoulders like another man would put on a scarf..."
                        ">You let out a groan and throw the man into his buddies..."
                        $ renpy.play('sounds/groan.mp3')
                        pause 1
                        $ renpy.play('sounds/door_down.mp3')
                        with hpunch
                        ">The bandit that you threw was pretty skinny, but your attackers took a good note of your strength..."
                        ">You rush them while they hesitate..."
                        with vpunch
                        with hpunch
                        ">You dish out punches left and right. You take considerable amounts of damage yourself, but the bandits are starting to fall to the ground one after another..."
                        hide image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
                        play music "music/JafarsHour.mp3" fadein 1 fadeout 1 #JAFAR
                        sch12_2 "What's going on here!?"
                        sch12_2 "Hey, are you alright?!"
                        sch12_2 "Easy now... We will take care of these guys..."
                        sch12_2 "You gave them a good beating... But from the looks of it you also did miss quite a few punches yourself..."
                        sch12 "Still... There were six of them and you defeated them all..."
                        sch12 "What did I tell you? Eat your proteins, do your exercises and the life will provide..."
                        sch12_2 "Your girl alerted the city guards so I was sent to investigate..."
                        sch12_2 "I would've never noticed this place if not for the broken door..."
                        sch12 "Did you do that? I told you those excercises will pay off eventually!"
                        play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
                        lola[10] "Old man, old man, are you alright?!"
                        lola[9] "Oh my good, you are bleeding!"
                        sch12_2 "He will be alright, girl..."
                        show blkfade with Dissolve(.3)
                        pause 1
                        hide blkfade with Dissolve(.3)
                        lola[8] "This was so exiting..."
                        lola[8] "I can't believe you just ran after that thief like that..."
                        lola[7] "Like \"how dares he to take yours from you\", right?"
                        lola[7] "You are one bad-ass old man ..."
                        lola[5] "Oh, wait, you are bleeding again, let me help you out..."
                        lola[7] "(This is so cool...)"
                        show blkfade with Dissolve(.7)
                        ">You take Lola back to the brothel. Your date with her is over."
                        ">You successfully captured the thief and got your 100 gold coins back."
                        $ gold +=100
                        ">Your relationship with Lola has improved."
                        ">Today Lola changed her opinion about you."
                        jump dayends
        "-Give up on money and stay with Lola-":
            pass
label giveupmoney:
    lola[5] "Huh? You're not going after him?"
    stop music fadeout 1
    sch7 "Wise choice, kind master..."
    lola[43] "Well, yeah, it's only money, so as long as you have more of those it's just not worth it I suppose..."
    lola[5] "And you do have much, much more of them, right?"
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    menu:
        sch7 "Kind master does? A coin for the poor, then?"
        "\"I just got robed! Have you no shame?!\"":
            sch7 "No shame, no dignity... Crocus has nothing..."
            sch7 "Poor, feeble crocus..."
        "\"Sure. (Give crocus few gold coins.)\"":
            ">You give the beggar 10 gold coins."
            $ renpy.play('sounds/coins.mp3')
            $ gold -=10
            sch8 "Thank, thank you, kind master. I wish you and your little companion all the best!"
            lola[6] "Thanks, gramps!"
        "\"Lola, show him your tits again.\"":
            lola[6] "OK!!!"
            show blkfade with Dissolve(.3)
            pause 1
            hide blkfade with Dissolve(.3)
            lola[37] "........................................................................\n........................................................................\n........................................................................"
            sch8 "Yes, yes... This is great... Just stand like this, little one..."
            lola[36] "What are you doing, gramps?"
            sch8 "Nothing, nothing, my girl... I have an itch in my crotch and I'm scratching it, that's all..."
            lola[37] "Oh, OK!"
    label runningfromden:
    show blkfade with Dissolve(.3)
    pause 1
    hide blkfade with Dissolve(.3)
    lola[0] "Alright, so let's keep going?"
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1 #SAD
    #play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
    show image im.Alpha("interface/blackfade.png", 0.5) behind blkfade
    ">You keep going through the cheapside, but all you can see is dozens and dozens of beggars, piles of garbage and buildings in need of repairs..."
    hide image im.Alpha("interface/blackfade.png", 0.5) behind blkfade
    lola[9] "Yikes! So many people begging for money here..."
    menu:
        lola[9] "Can you give me a little gold coins so that I could give them to some of the people here?"
        "\"Just show them your tits.\"":
            lola[3] "Tsk... You can't feed the hungry with your tits..."
            lola[43] "Well, unless you want to feed them with milk..."
            lola[1] "heh..."
            lola[9] "Those poor people are starving, and you won't spare a coin?"
            lola[10] "Che-e-e-e-e-e-epo!"
            show blkfade with Dissolve(.3)
            pause.5
            ">You take Lola back to the brothel. Your date is over. You've been robed today and lost 100 gold coins."
            ">Your relationship with Lola has improved a little, although Lola now thinks that you are really really cheap."
            jump dayends
        "\"Sure. Here is 10 gold coins.\"":
            $ gold -=10
            lola[3] "Only 10? Well, better then nothing, I suppose..."
            show image im.Alpha("interface/blackfade.png", 0.5) behind blkfade
            ">You keep going and every now and then Lola stops to give another beggar a coin..."
            show blkfade with Dissolve(.3)
            ">You take Lola back to the brothel. Your date is over. You've been robed today and lost 100 gold coins."
            ">Your relationship with Lola has improved a little."
            jump dayends
        "\"Sure here is 80 gold coins.\"":
            $ gold -=80
            lola[5] "Wow! That's pretty generous, considering that you already got robbed today..."
            lola[5] "Are you that generous or that rich?"
            lola[6] "No matter! Thank you so much!"
            show image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
            ">You keep walking, but stop near every beggar so that Lola could give them a coin or two..."
            hide image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
            lola[6] "One for you, and two for you... la-la-la.{image=note.png}" 
            show image im.Alpha("interface/blackfade.png", 0.5) with Dissolve(.3)
            ">She seems to be having a great time."
            show blkfade with Dissolve(.3)
            ">You take Lola back to the brothel. Your date is over. You've been robed today and lost 100 gold coins."
            ">Your relationship with Lola has improved. Lola thinks of you as of a kind and generous person man."
            jump dayends
        "\"I got robbed. No charity today!\"":
            lola[10] "You are so mean, and cheap, and boring..."
            lola[2] "Take me home now!"
            show blkfade with Dissolve(.3)
            ">You take Lola back to the brothel. Your date is over. You've been robed today and lost 100 gold coins."
            ">Despite everything your relationship with Lola improved a little."
            ">Lola respects you more now... go figure!"
            jump dayends
            


            
            

  

##############MARKET###############################
label loladatemarket:
    
    $ bought4loli = 0
    $ tempflag1 = False
    $ tempflag2 = False
    lola[11] "Yes! Yes! Let's go to the market!"
    show blkfade with Dissolve(.3)
    $ renpy.play('sounds/door2.mp3')
    pause 1
    hide blkfade with Dissolve(.3)
    #play music "music/Marketplace(short).mp3" fadein 1 fadeout 1 #MARKET
    lola[5] "So many people here..."
    lola[8] "Look at that store over there...."
    lola[7] "No, look at this one!"
    lola[6] "They have all sorts of things for sale here...."
    menu:
        lola[8] "Will you buy something for me?"
        "\"What? Out of question!\"":
            lola[3] "I see..."
            lola[3] "Alright, I'll just look at things then!"
        "\"Maybe, if you behave.\"":
            lola[6] "I will, I promise!"
        "\"No problem. Whatever you want.\"":
            lola[7] "Really?!"
            lola[8] "You're the best!"
    lola[6] "Hurry up, let's visit that store over there..."
    lola[5] "And then that one..."
    lola[1] "No wait, can we go visit this one first!"
    lola[5] "So many things on sale here!!!"
    $ renpy.play('sounds/iris_run.mp3')
    show blkfade with Dissolve(.3)
    pause 1
    hide blkfade with Dissolve(.3)
    sch5 "Hello my friend. Nice to see you."
    sch5 "Who is your little companion?"
    lola[0] "Hello, mister."
    sch5 "Aren't you the cutest?!"
    lola[6] "Me-he-he! That's me!"
    sch5 "A cutie like you must love fruits?"
    lola[9] "Actually I'm looking for a ball-candy on a stick."
    lola[9] "Do you know where they sell'em, mister?"
    sch5 "Candy-balls? Sure... You just keep going this way and on your right you will see a candy stand."
    sch5 "They should have all sorts of sugary treats there."
    lola[0] "Great! Thank you, mister!"
    sch5 "You are very welcome, little thing."
    lola[7] "Come on, old man, hurry up! I wanna see if they really sell my ball-candy there."
    $ renpy.play('sounds/iris_run.mp3')
    show blkfade with Dissolve(.3)
    pause 1.5
    hide blkfade with Dissolve(.3)
    lola[8] "Oh my god! So many sweets!"
    lola[3] "I only care for the ball-candy on sticks, though..."
    menu:
        lola[8] "Will you buy me one? \nPlease? Pretty please?"
        "-Buy a ball-candy on a stick for 30 gold.-":
            $ gold -=30
            $ tempflag1 = True
            $ bought4loli +=1
            "You bought a candy for 30 gold coins."
            lola[6] "Thank you! You're the best!"
        "-Do not buy. Save money.-":
            lola[9] "I really wanted that candy..."
            lola[10] "Why do you have to be so cheap?"
    show blkfade with Dissolve(.3)
    pause.5
    hide blkfade with Dissolve(.3)
    if tempflag1:
        lola[26] "Hey, what is this store selling? *Slurp-slurp!*"
        lola[27] "*Slurp!* Who would buy these silly things?"
        lola[28] "Hey, how about this one?"
        lola[29] "Oh, no wait, they sell hairbands over there!"
        lola[29] "Let's go let's go!!"
        show blkfade with Dissolve(.3)
        pause.5
        hide blkfade with Dissolve(.3)
        lola[27] "Oh... this one is cute...*slurp!*"
        lola[28] "And this one is so pretty..."
        lola[27] "Hm.......*slurp-slurp-slurp*"
        lola[29] "Oh, wow! I love this one!"
    else:
        lola[0] "Hey, what is this store selling?"
        lola[6] "He-he, who would buy these silly things?"
        lola[8] "Hey, how about this one?"
        lola[5] "Oh, no wait, they sell hairbands over there!"
        lola[5] "Let's go let's go!!"
        show blkfade with Dissolve(.3)
        pause.5
        hide blkfade with Dissolve(.3)
        lola[8] "Oh... this one is cute..."
        lola[5] "And this one is so pretty..."
        lola[7] "Hm......."
        lola[8] "Oh, wow! I love this one!"
    menu:
        lola[30] "Em... Would you buy this hairband for me?"
        "-Buy a hairband for 70 gold coins.-":
            ">You bought a hairband for 70 gold coins."
            $ gold -=70
            $ tempflag2 = True
            $ bought4loli +=1
            lola[30] "Thank you so much!"
        "-Do not buy. Save money.-":
            lola[33] "Tsk... Whatever... Keep your money, you cheapo..."
    show blkfade with Dissolve(.3)
    pause 1
    hide blkfade with Dissolve(.3)
    if bought4loli == 2:
        lola[31] "I had such a great time today! \n*Slurp-slurp!*"
        lola[31] "Thank you for taking me here!! And for buying me all this stuff!"
        lola[31] "So... Let's go home?"
        show blkfade with Dissolve(.7)
        ">You take Lola back to the brothel."
        ">Your relationship with Lola has improved today."
        $ loladates += 1
    elif bought4loli == 1:
        if tempflag1:
            lola[27] "Well, this was fun..."
            lola[28] "Thank you for taking me here."
            lola[27] "Let's go home now?"
            show blkfade with Dissolve(.7)
            ">You take Lola back to the brothel."
            ">Your relationship with lola didn't change much."
        elif tempflag2:
            lola[32] "Well, this was fun..."
            lola[32] "Thank you for taking me here."
            lola[32] "Let's go home now?"
            show blkfade with Dissolve(.7)
            "You take Lola back to the brothel."
            "Your relationship with lola didn't change much."
    elif bought4loli == 0:
        play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
        lola[3] "Well, this was \"fun\"..."
        lola[3] "Thank you for taking me here."
        lola[3] "Let's go home now..."
        show blkfade with Dissolve(.7)
        ">You take Lola back to the brothel."
        ">Your relationship with lola has gotten worse."
        $ loladates -= 1
    $ quest7food = False
    $ ldatemarket = False
    hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
    ">It's getting late. You decide to head home."
    jump dayends
############Tavern#############################
label loladatetavern:
    $ quest7food = False
    $ loladates += 1
    $ ldatetavern = False
    lola[11] "Yes, yes, let's visit that tavern Iris works at..."
    $ renpy.play('sounds/door2.mp3')
    show blkfade with Dissolve(.5)
    pause 2
    hide blkfade with Dissolve(.5)
    show image "04_pt/slavem/bld2.png" with Dissolve(.3)
    show lola_f 13 at left with d3
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    sch1000 "It's pretty much empty..."
    show lola_f 14 at left with d3
    sch1000 "Right, Iris told me that it's usually like this during the day..."
    hide lola with d3
    show lola_f 15 at left with d3
    sch1000 "Let's get a table and something to drink!"
    show blkfade with Dissolve(.5)
    pause 1
    hide lola
    hide blkfade with Dissolve(.5)
    show lola_f 13 at left with d3
    sch1000 "I wonder if Iris is working today..."
    hide lola with d3
    show iris 17 at center with d3
    sch1100 "Welcome to \"The Blue Bull\" tavern..."
    sch1100 "Oh, it's you guys..."
    hide iris with d3
    show iris 18 at center with d3
    sch1100 "Listen, father still doesn't know that I'm also working in the brothel, so just act normal, OK?"
    sch1100 "Let me pour you some wine then..."
    hide iris with d4
    ">Iris bends over a little and pours wine into your cup..."
    menu:
        "-Give her butt a squeeze-":
            ">You reach out, grab one of the girl's butt cheeks and give it a good squeeze..."
            show iris 100 at center with d4
            sch1100 "Careful... The place is almost empty today..."
            sch1100 "My father might notice..."
            show lola_f 14 at left
            show iris 75 at center
            with d4
            sch1000 "You have the best job, Iris..."
            hide lola
            hide iris
            with d5
        "\"Lola, grab her ass!\"":
            show lola_f 15 at left with d3
            sch1000 "Really?"
            sch1000 "Alright!!!"
            show iris 101 at center
            hide lola
            with d3
            sch1100 "What?"
            hide lola
            hide iris
            with d5
            ">Lola reaches out and grabs one of the Iris' butt cheeks. \nYou do the same..."
            show iris 102 at center with d3
            sch1100 "What? What are you doing, guys? Stop it, you will get me in trouble!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            hide iris with d5
        "-Give her butt a slap-":
            $ renpy.play('sounds/slap.mp3')
            with hpunch
            show iris 100 at center with d3
            sch1100 "Hey... Careful, not so loud." 
            show lola_f 14 at left
            show iris 75 at center
            with d3
            sch1000 "Me too, me too!"
            $ renpy.play('sounds/slap.mp3')
            with hpunch
            show iris 100
            sch1100 "Lola?! What are you doing? Women are not supposed to do this..."
            show lola 13 with d3
            sch1000 "Really? Oh, I didn't know, sorry..."
            hide iris with d3
            show iris 100 with d3
            sch1100 "That's OK..."
    show blkfade with Dissolve(.5)
    pause 1
    hide lola
    hide iris
    hide blkfade with Dissolve(.5)
    lola[44] "Mom says that you are very popular among the customers these days..."
    show iris_f 28
    sch1100 "Shush! Keep it down, you silly girl."
    sch10_45 "Oops, sorry."
    show iris_f 19
    sch1100 "But yeah... Every time I come to the \"Phoenix\" I have customers already waiting for me..."
    sch1100 "That's quite amazing... I never thought I could be that popular..."
    sch10_46 "Yes, men seem to like you a lot... What's your secret?"
    show iris_f 21
    sch1100 "A secret? Don't be silly, there is no such thing..."
    sch10_46 "Hm... You always swallow, right?"
    hide iris with d3
    show iris 22 with d3
    sch1100 "What? Lola, honestly, are you stupid or something?"
    sch1100 "Can we {size=+7}not{/size} discuss this {size=+5}here{/size}?"
    sch10_45 "Right, right, I'm sorry, Iris. Don't get mad."
    show iris 27 with d3
    sch1100 "I'm not mad, I just don't want to get in trouble with my father..."
    sch1100 "Let's just change the topic, ok?..."
    hide iris with d3
    show iris_f 29 with d3
    sch1100 "So what brings you guys here today?"
    sch10_46 "My curiosity!"
    sch10_46 "I've never been to an actual tavern before..."
    sch1100 "Really, how come?"
    sch10_45 "My mother wouldn't let me..."
    sch1100 "I see..."
    show iris 24 with d3
    sch1100 "What do you think of this place then? Do you like it here?"
    sch10_46 "I love it!"
    sch10_46 "You told me that, you guys, dance for the patrons sometimes..."
    show iris 20 with d3
    sch1100 "Well, yeah, but during the night hours..."
    sch10_44 "I would love to see you dance...."
    show iris 28 with d3
    sch1100 "Tsk... my father still wouldn't let me..."
    play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
    hide iris
    show maslab 7 at right
    show iris 28 at left
    with d3
    sch600 "You and your dancing..."
    hide iris with d3
    show iris_f 28 at left
    sch1100 "Father? How long have you been listening?"
    hide maslab with d3
    show maslab 3 at right with d3
    sch600 "Long enough to hear that you are still hung up on your silly idea to dance with the rest of the girls..."
    show iris_f 65 with d3
    sch1100 "But everyone is doing it!"
    hide maslab with d3
    show maslab 6 at right with d3
    sch600 "You are my daughter! You're not gonna dance! Not under my roof!"
    show iris_f 28 with d3
    sch1100 "Fine! I'm gonna be a whore then!"
    hide maslab with d3
    show maslab 8 at right with d3
    sch600 "What? Have you lost your mind!?"
    hide iris with d3
    show iris_f 28 at left with d3
    sch1100 "You embarrass me in front of my friends! I hate you!"
    hide iris with d3
    $ renpy.play('sounds/iris_run.mp3')
    hide maslab with d3
    show maslab 3 at right with d3
    sch600 "Where are you going! I'm still talking to you! Come back here!"
    hide maslab with d3
    sch10_47 "..........."
    sch10_47 "........................"
    sch10_47 "........................................"
    sch10_48 "I don't feel like staying here any longer... Let's sneak out quietly..."
    show blkfade with Dissolve(.5)
    pause 1
    $ renpy.play('sounds/door2.mp3')
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
    hide image "slavem/bld2.png" 
    hide blkfade with Dissolve(.5)
    sch10_8 "Thank you for taking me to see an actual tavern..."
    sch10_9 "I hope Iris will be alright..."
    show blkfade with Dissolve(.5)
    pause 1
    ">You take Lola home. Your relationship with her has improved."
    jump dayends
####BROTHEL##########################
label loladatebrothel:
    $ ldatebrothel = False
    sch10_13 "You want to stay here at Mom's brothel?!"
    sch10_13 "But I spend all my time here as it is..."
    sch10_11 "I want to go somewhere esle."
    jump lolaout2
###STORE######
label loladatestore:
    $ quest7food = False
    $ loladates += 1
    $ ldatestore = False
    sch10_11 "Yeah! Let's go visit Azalea!"
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with Dissolve(.3)
    $ renpy.play('sounds/door2.mp3')
    pause 1.5
    hide blkfade with Dissolve(.3)
    $ renpy.play('sounds/door.mp3')
    sch2 "Hello, mister. Welcome to my store."
    sch10 "Hello Azalea."
    sch2 "Hey, kiddo."
    sch10_2 "What did I tell you about calling me that?"
    sch3n "Alright, alright. Hello, old mature woman..."
    sch10_3 "Yeah, whatever...."
    sch10 "Oh, hey, what's this?"
    sch5n "Huh?"
    sch10 "Wow, what is that? ...A necklace?"
    sch10 "How do I wear it?"
    sch6n "What?"
    sch10_39 "Phas-phis? \n{size=-4}(Like this?){/size}"
    sch2 "Hey, put that down, I'm still working on that one, you silly kid."
    sch10_38 "Pha-phaki. Kha-pha-peeth? \n{size=-4}(I like it. Can I keep it?){/size}"
    sch3n "No, I said put it down..."
    sch10_3 "Fine... You're no fun today."
    sch2 "What about you mister? See anything you like?"
    sch10_7 "Like your tits?"
    sch7n "What? Hey!"
    menu:
        sch10_7 "What do you think of her outfit, old man? Do you like it?"
        "\"Yeah. It's great.\"":
            sch2 "You see? He likes it!"
            sch10_40 "Well, of course he does! He can totally see you nipples in that thing!"
        "\"Meh... It's OK.\"":
            sch10_1 "You see? He doesn't like it!"
            sch10_1 "You wanna know why? Because he can totally see you nipples in that thing!"
            sch10_7 "That's insulting!"
        "\"I'm not old.\"":
            sch2 "Yeah, you keep calling him that, but he doesn't look that old to me either."
            sch10_5 "What are you talking about! The man is ancient! Aren't you, old man?"
            sch10_6 "He probably was already around when the catastrophe hit."
            sch3n "What? Don't be silly!"
            sch10_7 "Yeah, you see how quiet he's gotten? You wanna know why?"
            sch10_40 "Because he can totally see you nipples in that thing!"
    sch2 "Hey, you make it sound like if I'm topless here or something."
    sch2 "I'm wearing a top."
    sch10_7 "You do, do you?"
    sch10_7 "Sorry I guess I didn't notice it..."
    sch10_6 "Because your nipples distracted me!"
    sch2 "The-hee-hee. What about you, you little slut!?"
    sch2 "I'm sure your friend here is having a hard time hanging out with you, because your tits are barely covered."
    sch2 "He's having a \"hard time hanging out\", got it?"
    sch10_3 "Whatever, topless girl. It's a fair game as long as your nipples covered."
    sch10_40 "But I can see your's clearly!"
    sch10_2 "Yeah, you might as well take that stupid thing off!"
    show image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
    ">Lola grabs the piece of silk covering Alzalea's breasts and rips it off her body!"
    play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
    hide image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
    sch10_2 "There! Much better this way! I can be a dress designer too!"
    sch8n "You little whore! Come here!"
    show image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
    sch1000 "Whe-ee-ee! No, leave me alone!"
    sch1000 "Don't touch me! Ha-ha-ha!"
    ">Girls start to wrestle and Azalea pulls Lola's top all the way up!"
    show image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
    sch2n "There! Now we're even!"
    sch10_41 "What are you doing, you whore!"
    sch9n "You are the whore!"
    sch10_37 "No, you are!"
    sch2n "No you are!"
    menu:
        sch10_35 "Shut your face, whore! Let's make the old man decide!"
        "\"Lola is a whore.\"":
            sch2n "You see, you see? Even your friend is agreeing with me!"
            sch10_37 "Of course he does! You are half naked!"
            sch9n "You are half naked too!"
            sch10_37 "Not as much as you are, you slut!"
        "\"Azalea is a whore.\"":
            sch10_37 "Aha! The wise old man has spoken!"
            sch2n "He doesn't look that old to me..."
            sch10_36 "Doesn't matter! I won!"
            sch2n "No you didn't!"
            sch10_36 "Yes, I did, you slut!"
        "\"You both are whores.\"":
            sch10_36 "Hey, how rude!"
            sch9n "Yeah, what's the matter with you, being so mean out of sudden..."
            sch10_37 "To be fair though, you are half-naked."
            sch2n "Oh, yeah? What about you? Your tits are in a plain view!"
            sch10_36 "{size=+5}You{/size} did this, you slut!"
        "\"No one is a whore.\"":
            sch10_36 "Whaaaat? Are you starting to loose your sight old man?"
            sch10_36 "That girl is topless!"
            sch2n "What about you? Your tits are in a plain view as well!"
            sch10_37 "Whatever, slut!"
    sch2n "Hey, don't call me a slut!"
    sch10_41 "Slut, slut, slut, slut, sluterson, slut, sluuuut!"
    sch10n "Come here, you brat!"
    sch10_42 "Whee-eee! No, you keep your nipples away from me!"
    show blkfade with Dissolve(.3)
    ">You had a great time today, and so did Lola. Your relationship with her has improved greatly."
    jump dayends
#################PALACE###############
label loladatepalace:
    $ titsout = False
    sch10_11 "The Slave-girl school? How exiting! Let's go!"
    show blkfade with Dissolve(.3)
    $ renpy.play('sounds/door2.mp3')
    pause 1.5
    hide image "slavem/bld.png" 
    hide blkfade with Dissolve(.3)
    show image "slavem/bld2.png" with Dissolve(.3)
    show image im.Flip("lola_dates/l10.png", horizontal=True) at left with Dissolve(.3)
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    #play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
    sch1000 "Jafar's Slave-Girl Academy... I heard all sorts of funny rumors about this place..."
    sch1000 "I wonder if any of it are actually true..."
    hide image im.Flip("lola_dates/l10.png", horizontal=True) at left with Dissolve(.3)
    menu:
        "\"It's all true.\"":
            show image im.Flip("lola_dates/l11.png", horizontal=True) at left with Dissolve(.3)
            sch1000 "Really? Amazing....."
            hide image im.Flip("lola_dates/l11.png", horizontal=True) at left with Dissolve(.3)
        "\"it's all lies.\"":
            show image im.Flip("lola_dates/l11.png", horizontal=True) at left with Dissolve(.3)
            sch1000 "I don't believe you."
            hide image im.Flip("lola_dates/l11.png", horizontal=True) at left with Dissolve(.3)
            show image im.Flip("lola_dates/l12.png", horizontal=True) at left with Dissolve(.3)
            sch1000 "You don't even know what \"things\" I'm talking about..."
            hide image im.Flip("lola_dates/l12.png", horizontal=True) at left with Dissolve(.3)
        "\"................\"":
            show image im.Flip("lola_dates/l12.png", horizontal=True) at left with Dissolve(.3)
            sch1000 "I bet it's true! All of it!!!"
            hide image im.Flip("lola_dates/l12.png", horizontal=True) at left with Dissolve(.3)
    show image im.Flip("lola_dates/l11.png", horizontal=True) at left with Dissolve(.3)
    sch1000 "It's so quiet here... I wonder what's going on inside..."
    sch1000 "You think they would let us in?"
    hide image im.Flip("lola_dates/l11.png", horizontal=True) at left with Dissolve(.3)
    menu:
        "\"Let's sneak in.\"":
            show image im.Flip("lola_dates/l06.png", horizontal=True) at left with Dissolve(.3)
            sch1000 "Really? OK!!!"
            hide image im.Flip("lola_dates/l06.png", horizontal=True) at left with Dissolve(.3)
            show blkfade with Dissolve(.3)
            ">You find a back door and sneak into the academy's building..."
            play music "music/croft_manor.mp3" fadein 1 fadeout 1
            $ renpy.play('sounds/door.mp3')
            pause 1.5
            hide image "slavem/bld2.png" 
            hide blkfade with Dissolve(.3)
            show image "slavem/bld.png" with Dissolve(.3)
            sch10_5 "(Wow... This place is huge...)"
            ">A couple of students walks by you... They pay you no mind."
            sch10_7 "(Did you see those outfits? I could totally see their nipples!)"
            sch10_6 "(This place is even more fun then mom's brothel!)"
            play music "music/JafarsHour.mp3" fadein 1 fadeout 1 #JAFAR
            jaf3 "And who are you supposed to be?"
            sch10_5 "Yikes!!!"
            menu:
                "\"Your majesty!\"":
                    jaf2 "Huh?"
                    jaf2 "Oh, it's you, old man?"
                "\"Jafar? Hey, man!\"":
                    jaf3 "\"Hey, man\"? Are you trying to be funny with me, peasant?"
                    jaf3 "Your insolence will cost you--"
                    jaf2 "Wait a second, it's you, old man. I didn't recognize you at first."
            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
            jaf6 "What are you doing sneaking around my school? Don't you have anything better to do?"
            jaf6 "How is our princess faring?"
            jaf6 "Is there any progress in her.... education?"
            menu:
                "\"Yes. She's almost ready.\"":
                     jaf "Splendid! I knew you wouldn't let me down, old man."
                     jaf "This is a great news indeed."
                "\"Yes. But I will need more time.\"":
                    jaf2 "I see... Well, there is no rush..."
                    jaf4 "Just make sure she is fully trained and completely broken before the wedding day, that's all I ask of you."
                "\"No. She is so stubborn!\"":
                    jaf3 "That insolent woman... I true princess nothing less..."
                    jaf2 "But you better succeed, in this, old man."
                    jaf2 "You know, I do not tolerate failure..."
            jaf7 "Huh?!"
            jaf3 "Hey, you girl."
            sch10_9 "M-me? Y-your H-highness?"
            jaf3 "Yes, girl, you. Why aren't you wearing your uniform?"
            sch10_9 "I..."
            sch10_9 "I'm n-not..."
            sch10_10 "I'm sorry, your majesty."
            jaf3 "What are you mumbling down there? Are you being disobedient with me, girl?"
            sch10_10 "N-no, your highness, I wouldn't dare..."
            jaf6 "Show me your tits, girl!"
            $ titsout = True
            sch10_9 "Of course, your highness!"
            sch10_9 "........................"
            show blkfade with Dissolve(.3)
            pause.5
            hide blkfade with Dissolve(.3)
            sch10_34 "...........................................\n...........................................\n..........................................."
            jaf "Hm... Good. There is still hope for your left I suppose..."
            jaf6 "But next time make sure you wear your uniform inside the school building."
            sch10_34 "Of course, your majesty. I'm so very sorry."
            jaf2 "Alright, I will be on my way then."
            jaf4 "Today I'm giving a lecture on \"Men are from mars, women are from the pits of hell\" theory."
            jaf2 "I hope to hear some good news from you soon, old man..."
            show blkfade with Dissolve(.3)
            pause.8
            hide blkfade with Dissolve(.3)
            with hpunch
            play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
            sch10_35 "{size=+7}Do you know who that was?{/size}"
            sch10_35 "Jafar himself! OMG! I'm such a big fan!!!"
            sch10_35 "And he was talking to you like if you know each-other?!"
            menu:
                "\"Yeah. He is like my buddy.\"":
                    sch10_36 "Really? This is so awesome!"
                    sch10_37 "I knew you were cool!"
                "\"He is my boss.\"":
                    sch10_37 "Well, he is a sultan. Kinda an everyone's boss by definition, wouldn't you say?"
                "\"Your tits are still hanging out.\"":
                    $ titsout = False
                    sch10_36 "Oh, right..."
                    show blkfade with Dissolve(.3)
                    pause.5
                    hide blkfade with Dissolve(.3)
                    sch10_1 "Me-hee-hee... I can't believe the sultan asked to see my tits..."
                    sch10_1 "I'm never gonna wash them again..."
                    sch10_9 "No, wait, that would be nasty..."
            show blkfade with Dissolve(.3)
            pause.5
            hide blkfade with Dissolve(.3)
            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
            sch "What is going on here? And why are you not wearing your uniform, girl?"
######################################################################################
        "\"Let's peek through a window.\"": 
            show image im.Flip("lola_dates/l06.png", horizontal=True) at left with Dissolve(.3)
            sch1000 "Yeah! Let's do that!!!"
            hide image im.Flip("lola_dates/l06.png", horizontal=True) at left with Dissolve(.3)
            show blkfade with Dissolve(.3)
            pause.5
            play music "music/croft_manor.mp3" fadein 1 fadeout 1
            ">You and Lola carefully walk around the building looking for a window to peek through..."
            hide blkfade with Dissolve(.3)
            sch10_6 "(Hey, here, how about this one!)"
            show image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
            ">You take a careful look through the window Lola pointed out."
            ">You see a classroom full of students."
            ">Some of the girls sitting on their stools others are on all fours, being the stools."
            hide image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
            sch10_5 "(Hey, hey, look at the teacher. Is that who I think that is?)"
            show image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
            ">You see the teacher giving a lecture. It's the headmaster himself - the Sultan jafar."
            hide image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
            sch10_5 "(It's him isn't it? I can't believe it! This place is so amazing!)"
            sch10_5 "(What do you think the lecture is about?)"
            menu:
                "\"About men being superior over women?\"":
                    sch10_6 "(You think? Isn't it pretty obvious? Why talk about it?)"
                "\"About women being superior over men?\"":
                    sch10_5 "(You think?)"
                    sch10_5 "(But it's not really true is it? I mean it's not a question of superiority...)"
                    sch10_6 "(Men are just men, and women are... just women... No?)"
                "\"About men and women being equal?\"":
                    sch10_6 "(Huh? In what way? That's silly.)"
                    sch10_5 "(Is it about women getting more masculine or about men becoming more feminine?)"
                    sch10_9 "(Neither is good for the society, wouldn't you agree?)"
                "\"Shush! Let's listen.\"":
                    sch10_8 "(OK!)"
                    show image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
                    ">You try to pick up on what jafar is saying."
                    ">You can't hear clearly and can only make out parts of what he says..."
                    jaf4 "...yes.......and that's how it is..."
                    jaf4 "......so if men came from mars, where did women come from I ask you?!...."
                    jaf4 "....been a big question for generations, ever since the catastrophe that singed our planet dead and turned it into a scorching desert...." 
                    jaf3 ".....ms. Fatima, what is it so interesting there? care to share it with the rest of us......."
                    jaf3 ".....yes......\n...all of your clothes please..."
                    jaf4 "...now write down \"I'm a silly, silly whore\" fifty times..."       
                    hide image im.Alpha("blackfade.png", 0.5) with Dissolve(.3)
            play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
            show blkfade with Dissolve(.3)
            pause.5
            hide blkfade with Dissolve(.3)
            sch "What is going on here?"
            sch10_5 "Busted!"
            sch "And why are you not wearing your uniform, girl?"

######################################################################################################
    
    if titsout:
        sch "And cover your tits, would you? We do not tolerate vulgarity in our academy."
        sch10_36 "Of course, miss. I'm s-sorry."
        show blkfade with Dissolve(.3)
        pause.5
        hide blkfade with Dissolve(.3)
        sch10_9 "......"
    sch"Who are you, girl? I do not recognize you."
    sch "Are you a freshman?"
    sch10_9 "Em..."
    menu:
        "\"She is with me.\"":
            sch "Is she now..."
            sch "And you are...?"
            sch "Oh, it's you, sir... It's nice to see you..."
        "\"Hello, mistress Rose.\"":
            sch "Oh, it's always nice to see one of our benefactors."
    sch "Headmaster Jafar is visiting our school today..."
    ros04 "His majesty even decided to give a short lecture for one of our most advanced classes."
    ros05 "Trully, our academy is the most prestigious institutions around. \nNo question about it."
    sch10_8 ".............................."
    ros04 "Are you here to entrust another one of your slave-girls to our care?"
    ros02 "This one {size=+5}does{/size} look like a {size=+5}very{/size} difficult child indeed."
    sch10_3 "(What?)"
    sch "I apologize, but I must leave you now."
    ros04 "My presence is required in the school's dungeons... er I mean, library."
    show blkfade with Dissolve(.3)
    pause.5
    hide blkfade with Dissolve(.3)
    sch10_1 "Did you see her dress?"
    sch10_7 "I coudn't see her nipples but pretty much everything else was on display!"
    sch10_9 "................"
    sch10_9 "This place is simply magical..."
    sch10_10 "Now I want to be a student here!"
    sch10_9 "You think mother will agree to pay the tuition?"
    sch10_3 "Yeah, fat chance of that happening..."
    sch10_6 "Anyway, thank you for bringing me here today."
    sch10_6 "I had a great time."
    sch10 "Let's go home?"
    $ quest7food = False
    $ loladates += 1
    $ ldatepalace = False
    show blkfade with Dissolve(1)
    hide image "slavem/bld.png" with Dissolve(.3) 
    ">You take Lola home. Your relationship with her has improved."
    jump dayends
####################LOLA NIGHT DATES##########
label lolaacademy:
    $ loladates += 1
    $ lnightacademy = False
    sch10_50 "The sultan's Palace? Cool! Let's go then!"
    show blkfade with d3
    $ renpy.play('sounds/door2.mp3')
    pause 2
    hide blkfade with d3
    
    sch10_49 "Wow....."
    sch10_49 "It looks even bigger in the dark..."
    sch10_50"I wonder how it would feel to live in this place... To be a princess, you know...?"
    sch10_33 "Hm...."
    sch10_33 "It's so quiet around here, and I don't see any guards..."
    sch10_30 "Don't you think it's almost too quiet?!"
    play music "music/Vision2.mp3" fadein 1 fadeout 1 #TENSION
    menu:
        sch10_30 "You think maybe something terrible happened to the guards?"
        "\"That's just your imagination.\"":
            sch10_33 "You think? Well, maybe you're right..."
            sch10_49 "I just thought that the palace is supposed to be well guarded at all times..."
            sch10_49 "Even more so during the night..."
            sch10_50 "But what do I know? I've never even been here before, so if you say that everything is fine then--"
        "\"You're right! We need to do something!\"":
            sch10_30 "Y-y-yes! I knew it! Something is definitely up!"
            sch10_30 "You think there may be thieves?"
            sch10_49 "They hired a whore to give poisoned wine to the city guards and then made their way into the the palace..."
            sch10_30 "Or maybe, it's a group of assassins..."
            sch10_49 "Their target is the Sultan, but they will eliminate anyone who would dare to stay in their way..."
            sch10_30 "And that's why the guards are nowhere to be found now!"
            sch10_30 "Because the assassins buried them alive!"
            sch10_30 "We might be standing on their graves right now--"
        "\"Let's leave before we get in trouble...\"":
            $ loladates -= 1
            $ lnightacademy = True
            sch10_33 "But I love trouble..."
            sch10_33 "Alright, alright, I'm going..."
            show blkfade with d3
            pause 1
            hide blkfade with d3
            play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
            jump wheretogowithl

    play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
    who "Yes...{image=textheart.png} Yes, like that...{image=textheart.png}"
    sch10_30 "(Yikes! Did you hear that?)"
    ".................................."
    ".................................."
    menu:
        "\"I don't hear anything.\"":
            sch10_49 "(That's because your hearing is no good anymore, old man.)"
            sch10_30 "(I definitely heard something...)"
        "\"Yes, I did!\"":
            pass
    whom "I don't know about this, Madder..."
    whom "Oh, quit your whining, Rasul. It's my treat..."
    who "So, you like it when I move my hand like this?"
    whom "Yes, of course, just keep going!"
    ".............................."
    sch10_30 "(The voices are coming from behind that bush...)"
    sch10_49 "(What do you think is going on there?)"
    ".............................."
    whom "I'm almost there... almost..."
    who "Yes, give it me!{image=textheart.png}"
    whom "Argh! Yeah! There, you dirty whore! All over you face!"
    who "Ahh...{image=textheart.png} Yes...{image=textheart.png}"
    whom "Me too, I'm about to..."
    whom "Take it in your mouth, slut. My friend here never came in a girl's mouth before."
    who "Really? That's adorable..."
    whom "Madder, shut up, you're ruining it for me..."
    whom "My bad. Well, I'm done here, so I'll just get back to my post. You kids have fun."
    who "Slurp, slurp, gltch, slurp....{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    $ renpy.play('sounds/rustling.mp3')
    menu:
        sch10_30 "Oh crap, someone's is coming!"
        "\"Shit! Time to run!\"":
            sch10_30 "Yes, let's go, let's go!!!"
            show blkfade with d5
            $ renpy.play('sounds/iris_run.mp3') #Run
            pause 1
            hide blkfade with d5
            sch10_30 "Ha-ha-ha! This was so much fun!"
            sch10_50 "I knew I would love the city during the night even more!"
            sch10_30 "I wonder who that girl was..."
            sch10_49 "Probably someone I know, a girl from mom's brothel..."
            sch10_50 "Well, I think that's enough for today, I'm getting a bit sleepy."
            if loladates == 5:
                jump bringlolahome
            else:
                sch10_50 "Will you take me home now?"
                ">You take Lola home. Your relationship with her has improved."
                show blkfade with Dissolve(.5)
                pause.5
                jump dayone
        "\"That's OK, I think I know him.\"":
            sch10_30 "Really?"
            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
            sch12 "Huh? who's there?!"
            sch12 "Oh, it's you, my friend."
            sch12 "What are you doing here?"
            sch12 "Taking another one of your slave-girls for a walk I see..."
            sch10_30 "Hello, mister."
            sch12 "good evening, citizen."
            whom "I'm about to... I'm about to..."
            who "Yes!{image=textheart.png} Release it all in my mouth!{image=textheart.png}"
            whom "Argh! You whore!"
            sch10_50 "!!!!!!!!!!!!!!!!!!!"
            sch12 "Heh, don't mind Rasul. Today is his birthday, so I bought him a whore from that \"phoenix\" place..."
            sch10_50 "I knew it! She must be someone I know!"
            whom "aha... aha.... can't believe you swallowed it all..."
            who "Well, your friend said it was your first time, so I wanted to make sure you remember it...{image=textheart.png}"
            whom "Thank you, err... whore."
            whom "I need to get back to my post now..."
            who "By all means...{image=textheart.png}"
            who "I will clean up a bit and then I'll be right behind you...{image=textheart.png}"
            $ renpy.play('sounds/rustling.mp3')
            pause 1
            sch4 "!!!!!!!!!!!!!!!!!!!"
            sch12 "Come on out, Captan. No need to be shy..."
            sch4 "Khem, good evening..."
            sch4 "Madder, what are you still doing here? Get back to your post at once!"
            sch12 "Alright! This is the captain I remember!"
            sch4 "I said now!"
            sch12 "Yessir!"
            sch12 "See you later guys!"
            sch4 "The palace is closed for visitors during the night... Leave now..."
            sch4 "Please hurry up..."
            $ renpy.play('sounds/rustling.mp3')
            who "What's this commotion about?"
            sch4 "Dammit..."
            dah5 "Hm...? Oh, hey, Lola."
            dah10 "Does your mom know that you are outside during the night?"
            sch10_49 "Crap..."
            sch4 "This is not what you think it is... I can explain..."
            dah4 "He's so adorable..."
            sch10_50 "That's OK, mister guard. I live in a brothel..."
            sch10_49 "Many of the city guards visit us every night..."
            sch10_50 "I don't remember seeing you there, though..."
            sch4 "Alright! I've had enough of this! Get out of here, all of you!"
            sch4 "I said leave now, or you will spend the rest of the night in the dungeon!"
            sch10_33 "I guess we better go..."
            dah5 "I hope I'll see you again, big guy... You were so..."
            dah7 "Delicious...{image=textheart.png}"
            sch4 "Please leave..."
    show blkfade with Dissolve(.5)
    play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
    pause 1
    hide blkfade with Dissolve(.5)
    dah3 "So, what are you guys up to?"
    sch10_16 "Nothing! The Old man here is just showing me the city..."
    dah2 "Really? Are you sure that's the only thing he is showing you...?"
    sch10_21 "Em... Yeah, whatever, sorry, I don't get \"grown-up\" jokes..."
    sch10_24 "Just don't tell my mom, OK?"
    dah3 "\"Grown-up\" jokes? You are only a few years younger than me, girl."
    sch10_20 "Just please don't tell my mom..."
    sch10_20 "She will ground me for life if she finds out..."
    dah2 "Alright... Alright... I will keep your little love affair a secret, but you owe me one..."
    sch10_24 "Love affair? Me and the old man?"
    sch10_24 "Oh, this joke I do get! It's funny."
    dah1 "No need to deny it... This man knows how to handle a woman properly, you are in for a treat!"
    sch10_19 "What?!"
    dah3 "Alright, I gotta go now. I want to take a bath before I go to sleep..."
    dah2 "Goodnight Lola."
    if loladates == 5:
        sch10_19 "Love affair? Heh..."
        sch10_19 "Grown-ups and their love bullshit..."
        sch10_22 "I don't mind sucking your old cock if needs be, but what's love have to do with it?"
        sch10_21 "Whatever..."
        sch10_18 "I had fun today. Thank you for spending your time with me..."
        jump bringlolahome
    else:
        sch10_24 "Wait, I'll go with you..."
        sch10_18 "Thank you for taking me out tonight, old man. It was fun..."
        sch10_24 "Dahlia will walk me back to the brothel... I will be save with her don't worry..."
        dah3 "Alright, let's go girl."
        dah2 "And as for you, my friend, you make sure you visit me again, soon, OK?"
        dah1 "It's been a while and I feel like I need some \"old man\" loving!"

        sch1000 "So, so, did you suck that guard's cock back there?"
        sch9 "Yup. His and his friend's."
        sch1000 "So cool! Tell me everything."

        ">You return home and go to sleep."
        ">Your relationship with Lola has improved."
        show blkfade with Dissolve(.5)
        pause.5
        jump dayone
#######NIGHT TAVERN##############
label lolatavern:
    $ loladates += 1
    $ lnighttavern = False
    sch10_30 "I've never been to a tavern during the night hours... This is gonna be fun!"
    show blkfade with Dissolve(.5)
    $ renpy.play('sounds/door2.mp3')
    pause 2
    hide blkfade with Dissolve(.5)
    $ renpy.play('sounds/door.mp3')
    show image "slavem/bld.png" with d3
    show image "slavem/bld2.png" with d3
    show maslab 1 at right with d3
    play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
    sch600 "Welcome, welcome my friend. *spit*"
    sch600 "Say, who is your little companion?"
    show lola_f 6 at left 
    show maslab 2
    with d3
    sch1000 "Good evening, mister."
    hide maslab with d3
    show maslab 2 at right with d3
    sch600 "You are the Fat Lily's kid, right? Loli, was it?"
    show lola_f 7 with d3
    sch1000 "Actually it's Lola..."
    show maslab 8 with d3
    sch600 "Really? I could've sworn your name was Loli..."
    show maslab 1 with d3
    sch600 "Well, in any case, sit anywhere you like, I will let Iris know that you guys are here..."
    show blkfade with Dissolve(.5)
    pause 1
    hide lola
    hide maslab
    hide blkfade with Dissolve(.5)
    show iris 17 with d3
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    sch1100 "Hello, guys. Welcome to \"The Blue Bull\"."
    hide iris with d3
    menu:
        "-Grab her butt-":
            ">You reach out and grab the girl's butt."
            show iris 100f with d3
            sch1100 "Hey, what are you doing? Not in front of Lola..."
            sch10_51 "Huh? Oh, don't mind me..."
            sch10_52 "Please, I want to see the actual night life, not the censored version..."
            sch10_53 "Plus, didn't you tell me the other day how much you love it when the old man here grubs your ass in front of everyone?"
            show iris 101f with d3
            sch1100 "Lola! You silly girl! I shared that only with you!"
            show iris 102f with d3
            sch1100 "So embarrassing... stupid child."
            sch10_54 "I'm sorry, Iris. Please don't get mad..."
            hide iris with d3
        "-Slap her butt-":
            $ renpy.play('sounds/slap.mp3')
            with hpunch
            pause.5
            show iris 100f at center with d3
            sch1100 "Do you have to be so loud?"
            sch10_52 "The other day you told you enjoy it!"
            sch10_53 "In fact \"The louder the better\" were the exact words."
            show iris_f 76 with d3
            sch1100 "I know... Just don't want to get in trouble with my old man, that's all..."
            hide iris with d3
        "\"Hello, Iris.\"":
            sch10_55 "What? Aren't you gonna grab her ass or something?"
            show iris_f 76 at center with d3
            sch1100 ".........................."
            sch10_53 "Come on, old man, she loves that!"
            hide iris with d3
            show iris_f 75 at center with d3
            sch1100 "Lola! Mind your own business please..."
            sch10_54 "Huh? What did I say?"
            hide iris with d3
    show blkfade with Dissolve(.5)
    pause.3
    hide blkfade with Dissolve(.5)
    sch10_51 "(So did you tell your father about your second job yet?)"
    show iris_f 19 at center with d3
    sch1100 "No, not really... I'm waiting for the right moment..."
    sch10_52 "(Which will happen never?)"
    hide iris with d3
    show iris_f 20 at center with d3
    sch1100 "Exactly! I don't think I will ever master enough courage to confess..."
    show iris_f 19 with d3
    sch1100 "Plus I really like how things are right now, don't want to change anything..."
    sch1100 "At the moment everyone seems to be happy, so why ruin it?"
    show iris_f 24 with d3
    sch1100 "What about you, girl? What does Lily say about you being out during the night..."
    sch10_52 "Me-hee-hee. She doesn't know..."
    sch10_54 "Please, don't tell her!"
    hide iris with d3
    show iris_f 23  with d3
    sch1100 "Of course, not, don't be silly..."
    hide iris with d3
    show iris_f 29 with d3
    sch1100 "Oh, I need to take an order... I'll be right back..."
    hide iris with d3
    sch10_56 "Hm..."
    menu:
        sch10_53 "So, old man, what do you think of Iris?"
        "\"She is hot.\"":
            sch10_53 "Yes, she is..."
            sch10_56 "But that's not what I meant..."
        "\"She is weird.\"":
            sch10_55 "Weird? In what way..."
            sch10_56 "You know what? I don't wanna know!"
            sch10_57 "You are weird, but Iris is cool!"
            sch10_56 "But that's not what I meant..."
        "\"What do you mean?\"":
            pass
        "\"Not my type.\"":
            sch10_55 "Really? How come...?"
            sch10_55 "Men seem to go crazy about her back at the brothel..."
            sch10_55 "Is it because she is too old?"
            sch10_53 "Am I more your type, you old perv?"
            sch10_56 "Anyway, that's not what I meant..."
        "\"So my type!\"":
            sch10_55 "She is? Really?"
            sch10_55 "Is it because she is old? Do you prefer mature women then?"
            sch10_56 "Hm... Mature women, huh?..."
            sch10_57 "Well, anyway, that's not what I meant."
    sch10_53 "What I meant was, how is she in bed?"
    sch10_53 "Come on, did you forget that I live in a brothel!? I know who comes and goes and who visits who..."
    sch10_53 "So tell me. Please?"
    menu:
        sch10_52 "And I will tell you what Iris says about you..."
        "\"She is wild in bed.\"":
            sch10_55 "Is she? Is she?"
            sch10_58 "I knew it!"
        "\"She is Aggressive...\"":
            sch10_58 "I bet she is..."
            sch10_53 "Men at the brothel say that she is \"feisty\"."
            sch10_56 "Although I don't know what that means..."
        "\"She is submissive...\"":
            sch10_55 "She is?"
            sch10_56 "Well that would depend on the man I guess..."
            sch10_58 "You were able to tame her then? Good job, old man!"
        "\"She enjoys anal.\"":
            sch10_59 "She's what!?"
            sch10_59 "Seriously!?"
            sch10_58 "Well, of course! That's why she is so popular! That's her secret!"
        "\"She likes to be choked.\"":
            sch10_55 "Really?"
            sch10_58 "That's kinky..."
        "\"She is frigid in bed.\"":
            sch10_54 "She is?"
            sch10_57 "I don't believe you..."
            sch10_56 "She is very popular among the customers back at the \"Phoenix\"."
            sch10_56 "Why do you think that is? Because she gives good massages?"
            sch10_58 "I don't think so!"
            
    sch10_52 "Hm... This is fun. I lo-o-o-o-ove gossiping about sex!"
    sch10_53 "You want to know what Iris says about you now?"
    sch10_53 "Well, the other days, she said that you are the--"
    with hpunch
    show iris_f 20 with d3
    sch1100 "What are you guys talking about?"
    sch10_60 "Yikes! What are you doing!? Don't sneak up on people like that!"
    hide iris with d3
    show iris_f 21 with d3
    sch1100 "What? I didn't sneak..."
    hide iris with d3
    show iris_f 22 with d3
    sch1100 "What {size=+7}were{/size} you guys talking about?"
    sch10_61 "Nothing! Stop the interrogation already!" 
    sch10_61 "The old man here was telling me that he can't get it up anymore, that's all..."
    hide iris with d3
    show iris_f 21 with d3
    sch1100 "Really?!"
    hide iris with d3
    menu:
        "\"Shut up, you brat! That's not true!\"":
            sch10_52 "That's OK, old man...Mee-hee-hee!"
            sch10_53 "This is a safe environment! You can share and not be afraid..."
            show iris_f 24 with d3
            sch1100 "Lola, I don't think it's true..."
            hide iris with d3
            show iris 103f with d3
            sch1100 "Becuase, last time we had sex it was like a freaking iron rod..."
            sch10_55 "Really? Tell me more!"
            hide iris with d3
            show iris_f 20 with d3
            sch1100 "Oops, sorry, I don't think it's very professional for me to discuss such things..."
            hide iris with d3
            show iris_f 19 with d3
            sch1100 "And why do you keep calling him \"Old Man\"?"
            sch1100 "He is younger then my father even..."
            if strength >= 0 and strength < 3:
                hide iris with d3
                show iris_f 27 with d3 
                sch1100 "Although his body is in a terrible shape..." 
            elif strength >= 3 and strength < 6:
                hide iris with d3
                show iris_f 24 with d3 
                sch1100 "Although I wish he took a better care of his body..."
            elif strength >= 6 and strength < 9:
                hide iris with d3
                show iris_f 26 with d3 
                sch1100 "And he is in a decent physical shape..."
            elif strength >= 9:
                hide iris with d3
                show iris_f 20 with d3 
                sch1100 "And he is in an amazing physical shape..."
                sch1100 "Just touch his bicep..."
        "\"Yup... Erection is a tricky business.\"":
            hide iris with d3
            show iris_f 21 with d3 
            sch1100 "Really? But last time we had sex it was like an iron rod..."
            sch10_55 "Really? Tell me more!"
            hide iris with d3
            show iris_f 20 with d3
            sch1100 "Oops, sorry, I don't think it's very professional for me to discuss such things..."
            hide iris with d3
            show iris_f 19 with d3
            sch1100 "And why do you keep call him \"Old Man\"?"
            sch1100 "He is younger then my father..."
            if strength >= 0 and strength < 3:
                hide iris with d3
                show iris_f 27 with d3 
                sch1100 "Although your body is in a terrible shape..." 
            elif strength >= 3 and strength < 6:
                hide iris with d3
                show iris_f 24 with d3 
                sch1100 "Although I wish you took a better care of your body..."
            elif strength >= 6 and strength < 9:
                hide iris with d3
                show iris_f 26 with d3 
                sch1100 "And you are in a decent physical shape..."
            elif strength >= 9:
                hide iris with d3
                show iris_f 20 with d3 
                sch1100 "And you are in an amazing physical shape..."
                sch1100 "Just touch his bicep..."
        "\"Actually Lola told me she is frigid in bed.\"":
            sch10_59 "Wha-a-at?!"
            sch10_57 "You..."
            sch10_57 "You..."
            sch10_62 "Why are you so mean?"
            show iris_f 26 with d3 
            sch1100 "Aw, calm down, Lola. He didn't mean it."
            hide iris with d3
            show iris_f 27 with d3 
            sch1100 "What's the matter with you? How you could say such a thing?"
            sch10_63 "Big stupid meanie..."
        "\"Nope. Lola told me she likes girls...\"":
            show iris_f 19 with d3 
            sch1100 "Like that's a big secret..."
            sch10_56 "Hey, I never actually said that I like other girls... I just said I'm curious..."
            sch10_52 "And I like Iris... Iris you can be my wife!"
            hide iris with d3
            show iris_f 26 with d3 
            sch1100 "Aw... Isn't she adorable..."
        "\"Lola told me she's done it with a camel.\"":
            show iris_f 23 with d3 
            sch1100 ".............."
            sch10_51 ".............."
            sch10_52 "Hee-hee-hee. That's just silly..."
            hide iris with d3
            show iris_f 23 with d3 
            sch1100 "You guys are funny..."
    show blkfade with Dissolve(.5)
    hide iris
    pause.5
    hide blkfade with Dissolve(.5)
    show iris_f 19 with d3 
    sch1100 "Oh, hey, I think they are about to start..."
    sch10_61 "Who's about to do what?"
    hide iris with d3
    show iris_f 26 with d3 
    sch1100 "The dance... You told me the other day that you would love to see the girls dancing in our tavern, well, now is your chance..."
    sch10_55 "Really, really?"
    sch10_58 "Awesome!!! Bring on the dirty dancing!"
    sch10_60 "I know how much you want to dance too. I'm sorry your father wouldn't let you..."
    hide iris with d3
    show iris_f 24 with d3
    sch1100 "Actually, I kinda made my peace with that..."
    sch10_55 "Really?"
    hide iris with d3
    show iris_f 23 with d3
    sch1100 "Yeah... I figured, I do what I want aren't I? I mean I work in a brothel..."
    hide iris with d3
    show iris_f 20 with d3
    sch1100 "I don't think it's fair if I keep giving my father grief about that dancing..."
    sch10_54 "Makes, sense I suppose..."
    hide iris with d3
    show iris_f 24 with d3
    sch1100 "Yup. So from now on I will be the exemplary daughter!"
    sch10_58 "(Well, accept for being a wore.)"
    hide iris with d3
    show iris_f 19 with d3
    sch1100 "Oh, shut up, you!"
    hide iris with d3
    show iris_f 26 with d3
    sch1100 "OK, they are starting!"
    lola[58] "This is so exiting!"
    show blkfade with Dissolve(1.5)
    pause.5
    hide iris
    ">later that night..."
    hide blkfade with Dissolve(.3)
    $ renpy.play('sounds/door2.mp3')
    hide image "04_pt/slavem/bld2.png" with d3
    lola[30] "This was amazing! Thank you for taking me there!!!"
    if loladates >= 5:
        jump bringlolahome
    else:
        lola[50] "I'm feeling a bit sleep now... Could you take me home?"
        hide image "04_pt/slavem/bld.png" with d3
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        ">You take Lola back to the brothel."
        ">Your relationship with Lola has improved."
        show blkfade with Dissolve(.5)
        pause 2
        jump dayone

#####MARKET AT NIGHT###############
label lolamarketnight:
    lola[30] "Market square, huh? Alright, let's go!"
    $ loladates += 1
    $ lnightmarket = False
    show blkfade with Dissolve(.3)
    pause 1
    show image "04_pt/slavem/bld2.png" behind blkfade
    show image im.Flip("lola_dates/l01.png", horizontal=True) at left behind blkfade
    hide blkfade with Dissolve(.3)
    play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1  #NIGHT
    sch1000 ".............."
    sch1000 "It so...... deserted... "
    sch1000 "Not a single soul in sight..."
    hide image im.Flip("lola_dates/l01.png", horizontal=True) at left with Dissolve(.3)
    menu:
        "\"How old are you exactly?\"":
            show image im.Flip("lola_dates/l02.png", horizontal=True) at left with Dissolve(.3)
            sch1000 "I already told you this: old enough."
            hide image im.Flip("lola_dates/l02.png", horizontal=True) at left with Dissolve(.3)
        "\"So what's the deal with your hair?\"":
            show image im.Flip("lola_dates/l02.png", horizontal=True) at left with Dissolve(.3)
            sch1000 "What do you mean?"
            menu:
                "\"It's... blond.\"":
                    hide image im.Flip("lola_dates/l02.png", horizontal=True) at left with Dissolve(.3)
                    show image im.Flip("lola_dates/l03.png", horizontal=True) at left with Dissolve(.3)
                    sch1000 "Oh, that... Well, I'm not sure..."
                    hide image im.Flip("lola_dates/l03.png", horizontal=True) at left with Dissolve(.3)
                    show image im.Flip("lola_dates/l04.png", horizontal=True) at left with Dissolve(.3)
                    sch1000 "Fat Lily is not my real mom, she is just taking care of me..."
                    sch1000 "I never knew my real mom but whoever she was I guess she is not from around here..."
                    hide image im.Flip("lola_dates/l04.png", horizontal=True) at left with Dissolve(.3)
                "\"You're missing a pigtail.\"":
                    hide image im.Flip("lola_dates/l02.png", horizontal=True) at left with Dissolve(.3)
                    show image im.Flip("lola_dates/l03.png", horizontal=True) at left with Dissolve(.3)
                    sch1000 "Oh, that..."
                    sch1000 "Yeah, my daddy did that..."
                    hide image im.Flip("lola_dates/l03.png", horizontal=True) at left with Dissolve(.3)
                    show image im.Flip("lola_dates/l04.png", horizontal=True) at left with Dissolve(.3)
                    sch1000 "One day, long time ago he put me on display in front of a bunch of people..."
                    sch1000 "They were yelling out all sorts of suggestions and my daddy would pick the ones he liked and follow them..."
                    sch1000 "It was fun at first, but then people started to ask for some really bizarre and mean things..."
                    hide image im.Flip("lola_dates/l04.png", horizontal=True) at left with Dissolve(.3)
                    show image im.Flip("lola_dates/l05.png", horizontal=True) at left with Dissolve(.3)
                    sch1000 "That upset my daddy so when somebody yelled out \"Cut one of her pigtails off\" he went ahead and just did it..."
                    sch1000 "And that was the end of the whole thing..."
                    hide image im.Flip("lola_dates/l05.png", horizontal=True) at left with Dissolve(.3)
                    show image im.Flip("lola_dates/l06.png", horizontal=True) at left with Dissolve(.3)
                    sch1000 "My daddy is a jerk I guess... But he is my daddy still, so don't you dare say bad things about him..."
                    hide image im.Flip("lola_dates/l06.png", horizontal=True) at left with Dissolve(.3)
                    show image im.Flip("lola_dates/l07.png", horizontal=True) at left with Dissolve(.3)
                    sch1000 "........................"
                    hide image im.Flip("lola_dates/l07.png", horizontal=True) at left with Dissolve(.3)
    lola[50] "Emmm...."
    lola[49] "er..... em......"
    menu:
        lola[33] "That's weird... Suddenly I don't know what to say anymore..."
        "\".............................\"":
            pass
        "\".............................\"":
            pass
        "\".............................\"":
            pass
    show image "04_pt/slavem/bld.png" with d5
    a5 "Well, that's because I'm out of ideas..."
    lola[64] "Daddy!"
    a1 "Crap..."
    a1 "I could take my time and come up with something clever for this date scene--"
    lola[65] "This is not a \"date\", daddy."
    a4 "Oh, so {size=+5}now{/size} you want to talk? A moment ago it was like silence in my head!"
    lola[66] "I'm sorry..."
    a6 "Shut it! You're no help at all... Your only skill is your sex appeal."
    lola[67] "You want to see my tits?"
    a4 "Keep interrupting me and I will write you out of this game along with your useless tits!"
    lola[68] "(my tits are not useless.)"
    a4 "What did I just tell you?!"
    lola[68] ".............."
    a5 "So, like I was saying: I could come up with something clever, but clever takes time..."
    a6 "You know what doesn't take any time though?"
    a7 "Lame and boring doesn't take any time!"
    a1 "But the last thing I want to do is fill this game with boring content..."
    a6 "But the more time I take to work on this beast of a game the less support I get..."
    a7 "For every donation I receive lately I lose a few {a=http://akabur.hentaiunited.com}hentaiunited{/a} subscribers..."
    a5 "And if that wasn't enough I also get these irritating comments and emails all the fucking time..."
    a6 "\"I want my game akabur...\" \n\"I've been waiting for so long, Akabur...\""
    a6 "\"Hurry up, Akabur...\" \n\"Release at least something, Akabur...\""
    a7 "And all I want is to make a good game, instead of some uninspired crap..."
    a1 "Is that too much to ask?"
    with hpunch
    a7 "{size=+7}This is so infuriating!!!{/size}"
    a1 "So, how about this then?"
    a1 "I will release the game a couple of days sooner, but to compensate for that I'm not gonna write this scene!"
    lola[68] "What?"
    a4 "I swear, girl, one more peep outta you and I'm turning you into a shemale!"
    lola[69] "!!!!!!!!!!!!!!!!!!!!!"
    a5 "So here is the synopsis then: Lola and Genie come to the Market square..."
    a5 "They walk around and talk about stuff. The date ends."
    a5 "Your relationship with Lola has improved."
    a5 "The End."
    a6 "Well, whadda you know, another scene is ready, just like that... Moving on to the next one!"
    lola[68] "(my tits are not useless.)"
    with d3
    if loladates == 5:
        jump bringlolahome
    else:
        hide image "04_pt/slavem/bld2.png" 
        hide image "04_pt/slavem/bld.png"
        with d3
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        show blkfade with Dissolve(.3)
        pause 2
        jump dayone
    
   
#########LOLA GOES HOME#################  
label bringlolahome:
    play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
    $ quest8start00 = True
    $ lolacomeatnight = False
    show blkfade with d3
    hide iris
    pause 1
    hide blkfade with d3
    lola[33] "Hm... I don't feel like going home yet..."
    lola[50] "You know what I want to do instead?"
    lola[50] "I want to see where you live..."
    lola[50] "Yeah! How about you show me your house?"
    hide image "04_pt/slavem/bld.png" with d3
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    ">You take Lola to your house..."
    show blkfade with d3
    pause 1
    $ renpy.play('sounds/door2.mp3')
    hide blkfade with d3
    show bld with d3
    show lola_f 1 at left with d3
    sch1000 "So this your \"base of operations\", huh?"
    hide lola with d3
    show lola_f 7 at left with d3
    sch1000 "Not nearly as impressive as I thought it would be..."
    hide lola with d3
    show lola_f 4 at left with d3
    sch1000 "Is it just you living here?"
    hide lola with d3
    show lola_f 1 at left with d3
    sch1000 "Oh, hey, this door is locked? Who's room is this?"
    hide lola with d3
    menu:
        "\"The one of my slave.\"":
            show lola_f 8 at left with d3
            sch1000 "Really? That's so cool!"
            sch1000 "Can you wake her up and let me poke her with a stick or something?"
            hide lola with d3
            show lola_f 7 at left with d3
            sch1000 "No wait, that would be silly."
            hide lola with d3
            show lola_f 8 at left with d3
            sch1000 "Do you poke her with {i}{size=+4}your stick{/size}{/i} every now and then, old man?"
            sch1000 "I bet you do..."
            hide lola with d3
        "\"The one of my slave, Princess Jasmine.\"":
            show lola_f 4 at left with d3
            sch1000 "You think I will just believe anything you say, don't you?"
            hide lola with d3
            show lola_f 5 at left with d3
            sch1000 "I'm not {size=+5}that{/size} gullible!" 
            hide lola with d3
        "\"Some project I'm working on.\"":
            show lola_f 9 at left with d3
            sch1000 "Really? You mean a slave you're currently training?"
            hide lola with d3
            show lola_f 8 at left with d3
            sch1000 "Cool!"
            hide lola with d3
        "\"The treasury.\"":
            show lola_f 9 at left with d3
            sch1000 "Really? It doesn't look like it... The door is so old and doesn't look sturdy enough..."
            hide lola with d3
            show lola_f 1 at left with d3
            sch1000 "Oh, wait, you are hiding your treasures in plain sight, right?"
            hide lola with d3
            show lola_f 6 at left with d3
            sch1000 "You are so smart!"
            hide lola with d3
    show lola_f 9 at left with d3
    sch1000 ".........hm."
    hide lola 
    show lola_f 7 at left with d3
    sch1000 "Your house is really small though!"
    sch1000 "I thought you were rich..."
    hide lola 
    show lola_f 8 at left with d3
    sch1000 "Oh well..."
    hide lola  
    show image "lola_dates/l06.png" at right with Dissolve(.3)
    sch1000 "So what are we going to do now?"
    hide image "lola_dates/l06.png" at right with Dissolve(.3)
    menu:
        "\"I have no idea.\"":
            show image "lola_dates/l04.png" at right with Dissolve(.3)
            sch1000 "Hm......"
            hide image "lola_dates/l04.png" at right with Dissolve(.3)
            show image "lola_dates/l08.png" at right with Dissolve(.3)
            sch1000 "I have one..."
            hide image "lola_dates/l08.png" at right with Dissolve(.3)
        "\"Dance for me.\"":
            show image "lola_dates/l04.png" at right with Dissolve(.3)
            sch1000 "Hm... I don't feel like dancing..."
            hide image "lola_dates/l04.png" at right with Dissolve(.3)
            show image "lola_dates/l08.png" at right with Dissolve(.3)
            sch1000 "But I have a better idea."
            hide image "lola_dates/l08.png" at right with Dissolve(.3)
        "\"Play tag. Tag! You're it!\"":
            show image "lola_dates/l04.png" at right with Dissolve(.3)
            sch1000 "How childish... Stop treating me like a kid..."
            hide image "lola_dates/l04.png" at right with Dissolve(.3)
            show image "lola_dates/l08.png" at right with Dissolve(.3)
            sch1000 "I'm not a child and I will prove that to you that right now!"
            hide image "lola_dates/l08.png" at right with Dissolve(.3)
    show image "lola_dates/l08.png" at right with Dissolve(.3)
    sch1000 "Remember when I asked you to take me out for the first time, I said that I will make it worth it to you."
    hide image "lola_dates/l08.png" at right with Dissolve(.3)
    menu:
        "\"You did?\"":
            show image "lola_dates/l04.png" at right with Dissolve(.3)
            sch1000 "Yes... Don't you remember?"
            hide image "lola_dates/l04.png" at right with Dissolve(.3)
            show image "lola_dates/l06.png" at right with Dissolve(.3)
            sch1000 "Aww... Are you forgetting things because of your old age? \nHow cute..."
            hide image "lola_dates/l06.png" at right with Dissolve(.3)
        "\"I do remember.\"":
            show image "lola_dates/l06.png" at right with Dissolve(.3)
            sch1000 "Great...."
            hide image "lola_dates/l06.png" at right with Dissolve(.3)
    show image "lola_dates/l08.png" at right with Dissolve(.3)
    sch1000 "So what if I do it now? Make it worth it for I mean."
    sch1000 "Hm.... What should I do?"
    hide image "lola_dates/l08.png" at right with Dissolve(.3)
    
    menu:
        "\"Give me some money.\"":
            show image "lola_dates/l09.png" at right with Dissolve(.3)
            sch1000 "Seriously?"
            sch1000 "I thought you already have plenty of that..."
            sch1000 "Plus do I look like I have any money?"
            hide image "lola_dates/l09.png" at right with Dissolve(.3)
            show image "lola_dates/l08.png" at right with Dissolve(.3)
            sch1000 "No, I have a much better idea!"
            hide image "lola_dates/l08.png" at right with Dissolve(.3)
        "\"A blowjob would be nice.\"":
            show image "lola_dates/l09.png" at right with Dissolve(.3)
            sch1000 "A blowjob, huh? Hm..."
            sch1000 "I dunno..."
            hide image "lola_dates/l09.png" at right with Dissolve(.3)
        "\"Show me your tits.\"":
            show image "lola_dates/l09.png" at right with Dissolve(.3)
            sch1000 "I could do that, but I don't think it will cover my debt to you, I want to do something more significant..."
            hide image "lola_dates/l09.png" at right with Dissolve(.3)
            show image "lola_dates/l08.png" at right with Dissolve(.3)
            sch1000 "Hey, I have an idea!"
            hide image "lola_dates/l08.png" at right with Dissolve(.3)
        "\"How about a handjob?\"":
            show image "lola_dates/l09.png" at right with Dissolve(.3)
            sch1000 "Hm..."
            sch1000 "Right here?"
            hide image "lola_dates/l09.png" at right with Dissolve(.3)
            show image "lola_dates/l08.png" at right with Dissolve(.3)
            sch1000 "Well, I do owe you, so maybe I should do it..."
            hide image "lola_dates/l08.png" at right with Dissolve(.3)
            show image "lola_dates/l06.png" at right with Dissolve(.3)
            sch1000 "Alright! I'll do it! Take your cock out!"
            hide image "lola_dates/l06.png" at right with Dissolve(.3)
            jump cockout
        "\"Let's fuck.\"":
            show image "lola_dates/l09.png" at right with Dissolve(.3)
            sch1000 "What? Hey, I don't owe you {size=+5}THAT{/size} much, you old perv!"
            hide image "lola_dates/l08.png" at right with Dissolve(.3)
    show image "lola_dates/l08.png" at right with Dissolve(.3)
    sch1000 "How about a handjob?"
    hide image "lola_dates/l08.png" at right with Dissolve(.3)
    hide image "lola_dates/l09.png" at right with Dissolve(.3)
    show image "lola_dates/l06.png" at right with Dissolve(.3)
    sch1000 "Yes! It will be fun! \nCome on, take your dick out, let me touch it!"
    hide image "lola_dates/l06.png" at right with Dissolve(.3)
    label cockout:
    show blk50 with d3    
    ">Your take your, already semi-hard cock out..."
    play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
    ">Lola is looking at it intently..."
    lola[17] "It's bigger than I expected..."
    ">Lola takes your cock with both hands and starts jerking it somewhat hastily ..."
    hide blk50 with d3    
    show hjob with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    lola[16] "Nice... You have a great cock..."
    lola[17] "Not that I've seen that many of them, or anything..."
    lola[16] "I mean, I live in a brothel so I see all sorts of things..."
    lola[16] "But this is my first time giving handjob to a person..."
    lola[17] "I've been practicing with bannanas and empty wine bottles when mother wasn't looking..."
    lola[17] "Am I doing this right?"
    hide hjob with Dissolve(.3)
    menu:
        "\"Yup, just keep going.\"":
            show hjob with Dissolve(.3)
            lola[18] "OK!"
        "\"Do it faster.\"":
            show hjob with Dissolve(.3)
            lola[18] "Alright, I will try to do it faster."
            lola[19] "Like this. Do you like it?"
        "\"Do it slower.\"":
            show hjob with Dissolve(.3)
            lola[19] "Slower, really? Ok, I'll try..."
            lola[19] "Like this?"
        "\"Your skills are lacking.\"":
            show hjob with Dissolve(.3)
            lola[20] "Sorry... I don't have much experience in this area..."
            lola[20] "I've seen girls back in the brothel do it so many times, I thought this was easy..."
            lola[17] "Just hang on, please. I will do my best and try to make you cum...."
    lola[23] "Yes, I'm not a little girl anymore..."
    lola[22] "Ah...{image=textheart.png} Look at me, I'm a little slut!"
    lola[18] "He-he..."

    lola[16] "A Big fat dick in my hands! La-la-la!{image=note.png}"
    lola[16] "I'm a little slut, I'm a whore! La-la-la!{image=note.png}"
    hide hjob with Dissolve(.3)
    menu:
        "\"Cool song!\"":
            show hjob with Dissolve(.3)
            lola[18] "You like it? I made it up myself the other day!"
            lola[18] "There is more..."
            lola[24] "I'm a little nasty whore! La-la-la!{image=note.png}"
            lola[24] "I suck dicks and drink cum! La-la-la!{image=note.png}"
            lola[17] "He-he-he! It doesn't rhyme much but it's so dirty!"
        "\"Stop singing. Concentrate on your task.\"":
            show hjob with Dissolve(.3)
            lola[17] "Yes, sorry, I get distracted easily..."
            lola[17] "But, I thought maybe it will help you to cum sooner..."
            lola[17] "Back in the brothel I hear girls call themselves all sorts of names..."
            lola[23] "Men love that!"
            lola[17] "They do, right?"
        "\"...............\"":
            show hjob with Dissolve(.3)
            pass

        
    lola[17] "How are you doing? Are you going to cum anytime soon?"
    hide hjob with Dissolve(.3)
    menu:
        "\"Yes I am! speed up!\"":
            show hjob with Dissolve(.3)
            lola[17] "My arms are a little tired..."
            lola[23] "But I will try!"
        "\"Yes I am! put in your mouth!\"":
            show hjob with Dissolve(.3)
            lola[24] "What? Em... Not that I don't want to...."
            lola[20] "But I'm afraid I will choke on your cum and ruin everything for you..."
    lola[23] "Cum for me, you fat bastard, you amazing stallion!"
    lola[23] "Fill me with your cum! Make me your pregnant whore!"
    lola[23] "Be my sultan! You are the best! You are a worthless waste of space!"
    lola[20] "I'm sorry, I don't know what I'm saying... I heard girls back at the brothel say these things..."
    hide hjob with Dissolve(.3)
    menu:
        "\"Here it comes, slut!\"":
            show hjob with Dissolve(.3)
            lola[19] "?!!!!!"
            lola[20] "What? What I have to do now?\""
        "\"Argh! You whore! I'm cumming!":
            show hjob with Dissolve(.3)
            lola[20] "Come! Come er... C-come for me.\""
        "\"Oh, yes! Yes! Now!":
            show hjob with Dissolve(.3)
            lola[20] "What? OH! Should I jerk it faster? Should I stop?"
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show hjobcum with Dissolve(.3)
    hide hjob with Dissolve(.3)
    lola[18] "You're coming, you're coming!!!"
    lola[20] "What should I do now, what should I do?"
    lola[20] "Should I keep jerking it, should I put it in my mouth?"
    lola[25] "Am I doing this right? I'm sorry!"
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show hjobover with Dissolve(.3)
    hide hjobcum with Dissolve(.3)
    show heart at Position(xpos=570, ypos=90, xanchor=0, yanchor=0) with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide hjobover 
    hide heart
    with d5
    menu:
        lola[20] "So, how was it? Did I do everything right? Did you enjoy it?"
        "\"Yeah. It was perfect.\"":
            lola[18] "Really? Really?"
            lola[18] "Yay! I'm so happy!"
        "\"It was OK, but you need more practice.\"":
            lola[18] "Of course, of course! I want to learn!"
            lola[20] "Will you let me practice on you?"
            lola[21] "Wait, are you saying this only to get free handhobs from me?"
            lola[24] "Yay! That means you liked it!"
        "\"It was bad. You still owe me.\"":
            lola[20] "Oh, I'm sorry... I really tried to do my best."
            lola[20] "Will you let me practice on you?"
            lola[21] "Wait, are you saying this only to get free handhobs from me?"
            lola[24] "Yay! That means you liked it!"
        "\"Awful. Just awful. You have no skill.\"":
            lola[20] "I knew it..."
            lola[25] "I'm so sorry... I will try to get better, I promise!"
            lola[20] "Will you let me practice on you?"
            lola[21] "Wait, are you saying this only to get free handhobs from me?"
            lola[24] "Yay! That means you liked it!"
    lola[23] "Let's do it again now! Let's do it again!"
    lola[19] "Oh, your \"thing\" is not gonna be able to get up for a while now, right?"
    lola[24] "Well alright then. I think I better get home then."
    lola[18] "Could you walk me home please?"
    show blkfade with Dissolve(1) 
    ">You take lola home."
    ">Your relationship with Lola moved to another level."
    pause 1
    jump dayone
            
            
    
    
####LOLA'S ROOM##########
label lolasroom:
    if not jas_met_lola:
        hide blkfade
        show blkfade with d3
        $ renpy.play('sounds/door.mp3')
        pause.7
        hide blkfade with d3
        lola[52] "Hello..."
        show jas 3 with d3
        j "You again..."
        hide jas with d3
        show jas 4 with d3
        j "What is she doing here?"
        j "Oh, I see... So that new room was meant for her?"
        j "Well of course..."
        hide jas with d3
        show jas 15 with d3
        j "And I thought that maybe you decided to improve my living conditions..."
        hide jas with d3
        show jas 14 with d3
        j "Silly me..."
        lola[61] "S-sorry, lady..."
        hide jas with d3
        show jas 16 with d3
        j "Yeah, whatever, welcome to the family."
        hide jas with d3
        show jas 14 with d3
        j "Get ready to get fucked, abused and humiliated on a daily basis."
        lola[58] "Alright!!!"
        hide jas with d3
        show jas 10 with d3
        j "Oh my... She's messed up..."
        lola[61] "Huh?"
        hide jas with d3
        show jas 14 with d3
        j "So, what's the deal, old man? Why is she here?"
        hide jas with d3
        show jas 12 with d3
        j "do I not satisfy you pervy needs anymore?"
        hide jas with d3
        show jas 16 with d3
        j "Tsk... Pathetic old man..."
        hide jas with d3
        show jas 14 with d3
        j "Do whatever you want, I couldn't care less..."
        j "I will be in my room..."
        hide jas with d3
        $ renpy.play('sounds/door2.mp3')
        pause.5
        lola[56] "Me too..."
        pause.5
        $ jasmeetslola = False
        $ jas_met_lola = True
        jump leavejroom
    else:
        show blkfade with d3
        $ renpy.play('sounds/door.mp3')
        pause.7
        show image "04_pt/slavem/sorry.png" behind blkfade
        hide blkfade with d5
        show ctc7 at right
        pause 
        hide ctc7
        hide image "04_pt/slavem/sorry.png" with d5
        jump leavejroom
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    