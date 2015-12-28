label dawhore:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with d3
    pause.7
    show iris 84 at right behind blkfade
    hide blkfade with d3
    sch1100 "Hello. Welcome to the \"Red Phoe--"
    show iris 86 at right with d3
    sch1100 "Oh, it's you..."
    show iris 84 at right with d3
    sch1100 "So... em..."
    show iris 86 at right with d3
    sch1100 "Thanks to you I'm a real whore now..."
    sch1100 "You will have to pay in gold for my services of course..."
    label dont_show_tits:
    menu:
        "You currently have [gold] gold. \nWould you like to give 150 gold to Iris?"
        "\"No problem.\"":
            if gold >= 150:
                $ gold -=150
                m "No problem..."
                ">You give Iris 150 gold coins."
                show iris 84 at right with d3
                sch1100 "Alright! Follow me."
                show blkfade with d3
                hide iris with d3
                pause.7
                jump iris_the_sex
            else:
                sch1100 "Doesn't look like you can afford it..."
                hide iris with d3
                jump brothelmain
        "\"I have to pay? No, thanks!\"":
            m "What? I have to pay for that? No, thanks!"
            show iris 82 at right with d3
            sch1100 "...................."
            show blkfade with d3
            hide iris with d3
            pause.7
            hide blkfade with d3
            play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
            jump brothelmain
        "\"Just show me your tits.\"":
            m "Actually, Iris, all I want is to take a peek at your tits..."
            show iris 88 at right with d3
            sch1100 "W-what? How can you ...? You are my father's frien--"
            show iris 86 at right with d3
            sch1100 "Oh... I guess it's a bit too late for that, huh?"
            sch1100 "Well... I don't think there is a problem as long as I get paid."
            show iris 84 at right with d3
            sch1100 "Give me 5 gold coins and you can look all you want..."
            menu:
                "\"Sure. Here you go.\"":
                    if gold >= 5:
                        $ gold -=5
                        m "Sure. Here you go."
                        ">You give Iris 5 gold coins."
                        sch1100 "Thank you very much."
                    else: 
                        m "(Crap!)"
                        m "(I don't even have 5 gold coins to spare... What a bummer...)"
                        sch1100 "Huh? What happened?"
                        sch1100 "You decided that they're not worth 5 gold coins, didn't you?"
                        g4 "Y-yeah, that's what happened..."
                        sch1100 "*Sigh*"
                        jump dont_show_tits
                "\"5 gold coins? No, thanks.\"":
                    m "5 Gold coins? No thanks..."
                    sch1100 "Oh well..."
                    show blkfade with d3
                    show iris 82 at right behind blkfade
                    pause.7
                    hide blkfade with d3
                    sch1100 "If you still want to go upstairs with me it will be 150 gold coins."
                    jump dont_show_tits
                "\"Show them for free. You owe me!\"":
                    m "How about you show them to me for free. You owe me this much, don't you think so, Iris?"
                    show iris 86 at right with d3
                    sch1100 "Hm..."
                    sch1100 "Well, if it wasn't for you, I just wouldn't be here..."
                    sch1100 "So I suppose I do owe you..."
            show blkfade with d3
            show iris 104 at right behind blkfade
            pause.7
            sch1100 "Alright, here we go..."
            hide blkfade with d5
            show con1 at right
            show ctc7 at right
            pause
            hide con1
            hide ctc7
            sch1100 "......."
            show iris 105 at right with d3
            sch1100 "......."
            show iris 90 at right with d3
            sch1100 "Well, what do you think? Do you like 'em?"
            menu:
                "\"Oh, yes. Your tits are perfect.\"":
                    g9 "Oh, yes. Your tits are perfect, Iris."
                    sch1100 "Thank you!"
                    sch1100 "So, how about going upstairs with me now?"
                    sch1100 "You will have to pay more than 5 gold coins for that, of course."
                "\"Well... They could be bigger...\"":
                    m "Well... They could be bigger..."
                    show iris 106 at right with d3
                    sch1100 "*Sigh* I know...."
                    sch1100 "So... You want to go upstairs now maybe?"
                "\"I don't like small tits.\"":
                    m "Not a big fan of small tits, sorry..."
                    show iris 106 at right with d3
                    sch1100 "............."
                    sch1100 "Em... So I guess you don't want to go upstairs with me then?"
                    sch1100 "*Sigh*"
            menu:
                "You currently have [gold] gold. \nWould you like to give 150 gold to Iris?"
                "\"Why not? Lead the way.\"":
                    if gold >= 150:
                        $ gold -=150
                        m "Why not? Lead the way."
                        show iris 90 at right with d3
                        sch1100 "Alright! Follow me."
                        show blkfade with d3
                        hide iris with d3
                        pause.7
                        jump iris_the_sex
                    else:
                        sch1100 "Doesn't look like you can afford it..."
                        hide iris with d3
                        jump brothelmain
                "\"Maybe some other time, Iris.\"":
                    m "Maybe some other time, Iris."
                    sch1100 "Too bad... Well, thank you for stopping by..."
                    show blkfade with d3
                    hide iris with d3
                    pause.7
                    hide blkfade with d3
                    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                    jump brothelmain
                               
                                    
