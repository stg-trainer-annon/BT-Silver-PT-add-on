#####BROTHEL'S LABELS##############
#TAKING LOLA OUT######
label lolaout:
    play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
    show blkfade with d5
    pause.3
    hide blkfade with d5
    lola[11] "You came!!!"
    sch3 "Did you bring something delicious for mommy?"
    show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
    show image "04_pt/slavem/boxdelicious.png" with moveinleft
    ">You hand over something delicious to lily."
    hide image "04_pt/slavem/boxdelicious.png" with moveoutright
    hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
    sch3 "Oooo! This smells good!"
    sch3 "Mommy needs some \"alone\" time with this bad-boy now!"
    sch3 "You kids have fun!"
    lola[11] "Great! So, where are you gonna take me, old man?"
label lolaout2:
    menu:
        lola[11] "I don't go out much so anywhere is fine with me!"
        "-Market square-" if ldatemarket:
            jump loladatemarket
        "-Tavern-" if ldatetavern:
            jump loladatetavern
        "-Brothel-" if ldatebrothel:
            jump loladatebrothel
        "-Azalea's Store-" if ldatestore:
            jump loladatestore
        "-Cheapside-" if ldatecheapside:
            jump loladatecheapside
        "-\"JSGA\"-" if ldatepalace:
            jump loladatepalace
####COMEATNIGHT#################
label lolacomeatnight:
    show blkfade with d5
    pause.3
    hide blkfade with d5
    play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
    lola[11] "You came!!!"
    sch3 "Did you bring something delicious for the mommy?"
    show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
    show image "04_pt/slavem/boxdelicious.png" with moveinleft
    ">You hand over something delicious to lily."
    hide image "04_pt/slavem/boxdelicious.png" with moveoutright
    hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
    sch3 "Oooo! This smells good!"
    sch3 "Mommy needs some \"alone\" time with this bad-boy now!"
    sch3 "You kids have fun!"
    lola[11] "Great! So, where are you gonna take me, old man?"
    lola[11] "......................................."
    $ renpy.play('sounds/door2.mp3')
    lola[11] "............."
    lola[12] "OK, she finally left..."
    lola[13]"Listen, I've been thinking...."
    lola[14] "I would really appreciate it if you could take me out for a walk after the dusk..."
    menu:
        lola[14] "I want to see what is it like to be out during the night..."

        "\"What will Lily say?\"":
            lola[12] "Nothing, mom would never allow it, so we're just not gonna tell her..."
            lola[14] "It will be our little secret!"
        "\"I can do that. No problem.\"":
            lola[11] "You're the best!!!"
        "\"Could be dangerous. Rather not do that.\"":
            lola[14] "Stop teasing me! You don't mean it, and only saying this to see how I would react..."
            lola[11] "Me-hee-hee, I got you all figured out!"
    lola[13] "Alright. Comeback tonight then, I will be waiting!"
    $ quest7completefood = False
    $ lolacomeatnight = True
    show blkfade with Dissolve(.5)
    pause.5
    hide blkfade with Dissolve(.5)
    jump brothelmain
###LOLA OUT AT NIGHT#######
label lolaoutnight:
    sch3 "Oh, no, dear. Not after the sunset..."
    sch3 "Come back tomorrow during the day..."
    sch3 "But don't forget my favorite \"something delicious\"!"
    lola[12] "{size=-4}(Pst! Hey, what are you doing!){/size}"
    lola[12] "{size=-4}(Don't talk to my mom about this. You gonna ruin everything!){/size}"
    lola[12] "{size=-4}(Just wait for me outside, I will sneak out...){/size}"
    show image "04_pt/slavem/bld.png" with Dissolve(.3) 
    pause.5
    hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
    show blkfade with Dissolve(.5)
    $ renpy.play('sounds/door2.mp3')
    pause 1
    hide blkfade with Dissolve(.5)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7

    ".................................."
    ".................................."
    ".................................."

    sch1000 "Old man? Hey old man! Over here."
    lola[50] "It took me longer than I expected, sorry."
    label wheretogowithl:
    menu:
        lola[50] "So... Where are you gonna take me tonight?"
        "-The Palace-" if lnightacademy:
            jump lolaacademy
        "-Tavern-" if lnighttavern:
            jump lolatavern
        "-Market-" if lnightmarket:
            jump lolamarketnight

            

            
#DATE WITH LILY
label datewithlily:
    play music "music/India's Different (Dancing).MP3" fadein 1 fadeout 1 #DANCING
    #play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with Dissolve(.3)
    show image "quest05/lily02.png" at center behind blkfade
    pause.7
    hide blkfade with Dissolve(.3)
    sch300 "Well hello, my handsome stallion... I've been expecting you."
    sch300 "Did you bring me anything special?"
    hide image "quest05/lily02.png" at center with Dissolve(.3)
    show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
    show image "04_pt/slavem/boxnice.png" with moveinleft
    ">You hand over something nice to Lily."
    hide image "04_pt/slavem/boxnice.png" with moveoutright
    hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
    show image "quest05/lily02.png" at center with Dissolve(.3)
    sch300 "Aw... I love something nice! It's like my favorite thing ever!"
    sch300 "Thank you, love."
    sch300 "Is there something else?"
    hide image "quest05/lily02.png" at center with Dissolve(.3)
    show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
    show image "04_pt/slavem/boxdelicious.png" with moveinleft
    ">You hand over something delicious to Lily."
    hide image "04_pt/slavem/boxdelicious.png" with moveoutright
    hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
    show image "quest05/lily02.png" at center with Dissolve(.3)
    sch300 "It smells so good! Something delicious is like my favorite dish ever! How did you know?"
    sch300 "Well, you sure know how to put a woman in a good mood."
    sch300 "Alright, let's go upstairs now..."
    sch300 "You can leave your cloak here..."
    hide image "quest05/lily02.png" at center with Dissolve(.3)
    ">You take your cloak off and follow Lily to the second floor."
    show image "04_pt/lola/q5/lola01.png" at center with Dissolve(.3)
    sch1000 "Have fun, guys!"
    show blkfade with Dissolve(.7)
    ">You spent the night with lily..."
    ">It was a terrifying experience..."
    ">You are now emotionally scarred for life and don't feel like having sex ever again..."
    ".............................."
    ">....ever."
    show image "04_pt/slavem/sex.png" with Dissolve(3)
    hide image "04_pt/slavem/onaquest.png." 
    show ctc7 at right
    pause
    hide con1
    hide image "04_pt/slavem/sex.png" with Dissolve(3)
    $ quest7complete = True
    $ quest7completefood = True
    $ quest7thing = False
    $ quest7food = False
    $ onquest = False
    $ quest7start = False
    $ renpy.play('sounds/win2.mp3')                        
    show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    ">You bedded lily long and well. She trusts you now, so you can take her daughter out during the daytime from now on."
    ">Don't forget to bring some food for her mother though."
    hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayone
#DAHLIA
label dahliawhore:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
    show blkfade with d3
    pause.7
    show dahlia 2 at right behind blkfade
    hide blkfade with d3
    "Hello, darling..."
    "Are you feeling lonely? I have a cure for that \"illness\" of yours..."
    menu:
        "\"Yes... So lonely...\"":
            dah "Like so many things in this world, the cure from your loneliness does not come free of course..."
            menu:
                "You currently have [gold] gold. \nWould you like to give 100 gold to Dahlia?"
                "\"Yes.\"":
                    if gold >= 100:
                        $ gold -=100
                        hide dahlia with d3
                        show dahlia 3 at right with d3
                        dah "Thank you. Your gold will be well spent, I assure you..."
                        dah "Now, follow me..."
                        show blkfade with d3
                        pause.7
                        hide blkfade with d3
                        dah "So, it is just me and you here, darling..."
                        dah "What would you like me to do now...?"
                        dah "Would you like to talk?"
                        dah "Or maybe you want me to dance for you first?"
                        dah "Oh would you rather jump straight to business?"
                        label akasaysno:
                        menu:
                            "\"Dance for me...\"":
                                show blkfade with d3
                                pause.7
                                hide blkfade with d3
                                a5 "Yeah................"
                                a5 "That's not happening..."
                                show blkfade with d3
                                pause.7
                                hide blkfade with d3
                                jump akasaysno
                            "\"Let's talk first...\"":
                                show blkfade with d3
                                pause.7
                                hide blkfade with d3
                                a5 "Nope... Didn't have enough time to put this one into the game either...."
                                show blkfade with d3
                                pause.7
                                hide blkfade with d3
                                jump akasaysno
                            "\"Bend over...\"":
                                hide dahlia with d3 
                                show dahlia 4 at right with d3
                                dah "Somehow I knew you would say that..."
                                dah "As you wish..."
                                play music "music/Bushwick Tarantella Loop.MP3" fadein 1 fadeout 1  #DAHLIA_SEX
                                #play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
                                show blkfade with d3
                                hide dahlia
                                show dahsex1 behind blkfade 
                                pause 1
                                hide blkfade with d3
                                show con1 at right
                                show ctc7 at right
                                pause
                                hide con1
                                hide ctc7
                                "*Tschflop!Flop! Flop!*"
                                dah[1] "Yes... Oh, yes... It's was a long overdue somebody to gave me a proper fucking..."
                                "*Flop! Flop! Flop!*"
                                dah[1] "Yes, yes...{image=textheart.png} Ah...{image=textheart.png} ah...{image=textheart.png} Yes, harder...{image=textheart.png}"
                                "*Flop! Flop! Flop!*"
                                dah[1] "Yes...{image=textheart.png} I love it... You are the best..."
                                "*Flop! Flop! Flop! Gltch! Gltch! Flopp!*"
                                dah[1] "Yes...{image=textheart.png} Yes, fuck me harder...{image=textheart.png}"
                                dah[1] "Oh, you are the best...."
                                dah[2] "Oh, wait, I already said that..."
                                dah[1] "Faster, my love, faster!"
                                "*Flop! Flop! Flop!*"
                                dah[1] "......"
                                dah[2] "If you want me to do something else, let me know..."
                                hide dahsex1 with d5
                                menu:
                                    "\"I want you to suck my cock now.\"":
                                        stop music fadeout 2
                                        dah[2] "Oh, absolutely..."
                                        dah[2] "I will suck you real good!"
                                        show blkfade with d3
                                        label dahliasuckscock2:
                                        play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
                                        show dahbj behind blkfade
                                        pause.5
                                        hide blkfade with d3
                                        dah "*slurp... Slurp... Gulp... Slurp... Slurp...*"
                                        dah "Thank you... *slurp* ... so much, for... *slurp*... letting me... *slurp* ...suck you cock... *slurp!*"
                                        dah "Oh, I could... *slurp* ...do this... *slurp*... all day... *slurp*..."
                                        dah "*slurp* Oh, I can feel it's... *slurp* ...getting enen bigger... *slurp!*..."
                                        dah "*Slurp*... Are you about to *slurp!* cum?"
                                        dah "*slurp!* Yes! Give it to me! ...*Slurp!* ...Give me your sperm! *Slurp!*"
                                        dah "*Slurp...*{p}*slurp...*{p}*slurp...*"
                                        hide dahbj with d5
                                        menu:
                                            "-Cum in her mouth-":
                                                show blkfade with d3
                                                show dahbj2 behind blkfade
                                                with flashbulb
                                                dah "!!!!!!!!!!!!!!!!!!!!"
                                                dah "*Gulp! Gulp!*"
                                                hide blkfade with d3
                                                dah "!!!!!!!!!!!!!!!!!!!"
                                                dah "*Gulp! Gulp! Gulp! Gulp!*"
                                                dah "*Gulp!...*{p}*Gulp!...*{p}*Gulp!...*{p}"
                                                dah "*Gulp...*"
                                                dah ".............................................................."
                                                dah "*Gulp....*"
                                                dah "..............................................................."
                                                show blkfade with d3
                                                hide dahbj2
                                                pause.7
                                                hide blkfade with d3
                                                dah[11] "Thank you, darling..."
                                                dah[4] "*Gulp!*...................."
                                                dah[7] "Mu-uaha....  So delicious...{image=textheart.png}"
                                                dah[6] "This was amazing... You rocked my world darling..."
                                                dah[6] "Yes, I say this to all my clients, but today is one of those rare occasions when I actually mean it..."
                                                dah[5] "Please come back any time..."
                                                show blkfade with d3
                                                ">You leave the brothel."
                                                hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                                                if brothelnight:
                                                    ">You return home and go to sleep."
                                                    show image "interface/blackfade.png" with Dissolve(.3)
                                                    pause 1
                                                    jump dayone
                                                else:            
                                                    ">It's getting late. You decide to head home."
                                                    jump dayends
                                            "-Cum on her face-":
                                                show blkfade with d3
                                                show dahbj3 behind blkfade
                                                dah "Ah!{image=textheart.png} Yes! Give it to me!"
                                                with flashbulb
                                                dah "!!!!!!!!!!!!!!!!!!!!"
                                                hide blkfade with d3
                                                dah "*Gulp! Gulp!*"
                                                dah "Ah...{image=textheart.png} Yes...{image=textheart.png}"
                                                dah "It's so hot... And there is so much of it..."
                                                dah "*Gulp!* I caught some with my mouth! *Gulp!* and some more!"
                                                dah "ah, you're just keep cumming and cumming! Ah! *pant!*"
                                                dah "Aha...{image=textheart.png} Ah...{image=textheart.png} Ah...{image=textheart.png}"
                                                show blkfade with d3
                                                hide dahbj3
                                                pause.7
                                                hide blkfade with d5
                                                dah[12] ".................................................."
                                                dah[12] "Look at me... I'm all covered in your hot semen..."
                                                dah[13] "Ah...{image=textheart.png} It's been a while since I had this much fun!"
                                                dah[13] "I hope I will see you again soon..."
                                                show blkfade with d3
                                                "You leave the brothel."
                                                hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                                                if brothelnight:
                                                    "You return home and go to sleep."
                                                    show image "interface/blackfade.png" with Dissolve(.3)
                                                    pause 1
                                                    jump dayone
                                                else:            
                                                    "It's getting late. You decide to head home."
                                                    jump dayends
                                    "\"I want you to lick my ass now.\"":
                                        #############Pleasure 2######Ass Liking########
                                        dah[7] "Oh, absolutely! Let me at it! Let me lick your asshole!"
                                        dah[6] "....huh?"
                                        dah[9] "Oh, wait, you serious?"
                                        dah[9] "Oh... alright, bend over then..."
                                        show blkfade with d3
                                        label dahlialiksass:
                                        play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
                                        show dahassl behind blkfade
                                        pause.5
                                        hide blkfade with d3                                            
                                        dah "*Slurp*... *Slurp*... I would rather suck your cock, but if that's what you want... *slurp*..."
                                        dah "*Slurp... Lick... Slurp...*"
                                        dah "*Slurp...* Do you like my tongue in your butt-hole? *Slurp*..."
                                        dah "*Slurp...*{p}*Lick...*{p}*Slurp...*"
                                        dah "*Slurp* Are you getting, close? *Slurp*."
                                        dah "*Slurp* You are, aren't you?..."
                                        show blkfade with d3
                                        hide dahassl
                                        show white
                                        pause.2
                                        hide white
                                        pause.2
                                        show white
                                        pause.2
                                        hide white
                                        pause.2
                                        with flashbulb
                                        dah "Yes, come on, come for Dahlia, you perverted, fuck... er. I mean, darling. *Slurp! Slurp! Slurp!*"
                                        show dahassl2 behind blkfade
                                        hide blkfade with d3
                                        dah "*Slurp...*{p}*Lick...*{p}*Slurp...*"
                                        dah "*Slurp...*{p}*Lick...*{p}*Slurp...*"
                                        dah "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                                        dah "Yes! Come! Come! *Slurp!*"
                                        dah "*Slurp...*{p}*Lick...*{p}*Slurp...*"
                                        show blkfade with d3
                                        hide dahassl2
                                        pause.5
                                        hide blkfade with d5
                                        dah[5] "Hey, I actually almost enjoyed this..."
                                        dah[6] "Although I hope this will not become a new trend or anything..."
                                        dah[5] "Well, feel free to come visit me any time, darling..."
                                        dah[8] "(And now I need to go brush my teeth... And wash my face...)"
                                        dah[9] "(And probably take a bath... and maybe drink some wine...)"
                                        show blkfade with d3
                                        ">You leave the brothel."
                                        hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                                        if brothelnight:
                                            ">You return home and go to sleep."
                                            show image "interface/blackfade.png" with Dissolve(.3)
                                            pause 1
                                            jump dayone
                                        else:            
                                            ">It's getting late. You decide to head home."
                                            jump dayends

                                    "\"I just want to keep fucking you.\"":
                                        dah[1] "Keep at it then! Fuck me harder! Make me scream!"
                                        show blkfade with d3
                                        ##############Pleasure 2##########Fuck######
                                        label dahliafucks2:
                                        play music "music/Bushwick Tarantella Loop.MP3" fadein 1 fadeout 1  #DAHLIA_SEX
                                        show dahsex1 behind blkfade
                                        pause.5
                                        hide blkfade with d3
                                        dah[1] "Yes! Yes! Bang that butt of mine!"
                                        dah "*Flop! Flopth! Phlopph! Glth! Flop!*"
                                        dah[3] "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
                                        dah[3] "Yes...{image=textheart.png} Yes...{image=textheart.png}"
                                        dah[4] "Oh, you're actually quite good at this..."
                                        "*Flopp! Flopp! Flopp! Tschlop!*"
                                        dah[6] "Oh, wow.....{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                                        dah[5] "Yes! Now I feel it...{image=textheart.png} keep going...{image=textheart.png}"
                                        dah[5] "Ah...{image=textheart.png} ah...{image=textheart.png} this is ...ah{image=textheart.png} ... amazing...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                                        "*Tschlop! Tschlop! Tschlop!*"
                                        dah[6] "How much longer can you go like that you beast?"
                                        dah[5] "Ah...{image=textheart.png} ah...{image=textheart.png} agh..."
                                        $ notsafe = renpy.random.randint(1, 2)    
                                        if notsafe == 1: 
                                            dah[6] "If you feel like cumming please do not restrain yourself..."
                                            dah[6] "You can come inside of me. It's safe... ngh!..."
                                        else:
                                            dah[5] "This is so good..."
                                            dah[6] "But... ah... please, {size=+5}do not{/size} come inside of me... ah..."
                                        hide dahsex1 with d5
                                        menu:
                                            "-Cum inside-":
                                                show dahsex2 with d5
                                                if notsafe == 1: 
                                                    dah[8] "Oh! You are...{image=textheart.png} cumming inside of me!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                                                    dah[5] "Aaaaaah!{image=textheart.png} Yeeeees!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                                                    dah[5] "Oh, havens, yes! I can feel your hot cum filling me from the inside!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                                                    dah[6] "Yes... yes... ah...{image=textheart.png} ah...{image=textheart.png}"
                                                    dah[6] "i'm..... ngh...."
                                                    dah[6] "ngh......"
                                                    dah[6] "......................................"
                                                    with hpunch
                                                    dah[7] "{size=+7}CUMMIIIIIING!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}{/size}"
                                                    dah[7] "Ah...{image=textheart.png} ah...{image=textheart.png}"
                                                    show con1 at right
                                                    show ctc7 at right
                                                    pause
                                                    hide con1
                                                    hide ctc7
                                                    show blkfade with d3
                                                    hide dahsex2
                                                    pause.5
                                                    hide blkfade with d3
                                                    play music "music/GoingtoKillMe.mp3" fadein 7 fadeout 3    # Maslab_BG
                                                    dah[6] "This was amazing... You rocked my world darling..."
                                                    dah[6] "Yes, I say this to everyone, but today is one of those rare occasions when I actually mean it..."
                                                    dah[6] "Please come back any time..."
                                                    show blkfade with d3
                                                    ">You leave the brothel."
                                                    hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                                                    if brothelnight:
                                                        ">You return home and go to sleep."
                                                        show image "interface/blackfade.png" with Dissolve(.3)
                                                        pause 1
                                                        jump dayone
                                                    else:            
                                                        ">It's getting late. You decide to head home."
                                                        jump dayends
                                                else:
                                                    show dahsex2 with d5
                                                    dah[7] "Ah... yes..."
                                                    dah[9] "Huh? What?! Ah! No, what are you doing? I told you not to come inside!"
                                                    dah[7] "Ah... it's so hot! Your sperm is filling me...."
                                                    ######Why inside, you jerk?"####
                                                    show blkfade with d3
                                                    hide dahsex2
                                                    pause.5
                                                    hide blkfade with d3
                                                    dah[10] "Did you enjoy yourself?"
                                                    dah[10] "Of course you did! Enough to ignore me asking you not to come inside!"
                                                    dah[10] "What's the matter with you? Are you ten years old or something?"
                                                    dah[10] "Don't you know what happens when you do that?"
                                                    dah[10] "If I get pregnant that baby will be your responsibility, you dumb little man..."
                                                    show blkfade with d3
                                                    ">You leave the brothel."
                                                    hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                                                    if brothelnight:
                                                        ">You return home and go to sleep."
                                                        show image "interface/blackfade.png" with Dissolve(.3)
                                                        pause 1
                                                        jump dayone
                                                    else:            
                                                        ">It's getting late. You decide to head home."
                                                    jump dayends
                                            "-Pull out-":
                                                show dahsex3 with d5
                                                dah[6] "Oh! Yes! Cover me with your cum!!!"
                                                dah[7] "Ah! Yes! Yes!!!"
                                                dah[7] "Ah...{image=textheart.png} It's so hot! Ah! Yes!"
                                                dah[8] "Ah...{image=textheart.png} Your sperm just fying everywhere... ah...{image=textheart.png}"
                                                dah[7] "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
                                                show blkfade with d3
                                                hide dahsex3
                                                pause.7
                                                hide blkfade with d5
                                                dah[7] "This was amazing... You rocked my world darling..."
                                                dah[6] "Yes, I say this to all my clients, but today is one of those rare occasions when I actually mean it..."
                                                dah[5] "Please come back any time..."
                                                show blkfade with d3
                                                ">You leave the brothel."
                                                hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                                                if brothelnight:
                                                    ">You return home and go to sleep."
                                                    show image "interface/blackfade.png" with Dissolve(.3)
                                                    pause 1
                                                    jump dayone
                                                else:            
                                                    ">It's getting late. You decide to head home."
                                                    jump dayends

                                

                            "\"Suck my cock.\"":
                                play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
                                hide dahlia with d3 
                                show dahlia 4 at right with d3
                                dah "Yes! I want it in my mouth badly!"
                                dah "Thank you!"
                                show blkfade with d3
                                hide dahlia
                                show dahbj behind blkfade 
                                dah "*Slurp... *{p}*slurp...*{p}*slurp...*"
                                pause 1
                                hide blkfade with d3
                                show con1 at right
                                show ctc7 at right
                                pause
                                hide con1
                                hide ctc7
                                dah "*Slurp... gulp... slurp..*."
                                dah "*Slurp...* your... *gulp* cock, master... *slurp*..."
                                dah "It's... *slerp-slurp* ...so delicious... *slurp*..."
                                dah "Do you... *slurp* ...like it, how I... *slurp* suck it? *slurp!*"
                                dah "I wish I could... *slurp* suck it... *gulp*... all day long..."
                                dah "*Slurp... *{p}*slurp...*{p}*slurp...*"
                                hide dahbj with d5
                                menu:
                                    "\"Now I want to fuck you.\"":
                                        dah[6] "I was hoping you would say that..."
                                        show blkfade with d3
                                        jump dahliafucks2
                                    "\"Now, lick my asshole.\"":
                                        dah[7] "Oh, absolutely! Let me at it! Let me lick your asshole!"
                                        dah[6] "....huh?"
                                        dah[9] "Oh, wait, you serious?"
                                        dah[9] "Oh... alright, bend over then..."
                                        show blkfade with d3
                                        jump dahlialiksass
                                    "\"Keep going!\"":
                                        show blkfade with d3
                                        jump dahliasuckscock2
                                        
                            "\"Lick my ass.\"":
                                dah "What...? Oh, so you one of \"those\"... Yes, of course...."
                                hide dahlia waith d3
                                show dahlia 4 at right with d3
                                dah "I looooove licking asses... apparently..."
                                hide dahlia waith d3
                                show dahlia 5 at right with d3
                                dah "Oh, let's just get this over with... Spread your buttcheeks... Dahlia will lick you real clean now..."
                                dah "................"
                                show blkfade with d3
                                hide dahlia
                                show dahassl behind blkfade 
                                play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
                                dah "*Slurp*... *Slurp*...."
                                dah "How's that? Do you like it?"
                                pause 1
                                hide blkfade with d3
                                show con1 at right
                                show ctc7 at right
                                pause
                                hide con1
                                hide ctc7
                                dah "*Slurp*... *Slurp*... I'm practically fucking your ass with my tongue, you know... *slurp*..."
                                dah "*Slurp... Lick... Slurp...*"
                                dah "*Slurp...* This is so degrading... *Slurp*..."
                                dah "(Is this why I actually kinda enjoy this? Hm, Interesting...)"
                                dah "*Slurp...*{p}*Slurp...*{p}*Lick...*"
                                hide dahassl with d3
                                show image "04_pt/dahlia/animation/asslout.png" with d3
                                dah "Well, if you ass wasn't clean before, it is now... *slurp*"
                                dah "Want me to do something different now?"
                                hide image "04_pt/dahlia/animation/asslout.png" with d3
                                menu:
                                    "\"Now I want to fuck you.\"":
                                        dah[3] "Of course..."
                                        show blkfade with d3
                                        pause.5
                                        jump dahliafucks2
                                    "\"Now, suck my cock.\"":
                                        dah[3] "Right... Give it to me..."
                                        show blkfade with d3
                                        jump dahliasuckscock2
                                    "\"Nope. Keep going!\"":
                                        dah[3] "Of course..."
                                        show blkfade with d3
                                        pause.5
                                        jump dahlialiksass
                    else:
                        dah "Doesn't look like you can afford it, honey. Well, I don't work for free honey."
                        hide dahlia with d3
                        play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                        jump brothelmain
                "\"Not today.\"":
                    dah "Well, I don't work for free honey. Come back if you change your mind."
                    play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                    jump brothelmain
        "\"Not today.\"":
            dah "Pitty..."
            play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
            show blkfade with d3
            hide dahlia with d3
            pause.5
            hide blkfade with d3
            jump brothelmain


