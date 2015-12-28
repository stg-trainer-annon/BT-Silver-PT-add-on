###JASMINE
label jasminewhore:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with d3
    pause.7
    show jas_f 24 at right behind blkfade
    hide blkfade with d3
    j "Hello, welcome to the \"Red Phoenix\"."
    j "My name is Jasmine and--"
    show jas_f 22 at right with d3
    j "Old man??"
    j "What is it? Did something happen back at home?"
    menu:
        "\"Treat me like you would any other client.\"":
            m "Just treat me like you would any other client."
            j "Treat you like I would..."
            hide jas with d5
            show jas 23 at center with d3
            j "You can't be serious..."
            show emo8 at Position(xpos=700, ypos=100, xanchor=0, yanchor=0)
            sch900 "Jasmine, is everything alright there, dear?"
            hide emo8 with d3
            j "Y-yes, everything is fine. Just talking to a client..."
            hide jas  with d3
            show jas 21 at center with d3
            j "Alright..."
            j "Treat you just like any other client I shall."
            j "My services will cost you 100 gold coins."
            menu:
                "You currently have [gold] gold. \nWould you like to give 100 gold to Jasmine?"
                "\"Yes.\"":
                    if gold >= 100:
                        $ gold -=100
                        ">You give jasmine 100 gold coins."
                        j "Alright. Follow me then..."
                        show blkfade with d3
                        hide jas
                        pause.7
                        jump jas_action
                    else:
                        hide jas with d3
                        show jas 22 at center with d3
                        j "You don't have enough money? You gotta be kidding! What happened to all the gold I have earned for you for the past weeks?"
                        hide jas with d3
                        show jas 21 at center with d3
                        j "Tsk... tipical..."
                        show blkfade with d3
                        hide jas
                        pause.7
                        hide blkfade with d3
                        jump brothelmain
                "\"I changed my mind.\"":
                    hide jas with d3
                    show jas 21 at center with d3
                    j "Whatever..."
                    show blkfade with d3
                    hide jas
                    pause.7
                    hide blkfade with d3
                    if brothelnight:
                        play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
                    else: 
                        play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                    jump brothelmain
        "\"Sorry. I'm here to see someone else.\"":
            show jas_f 21 at right with d3
            j "I see..."
            show blkfade with d3
            hide jas
            pause.7
            hide blkfade with d3
            if brothelnight:
                play music "music/Ozone.ogg" fadein 1 fadeout 1   # NIGHT_2
            else: 
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
            jump brothelmain
            