#############THE_SEX#####################
label iris_the_sex:
play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
ir[1] "......................................."
m "Why are you so quiet all of a sudden?"
ir[3] "Right, sorry..."
ir[3] "I dunno, I guess it's a little bit weird because... you know... it's you."
menu:
    "\"It's not weird. Get on the bed!\"":
        m "It's not weird. Now get on that bed!"
        ir[4] "Yes!"
        ir[4] "Let's just do this. Just treat me like you would treat any other whore!"
    "\"It's a little weird, I suppose...\"":
        m "Yes, it's a little bit weird I suppose..."
        ir[4] "Yes... But don't worry, you came here to have some fun, and I will do everything in my power not to disappoint you!"
    "\"Hm......\"":
        m "Hm..."
        ir[3] "Yes, I thought so..."
        ir[4] "But it doesn't change anything. Just try not to think about my father, alright?"
        g4 "Your... father? You mean Maslab? Why would I think about him now?"
        ir[3] "Oh, right, I guess I should have better kept that advice to myself then... sorry..."
ir[1] "So..."
ir[1] "You just lie down and let me take care of you, alright?"
ir[1] "Let me unbutton your cloak first..."
ir[3] "Now your pants..."
$ renpy.play('sounds/boing02.mp3')
with hpunch
ir[5] "!!!!!!!!!"
ir[4] "Oh, wow... You are all ready to go!"
g9 "Heh..."
stop music fadeout 2
ir[3] "Your... cock is...{w} so big..."
ir[3] "Let me just...{w} no, maybe like this...{w} Wait...."
$ renpy.play('sounds/gltch.mp3')
with hpunch
with kissiris
ir[6] "Ooooohhhhhhhhhhhh....{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
g4 "Aaaagh....."
ir[7] "Yes....{image=textheart.png}{image=textheart.png}{image=textheart.png}"
show image "03_iris/ir02.png" behind blkfade
hide blkfade with Dissolve(1)
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
sch1100 "Ah....."


