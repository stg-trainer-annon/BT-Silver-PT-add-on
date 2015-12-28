label dah_jas_sex:
play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
show blkfade with d3
pause.7
show dahlia 3 at right behind blkfade
hide blkfade with d3
sch900 "Hello, there, sweetheart."
sch900 "Did you say it was me and Jasmine you wanted to keep you company this time?"
menu:
    "\"Yes. You and Jasmine.\"":
        sch900 "I see..."
        hide dahlia with d3
        show dahlia 1 at right with d3
        sch900 "Jasmine, come here, dear. You've been chosen..."
        show jas 24 at left with d3
        j "Hello. My name is Jasmine. How can I--"
        hide jas with d3
        show jas 23 at left with d3
        j "Oh..."
        hide dahlia
        show dahlia 2 at right with d3
        sch900 "What is it, dear?"
        hide jas with d3
        show jas 24 at left with d3
        j "N-nothing... everything is fine..."
        hide dahlia
        show dahlia 4 at right with d3
        sch900 "Well, alright then..."
        sch900 "Do you have the gold to support your cravings, my love?"
        sch900 "I assure you, me and Jasmine here can give you something to boast to your friends about, but only if you have the gold on you..."
        menu:
            "You currently have [gold] gold. \n Would you like to give 250 gold to Dahlia?"
            "\"Alright. Here is your money.\"":
                if gold >= 250:
                    $ gold -=250
                    ">You give Dahlia 250 gold coins."
                    sch900 "Thank you, dear."
                    hide dahlia with d3
                    show dahlia 4 at right with d3
                    sch900 "Alright then, shall we go upstairs?"
                    hide dahlia with d3
                    hide jas with d3
                    show jas 22 at left with d3
                    j "(Pst... Old man, what are you doing here?)"
                    show emo8 at Position(xpos=700, ypos=100, xanchor=0, yanchor=0) 
                    sch900 "Come on, now, Jasmine, let's go..."
                    show blkfade with d3
                    pause.7
                    hide dahlia
                    hide iris
                    jump dah_jas_action
                else:
                    sch900 "Doesn't look like you can afford this, honey. Well, we don't work for free..."
                    show iris_f 89 at left with d3
                    j ".............."
                    show blkfade with d3
                    pause.7
                    hide dahlia
                    hide emo8
                    hide jas
            
                    hide blkfade with d3
                    jump brothelmain
            "\"Sorry forgot my money pouch.\"":
                sch900 "Well, we don't work for free, honey..."
                j "..............."
                show blkfade with d3
                pause.7
                hide dahlia
                hide jas
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
        
#################################################################################