####################################################################
label jas_action:
jas[46] "I can't believe you're doing this to me..."
jas[47] "Twisted old man... Are you purposefully trying to humiliate me?"
jas[44] "No, don't answer that..."
m "..........................................."
jas[46] "So, what do you expect me to do now?"
label _back:
menu:
    "\"Now introduce yourself to me...\"":
        m "Now introduce yourself to me..."
        jas[46] "What?"
        m "Introduce yourself..."
        jas[45] "Em... alright... My name is jasmine..."
        m "And?"
        jas[44] "And I am... a whore...?"
        m "Yes you are. And what were you before?"
        jas[46] "Tsk..."
        m "What were you before you changed careeers, girl?"
        jas[44] "{size=-5}A princess...{/size}"
        m "I don't hear you..."
        jas[51] "A princess! I used to be a princess!"
        m "And what are you now?"
        jas[46] "..........."
        m "What are you?"
        jas[49] "A whore....."
        m "Good... Do you let people fuck you for money then?"
        jas[46] ".... y-yes..."
        m "Do you let them use your asshole as well?"
        jas[44] "*sob* s-sometimes..."
        m "Do you let them cum on your face?"
        jas[56] "*Sob!* {size=-5}Yes...{/size}"
        g4 "What? I don't hear you, girl!"
        jas[57] "Yes! I let them cum on my face! I'm a nasty disgraceful whore! *Sob!*"
        m "Good, now it's time to fuck you."
        m "Spread you legs a little and give me your arms..."
        jas[56] "What?"
        m "Yes, like this..."
        jas[56] "What are you--"
        jas[44] "............."
    "\"Undress and go on all fours.\"":
        m "Undress and go on all fours."
        jas[47] "(Tsk... how original...)"
        jas[49] "Huh? Wait a second! What are you--"
        jas[51] "AAAAAHh!"
    "{size=-3}\"Put a banana in your mouth. Pretend to be monkey.\"{/size}":
        g9 "How about you put a banana in your mouth and pretend to be a monkey?"
        jas[49] "What?"
        jas[47] "What is the matter with you?"
        m "Just kidding..."
        jas[49] "This not even remotely funny..."
        g9 "Your reaction is..."
        jas[47] "Tsk..."
        jump _back
    "\"Support AKABUR!\"":
        m "If you enjoy this game and feel like supporting the author, follow {a=http://akabur.hentaiunited.com}this link.{/a} Click the \"Join Now\" button under his profile and join the site."
        m "Or you could always just send him a buck or two via Yandex_MONEY: 41001849167270."
        m "Or WebMoney: R133931000745."
        m "Or through PayPal."
        m "Akabur's PayPal address is {size=+7}not{/size} akaburfake2@yahoo.com. That's just his email."
        jas[46] "What on earth are you talking about?"
        g4 "Er... I'm not sure..."
        m "Hm... You ever feel like your entire life could be just an illusion?"
        jas[46] "What?"
        m "A product of some guy's imagination... Like if this entire world was actually running on a \"ren'py\" game engine?"
        jas[48] "What's a... \"renpai\"?"
        m "Well, I'm not sure myself, but I think it could be the very essence of this universe..."
        jas[49] "What? Are you drunk? Did you bring me here to waste my time, old fool?"
        m "Right... Got sidetracked a little, sorry..."
        jump _back