sch1100 "Yes! Yes! Fuck me!"
sch1100 "Oh, this is amazing..."
sch1100 "Ah... This is actually happening... I'm a whore... I'm an actual whore!"
g4 "Yes, you are! Yes your are! Oh, this is good!"
sch1100 "Yes! Yes! Promise to treat me like a whore! Promise me!"
sch1100 "Please! Oh, your cock... ah..."
sch1100 "ahh...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
g4 "Oh, hey, I really like your little tattoo, down there."
show image "03_iris/ir03.png" with d3
sch1100 "Yes, me too. It's so naughty, right? ah..."
sch1100 "It's like a sign for all the men: \"My pussy is that way. Please use it as you will!\""
hide image "03_iris/ir02.png" 
show image "03_iris/ir02.png" with d3
sch1100 "Ah, that's so hot!"
sch1100 "Oh, yes... yes... I love it, just to slide up and down your enormous dick! Yes!"
g4 "Argh..."
hide image "03_iris/ir04.png" 
show image "03_iris/ir04.png" with d3
sch1100 "Imagine what my father would say?!"
g4 "What?"
g4 "No, don't bring your fucking dad into this!"
g4 "I don't want to think about him now!!!"
hide image "03_iris/ir02.png" 
show image "03_iris/ir02.png" with d3
sch1100 "But it's so hot! He would never believe ah...{image=textheart.png}"
sch1100 "He would never believe... that I... his little Iris..."
hide image "03_iris/ir05.png" 
show image "03_iris/ir05.png" with d3
sch1100 "Could be a whore..."
sch1100 "Every time I come here, men fuck me..."
sch1100 "All sorts of men... Merchants from the market, city guards, my father's old accomplices..."
sch1100 "Ah, yes... Yes, like this! Yes!"
sch1100 "It is only a matter of time until my father finds out..."
g4 "*Panting heavily*"
menu:
    "\"I suppose... But better later than sooner.\"":
        g4 "You're right... But better later than sooner."
        hide image "03_iris/ir03.png" 
        show image "03_iris/ir03.png" with d3
        sch1100 "Why? I don't care anymore..."
        sch1100 "To be honest I wouldn't mind if he entered into the room this very minute..."
        g4 "What?"
        hide image "03_iris/ir02.png" 
        show image "03_iris/ir02.png" with d3
        sch1100 "Yes! Ah! He would come in and see you fuck his precious Iris like the cheap whore that she is! Oh, that would be {size=+7}so{/size} hot!"
        g4 "What the....? I hope this is not some twisted game, you and Maslab play..."
        g4 "He is not hiding under this bed with a dagger with my name on it, is he?"
        hide image "03_iris/ir06.png" 
        show image "03_iris/ir06.png" with d3
        sch1100 "Heh, of course not. Don't be so silly."
        hide image "03_iris/ir02.png" 
        show image "03_iris/ir02.png" with d3
        sch1100 "Although that would be even hotter..."
        g4 "Whatever you say, just keep jumping on my cock like that."
        sch1100 "Y-yeees! Ah!"
    "\"Who cares! Quit yapping about your old man!\"":
        g4 "Who gives a damn! Quit yapping about your old man already, Iris."
        g4 "He is the last thing I want to think about right now!"
        hide image "03_iris/ir02.png" 
        show image "03_iris/ir02.png" with d3
        sch1100 "Right... ah... sorry.... Just keep fucking me, yes!"
    "\"I will keep your secret, don't worry.\"":
        g4 "I will, agh, keep your secret, don't worry."
        hide image "03_iris/ir06.png" 
        show image "03_iris/ir06.png" with d3
        sch1100 "Oh, that's OK... I almost want him to find out..."
        sch1100 "That old fool! That would teach him a lesson, sure!"
        hide image "03_iris/ir02.png" 
        show image "03_iris/ir02.png" with d3
        sch1100 "Yes! Yes! Keep fucking me!"
