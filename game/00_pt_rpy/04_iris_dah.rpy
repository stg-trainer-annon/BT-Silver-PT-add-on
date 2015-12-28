###DAHLIA AND DA
label dahliaandda:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    hide blkfade 
    show blkfade with d3
    pause.7
    show dahlia 3 at right behind blkfade
    hide blkfade with d3
    sch900 "Hello, there, sweetheart."
    sch900 "Did you say it was me and Iris you wanted to keep you company this time?"
    menu:
        "\"Yes. You and Iris.\"":
            sch900 "I see..."
            hide dahlia with d3
            show dahlia 1 at right with d3
            sch900 "Iris, come here, dear. You've been chosen..."
            show emo7 at Position(xpos=0, ypos=100, xanchor=0, yanchor=0) 
            sch1100 "Really? REALLY?!"
            hide emo7
            show emo7 at Position(xpos=0, ypos=100, xanchor=0, yanchor=0) 
            sch1100 "I'm coming!!!"
            hide emo7
            show iris_f 84 at left with d3
            sch1100 "Hello! Welcome to--"
            hide iris with d3
            show iris_f 86 at left with d3
            sch1100 "Oh, hi there, old man..."
            hide dahlia with d3
            show dahlia 5 at right with d3
            sch900 "Iris?! Your manners!"
            hide iris with d3
            show iris_f 83 at left with d3
            sch1100 "Oh, right, sorry."
            hide iris with d3
            show iris_f 84 at left with d3
            sch1100 "Em... welcome to the \"Red Phoenix\"..."
            sch1100 "Sweetheart..."
            hide dahlia with d3
            show dahlia 3 at right with d3
            sch900 "Both myself and Iris are available at the moment, and would be very happy to get to know you better, sweetheart..."
            sch900 "Booking us both will cost you 250 gold coins."

            menu:
                "You currently have [gold] gold. \n Would you like to give 250 gold to Dahlia?"
                "\"Alright. Here is your money.\"":
                    if gold >= 250:
                        $ gold -=250
                        "You give Dahlia 250 gold coins."
                        sch900 "Thank you, dear."
                        hide dahlia with d3
                        show dahlia 4 at right with d3
                        sch900 "Alright then, shall we go upstairs?"
                        hide iris with d3
                        show iris_f 86 at left with d3
                        sch1100 "....................."
                        show blkfade with d3
                        pause.7
                        hide dahlia
                        hide iris
                        jump dah_iris_action

                    else:
                        sch900 "Doesn't look like you can afford this, honey. Well, we don't work for free..."
                        show iris_f 89 at left with d3
                        sch1100 "{size=-5}(.....This sucks!){/size}"
                        show blkfade with d3
                        pause.7
                        hide dahlia
                        hide iris
                        hide blkfade with d3
                        jump brothelmain
                "\"Sorry forgot my money pouch.\"":
                    sch900 "Well, we don't work for free, honey. Come back if you change your mind."
                    show iris_f 89 at left with d3
                    sch1100 "{size=-5}(.....This sucks!){/size}"
                    show blkfade with d3
                    pause.7
                    hide dahlia
                    hide iris
                    hide blkfade with d3
                    if brothelnight:
                        play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                    else:
                        play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                    jump brothelmain
        "\"No, changed my mind.\"":
            sch900 "As you wish..."
            show blkfade with d3
            pause.7
            hide dahlia
            hide blkfade with d3
            if brothelnight:
                play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
            else:
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
            jump brothelmain
            
        


            