label dah_jas_action:
show ctc7 at right
pause
hide ctc7
jas[43] "(Old man, what is the meaning of this? What are you doing here?)"
m "(What do you mean?)"
jas[43] "(I mean, you know perfectly well that you can... em...)"
jas[44] "(I mean, you don't have to come here if you want to... er..)"
jas[45] "(...you know....)"
jas[46] "(Plus, I don't approve of you wasting our money on whores!)"
m "(Well, since you are one of those whores, your highness, part of that gold will end up back in my pocket anyways.)"
jas[47] "(That's not the point, old man--"
dah[2] "Well-well, now. What are you whispering for there, you lovebirds? Come on in already."
dah[3] "And make sure to lock the door, your maje--"
dah[6] "khem, I mean, Jasmine."
jas[45] "That's OK, Dahlia. He knows who I really am..."
dah[2] "Is that so?"
dah[3] "Well, I guess many people do these days..."
dah[2] "Hm... Since we don't have to pretend anymore, I have an idea..."
jas[43] "Hm?"
dah[1] "Your majesty, if you please... There is something I wanted to do for quite some time now..."
jas[48] "Yes, go on..."
dah[4] "Em... Oh wow, it's so unlike me to be lost for words..."
dah[6] "I think I still respect you too much..."
dah[7] "But that's what would make what we're about to do this much exciting..."
jas[47] "What is it? Spill it out already, woman!"
dah[1] "Em... How about I show you instead?"
dah[2] "Let me help you out of your pants first..."
jas[45] "Oh..."
dah[5] "Now, if you would..."
jas[45] "Huh?"
jas[48] "What?"
jas[49] "Dahlia?!"
jas[45] "Oh, I see now..."
dah[7] "Do you mind, your majesty?"
jas[50] "Not at all! Stick your tongue in it... oh, yes.. yes..."
sch900 "*Slurp-slurp-slurp*"
jas[50] "Yes...{image=textheart.png}"
menu:
    g4 "(Did they forget I'm here too?)"
    "\"Girls? Aren't you forgetting something?\"":
        m "Girls? Aren't you forgetting something? Or rather some{size=+5}ONE{/size}?"
        dah[8] "!!!!!!!!!!!!!!!"
        dah[3] "I can't believe this! How unprofessional! I'm so sorry, sweetheart!"
        dah[6] "I got so carried away, I forgot about everything and everyone else... This is so unlike me..."
    "\"How dare you ignore me, whores?!\"":
        g4 "How dare you ignore me, whores?!"
        sch900 "*Slurp* ???!!!!!!!!!!!!!!!!!!!!!"
        jas[50] "Ah...{image=textheart.png}"
        dah[8] "I'm so terribly sorry, sweetheart! This is so not in my character..."
        dah[3] "Your majesty, the client must be our first priority at all times, I hope you understand..."
        jas[44] "Yes, yes, this is not my first day on this job..."
    "\".....................................................\"":
        sch900 "*Slurp-slurp-slurp* Do you like it when I move my tongue like this, your majesty?"
        jas[45] "Ah...{image=textheart.png} y-yes...{image=textheart.png}"
        sch900 "*Slurp-slurp-slurp* How about this, your majesty?"
        jas[51] "Ah...{image=textheart.png} yes, this is good too."
        jas[51] "You don't heave to address me as \"Your majesty\" all the time, though, Dahlia..."
        dah[6] "I'm sorry, I can't help it..."
        dah[6] "Even before your fall from graces of majesty, I used to dream about going down on you..."
        dah[7] "Princess Jasmine... The jewel of agrabah... and now she is here... All mine *Slurp-surp-slurp!*"
        jas[44] "............................................"
        jas[44] "..........................................................................."
        jas[47] "{size=-5}(I am still very much the Jewel of Agrabah...){/size}"
        jas[51] "ah...{image=textheart.png} yes...{image=textheart.png}"
        sch900 "*Slurp-slurp-slurp!*"
        with hpunch
        dah[8] "{size=+7}By the great desert sands!!!{/size}"
        jas[49] "What? What happened?!"
        dah[6] "I'm so sorry sweetheart! We completely forgot about you!"
        m "......................"
        jas[48] "Oh, that............."
        dah[6] "So unlike me, so unprofessional!"