sch1100 "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
hide image "03_iris/ir07.png" 
show image "03_iris/ir07.png" with d3
sch1100 "ah..................."
sch1100 "............................."
sch1100 "........................................"
g4 "Iris?"
sch1100 "Oh, I'm sorry, I was just thinking... ah...{image=textheart.png} ah...{image=textheart.png}"
sch1100 "Ever since I started ... ah...{image=textheart.png} working here..."
hide image "03_iris/ir08.png" 
show image "03_iris/ir08.png" with d3
sch1100 "I... *sob* ah...{image=textheart.png} I... *sob*"
g4 "Oh, no! Don't you dare to start crying!"
hide image "03_iris/ir09.png" 
show image "03_iris/ir09.png" with d3
sch1100 "*sob-sob* I'm so-o-o-o-o-ory!"
sch1100 "*sob-sob* It's just... It's just..."
hide image "03_iris/ir10.png" 
show image "03_iris/ir10.png" with d3
sch1100 "*sob* I'm so happy! *sob*"
sch1100 "*sob-sob* ah...{image=textheart.png}"
sch1100 "But this is so... ah...{image=textheart.png} unprofessional, I know..."
hide image "03_iris/ir09.png" 
show image "03_iris/ir09.png" with d3
sch1100 "Ah...{image=textheart.png} so embarrassing. Ah...{image=textheart.png}"
sch1100 "Could you do me a favor and not tell Dahlia that I have been crying during sex again?"
g4 "Sure thing. Now, shut up, and let me enjoy that teeny body of your in peace, alright?!"
hide image "03_iris/ir08.png" 
show image "03_iris/ir08.png" with d3
sch1100 "Of course, I'm sorry. Just tell me what to do!"
menu:
    "\"Be aggressive!\"":
        g4 "Be more aggressive!"
        hide image "03_iris/ir04.png" 
        show image "03_iris/ir04.png" with d3
        sch1100 "Alright!"
        sch1100 "Come on, old man! I have been a really bad girl! Punish me!"
        g4 "Yes, that's more like it!"
        hide image "03_iris/ir03.png" 
        show image "03_iris/ir03.png" with d3
        sch1100 "Yes! Ah! Yes! Punish this little whore with your cock!"
        g4 "Yes! Yes, you slut!"
        hide image "03_iris/ir05.png" 
        show image "03_iris/ir05.png" with d3
        sch1100 "Ah! Fuck this little whore! Yes! She's been bad!"
        hide image "03_iris/ir11.png" 
        show image "03_iris/ir11.png" with d3
        sch1100 "Nothing but a worthless whore! Give her the fuck of her life!"
        sch1100 "Yes! Just like this! Oh, yes!"
        g11 "*Growl*"
        hide image "03_iris/ir12.png" 
        show image "03_iris/ir12.png" with d3
        sch1100 "Yes, yes! Make me cum, old man! Make this little disobedient slut cum!"
        g11 "Argh..."
        sch1100 "Oh, I love it when men cum in my pussy! Ah! Yes!"
        sch1100 "Right before the cum starts shooting out of the cock it gets much bigger in size! I can always feel it!"
        sch1100 "It always makes me cum as well... ah.. yes! Yes!"
        g11 "Argh! You fucking whore! I'm almost there!"
        hide image "03_iris/ir13.png" 
        show image "03_iris/ir13.png" with d3
        sch1100 "Yes! Yes! Me too! Come on, old man! Cum! Cum! Let's cum together!"
    "\"Be submissive!\"":
        g4 "Be a bit more submissive!"
        hide image "03_iris/ir03.png" 
        show image "03_iris/ir03.png" with d3
        sch1100 "I could do that..."
        sch1100 "Ah... yes...{image=textheart.png} yes...{image=textheart.png} please, don't stop..."
        hide image "03_iris/ir05.png" 
        show image "03_iris/ir05.png" with d3
        sch1100 "I'm your obedient little slut... ah...{image=textheart.png}"
        g11 "Yes, you are!"
        hide image "03_iris/ir15.png" 
        show image "03_iris/ir15.png" with d3
        sch1100 "Yes... I will always do whatever you say, as long as you promise to fuck me like this as often as you can... ah...{image=textheart.png}"
        sch1100 "Ah...{image=textheart.png} thank you..."
        sch1100 "Thank you, old man. Thank you for taking your time to fuck me..."
        g11 "Argh, you little slut!"
        hide image "03_iris/ir08.png" 
        show image "03_iris/ir08.png" with d3
        sch1100 "Yes, I'm your little slut... And I'm ready to cum..."
        sch1100 "Ah...{image=textheart.png} Just let me know when.... Oh...{image=textheart.png} Your cock..."
        g11 "Grgh!"
    "\"Just be yourself!\"":
        g4 "Just be yourself, Iris."
        hide image "03_iris/ir02.png" 
        show image "03_iris/ir02.png" with d3
        sch1100 "Alright!"
        sch1100 "Fuck me then! Rip me apart with your cock of iron! Ah!"
        hide image "03_iris/ir04.png" 
        show image "03_iris/ir04.png" with d3
        sch1100 "Oh, yes! Up and down I go... Ah...{image=textheart.png} what a slut... yes...{image=textheart.png} yes...{image=textheart.png}"
        g11 "GRGH!"
        hide image "03_iris/ir05.png" 
        show image "03_iris/ir05.png" with d3
        sch1100 "This is so amazing... ah... yes, more, give me more, old man!"
        sch1100 "Yes! Fuck me harder!"
        with hpunch
        g11 "{size=+7}ARGGGHG!{/size}"
        hide image "03_iris/ir12.png" 
        show image "03_iris/ir12.png" with d3
        sch1100 "?!!!!!!!!!!!!!!"
        sch1100 "AH! Oh, so hard! Yes, yes, like that!"
        sch1100 "Are you ready to cum? Are you ready to cum?! Ah!"
        hide image "03_iris/ir13.png" 
        show image "03_iris/ir13.png" with d3
        sch1100 "I don't know how much longer I could hold on! Ah!"
        sch1100 "Just let me know when!!!"