##############SEX####################
label dah_iris_action:
show ctc7 at right
pause
hide ctc7
play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
dah[2] "Alright then. How about you allow us to make all your troubles fade away, huh, dear?"
m "Give it a try..."
dah[1] "Oh, have faith sweetheart. Just lie down and let us do our job..."
dah[3] "Now, you watch closely, Iris, I'm about to teach you something new."
ir[3] "Em... OK."
ir[5] "Hm? What are you.... doing?"
dah[1] "You just watch now, dear..."
ir[5] "B-but... what? H-how? In that position...?"
dah[7] "Yes, I'm going to lick his asshole clean."
ir[8] "What?! \nDahlia! \nEww!!!"
dah[9] "Be quiet girl. We don't say \"Eww\" to anything in this establishment, do you understand?"
ir[9] "B-but.... that's just...."
ir[8] "Eeewww!"
dah[9] "Iris! You came to me and asked me to teach you how to be a proper whore, did you not?"
dah[9] "If you changed your mind, you are free to leave right now and never come back!"
ir[10] "No, no, I'm sorry! You know how much I love working here..."
dah[3] "Well, alright then."
dah[2] "Plus this wouldn't be the first time I licked his asshole."
dah[2] "I was a bit hesitant at first to be honest, but now I learned how to find pleasure in it..."
ir[10] "Will I have to as well... em, I mean...."
dah[1] "Not today, dear. You just watch...."
dah[7] "Today his asshole is all mine!"
ir[1] "Alright... *sigh of relief*"
dah[2] "Although, you know what? How about you suck on that huge dick of his while I keep myself busy down here?"
ir[4] "Yes! I can do that!"
dah[5] "What do you think, sweetheart?"
dah[5] "Do you want Iris to put your big cock in her tiny wet mouth?"
m "Let's just start already."
dah[4] "Alight then..."
dah[7] "*Lick-lick*"
g7 "ah... this is nice..."
sch1100 "*Slurp-slurrple!*"
g5 "Oh, by the great Genie Gods, this is just perfect..."