###LOLA
label lolawhore:
    play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
    show blkfade with d5
    pause.3
    hide blkfade with d5
    lola[11] "Would you like to have sex with me, mister?"
    lola[11] "Stick your dick into my pussy and everything?"
    menu:
        "\"Yes please!\"":
            lola[11] "That will be 10 gold coins." 
            lola[13] "............?"
            lola[13] "No, wait, I mean 20 gold coins..."
            lola[14] "No, wait, 25...?"
            menu:
                "You currently have [gold] gold. \nWould you like to give 25 gold to Lola?"
                "\"Yes.\"":
                    if gold >= 25:
                        $ gold -=25
                        lola[11] "Alright!!!!"
                        lola[11]"Follow me upstairs, please."
                        sch3 "What is going on here?"
                        lola[14] "Mom? You were supposed to be out..."
                        sch3 "Lola, my girl, how many times did I tell you: I will never let you become a whore... Not under my roof."
                        lola[15] "You never let me have any fun! Ever!!!"
                        stop music fadeout 5
                        lola[15] "Why do you hate me so much?"
                        sch3 "I don't hate you, you silly girl, I'm just looking after you!"
                        lola[15] "Well I do hate you then! \nI hate you! \nI hate you!"
                        sch3 "Lola, my dear, don't make a scene in front of a customer."
                        lola[15] "I don't care! Just leave me alone everyone!!!"
                        $ quest7 += 1
                        sch3 "I apologize for the inconvenience, sir. My daughter is unrully."
                        sch3 "You will have to choose another girl."
                        play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                        jump brothelmain
                    else:
                        lola[13] "Doesn't look like you can afford it, honey. Well, I don't work for free..."
                        jump brothelmain
                "\"Not today.\"":
                    lola[12] "What? How dare you to resist my charm, you old perv?"
                    play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                    jump brothelmain
        "\"Not today.\"":
            lola[12] "What? How dare you to resist my charms, you old perv?"
            play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
            jump brothelmain