show image "06_jas/j01.png" behind blkfade
show ctc7 at right
play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
pause
hide ctc7
hide blkfade with d5
show ctc7 at right
pause
hide ctc7
g3 "What? You liking this?"
j "ah...{image=textheart.png} n-no..."
g3 "Be honest with me, girl."
g3 "You're enjoying this aren't you?"
show image "06_jas/j02.png" with d5
j "Maybe... A little bit... ah...{image=textheart.png}"
g3 "Tell me more..."
g3 "Tell me how much you enjoy getting fucked!"
show image "06_jas/j03.png" with d5
j "What? No! I'm just doing my job!"
g3 "Well, you are pretty good at it, I must say..."
g3 "Very... believable..."
show image "06_jas/j04.png" with d5
j "Of course... I'm a princess. There is nothing I couldn't do... you old fool."
label _back2:
show image im.Alpha("interface/blackfade.png", 0.5)
menu:
    m "Is that so?"

    "{size=-2}\"Say I'm princess whore! with every thrust.\"{/size}":
        hide image im.Alpha("interface/blackfade.png", 0.5)
        g3 "Can you say \"I'm a princess-whore!\" every time I impale you on my cock?"
        hide image "06_jas/j03.png"
        show image "06_jas/j03.png" with d5
        j "Tsk..."
        g3 "Oh, what a pity... I thought \"there was nothing you couldn't do...\""
        with hpunch
        "*Gltch!* *Whump!* *Slap!*"
        hide image "06_jas/j04.png"
        show image "06_jas/j04.png" with d5
        j ".................."
        with hpunch
        pause.3
        with hpunch
        "*Shlump!!* *Whump!*"
        hide image "06_jas/j05.png"
        show image "06_jas/j05.png" with d5
        j".................................."
        with hpunch
        "*Bloich!*"
        j "I'm a princess whore!..."
        g3 "You don't say..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        "*Whompt!* *Bloich!*"
        j "I'm a princess whore!... I'm a princess whore!..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        "*Whompt!* *Bloich!* *Ploich!*"
        hide image "06_jas/j06.png"
        show image "06_jas/j06.png" with d5
        j "I'm a princess whore!...I'm a princess whore!...I'm a princess whore!..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        "*Whompt!* *Bloich!* *Ploich!* *Gltch!* *Bloich!* *Ploich!*"
        hide image "06_jas/j07.png"
        show image "06_jas/j07.png" with d5
        j "I'm a princess whore!...I'm a princess whore!...I'm a princess whore!...I'm a princess whore!...I'm a princess whore!..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        "*Bloich!* *Bloich!* *Ploich!* *Gltch!* *Bloich!* *Ploich!*"
        hide image "06_jas/j08.png"
        show image "06_jas/j08.png" with d5
        j "I'm a princess whore!...I'm a princess whore!...I'm a princess whore!...I'm a princess whore!...I'm a princess whore!..."
        g3 "Ha-ha-ha. Alright, alright, you proved your point!"
        hide image "06_jas/j05.png"
        show image "06_jas/j05.png" with d5
        j "Tsk..."
        j "Whatever..."
    "\"Would you fuck an animal?\"":
        hide image im.Alpha("interface/blackfade.png", 0.5)
        g3 "Would you fuck an animal as well?"
        j "What? I would never fuck a tiger! Don't be silly!"
        g3 "Who said anything about fucking tigers?"
        j ".........................."
        jump _back2
    "\"Be quiet and do not moan.\"":
        hide image im.Alpha("interface/blackfade.png", 0.5)
        g3 "Alright then. How about I keep pounding you from behind like this, but you remain quiet?"
        j "What?"
        g3 "Yes! Not a moan not a sigh from you. Can you do that?"
        hide image "06_jas/j05.png"
        show image "06_jas/j05.png" with d5
        j "Tsk... You and your twisted games..."
        g3 "What is it? I thought \"there is nothing you couldn't do...\""
        hide image "06_jas/j06.png"
        show image "06_jas/j06.png" with d5
        j "Fine, whatever, I'll do it, let's get on with this already."
        g3 "As you wish."
        hide image "06_jas/j07.png"
        show image "06_jas/j07.png" with d5
        j "Ah...{image=textheart.png}"
        g3 "Is this you being quiet?"
        hide image "06_jas/j06.png"
        show image "06_jas/j06.png" with d5
        j "S-sorry..."
        hide image "06_jas/j05.png"
        show image "06_jas/j05.png" with d5
        j "{size=-5}(This will be tougher then I thought... But I can't let him win this argument! I'll show him what a true princess is capable of!){/size}"
        g3 "Did you say something?"
        j "......................"
        g3 "Alright! This is better!"
        g3 "Let me pick up the pace then!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        g3 "Just like this! Just like this! In and out, you little whore, in and out!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        j "......................................."
        g3 "Most impressive..."
        g3 "But what if I put some force into it?!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        g3 "Like this! Like this! Oohhh! Feels soooo good!"
        j ".........................."
        g3 "I gotta admit, you're being totally quiet so far..."
        g3 "What if I speed up even more?!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        g3 "ah! Yes! Yes! Just like this! Just like this!"
        j "................................"
        g3 "Nothing? Seriously?"
        g3 "You are able to remain completely quiet during rape..."
        g3 "Useful skill for a princess... I suppose?"
        j "..............................................."
        g3 "Alright, alright, you took everything I threw at you so far quite stoically, I'll give you that..."
        j "........................."
        g3 "Alright then, if you will be able to sustain this final onslaught, I will admit that I was wrong and that there is nothing a true princess could't do..."
        g3 "Are you ready? Here we go!!!"
        hide image "06_jas/j15.png"
        show image "06_jas/j15.png" with d5
        with hpunch
        with hpunch
        pause.2
        with hpunch
        pause.1
        with hpunch
        pause.3
        with hpunch
        pause.1
        with hpunch
        pause.2
        with hpunch
        pause.1
        with hpunch
        pause.1
        with hpunch
        pause.1
        j ".................................."
        g3 "Argh, you fucking whore! Ramming you pussy! Ramming your fucking pussy!"
        j "..................."
        g3 "And some more! And some more! Yes you slut! Yes! Oh, you're so wet!"
        with hpunch
        pause.1
        with hpunch
        pause.2
        with hpunch
        pause.1
        with hpunch
        pause.1
        with hpunch
        pause.1
        j ".......................*pt*..."
        g3 "What? Did you say something, whore?"
        j "AAAAAAAAAAAAAAAAAAAAAAAAH!!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide image "06_jas/j16.png"
        show image "06_jas/j16.png" with d5
        j "YEEES! YES!!!{image=textheart.png} FUCK ME, you old fool! Fuck me like this! Fuck me good!"
        g3 "Ha-ha-ha! You lost, you whore!"
        j "I don't care, you idiot! Just keep fucking me! Oh, it's so hard, you cock, I love it! Yes!{image=textheart.png}"
        jump quaet_orgasm