show ctc7 at right
pause
hide ctc7
show image "04_dah_iris/d_a01.png" behind blkfade
hide blkfade with d5
show ctc7 at right
pause
hide ctc7
sch1100 "*Glorp!* What are you doing?! *Slorp!*"
g3 "I couldn't resist..."
sch1100 "*Slurp-Gobl!*"
g3 "Your asshole is so... stretchy..."
sch1100 "*Slurp-gobl-slurp!*"
g3 "And your pussy is dripping wet... Let me help you keep it tidy! *Slurp*"
sch1100 "*Goble-slurp* Ah... No, ah... what are you doing...?"
sch900 "Leave the man be, girl. Whatever he is doing to you down there, he paid his hard earned gold for the right to do it."
sch1100 "*Slurp* B-but?"
show image "04_dah_iris/d_a03.png" with d3
sch900 "Let it go, I said. *Lick!*"
sch900 "Concentrate on the task at hand: suck his dick nice and good... *lick!*"
sch900 "Do you need help?"
show image "04_dah_iris/d_a04.png" with d3
sch900 "There!"
sch1100 "*Slurp?* No, wait, don't push my head like that..."
sch900 "Down you go, girl. All the way to the balls."
sch1100 "*Goble-slurp-goble-guble-slurp!*"
show image "04_dah_iris/d_a05.png" with d3
sch900 "Yes! Like this! So much better!"
sch900 "What about you, sweetheart? Are you enjoying yourself this far?"
menu:
    "\"Yes. But Iris could work harder I think.\"":
        hide image "04_dah_iris/d_a01.png" 
        show image "04_dah_iris/d_a01.png" with d3
        sch1100 "*Slurp?!*"
        hide image "04_dah_iris/d_a04.png" 
        show image "04_dah_iris/d_a04.png" with d3
        sch900 "You heard the man, girl! Down you go!"
        sch1100 "*Slurp-gulp!*"
        sch900 "Yes, yes, all the way to the balls! Don't forget to set your tongue to work too, men love that!"
        g3 "Yes, we do!"
        g3 "You think you could make her swallow my dick whole?"
        g3 "Down to my balls and then just hold it right there?"
        sch900 "Easy..."
        sch1100 "*Gulp?!*"
        sch900 "Down you go, girl!"
        show image "04_dah_iris/d_a06.png" with d3
        sch1100 "*Gltch!*"
        sch1100 "............................."
        sch1100 "..........................................................."
        sch900 "Like that? Do you like it, sweetheart?"
        g3 "Yes, I'm loving it. Just hold her there....."
        sch1100 "!!!!!!!!"
        show image "04_dah_iris/d_a07.png" with d3
        sch1100 "!!!!!!!!!!!!!!!!!!!!!!!!!"
        sch900 "She is starting to struggle..."
        g3 "Just a bit longer. My cock is so deep down her throat... what an amazing feeling...."
        sch1100 "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        show blkfade with d5
        ir[6] "*Khya! *cough-cough*!"
        ir[8] "Dahlia, what are you doing? I couldn't breathe! are you trying to kill me?!"
        dah[3] "Take a deep breath, dear..."
        ir[10] "Huh?"
        dah[10] "And now back to sucking!!"
        hide image "04_dah_iris/d_a04.png" 
        show image "04_dah_iris/d_a04.png" behind blkfade
        hide blkfade with d5
        sch1100 "*Goble-slurp!!!!*"
        g3 "Oh yes..."
    "\"So far so good. Keep going, girls.\"":
        sch900 "Splendid... *lick-lick*"
        sch1100 "*Slurp-slurp-slurp!*"
        sch900 "Let's see how deep I can go with my tongue..."
        sch900 "*Lick-slurp-slurp!*"
        g3 "Yes... very good..."
        sch1100 "*Slurp-Gulp-Slurp-Gobble-slurp!*"
        g3 "Iris, your asshole is simply gaping here..."
        sch1100 "*Slurp-slurp!*"
        g3 "It's like a little cave... The cave of wonders. *chuckle*"
        sch1100 "*Slurp!* Please, stop stretching it like that... It's embarrassing. *Goble-slurp-gulp!*"
        g3 "Look, my finger goes in and out without any hindrance..."
        sch1100 "*slurp-slurp!*"
        g3 "I'm guessing you take it up your ass quite often here?"
        sch900 "*Lick* Oh, yes, she does. Although not nearly as much as she used to..."
        sch900 "*Lick!* When she only started to work here, for some reason, every man had been obsessed over her little asshole..."
        g3 "You don't say..."
        sch900 "*Lick!* Yes... We used to call her \"Anal Iris\" for a while..."
        sch900 "*Lick!* The poor girl used to complain to me that nobody would even bother giving her pussy a proper fuck..."
        sch900 "*Lick!* They would just fuck her up her ass and leave her pussy and mouth completely unmolested..."
        sch900 "*Lick!* Her little butthole could only withstand such ferocious daily assaults for so long..."
        sch900 "*Lick!* Eventually it became loose and, from what I hear from the clients, not nearly as tight anymore..."
        sch900 "*Lick!* So Iris's popularity among customers has dropped somewhat..."
        g3 "I see... That explains things..."
        sch900 "*Lick!* Don't get me wrong though, she is still quite popular..."
        sch900 "*Lick!* And given time I'm sure her body will bounce back and her asshole will be stronger than ever..."
        hide image "04_dah_iris/d_a04.png" 
        show image "04_dah_iris/d_a04.png" with d3
        sch1100 "*SLURP-GULP!* Stop it! Stop talking about this, please... so embarrassing..."
        sch900 "*Lick!* Back to sucking, dear. Back to sucking. Here you go..."
        sch1100 "*Slurp-slurp-slurp!*"
    "\"Shut up and lick my asshole, Dahlia!\"":
        sch900 "You don't need to tell me twice, dear. *Slurp-lick-lick!*"
        g3 "Yes. Good..."
        sch900 "*lick-slurp-slurp-gulp!*"
        sch1100 "*Goble-goble-slorp!*"
        g3 "Iris, your pussy is dripping all over me..."
        sch1100 "*Goble-slurp-goble-guble-slurp!*"
        g3 "Is this because of my dick deep down your throat or because of what I'm doing to your asshole here?"
        sch1100 "*Slurp-gulp*"
        sch1100 "Gulp-Slurp!*"
        sch900 "*Lick!* Answer the good man, dear."
        sch1100 "*Slurp-gulp!* I... I don't know... *Slurp-goble-slurp!*"
        sch900 "*Lick!* Both, I'm guessing..."
        sch900 "Lick!* ah... My tongue is all over your asshole, sweetheart... *lick!*"
        g3 "Yes, yes, keep going..."
        sch900 "*Lick!* Your huge balls are resting on my face... ah... yes... down you go, Iris, down you go! Like this, yes. *lick!*"
        sch900 "*Lick!* *Panting* Oh my, I think I'm really starting getting into this!"
        show image "04_dah_iris/d_a09.png" with d3
        sch900 "*Lick!* Yes, Iris, keep moving your head up and down this magnificent cock!"
        sch1100 "*Slurp-slurp-slurp!*"
        sch900 "*Lickalickalick!!!* Yes! Just put your ass on my chin, your have balls on my face and let me fuck you with my tongue!!!"
        sch900 "*LickLicklicklickLicklicklickLicklicklickLicklicklickLick!!!*"
        g3 "Ah! Oh, wow! yes! Very good!"