menu:
    "-Give Iris a warning-":
        g11 "I'm about to cum! Here it comes!!"
        hide image "03_iris/ir16.png" 
        show image "03_iris/ir16.png" with d3
        sch1100 "Yes! Yes! Just cum inside! Fill this little pussy!"
        sch1100 "Yes! YEEES!"
    "-Just cum in her pussy-":
        g11 "AAAAAARGH!!!!!"
        hide image "03_iris/ir16.png" 
        show image "03_iris/ir16.png" with d3
        sch1100 "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
g11 "Yes, you want to be a proper whore! Here is your reward!"
sch1100 "AAAha-ah-ah! Yes!"
show white 
pause.2
hide white
pause.3
show white 
pause .1
hide white
show image "03_iris/ir17.png" with d5
with hpunch 
g11 "ARGH! You slut... ah..."
sch1100 "Ah, it's so hot... ah...{image=textheart.png}"
show white 
pause.2
hide white
pause.3
show white 
pause .1
hide white
with hpunch 
g11 "ARGH! You whore!!"
sch1100 "Yes! Yes, thst I am!"
hide image "03_iris/ir18.png" 
show image "03_iris/ir18.png" with d3
sch1100 "..................."
sch1100 "..........................."
g11 "What is it, whore, why did you go quiet?"
sch1100 "I'm... c-cumming... I'm sorry... I'm not supposed to keep it a secret... am I?"
sch1100 "Yes! I'm cumming! I'm cumming again!"
sch1100 "I'm sorry, father! I'm cumming...."
hide image "03_iris/ir19.png" 
show image "03_iris/ir19.png" with d3
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
sch1100 "Thank you for this, old man."
sch1100 "Thank you for making me feel like a woman."
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7


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



     
#        "Yes please!":
#            sch9 "That will be 120 gold coins, sweetie."
#            menu:
#                "You currently have [gold] gold. \nWould you like to give 80 gold to D.A.?"
#                "Yes.":
#                    if gold >= 120:
#                        $ gold -=120
#                        sch9 "Alright then, let's go upstairs."
#                        "You facefuck D.A."
#                        "After that you leave."
#                        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
#                        if brothelnight:
#                            "You return home and go to sleep."
#                            show image "interface/blackfade.png" with Dissolve(.3)
#                            pause 1
#                            jump dayone
#                        else:            
#                            "It's getting late. You decide to head home."
#                            jump dayends
#                    else:
#                        sch9 "Doesn't look like you can afford it, honey. Well, I don't work for free honey."
#                        jump brothelmain
#                "Not today.":
#                    sch9 "Well, I don't work for free honey. Come back when you change your mind."
#                    jump brothelmain
#        "Not today.":
#            sch9 "Oh, I see..."
#            jump brothelmain