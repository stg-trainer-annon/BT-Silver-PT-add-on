label delivermaterials:
    show image "04_pt/slavem/masteritem.png" with moveinright
    show image "04_pt/slavem/boxmaterials.png" with moveinleft
    ">You hand over the required materials to Azalea..."
    hide image "04_pt/slavem/boxmaterials.png" with moveoutright
    hide image "04_pt/slavem/masteritem.png" with moveoutleft
    aza[1] "Are these the materials?"
    aza[1] "Let's see... fabric, beads... \nYup, everything is here."
    aza[1] "I will start working on the dress right away..."
    aza[1] "But quality takes time, you know that, don't you?"
    aza[1] "Gimme a few days..."
    $ quest5start4 = False
    $ quest5start5 = True
    $ renpy.play('sounds/door2.mp3')
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    jump mainmenu
#############
label pickupdress1:
    show blkfade with d5
    pause.7
    hide blkfade with d5
    aza[1] "Yes, yes, your dress is ready!"
    aza[1] "I'm very pleased with the result, I think Iris will love it!"
    aza[1] "Do you know why she needs such a dress though?"
    aza[1] "I mean, it's so... slutty.  That's a whore's dress, no doubt..."
    menu:
        "\"Iris aspires to be a whore.\"":
            aza[1] "Does she now?"
            aza[1] "That's an interesting tidbit of information for sure..."
        "\"Iris? No, I need it for my slave-girl.\"":
            aza[1] "Huh? I thought you said Iris wanted this one?"
            aza[1] "Well, doesn't matter..."
        "\"Iris is into role-play.\"":
            aza[1] "And who isn't?"
            aza[1] "Wait, does it mean that you and Iris are doing it? Is her father ok with this?"
            aza[1] "Don't worry I will keep your secret."
        "\"None of your business, Azalea.\"":
            aza[1] "I know, I can be noisy sometimes, sorry."
    aza[1] "Normally I would charge 800 gold coins for a dress like this, but since you brought your own materials..."
    aza[1] "It will be 400 gold for you..."
    menu:
        "You currently have [gold] gold. \nWould you like to buy a whore's dress for 400 gold?"
        "\"Yes please.\"":
            if gold >= 400: 
                $ gold -=400
                $ quest5start6 = False
                $ quest5start7 = True
                $ quest5start5 = False
                aza[1] "Thank you for your purchase.. Here is your dress..."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxdress.png" with moveinright
                ">You received a whore's dress..." 
                hide image "04_pt/slavem/boxdress.png" with Dissolve(.4)
                hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                aza[1] "Have a nice day."
                $ renpy.play('sounds/door2.mp3')
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                show blkfade with d5
                pause.7
                hide blkfade with d5
                jump mainmenu
            else:
                ">You don't have enough gold..."
                aza[1] " Come back whenever you're ready. I'll put the dress aside for you."
                show blkfade with d5
                pause.7
                hide blkfade with d5
                jump store2
        "\"Maybe later.\"":
            aza[1] "Come back whenever you're ready."
            show blkfade with d5
            pause.5
            hide blkfade with d5
            jump store2 
#######################
label quest8startass:
    $ quest8start = False
    $ quest8start2 = True
    show blkfade with d3
    pause.3
    hide blkfade with d3
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    aza[1] "Hi there."
    show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
    show image "04_pt/slavem/boxirissketch.png" with moveinleft
    ">You hand over the drawing Lola gave you to Azalea."
    hide image "04_pt/slavem/boxirissketch.png" with moveoutright
    hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
    aza[1] "What's this?"
    aza[1] "It's from Lola?"
    aza[1] "What a silly drawing..."
    aza[1] "No, wait I've been holding it upside-down..."
    aza[1] "Hm...... I see...."
    aza[1] "Another whore dress, huh?"
    aza[1] "It's as if every woman who spends enough time in your company wants to be a whore."
    aza[1] "I also see you quite often... Should I start to worry?"
    aza[1] "I'm kidding... I know Lola wanted this for a while now..."
    aza[1] "Well, the design is quite good actually..."
    aza[1] "And, lucky for you, I think I have all the necessary materials in stock."
    aza[1] "So, you just give me a couple of days and you will have your dress..."
    aza[1] "See ya..."
    show blkfade with d3
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
    pause.3
    $ renpy.play('sounds/door2.mp3')
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    hide blkfade with d3
    jump mainmenu 
###############
label quest8start2:
    show blkfade with d3
    pause.3
    hide blkfade with d3
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    aza[1] "Hi there."
    aza[1] "The dress you ordered is ready..."
    aza[1] "Since I used my own materials for this one, I have no choice but charge you extra..."
    aza[1] "It will be 600 gold coins, please."
    menu:
        "You currently have [gold] gold. \nWould you like to pay 600 gold coins for the dress?"
        "\"Yes please.\"":
            if gold >= 600: 
                $ gold -=600
                $ quest8start2 = False
                $ quest8start3 = True
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxdress.png" with moveinright
                "You received the Lola's dress." 
                hide image "04_pt/slavem/boxdress.png" with Dissolve(.4)
                hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                aza[1] "I bet it will look fantastic on her..."
                show blkfade with d3
                pause.3
                $ renpy.play('sounds/door2.mp3')
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                hide blkfade with d3
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                jump mainmenu 
            else:
                aza[1] "You don't have enough gold? Well, alright. I'll just put it aside for now then."
                aza[1] "Come back any time, it will be waiting for you."
                show blkfade with d3
                pause.3
                $ renpy.play('sounds/door2.mp3')
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                hide blkfade with d3
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                jump mainmenu 
        "\"Maybe later.\"":
            aza[1] "Well, alright. I'll just put it aside for now then."
            aza[1] "Come back any time, it will be waiting for you."
            show blkfade with d3
            pause.3
            $ renpy.play('sounds/door2.mp3')
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            hide blkfade with d3
            play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
            jump mainmenu 
    
        
        
        
        
        
    
    
    
    