hide image "04_dah_iris/d_a08.png"
show image "04_dah_iris/d_a08.png" with d3
g3 "If you girls keep going at it like that, I don't think I will last much longer... agh..."
sch900 "*Lick!* Good! This is what we want, isn't that right, Iris, dear?"
sch1100 "*Slurp-slurp-slurp!*"
g3 "Agh... Yes, you keep sucking on it, you whore..argh..."
sch1100 "*Goble-slurp-gulp!*"
sch900 "*Lick!* Iris, dear, you must be careful now..."
hide image "04_dah_iris/d_a04.png" 
show image "04_dah_iris/d_a04.png" with d3
sch1100 "*Slurp??*"
sch900 "*Lick!* You need to start swallowing before even the first drop of his cum touches your tongue."
sch900 "*Lick!* From the way he is breathing I would say there will be a lot of it..."
sch900 "*Lick!* It will fill up your mouth before you know it!"
sch900 "*Lick!* You need to swallow it all, otherwise it will end up on my face..."
sch900 "*Lick!* Not that I'd mind, but this will be a good opportunity to test your swallowing skills..."
sch1100 "*Slurp-slurp-slurp!*"
hide image "04_dah_iris/d_a07.png" 
show image "04_dah_iris/d_a07.png" with d3
g3 "argh... yes... yes..."
sch900 "*Lick!* Yes, sweetheart, let that little slut have it! Cum right in her mouth!"
hide image "04_dah_iris/d_a08.png" 
show image "04_dah_iris/d_a08.png" with d3
g3 "Yes! Argh! You sluts!"
sch900 "*Lick!* Just make sure you warn us right before you start cumming, alright?"
g3 "Whatever, keep licking my asshole! Yes! Argh, you whores! You good little whores! Like this!"
sch1100 "*Slurp-golp-goble-slorp-slurp-gulp-slurp!*"
sch900 "*Lick-lick-lick-slurp-gulp-lick!*"
sch1100 "*Slurp-slurp-gulp-slurp!*"
g3 "*Panting heavily* ................."
menu:
    "\"Warn them.\"":
        g3 "Argh!... almost... I'm about to..."
        sch900 "*Lick!* Get ready girl!"
        sch1100 "*Gulp-gulp-gulp-gulp-gulp...*"
        g3 "Almost! Argh! You sluts! You little fucking sluts!!!"
        g3 "*GROAN!*"
        g3 "ARRRRGH!!!! YES!"
        sch900 "*LICK!!!!*"
        show white 
        pause.2
        hide white
        pause.3
        show white 
        pause .1
        hide white
        show image "04_dah_iris/d_a10.png" with d3
        with hpunch 
        sch1100 "!!!!!!!!!!!!!!!!"
        sch900 "Swallow, girl, keep swallowing!"
        g3 "Agh! YES! Right down your throat! Agh!"
        sch1100 "*Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!*"
        show image "04_dah_iris/d_a11.png" with d3
        sch900 "Yes, you can do it, girl!"
        sch1100 "*Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gulp!*"
        g3 "Argh! And some more! Swallow this!"
        show white 
        pause.2
        hide white
        pause.3
        show white 
        pause .1
        hide white
        with hpunch 
        sch1100 "*Gulp!* *Gulp!* *Gulp!* *Gulp!* *Gu--"
        sch1100 "*Goble!* *Cough!* Gulp!"
        g3 "Ah.... yes..."
        g3 "...............ah....."
        show image "04_dah_iris/d_a12.png" with d3
        sch900 "Well, look at you, dear! You got all of it! Good job!"
        show ctc7 at right
        pause
        hide ctc7
        show blkfade with d5
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        ir[7] "Ah...{image=textheart.png} ah...{image=textheart.png} Oh, my... I feel so full..."
        dah[1] "He cums a lot, doesn't he..."
        ir[6] "Yes, he does... always... ah...{image=textheart.png}"
        ir[6] "My belly is full of cum... It feels so warm inside..."
        dah[2] "Hehe... A feeling quite different from when the clients pump you full of cum through your asshole, is it not...?"
        ir[1] "Sort of the same and sort of different... hard to explain..."
        dah[2] "That's OK, dear, you rest now... You've earned it..."
        dah[3] "What about you sweetheart. You feel satisfied?"
        m "I do... But I wouldn't say that \"all my troubles have faded away\" as your advertisement promised..."
        dah[2] "Well, tell me then, did you think about your \"troubles\" when you were pumping this little bird here full of your semen?"
        m "Em... no, I guess not."
        dah[1] "Then I would say you did get your money's worth..."
        m "Fair enough..."
        m "I will be leaving now. Thank you for the great time."
        dah[2] "Make sure you come visit us often..."
        dah[3] "Dear, say goodbye to the client..."
        $ renpy.play('sounds/burp.mp3')
        with hpunch
        ir[6] "*Burp!*"
        ir[7] "*giggle* Oh, I'm sorry..."
        ir[1] "Thank you for everything, old man. I will say hi to my father from you." 
        show blkfade with Dissolve(2)
        ">Some time later you leave the brothel."
        hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
        if brothelnight:
            ">You return home and go to sleep."
            show image "interface/blackfade.png" with Dissolve(.3)
            pause 1
            jump dayone
        else:            
            ">It's getting late. You decide to head home."
            jump dayends

    "\"Just start cumming.\"":
        g3 "ARGH!!!!!!!!!!!!!"
        show white 
        pause.2
        hide white
        pause.3
        show white 
        pause .1
        hide white
        show image "04_dah_iris/d_a13.png" with d3
        with hpunch 
        sch1100 "?!?!?!??!!"
        sch1100 "?!?!?!?!"
        show white 
        pause.2
        hide white
        pause.3
        show white 
        pause .1
        hide white
        show image "04_dah_iris/d_a14.png" with d3
        with hpunch
        sch900 "What are you doing, girl?! Start swallowing!"
        g3 "Argh! Some more for you!"
        show white 
        pause.2
        hide white
        pause.3
        show white 
        pause .1
        hide white
        show image "04_dah_iris/d_a15.png" with d3
        with hpunch
        sch1100 "*gulp!*... *Gulp!* *Gulp!*"
        sch900 "Faster! You aren't swallowing quickly enough!"
        g3 "Argh! Yes! More for you, whores!"
        sch1100 "*Gulp!*.... *Gulp!*..."
        sch900 "Iris, you silly, girl, it's getting into my--"
        sch900 "It's--- *khem* hard to breathe..."
        sch900 "*Gulp!* I'll try to swallow some of it, but it's so awkward to--"
        sch900 "*Gulp!* Try and gulp anything down in this position!"
        g3 "ARGH! YES!!!"
        show white 
        pause.2
        hide white
        pause.3
        show white 
        pause .1
        hide white
        show image "04_dah_iris/d_a16.png" with d3
        with hpunch
        sch1100 "*Gulp...*"
        sch900 "Iris-- *Gulp!* Please--"
        sch900 "I can't get out from under him *Gulp!*--"
        with hpunch
        show image "04_dah_iris/d_a17.png" with d3
        sch900 "Please keep swallowing... *Gulp!* I don't want to drown in sperm..."
        sch900 "*Gulp!*..."
        show ctc7 at right
        pause 
        hide ctc7
        show blkfade with d5
        show ctc7 at right
        pause 
        hide ctc7


        ir[10] "Dahie, I'm so sorry, are you alright?"
        ir[10] "I tried to do my best, but it was so thick and there was so much of it..."
        dah[12] "Yes, he cums a lot, doesn't he?"
        ir[10] "I'm sorry..."
        ir[8] "You should've warned me, old man..."
        dah[13] "Now, dear, don't take this out on the customer. It is not his fault..."
        dah[12] "Although, I have to admit, for the first time in my long career as a whore, I got a bit scared that I might actually drown in sperm..."
        dah[13] "But all is well that ends well...."
        dah[12] "What about you sweetheart. You feel satisfied?"
        m "I do... But I wouldn't say that \"all my troubles have faded away\" as your advertisement promised..."
        dah[13] "Well, tell me then, did you think about your \"troubles\" when you were pumping this little bird here full of your semen?"
        m "Em... no, I guess not."
        dah[12] "Then I would say you did get your money's worth..."
        m "Fair enough..."
        m "I will be leaving now. Thank you for the great time."
        dah[12] "Make sure you come visit us often..."
        dah[13] "Dear, say goodbye to the client..."
        ir[1] "Good bye, old man. Thank you for choosing me..."
        ir[1] "Thank you for everything, really. I will say hi to my father from you." 
        show blkfade with Dissolve(2)
        "Some time later you leave the brothel."
        hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
        if brothelnight:
            "You return home and go to sleep."
            show image "interface/blackfade.png" with Dissolve(.3)
            pause 1
            jump dayone
        else:            
            "It's getting late. You decide to head home."
            jump dayends 