label lolaquest:
    play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
    show blkfade with d5
    pause.5
    hide blkfade with d5
    lola[13] "(Pst! Hey, mister.)"
    lola[13] "Listen, I'm so tired of sitting on my butt all day, cooped up in this old house..."
    lola[13] "My mother won't let me go anywhere by myself..."
    lola[12] "Unless it's a chore of some sort..."
    lola[13] "So, would you care to take me out...?"
    menu:
        lola[13] "I will make it worth it for you..."
        "\"Make it worth it how?\"":
            lola[13] "Somehow.. Anyhow, I don't care..."
            lola[13] "What do you want?"
            lola[12] "I could show you my tits or something..."
            lola[12] "It really doesn't matter, as long as you liberate me from my mother's oppression!"
        "\"What will your mother say?\"":
            lola[13] "Exactly... You will have to ask her first..."
        "\"What's up with your hair?\"":
            lola[13] "What? Oh, does it matter? We can always discuss this later."
    lola[13] "So, listen carefully, old man..."
    lola[13] "My mother will never entrust me to your care unless you make her \"happy\"..."
    menu:
        lola[13] "So you go ahead and do that thing that men always do to make her happy, alright?"
        "\"I will do it!\"":
            if onquest:
                ">You need to finish your current quest first, before you can take a new one."
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                jump brothelreopned
            else:
                lola[11] "Alright! Now go make mother trust you!"
                show image "interface/blackfade.png" with Dissolve(.3)
                pause.7
                hide image "interface/blackfade.png" with Dissolve(.3)
                play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
                sch3 "What? I can't possibly trust you with my daughter..."
                sch3 "Although... Hm..."
                sch3 "Take off that cloak of yours, I want to take a good look at you..."
                ">Reluctantly you take off your cloak."
                sch3 "Look at you, mr. handsome..."
                sch3 "Alright, that could work I suppose..."
                sch3 "But you need to do this properly, like they used to do it back in my days..."
                sch3 "First off, I want presents..."
                sch3 "I want something nice and something delicious."
                sch3 "Bring me one of each and then we'll talk..."
                menu:
                    "\"What do you mean by \"nice\"?\"":
                        sch3 "Something that I would like... \nUse your imagination!"
                    "\"What do you mean by \"delicious\"?\"":
                        sch3 "A dish of course... \nSomething with a lot of grease..."
                    "\"I will be on my way then...\"":
                        pass
                sch3 "I will be waiting..." 
                $ quest7 +=1
                $ quest7start = True
                $ quest7balsam = True
                $ quest7maslab = True
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
                jump mainmenu
        "\"Maybe later.\"":
            lola[12] "Tsk... You're boring..."
            play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
            jump brothelreopned

            