dah[3] "Let me help you out of your cloak, sweetheart..."
m "No need... You keep doing your thing, Dahlia."
dah[1] "Really?"
m "Yes, yes, I will just sit right here and..."
jas[46] "Huh? What are you--"
j "*Gobble!*"
g9 "He-he... You were saying, your majesty?!"
j "*Gulp-slurp!*"
m "Yeah, thought so..."
show image "05_dah_jas/dj01.png" behind blkfade
show ctc7 at right
play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
pause
hide ctc7
hide blkfade with d5
show ctc7 at right
pause
hide ctc7
j "*gulp!* *gubble!* *slorp!*"
g3 "Oh, yes... very good..."
sch900 "*Lick!* *SlurP!* *Lick!*"
j "*Gubble!* *Gulp!* *Slurp!*"
g3 "Yes, yes, work your tongue, whore..."
sch900 "Yes... To hear you disrespect her like that... it's so... arousing..."
show image "05_dah_jas/dj02.png" with d3
j "*Slurp?!*"
sch900 "*Lick!* I still mean no disrespect to *Lick!* you, of course, your majesty! *Lick!*"
show image "05_dah_jas/dj03.png" with d3
j "*Slurp!* *Slurp!* *Gulp!*"
g3 "Princess Jasmine... the famous whore of Agrabah..."
show image "05_dah_jas/dj06.png" with d3
j "*SLURP?!*"
g3 "What? Stop moaning and get back to sucking!"
sch900 "*Lick!* Yes! *Lick!* You tell her, sweetheart! *Lick!*"
sch900 "*Lick!* Yes! Let's double-team this bitch! *Lick!*"
hide image "05_dah_jas/dj05.png" 
show image "05_dah_jas/dj05.png" with d3
j "*Slurp-Slurp??*"
sch900 "*Lick!* No offense, your majesty...*Lick!*"
hide image "05_dah_jas/dj04.png" 
show image "05_dah_jas/dj04.png" with d3
g3 "Heh... where is this aggression coming from, Dahlia?"
sch900 "*Lick!* I'm not sure...*Lick!*"
g3 "I like it, though. Way to go..."
sch900 "*Lick!* Well in that case, make sure you drill her mouth good. She deserves that, that royal bitch! *Lick!*"
hide image "05_dah_jas/dj05.png" 
show image "05_dah_jas/dj05.png" with d3
j "*Slurp?!*"
sch900 "I'm sorry, your majesty, but that's what the client wants. You know the rules..."
hide image "05_dah_jas/dj02.png" 
show image "05_dah_jas/dj02.png" with d3
j "*Slurp!* *Slurp!* *Slurp!*"
sch900 "*Lick!*{w} Yes... Fuck her mouth... impale her face on your hard cock!{w} *Lick!*"
sch900 "*Lick!*{w} Nasty whore..."
sch900 "*Lick!*{w} Did you know that as soon as she started to work here...{w} *Lick-slurp!*"
sch900 "*Lick!*{w} She got so popular among the clients that the rest of us girls barely had any work left to do..."
sch900 "*Lick!*{w} Every man wanted her... And she was always so willing to serve them... all at once if needed be..."
sch900 "*Lick!*{w} So depraved and twisted this one is... {w}*Lick-slurp!*"
sch900 "*Lick!*{w} And when I found out who she really was, it just made me sick to my stomach..."
sch900 "*Lick!*{w} What kind of princess would stoop so low?{w} *Lick!*"
g3 "You don't say. Shame on you Jasmine."
hide image "05_dah_jas/dj01.png" 
show image "05_dah_jas/dj01.png" with d3
j "*Slurp???*"
g3 "Oh, no, no, you keep sucking..."
sch900 "*Lick!*{w} I always respected her so much, and I still do... somewhat..."
sch900 "And yet, this kind of behavior is so.... {w}unbecoming of a princess..."
hide image "05_dah_jas/dj07.png" 
show image "05_dah_jas/dj07.png" with d3
j "*Slurp!* *Slurp!* *Slurp!*"
g3 "This is nice, Dahlia..."
g3 "All this talk about her being a princess and yet a twisted whore is sure working for me!"
g3 "Keep going... Keep telling me stuff like that..."
j "*Slurp!*"
g3 "No, no, not you, Jasmine. You keep sucking. Yes, like this, all the way down to my balls..."
j "*Slurp!* *Slurp!* *Gubble!*"
g3 "Now, that's a good princess..."
sch900 "*Lick!*{w} *Lick!*{w} *Lick!*{w} Nasty slut with no shame..."
sch900 "*Lick!*{w} Is this how you serve your country now, you filthy whore?"
hide image "05_dah_jas/dj08.png" 
show image "05_dah_jas/dj08.png" with d3
j "*Slurp!*{w} *Gulp!*{w} *Slurp!*{w} *Sob...*{w} *Slurp!*"
sch900 "*Lick!*{w}........ *Spit!* You disgust me!"
sch900  "*Spit!*.... {w}*Lick!* *Lick!* *Lick!*"
g3 "Oh, yes... yes, this is good..."
sch900 "*Lick!*{w} From being an ideal princess to being an ideal whore...{w} \nWhat a trip..."
j "*Slurp!* *Slurp!* *Slurp!*"
sch900 "*Lick!*{w} Peasants, they used to look up to you... only but fantasize about you..."
sch900 "*Lick!*{w} And now they don't have to anymore, do they?"
sch900 "*Lick!*{w} All that is needed is a few shiny gold coins..."
sch900 "*Lick!*{w} Even the lowest of the low city beggars could come here, and stick it up your royal butt-hole..."
j "*Slurp!*{w} *Slurp!*{w} *Slurp!*"
sch900 "*Lick!*{w} That's right! Isn't that what happened awhile back?"
sch900 "*Lick!*{w} That crazy Crocus, the cripple from the Cheapside came here {w}*Lick!*{w} with enough gold to buy himself a night with her..."
g3 "What.....?"
sch900 "*Lick!*{w} Yes. He chose her, but our spoiled Princess refused him harshly... at first" 
g3 "Oh..."
sch900 "*Lick!*{w} Wait, that's not all..."
sch900 "Then, Fat Lily had a quiet chat with her..."
sch900 "And our Jasmine agreed to pleasure that dirty beggar with her hands..."
sch900 "*Lick!*{w} He had plenty of gold on him, so I would do the same..."
sch900 "*Lick!*{w} But what I would never do is put his disgusting prick in my mouth... and that's exactly what our here princess did."
g3 "What? Are you serious?"
j "*Slurp*{w} *Slurp*{w} *Slurp*"
sch900 "*Lick!* Yes, and she didn't have to, see..."
sch900 "'Cause I hear, that as soon as she touched him, the poor wretch started to cum, so she just leaned forward and took his dick in her mouth..."
g3 "Eww... Crocus? No way!..."
sch900 "*Lick!* Yes, and she swallowed all of it too... What a nasty, nasty whore our princess is, I might ask you. *Lick!*"
hide image "05_dah_jas/dj09.png" 
show image "05_dah_jas/dj09.png" with d3
j "*Slurp!*...............................................{w} *Sob...*"
j "*sob* ................................................................................"
sch900 "Huh? Your majesty?"
g3 "What's going on...?"
sch900 "I'm not sure... *Lick!* I think she is... about to--"
show white 
pause.2
hide white
pause.3
show white 
pause .1
hide white
hide image "05_dah_jas/dj10.png" 
show image "05_dah_jas/dj10.png" with d3
with hpunch 
j "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
sch900 "She is cumming!?"
sch900 "What a nasty slut! *Gulp!*{w} *Gulp!*{w} *Gulp!*{w} *Gulp!*{w} *Gulp!*"
g3 "Oh, yes! You fucking whore! Yes! Keep cumming with my dick in your mouth, you slut!"
g3 "Yes!..."
show white 
pause.2
hide white
pause.3
show white 
pause .1
hide white
hide image "05_dah_jas/dj11.png" 
show image "05_dah_jas/dj11.png" with d3
with hpunch 
g3 "{size=+7}ARGH!!!!!!!!!!!!!!!!!!!!{/size}"
show white 
pause.2
hide white
pause.3
show white 
pause .1
hide white
hide image "05_dah_jas/dj12.png" 
show image "05_dah_jas/dj12.png" with d3
with hpunch 
j "{size=+7}!!!!!!!!!!!!!!!!!!!!!!!!!{/size}"
g3 "{size=+7}Fucking whore! Take it all!{/size}"
show white 
pause.2
hide white
pause.3
show white 
pause .1
hide white
hide image "05_dah_jas/dj13.png" 
show image "05_dah_jas/dj13.png" with d3
with hpunch 
j "*Gulp!*{w} *Gulp!*{w} *Gulp!*{w} *Gulp!*{w} *Gulp!*{w} *Gulp!*{w} *Gulp!*"
sch900 "*Gulp!*{w} *Gulp!*{w} *Gulp!*{w} *Gulp!*{w} *Gulp!*{w} *Gulp!*"
hide image "05_dah_jas/dj14.png" 
show image "05_dah_jas/dj14.png" with flashbulb
j "*Gulp!*{w} *Gulp!*{w} *Gulp!*"
sch900 "*slurp!*...."
j "........"
show ctc7 at right
pause
hide ctc7
show blkfade with Dissolve(3)
show ctc7 at right
pause
play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
hide ctc7