hide image "06_jas/j02.png"
show image "06_jas/j02.png" with d5
j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
g3 "Yes, just like that! You loving this, aren't you!?"
j "ah...ah... ah..."
g3 "Answer me, woman!"
hide image "06_jas/j09.png"
show image "06_jas/j09.png" with d5
j "ah... n-no... I don't..."
g3 "Oh, but I think you are..."
g3 "What if I pick up the pace a little?"
hide image "06_jas/j02.png"
show image "06_jas/j02.png" with d5
j "Ah... ah... ah.. yes..."
j "Ah... yes... harder!"
g3 "You know, I think I'm getting closer.."
j "Yes! Yes! I'm almost there... almost there..."
g3 "Heh! That was a joke! I'm only warming up, woman!"
label quaet_orgasm:
hide image "06_jas/j10.png"
show image "06_jas/j10.png" with d5                                                   
j "Ah!{image=textheart.png} Ah!{image=textheart.png} No... I..."
j "I'm about to cum, I'm serious!"
g3 "What? We're just started!"
j "I know, I'm sorry... I've been so sensitive lately..."
hide image "06_jas/j11.png"
show image "06_jas/j11.png" with d5       
j "I'll try to hold it!"
g3 "You're damn right you'll try to hold it! You're not cumming until I tell you to cum!"
j "......................................."
g3 "Do you hear me, whore?"
hide image "06_jas/j12.png"
show image "06_jas/j12.png" with d5
with hpunch
pause.3
with hpunch
pause.3
j "No! No, no, don't say things like that! Ah...{image=textheart.png} it will only make me cum sooner!"
g3 "Huh...?"
hide image "06_jas/j11.png"
show image "06_jas/j11.png" with d5 
with hpunch
pause.3
with hpunch
pause.3
j "Oh, by the great desert sands, I'm... I'm almost there.. I... can't..."
g3 "Don't you dare, woman! Don't you--"
with hpunch
pause.3
with hpunch
pause.3
hide image "06_jas/j13.png"
show image "06_jas/j13.png" with d5 
j "Quick, say something nice to me!!"
g3 "What?" 
j "Please! Say something sweet, treat me with respect! I'm on the verge I'm about to..."
with hpunch
pause.3
with hpunch
pause.3
g3 "Alright, alright... You're beautiful...?"
j ".........................."
with hpunch
pause.3
with hpunch
pause.3
g3 "Khem... er... crap! Nothing comes to mind..."
g3 "You're pretty and elegant? And.... well educated... and... I admire your strength...?"
with hpunch
pause.3
with hpunch
pause.3
j "...................."
g3 "And I'm secretly in love with you! You are everything to me. My dear princess...?"
hide image "06_jas/j10.png"
show image "06_jas/j10.png" with d5 
j "Yes, that did it..."
g3 "Feeling better?"
with hpunch
pause.3
with hpunch
pause.3
j "What? Oh, yes, yes. I think I will be able to hold it a little longer now..."
j "Are you getting closer?"
with hpunch
pause.3
with hpunch
pause.3
g3 "I was, until you forced me to start talking about the mushy stuff..."
hide image "06_jas/j14.png"
show image "06_jas/j14.png" with d5 
j "Yes, I know, suppresses the orgasm like nothing else. Pretty clever, huh?"
g3 "Actually kind of yes..."
with hpunch
pause.3
with hpunch
pause.3
j "Yeah, Dahlia taught me that..."
g3 "But, you know... If I keep being nice and all, I'll never cum..."
hide image "06_jas/j10.png"
show image "06_jas/j10.png" with d5 
j "Right, right, just do what you think is necessary now! I think I will be alright!"
j "I'll try to hold it off! Maybe will think about my father or something."
g3 "Well, alright then, you whore!"
with hpunch
hide image "06_jas/j15.png"
show image "06_jas/j15.png" with d3 
j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
g3 "Yes! Yes! You dirty little slut!"
hide image "06_jas/j16.png"
show image "06_jas/j16.png" with d3 
j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} so hard!"
g3 "Shut the fuck up and let me cum!"
j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
g3 "Shut the fuck up, I said!"
hide image "06_jas/j17.png"
show image "06_jas/j17.png" with d3 
j "Ah...{image=textheart.png} ah...{image=textheart.png} I cant! I'm on the verge again... I'm sorry..."
g3 "That's alright, that's alright, I'm, almost there myself..."
j "Aw... You're being nice again. That helps..."
g3 "Shut your mouth, you slut!"
j "Ah!{image=textheart.png} No, I'm almost..."
j "I'M Cummiiiiiiing!{image=textheart.png}{image=textheart.png}{image=textheart.png} I'm sorry, I'm cumming I can't--"
g3 "{size=+7}Worthless whore! Argh!{/size}"
show white 
pause.2
hide white
pause.3
show white 
pause .1
hide white
hide image "06_jas/j18.png"
show image "06_jas/j18.png" 
with hpunch 
pause.3
with hpunch 
pause.3
with hpunch 
pause.3
show ctc7 at right
pause
hide ctc7
g3 "Take it, you slut! Right in your pussy!"
j "{size=+9}AAAAAhhhh!{image=textheart.png}{image=textheart.png}{image=textheart.png}{/size}"
g3 "{size=+9}Yes! Yes! Argh!{/size}"
with hpunch
hide image "06_jas/j19.png"
show image "06_jas/j19.png" with d5
j "ah...{image=textheart.png} I'm cumming...{image=textheart.png}"
g3 "Argh...."
j "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
hide image "06_jas/j20.png"
show image "06_jas/j20.png" with Dissolve(1)
show ctc7 at right
pause
hide ctc7
show blkfade with Dissolve(3)
show ctc7 at right
play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
pause
hide ctc7