####QUEST#8#############
label quest8start:
    play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
    show blkfade with d3
    pause.5
    hide blkfade with d3
    lola[11] "Hi there..."
    lola[13] "You know, that visit to your house the other night got me thinking..."
    lola[14] "Well, I had this idea for a while now..."
    lola[13] "But now I am absolutely certain!"
    lola[71] "I want to be a whore, just like Iris!"
    lola[12] "There is one {size=+5}big{/size} problem though..."
    lola[12] "My mom..."
    lola[12] "She still sees me as a child..."
    lola[13] "So I need to show her that I'm not a child anymore..."
    lola[14] "But I will need your help..."
    lola[14] "And your money..."
    lola[71] "To be completely honest you will have to do all the work..."
    menu:
        lola[13] "Can I count on you?"
        "\"Of course!\"":
                if onquest:
                    "You need to finish your current quest first, before you can take a new one."
                    jump brothelreopned
                else:
                    lola[71] "Great! Thank you! I will make it up to you, I promise!"
                    lola[70] "So here is my plan: first I will need a proper dress..."
                    lola[70] "Then I will let mother see me wear it, and as soon as she sees me in it she will understand."
                    lola[71] "She might even cry a little... Say stuff like \"My little girl, all grown up\"."
                    menu:
                        lola[13] "What do you think of my plan?"
                        "\"Sounds solid. What could go wrong?\"":
                            lola[70] "I know, right!? Pretty brilliant!"
                        "\"It's stupid.\"":
                            lola[12] "You're stupid!"
                    lola[13] "So, here is a simple drawing of a dress that I want. Could you take it to Azalea for me?"
                    show image "04_pt/slavem/masteritem.png" with moveinleft
                    $ renpy.play('sounds/win2.mp3')
                    show image "04_pt/slavem/boxirissketch.png" with moveinright
                    ">You receive a drawing of a very perverted dress made with crayons..." 
                    hide image "04_pt/slavem/boxirissketch.png" with Dissolve(.4)
                    hide image "04_pt/slavem/masteritem.png" with d3
                    lola[12]"Alright, just let me know when you will have the dress..."
                    $ flagone = True
                    label goodluckkiss:
                    menu:
                        lola[71] "Bye now..."
                        "\"A kiss for good luck?\"":
                            lola[71] "Of course!"
                            ">You have to stoop down to let Lola reach your cheek."
                            hide image "04_pt/iris/q5/iris99.png" at center with Dissolve(.3)
                            pause.5
                            $ renpy.play('sounds/kiss.mp3')
                            with kissiris
                        "\"Show me your tits for good luck?\"":
                            lola[12] "Right here? My mom could see..."
                            lola[13] "OK, I'll do it real quick. Are you ready?"
                            show blkfade with d3
                            hide blkfade with d3
                            lola[72] "..............................................{nw}"
                            show blkfade with d3
                            hide blkfade with d3
                            lola[71] "That's enough for now."
                        "\"Let me touch your tits for good luck?\"":
                            lola[13] "Sure, but hurry up. Do it while my mom is not watching..."
                            ">You grab Lola's tits and squeeze them..."
                            lola[13] "........................"
                            ">You give her breasts a few pulls and another squeeze then let go..."
                        "\"Massage my crouch for good luck?\"":
                            lola[13] "What?" 
                            lola[12] "Oh... Em... Ok...."
                            ">Lola massages your dick through you pants for a few seconds..."
                        "\"Give me a handjob for good luck?\"" if flagone:
                            $ flagone = False
                            lola[12] "What? Here? My mom would kill me!"
                            lola[13] "Some other time, OK?"
                            jump goodluckkiss
                    lola[71] "See you soon."
                    $ quest8start00 = False
                    $ quest8start = True
                    $ onquest = True
                    
                    show image "04_pt/slavem/qstart.png" with Dissolve(.3)
                    show image "04_pt/slavem/onaquest.png" with Dissolve(.3)
                    show con1 at right
                    show ctc7 at right
                    pause 
                    hide con1
                    hide ctc7
                    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                    hide image "04_pt/slavem/qstart.png" with Dissolve(.3)
                    show blkfade with d3
                    hide image "04_pt/slavem/bld2.png" 
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                    pause.3
                    hide blkfade with d3
                    jump mainmenu
        "\"Not interested.\"":
            lola[12] "You're boring!"
            show blkfade with d3
            pause.3
            hide blkfade with d3
            play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
            jump brothelreopned  