dah[7] "Your majesty, are you alright?"
dah[7] "All those things I said about you, I hope you understand that I only said them because that's what the client wanted..."
jas[52] "I don't care..."
dah[6] "No hard feelings then?"
dah[5] "You know how much I respect you, your majesty."
jas[53] "Enough, Dahlia. Enough of this..."
jas[54] "I used to be a princess, but things have changed and now I'm a whore."
jas[53] "I'm old enough and strong enough to accept the reality as it is, you don't need to sugarcoat it for me..."
dah[6] "Your majesty, I was merely..."
jas[55] "Enough from you!"
jas[55] "I sucked his dick, you ate my pussy, I came on your face and he came on mine. That's what happened, we are all adults here."
dah[4] "........"
jas[53] "Are you satisfied with our performance, old man?"
menu:
    m "Em..."
    "\"Yes. Absolutely.\"":
        m "Yes... Absolutely."
        m "You performed only too well as cum receptacles." 
        jas[55] "Tsk...."
        jas[54] "All I heard was: \"Yes.\""
    "\"Not really.\"":
        m "Not really, no..."
        jas[55] "Tsk..."
        jas[54] "Well, too bad. Feel free to file a complaint with Fat Lily."
    "\"Why so bossy?\"":
        m "Why so bossy all of a sudden?"
        jas[54] "Not bossy... Just being professional about this, is all."


jas[54] " Now if you excuse me, I was hoping to serve a few more customers before my shift is over..."
dah[3] ".......................majesty?"
m "Hm.........."

show ctc7 at right
pause
hide ctc7
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