menu:
    m "Well..."
    "\"...That was weird.\"":
        m "Well, that was.... weird."
        jas[45] "Yes, i know... But I feel so good... What about you?"
        g9 "Yes, I do feel good as well, you nasty whore..."
        jas[59] "*Giggle* Somehow I feel closer to you now..."
        m "I know, that's my fault... I dropped my guard down... Not supposed to be this way in front of you, you know..."
        jas[58] "I understand..."
        jas[59] "You're such a softie inside..."
        jas[50] "Usually I don't like men like that... But it is nice to know that you have a softer side..."
        m "Be quiet, you whore... *Chuckle*"
        jas[59] "*giggle* Yes, master!"
    "\"...That was fun.\"":
        m "Well, That was fun..."
        jas[45] "What? Oh, yes... I suppose..."
        m "I sure did enjoy myself..."
        jas[45] "I'm pleased to know that. Now if you don't mind I need to leave..."
        m "Er.. sure..."
        m "See you at home?"
        jas[45] "Yes... Until then..."
        ">Jasmine leaves the room..."
    "\"...I want my money back.\"":
        m "Well, I want my money back."
        with hpunch
        jas[49] "{size=+5}What?!!{/size}"
        m "That was terrible... You started to cum halfway through and forced me to be nice to you..."
        g4 "What kind of crap is this?"
        g4 "I want my money back!"
        jas[57] "What a jerk!"
        jas[47] "Burn in hell you old fool!"
        ">jasmine storms out of the room."
        $ renpy.play('sounds/door2.mp3')  
        with hpunch
        m "Wait, you forgot your clothes..."
        m "And what about my money?"
        g4 "Stupid whore..."

show ctc7 at right
pause
hide ctc7
"Some time later you leave the brothel."
hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
if brothelnight:
    ">You return home and go to sleep."
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayone
else:            
    ">It's getting late. You decide to head home."
    jump dayends


            
            
            
            
            
            









        

       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            