#######DRESS FOR LOLA#######
label quest8start3:
    play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
    show blkfade with d3
    pause.3
    hide blkfade with d3
    lola[13] "The dress is ready!?"
    lola[12] "Giveittome!!!"
    show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
    show image "04_pt/slavem/boxdress.png" with moveinleft
    ">You hand over the dress to Lola."
    hide image "04_pt/slavem/boxdress.png" with moveoutright
    hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
    lola[11] "Awesome! I can't wait to try this on!!!"
    lola[71] "Thank you for your help, old man."
    menu:
        lola[12] "Well, you better go now."
        "\"What about my reward?\"":
            lola[12] "What? Oh, right..."
            lola[13] "That will have to wait..."
        "\"You owe me 600 gold coins.\"":
            lola[12] "Seriously?"
            lola[12] "You are so, so, so cheap! It's unbelievable."
            lola[13] "Alright, whatever. Let's talk about this later."
        "\"See ya.\"":
            lola[71] "Bye now."
    hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
    $ quest8start3 = False
    $ quest8start4 = True
    $ quest8complete = True
    $ onquest = False
    $ renpy.play('sounds/win2.mp3')                        
    show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    ">Lola can work at the brothel now."
    hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    show image "interface/blackfade.png" with Dissolve(.3)
    pause.5
    jump dayends
    
    
##############################
label quest8start4:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with d3
    pause.5
    show lola 16 at center behind blkfade
    hide blkfade with d3
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    hide lola with d3
    show lola 17 at center with d3
    sch1000 "Thank you for choosing me."
    hide lola with d3
    show lola 18 at center with d3
    sch1000 "Em... er..."
    hide lola with d3
    show lola 17 at center with d3
    sch1000 "Oh, right. Would you like to have sex with me now?"
    sch1000 "That will be 5 gold coins..."
    hide lola with d3
    show lola 21 at center with d3
    sch1000 "No, wait, wait, I mean... 1000 gold coins..."
    sch1000 "No, that's way too much..."
    hide lola with d3
    show lola 17 at center with d3
    sch1000 "Em... OK, 500 gold coins then..."
    hide lola with d3
    menu:
        "You currently have [gold] gold. \nWould you like to give 500 gold to Lola?"
        "\"Yes.\"":
            if gold >= 500:
                $ quest8start4 = False
                $ quest8start5 = True
                jump lolawhoring
            else:
                show lola 21 at center with d3
                sch1000 "Doesn't look like you can afford it..."
                show lola 18 with d3
                sch1000 "This sucks!"
                show blkfade with d3
                hide lola 
                pause.5
                hide blkfade with d3
                jump brothelmain
        "\"Not today.\"":
            show lola 18 with d3
            sch1000 "Well, I don't work for free... Come back if you change your mind."
            show blkfade with d3
            hide lola 
            pause.5
            hide blkfade with d3
            jump brothelmain
label lolawhoring:
    
            show lola 16 at center with d3
            sch1000 "Huh?"
            show lola 19 at center with d3
            sch1000 "Oh, it's you old man!"
            hide lola with d3
            show lola 20 at center with d3
            sch1000 "I'm wearing your dress today... What do you think? Do you like it?"
            show con1 at right
            show ctc7 at right
            pause
            hide con1
            hide ctc7
            hide lola with d3
            $ flagone = True
            $ flagtwo = True
            label talking3:
            menu:
                "\"You look cute.\"":
                    show lola 22 at center with d3
                    sch1000 "Really...?"
                    show lola 21 at center with d3
                    sch1000 "Shoot! I was trying to create a more mature image..."
                    hide lola with d3
                "\"You look beautiful.\"":
                    show lola 19 at center with d3
                    sch1000 "You think?"
                    show lola 20 at center with d3
                    sch1000 "Thank you."
                    hide lola with d3
                "\"You look like a whore.\"":
                    show lola 19 at center with d3
                    sch1000 "Really, really?"
                    show lola 21 at center with d3
                    sch1000 "You're not just saying this to make me feel better, are you?"
                    hide lola with d3
                "\"I didn't recognize you...\"" if flagtwo:
                    show lola 20 at center with d3
                    sch1000 "Mee-hee-hee. You're silly."
                    sch1000 "Of course it's me..."
                    $ flagtwo = False
                    hide lola with d3
                    jump talking3
                "\"What have you done to yourself?\"" if flagone:
                    show lola 16 at center with d3
                    sch1000 "What? You don't like it?"
                    show lola 18 at center with d3
                    sch1000 "I don't believe you! I think you like my new look you just won't admit it..."
                    $ flagone = False
                    hide lola with d3
                    jump talking3
            show lola 23 at center with d3
            sch1000 "So, let's go upstairs then?"
            sch1000 "Follow me please..."
            show blkfade with d3
            pause 1
            hide lola 
            hide blkfade with d3
            show lily 1 at center with d3
            sch300 "What is going on here?"
            hide lily 1 with d3
            show lily 1 at right with d3
            show lola_f 16 at left with d3
            sch1000 "M-mother?! I... I can explain..."
            hide lily with d3
            show lily 1 at right with d3
            sch300 "Lola? What have you done to your hair girl?"
            sch300 "And where did you get that dress?"
            hide lola with d3
            show lola 25 at center with d3
            sch1000 "Doesn't matter, mom!? I'm with a client right now!"
            hide lola with d3
            show lola_f 24 at left with d3
            sch1000 "You are ruining everything again!"
            hide lily with d3
            show lily 1 at right with d3
            sch300 "With a client? What nonsense! Don't be silly girl!"
            sch300 "Go to your room at once!"
            hide lola with d3
            show lola_f 26 at left with d3
            sch1000 "M-mommy, please... I'm begging you..."
            hide lily with d3
            show lily 1 at right with d3
            sch1000 "Shush, girl. Back to your room I said!"
            hide lola with d3
            show lola_f 28 at left with d3
            sch1000 "I hate you, I hate you, I hate you!"
            hide lola with d3
            show lola_f 29 at left with d3
            sch1000 "You are not even my real mom!"
            hide lily with d3
            show lily 4 at right with d3
            sch300 "You mean little girl! You know I love you like my own!"
            sch300 "One more word and I'll have to slap some sense into you, girl!"
            hide lola with d3
            show lola_f 30 at left with d3
            sch1000 "I hate! You hear me?! {size=+5}I HATE YOU!!!{/size}"
            hide lily with d3
            show lily 5 at right with d3
            sch1000 "That's enough! Go to your room and take this ridiculous outfit off!"
            hide lola with d3
            show lola_f 31 at left with d3
            sch1000 "This is so unfair..."
            show blkfade with d3
            pause 1
            hide lola 
            hide lily
            hide blkfade with d3
            show lily 2 at center with d3
            sch300 "I apologize for making a scene in front of you..."
            sch300 "You will have to choose another girl..."
            show blkfade with d3
            hide lily
            hide bld2
            pause.5
            hide blkfade with d3
            if brothelnight:
                play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
            else:
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME                                               
            jump brothelmain

###############LOLA COMES##########
label quest8start5:
    show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
    ">You send Princess jasmine to her room."
    show sleeping with Dissolve(.3)
    "Jasmine goes to bed ...."
    j "ZZZzzzzz....."
    show blkfade with Dissolve(.3)
    hide sleeping with Dissolve(.3)
    show sleeping2 behind blkfade
    pause 3
    "......................"
    $ renpy.play('sounds/door3.mp3')
    "Knock-knock-knock..."
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    $ renpy.play('sounds/door3.mp3')
    "*Knock-knock-knock...*"
    ">Somebody is knocking on the door..."
    ">It's long past midnight... Who could this possibly be?"
    menu:
        "-Ignore the knocking-":
            $ renpy.play('sounds/door3.mp3')
            "*Knock-knock-knock...*"
            sch1000 "*Sob*... *sob*... Old man.... Please, let me in....*sob*"
            ">Lola? What is she doing here at this hour?"
            menu:
                "-Go to the door and let her in-":
                    pass                     
                "-Ignore her and go back to sleep-":
                    $ renpy.play('sounds/door3.mp3')
                    "Knock-knock-knock..."
                    sch1000 "*sob* Please.... Old man, let me in... I have nowhere else to go... *sob*."
                    $ renpy.play('sounds/door3.mp3')
                    "Knock-knock-knock..."
                    $ renpy.play('sounds/door3.mp3')
                    "Knock-knock-knock..."
                    sch1000 "Old ma-a-a-n! *sob*"
                    $ renpy.play('sounds/door3.mp3')
                    "*Knock-knock-knock...*"
                    "...............................{w}..............{w}...............{w}..............."
                    ">The knocking finally stopped. You go back to sleep."
                    $ lolawhoredays -=7
                    pause 1        
                    jump dayone
        "-Go and see who that is-":
            pass
    $ renpy.play('sounds/door.mp3')
    hide blkfade with Dissolve(.3)
    show bld with d3
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    lola[10] "Hi.... *sob*"
    lola[10] "Thank you for letting me in..."
    lola[10] "I had a fight with my stupid mother..."
    lola[10] "She is so stupid, I hate her!"
    show blkfade with d3
    pause.5
    hide blkfade with d3
    lola[62] "You remember that beautiful dress you bought for me?"
    lola[62] "Mother wanted to give it to one of the girls..."
    lola[63] "I said that she has no right to do that, and we got in a big fight and..."
    lola[62] "And..."
    lola[62] "And I just ran away..."
    lola[63] "I don't want to live in the stupid brothel any longer...."
    lola[63] "Can I stay with you for a while? *sob*"
    lola[63] "Old man, please... I will clean your house, or do whatever you want..."
    lola[56] "I know your house is not very big... But I don't take much space..."
    lola[55] "Maybe I can share a room with your slave-girl?"
    menu:
        "\"What a great idea!\"":
             lola[52] "Alright! Let's go wake her up!"
        "\"I don't think she will like it.\"":
            lola[56] "So what?"
            lola[56] "Aren't you her master? Just order her to like it..."
            lola[57] "I mean, that's how it works, doesn't it?"
        "\"You can sleep in my room.\"":
            lola[61]"Hm..."
            lola[61] "I would rather share a room with another girl..."
    show blkfade with d3
    pause.7
    hide blkfade with d3
    $ renpy.play('sounds/door.mp3')
    lola[56] "(So this is her room? It's pretty specious...)"
    lola[54] "(Alright, wake her up and introduce us!)"
    menu:
        "\"Wake up, you whore!!!\"":
            hide sleeping2 with d3
            pause 1
            show jas 15 at center with d3
            j ".......?"
            show jas 10 with d3
            j "What are you doing in my room at this time of the night?"
            show jas 13 with d3
            j "Huh?"
            hide jas with d3
        "\"Jasmine. Jasmine, are you asleep?\"":
            hide sleeping2 with d3
            pause 1
            show jas 10 with d3
            j "What is going on...?"
            hide jas with d3
        "\"Fire! Fire! Run for your life princess!!!\"":
            hide sleeping2 with d3
            pause 1
            show jas 15 at center with d3
            j "*yawn?*"
            show jas 13 at center with d3
            j "What? A fire!?"
            j "Oh my god! My jewels, and my dresses! Safe them first!"
            show jas 14 with d3
            j "Out of my way, old man, I need to leave the building!"
            lola[46] "Ha-ha-ha! This is funny!"
            show jas 10 at center with d3
            j "Huh?"
            hide jas with d3
    show jas 8 with d3
    j "Who is this girl?"
    lola[52] "Good evening. My name is Lola. It's nice to meet you."
    hide jas with d3
    show jas 11 with d3
    j "Yeah, whatever."
    hide jas with d3
    show jas 14 with d3
    j "Who is this little whore? Why did you bring her here?"
    lola[54] "I--"
    hide jas with d3
    show jas 8 with d3
    j "hush, girl, I'm not talking to you!"
    lola[57] "(What a meanie!)"
    show jas 4 with d3
    j "Listen here, \"my master\", and listen carefully..."
    show jas 14 with d3
    j "I am willing to put up with all sorts of perverted crap you force me to go through lately..."
    j "But {size=+5}ONLY{/size} for as long as I have my room for myself..."
    j "A place to relax and enjoy some peace..."
    show jas 8 with d3
    j "If you think that I will be sharing my personal space with some dirty peasant you found in a gutter, you are gravely mistaken!" 
    lola[57] "..............."
    hide jas with d3
    menu:
        "\"Fine. I got it. Calm down now.\"":
            pass
        "\"Listen to me, whore! I'm your master!\"":
            show jas 16 with d3
            j "You son of a jackal..."
            hide jas with d3
            show jas 14 with d3
            j "You think you can take everything from me and I will just keep quiet?" 
            j "You think you can just keep pushing and pushing, and I will just take it silently?"
            hide jas with d3
            show jas 6 with d3
            j "I don't mind going outside and flaunting my bare tits in front of complete strangers!"
            lola[53]"(Cool! I want to do that too.)"
            hide jas with d3
            show jas 12 with d3
            j "I even let you dress me like a common slave-girl and parade me half-naked in front of my subjects..."
            lola[58] "(Oh, this is awesome!)"
            hide jas with d3
            show jas 14 with d3
            j "But this, right here, could be the last drop! I'm warning you!"
            hide jas with d3
            menu:
                "\"Fine. Whatever. I understand.\"":
                    pass
                "\"Shut up, whore, or you will be punished!\"":
                    show jas 14 with d3
                    j "I don't give a damn about your stupid punishments, you old fool!"
                    j "Leave this girl here, and I will smother her in her sleep, I promise you that!"
                    lola[61] "Oh, wow, you know what, I don't feel like staying here anymore..."
                    hide jas with d3
    show jas 6 with d3
    j "Wise decision! Now get out of my room, both of you!"
    hide jas with d3
    show jas 14 with d3
    j "I need to get some sleep..."
    j "If I have to parade my body in front of dirty commoners again tomorrow, I at least want to look my best..."
    show blkfade with d3
    $ renpy.play('sounds/door2.mp3')
    hide jas
    pause.7
    hide blkfade with d3
    lola[55] "Wow... She is really scary..."
    lola[54] "I think I would rather return home and make peace with my mom now..."
    if quest9complete:
        lola[52]"Oh, wait, what's this a door for...?"
        show blkfade with d3
        pause.5
        hide blkfade with d3
        $ renpy.play('sounds/door.mp3')
        lola[55] "Hey, this room is empty! Why didn't you tell me you had a spare room!?"
        lola[53] "Oh, but this is perfect!"
        lola[58] "I'm staying here!!!"
        $ renpy.play('sounds/win2.mp3')
        show blkfade with d3
        ">Lola will be living with you from now on."
        $ lolamovedin = True
        $ emptyroom = False
        $ lolawaitsforroom = False
        $ quest8start5 = False
        $ jasmeetslola = True
        pause 1        
        jump dayone
    $ lolawaitsforroom = True
    lola[56] "I could still stay here if you had a spare room or something..."
    lola[52] "Well, anyway, I fell better now. Could you walk me home?"
    show blkfade with d3
    pause.7
    "You walk Lola back to the brothel, then return home and go to sleep..."
    $ lolawhoredays -=7
    pause 1        
    jump dayone


#######################################
####INVATING LOLA. ROOM READY#######
label lolawaitsforroom:
    show blkfade with d3
    show bld2 behind blkfade
    show lola 16 behind blkfade
    pause.5
    hide blkfade with d3
    sch1000 "Hi there..."
    hide lola with d3
    show lola 16 with d3
    sch1000 "Yeah, I'm not working, because my mom wouldn't let me..."
    hide lola with d3
    show lola 23 with d3
    sch1000 "But I'm still wearing this dress to irritate her..."
    hide lola with d3
    menu:
        "I have an empty room waiting for you.":
            show lola 19 with d3
            sch1000 "Seriously?"
            sch1000 "When can I move in??"
            hide lola with d3
            show lola 20 with d3
            sch1000 "Let's do it, right now!"
            sch1000 "Go outside and wait for me, I will sneak out!"
            show blkfade with d5
            hide lola
            hide bld2
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            $ renpy.play('sounds/door2.mp3')
            pause.5
            hide blkfade with d5
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            "................{w}..............{w}...............{w}..............."
            show lola 8 with d3
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            sch1000 "Alright. let's go!!"
            show blkfade with d3
            hide lola
            show bld
            $ renpy.play('sounds/door.mp3')
            pause 1
            hide blkfade with d3
            lola[55] "So this will be my room then? Awesome!"
            lola[61] "Thank you for letting me stay here, old man!"
            lola[52] "You're so nice..."
            lola[53] ".............."
            show blk50 with d3
            $ renpy.play('sounds/win2.mp3')                     
            "Lola will be living with you from now on."
            $ lolamovedin = True
            $ emptyroom = False
            $ lolawaitsforroom = False
            $ quest8start5 = False
            $ jasmeetslola = True
            show blkfade with d3
            pause 1        
            jump dayends
        "I will choose an actual whore then.":
            show lola 18 with d3
            sch1000 "I understand..."
            show blkfade with d3
            pause.5
            hide bld2
            hide lola
            hide blkfade with d3
            jump brothelmain

    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    