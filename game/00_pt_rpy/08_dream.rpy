label dream_01:
play music "music/tension2.mp3" fadein 1 fadeout 1 #TENSION2
#play music "music/fight.mp3" fadein 1 fadeout 1 #FIGHT
show white with Dissolve(1)
show ctc7 at right
pause
hide ctc7
sul03n "Jafar, I order you to stop!"
jaf[2] "Ah, but there is a new order now."
jaf[3] "MY ORDER!"
jaf[1] "Finally, {size=+5}YOU{/size} will bow to {size=+5}ME!{/size}"
jas[37] "We will never bow to you!"
ia01 "Why am I not surprised?!"
jaf[3] "If you won't bow before a sultan..."
jaf[3] "Then you will cower before a sorcerer!"
jaf[4] "Genie, my second wish..."
jaf[3] "I wish to be the most powerful sorcerer in the world!"
ali01 "Genie, stop!"
g12 "I'm sorry...."
show ctc7 at right
pause
hide ctc7
$ renpy.play('sounds/remedy01.ogg')
pause 1
with hpunch
pause 1
with vpunch
$ renpy.play('sounds/remedy02.ogg')
show ctc7 at right
pause
hide ctc7
ia02 "Ladies and gentlemen, a warm Agrabah welcome for Sorcerer Jafar!"
$ watched_dream_01 = True
show image "interface/blackfade.png" with Dissolve(.3)
hide image "04_pt/slavem/night.jpg"
hide image "04_pt/slavem/night2.jpg"
hide sleeping
pause 1
stop music fadeout 1
g5 "No! What have you done, you fool?!"
g6 "Oh... it was just a dream..."
m "Hm... Maybe something I ate...?"
jump dayone


####END_OF_DREAM_#_1################



label dream_02:
play music "music/tension2.mp3" fadein 1 fadeout 1 #TENSION2 (MUD)
show white with Dissolve(1)
show ctc7 at right
pause
hide ctc7
jaf[4] "Genie, my second wish..."
jaf[3] "I wish to be the most powerful sorcerer in the world!"
ali03 "Genie, don't...!"
g12 "I'm sorry, Al...."
$ renpy.play('sounds/magic4.ogg')
with black_magic
pause 1
ia02 "Ladies and gentlemen, a warm Agrabah welcome for Sorcerer Jafar!"

jaf[11] "Oh... Much better!"
jaf[11] "Now, where were we?"
jaf[12] "Ah, yes. Abject humiliation!"
$ renpy.play('sounds/tiger.mp3')
raj02 "*low growl*"
jaf[12] "Down, boy!!!"
$ renpy.play('sounds/magic4.ogg')
with black_magic
###Rajah turned into a tiger cub##############
pause 2.3
$ renpy.play('sounds/meow.mp3')
raj01 "meow..."
jaf[14] "Who's next?"
jaf[14] "How about you, old fool?"
sul03n "Jafar, I--"
$ renpy.play('sounds/magic4.ogg')
with black_magic
pause 1
sul04n "Oh, dear..."
jaf[11] "And as for you, my delicate flower..."
jas[37] "Jafar, you will pay for this, I swear!"
$ renpy.play('sounds/magic4.ogg')
with black_magic
pause 1
jas[60] "...........?"
jaf[12] "What is it, princess? Lost for words?"
jaf[13] "Admirable quality for a slave-girl..."
ali03 "Jafar! Keep your hands off of her!"
jas[61] "Ali?"
jaf[11] "Yes! Say hello to your precious Prince Ali!"
jaf[13] "Or should I just say..."
jaf[14] "Aladdin?"
$ renpy.play('sounds/magic4.ogg')
with black_magic
pause 1
jas[62] "Ali?!"
ali04 "Jasmine, I'm sorry..."
ali04 "I tried to tell you... I just..."
jaf[13] "So Ali turns out to be a merely Aladdin."
jaf[12] "And his personality flaws give me adequate cause..."
jaf[12] "To send him packing on a one-way trip to the ends of earth!"
ali02 "W-what?!"
ia02 "Good-bye, see ya!"
ali02 "No, wait!"
jas[63] "Jafar, don't you dare--"
jaf[14] "So long! Ex-Prince Ali!"
$ renpy.play('sounds/magic4.ogg')
with black_magic
pause 1
jaf[13] "Suits you right, riff-raff..."
jas[64] "Aladdin....."
stop music fadeout 1
$ watched_dream_02 = True
show image "interface/blackfade.png" with Dissolve(.3)
hide image "04_pt/slavem/night.jpg"
hide image "04_pt/slavem/night2.jpg"
hide sleeping
pause 1
g5 "No! Aladdin!"
g6 "Huh? another dream...?"
g6 "But it felt so real....."
g6 "Hm.... Who's that Aladdin fellow, I wonder?"
m "Well, I don't have time to brood over such things..."
m "Jasmine's training is coming along erally well, but not nearly as good as it should..."
m "I better pick up my game or I could get in trouble with the sultan..."
jump dayone
####END_OF_DREAM_#_2##################

label dream_03:
###FADEOUT#######################
play music "music/tension2.mp3" fadein 1 fadeout 1 #TENSION2 (MUD)
#play music "music/Vision2.mp3" fadein 1 fadeout 1 #TENSION
show white with Dissolve(1)
show ctc7 at right
pause
hide ctc7
ia02 "Hey, fat man, you want a cracker?"
sul04n "I..."
ia02 "Here! And some more!"
ia02 "What? You don't like it?"
ia02 "Here is another cracker! And another one!"
sul04n "Khe-khe... *cough!*"
ia02 "Here! Have lots of crackers!"
jas[65] "No, please stop this!"
jas[65] "Jafar, tell your wretched bird to leave my father alone!"
jaf[13] "Iago, if you will..."
ia01 "Alright, alright..."
jaf[11] "Pains me to see you reduced to this, Jasmine..."
jaf[11] "A beautiful desert bloom such as yourself should be on the arm of the most powerful man in the world."
jaf[11] "What do you say, my dear?"
jaf[13] "Why, with you as my queen by my side--"
with hpunch
jas[63] "{size=+5}NEVER!!!{/size}"
jaf[14] "I'll have to teach you some respect first then..."
jaf[12] "Genie!"
g12 "Yes, master?"
jas[65] "............?"
jaf[12] "I have made up my mind about my final wish..."
jaf[13] "I wish for princess Jasmine to fall desperately in love with me!"
$ renpy.play('sounds/magic4.ogg')
g13 "Ah, Master, there are a few addenda, some quid pro quo..."
jaf[14] "Don't talk back to me, you big blue lout!"
jaf[14] "You will do what I order you to do, slave!"
g13 "Well, master, like I said..."
jaf[14] "You dare to disobey me?!"
ia02 "Jafar, hey, Jafar, I think I have an idea!"
jaf[13] "Huh? What is it, Iago?" 
ia02 "*Whisper-whisper*"
jaf[11] "Why, Iago, but this is quite brilliant!"
g13 "Huh?"
jaf[13] "Alright, slave, my final wish..."
jaf[12] "I wish for you to become human!"
g13 "W-what?"
jaf[13] "Yes. A mere mortal..."
$ watched_dream_03 = True
show image "interface/blackfade.png" with Dissolve(3)
hide image "04_pt/slavem/night.jpg"
hide image "04_pt/slavem/night2.jpg"
hide sleeping
stop music fadeout 1
pause 1
g5 "No, you can't!"
g6 "Huh? That dream again..."
g6 "Is there some hidden meaning to this...?"
g6 "Jasmine was there... and Jafar..."
g6 "And that Genie, character, I think somehow it was me..."
g6 "This is so weird..."
menu:
    g6 "Maybe I should give ithis more thought?"
    "\"Nah... Just a silly dream.\"":
        m "Nah... Just a silly dream..."
        m "I have no time to brood over such things..."
    "\"It must mean something...\"":
        g6 "It must mean something..."
        g6 "I keep seeing the same dream..."
        g6 "And every time the story continues further and further..."
        g6 "Can't be just a figment of my imagination, can it now?"
        g6 "Hm............"
        m "....................."
jump dayone
################END_OF_DREAM_03##############

label dream_04:
play music "music/tension2.mp3" fadein 1 fadeout 1 #TENSION2 (MUD)
jaf[1] "Alright, slave, my last wish..."
jaf[12] "I wish for you to become human!"
g13 "W-what?"
jaf[13] "Oh, yes! With you, stripped off of your cosmic powers, I could truly be called the most powerful man in the entire world!"
g13 "M-master, when you say \"Human\"..."
g13 "No doubt, you mean to say that you are granting me my freedom, correct?"
jaf[14] "Don't put words into my mouth, slave!"
jaf[14] "Here is my wish: I wish for you to become an ordinary human being, but forever remain my slave!"
$ renpy.play('sounds/magic4.ogg')
g12 "No... No, this can't end like this..."
g12 "Not like this..."
g12 "Something went wrong... I..."
g "I feel someone else's presence..."
jaf[14] "What are you waiting for, slave of the lamp?!"
jaf[14] "Grant me my wish! Now!"
g "Someone is meddling with history..."
g "This is not right..."
g "What is this...? Who is that...?"
g "{size=-5}(Akabur...?){/size}"
jaf[14] "Slave! Grant me my wish, {size=+5}now!{/size}"
g12 "No...."
jaf[14] "What did you just say?!"
jaf[11] "Silly genie... You know you can't disobey me!"
g12 "......................................"
g12 "...................."
stop music fadeout 1
g12 "Jafar...."
jaf[13] "Huh?"
$ renpy.play('sounds/magic4.ogg')
with hpunch
pause.5
play music "music/GorillaTheme.mp3" fadein 1 fadeout 1 #GORILLA
g14 "{size=+10}I REFUSE YOUR WISH!{/size}" #CRAZY FACE#
jaf[15] "???"
jaf[15] "What?!"
jaf[15] "B-but y-you can't..."
jaf[15] "The lamp..."
ia01 "Ja-afa-ar, I don't like this!"
g14 "{size=+7}Jafar! I am stripping you of your powers as a wizard!{/size}"
jaf[15] "What? You can't do this!"
with hpunch
g14 "{size=+7}Watch me, you puny man!{/size}"
g14 "{size=+7}From now on you shall be nothing more but a mere human!{/size}"
jaf[14] "No! I'm commanding you to stop, slave of the lamp!"
jas[65] "Genie?"
g14 "{size=+5}Princess...{/size}"
g14 "{size=+5}I'm so sorry... I am still a slave of the lamp...{/size}"
jas[65] ".........."
g14 "{size=+5}I'm afraid the repercussions of my actions will be most severe...{/size}"
g14 "{size=+5}And could shake the very foundationS of the world itself...{/size}"
g14 "{size=+10}AAAAARRRRGH!{/size}"
with hpunch
play music "music/GorillaTheme.mp3" fadein 1 fadeout 1 #GORILLA
g15 "{size=+10}I'm burning ALL MY cosmic powers into this one act of disobedience...{/size}"
g15 "{size=+7}But a bond between genie and his lamp can never be broken...{/size}"
jas[65] "Genie... I..."
g15 "{size=+7}I'm sorry, Princess... I just couldn't let our story end like this...{/size}"
g15 "{size=+7}We were not supposed to lose this fight... I know it...{/size}"
jas[65] "Genie....?"
g15 "{size=+5}Damn you Akabur!{/size}"
with hpunch
g15 "{size=+10}Damn you, and your wretched following!{/size}"
g15 "{size=+10}You did this to us! It's all on you!...{/size}" #tears#
g15 "{size=+10}.....................{/size}"
jaf[14] "Stop it, slave! I order you to stop!"
g15 "{size=+10}AAAAAAAAAAARGH!!!{/size}"
jas[65] "Genie, what's going on, I'm scared..."
show blkfade with Dissolve(2)
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
"............{w}..........{w}..........{w}..........{w}..........{w}..........{w}..........{w}.........."

if dress01:
    show image "04_pt/slavem/wedding17c.jpg" behind blkfade
if dress02:
    show image "04_pt/slavem/wedding17b.jpg" behind blkfade
if dress03:
    show image "04_pt/slavem/wedding17.jpg" behind blkfade
if dress04:
    show image "04_pt/slavem/wedding17d.jpg" behind blkfade






stop music fadeout 1
g5 "But of course! The real Agrabah, Aladdin, carpet, and the real sultan!"
g5 "It's all coming back to me now! How could I forget my entire life?!"
g5 "And Jasmine..."
g5 "Oh, no what have I done!"
hide blkfade with Dissolve(2)
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1 #GRAPE_SODA
j "Ah.....{image=textheart.png}"
jaf[1] "Go ahead, my bride, thank the good people of Agrabah..."
j "Em... ah...{image=textheart.png} Thank you, good people of Agrabah..."
jaf[1] "No, not just say that. Let them know what you are thankful for."
j "Ah... Good people of Agrabah, Thank you for watching me ah..."
j "Ah...{image=textheart.png} Thank you for watching me get fucked... ah...{image=textheart.png}"
cr1 "Burn in hell, you disgusting whore!"
j "Ah...{image=textheart.png} No, please, I--"
jaf[1] "Don't mind them, keep going, just like we practiced..."
j "Ah...{image=textheart.png} yes..."
j "I hope I got pregnant today... in front of you all..."
cr1 "Can this disgusting woman stoop any lower?"
cr2 "How disgraceful..."
cr3 "How sad... Her mother must be turning in her grave..."
jaf[1] "Go on, go on..."
j "Ah...{image=textheart.png} Yes...{image=textheart.png} I came countless times in front of you all today..."
j "And my belly is full of sperm now..."
j "And..."
cr1 "Somebody, shut her up already!"
cr2 "We don't want to hear another word from you, whore!"
j "No please, I only want you to love me..."
j "I even let you watch me get fucked..."
j "Why don't you love me like you used to?"
cr1 "Is she serious?"
j "What am I doing wrong?"
cr1 "Shut up, whore!"
cr2 "You're beyond contempt!"
cr1 "We hate you, you slut!"
cr1 "Princess-whore!"
j "No, please don't call me that... I--"
j "I--- oh...{image=textheart.png}"
jaf[1] "{size=-4}(What is it? Don't tell me you are cumming again?){/size}"
j "{size=-4}(I'm sorry, I can't control it...){/size}"
jaf[1] "{size=-4}(Unbelievable... The old man really did a number on you. I need to reward him somehow later.){/size}"
j "{size=-4}(Ah, jafar, jahar, I'm cumming...){/size}"
jaf[1] "What are you telling me this for, you silly girl?"
jaf[1] "Tell this to your loyal subjects!"
j "Yes....{image=textheart.png}"
j "Good people of... ah...{image=textheart.png}"
j "I'M CUMMING!!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
cr1 "Princess whore! Stone her!"
j "Ahhhh!{image=textheart.png}"
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
show image "wedding_g.png" with d5
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
m "I can't watch this anymore..."
m "Jasmine...."
m "Jasmine, what have I done..."
m "And there is nothing I can do to fix this now..."
m "I burned all my powers away trying to stop Jafar..."
m " And now I'm a just a human... Sad powerless human..."
m "I... I'm so sorry...*sob*"
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
show image "wedding_g02.png" with d5
hide image "wedding_g01.png" 
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
ir[11] "Yes! Stone that bitch!"
play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
with hpunch
g4 "Iris?!"
ir[12] "Oh, hey old man."
ir[12] "I wasn't sure about coming to the parade, but I'm so glad I did."
ir[13] "I'm having the best time!"
ir[11] "Princess whore, princess whore! Come on people! Princess whore!"
ir[13] "Teehe-hee-hee."
m "..............."
ir[12] "Hey, what's the matter, old man?"
ir[12] "You look even gloomier then usual." 
#menu:
#    "\"What? Of course, I'm fine!\"":
#        g4 "What? Of course, I'm fine!"
#        g4 "Just something got in my eye..."
#        ir[14] "Whatever you say, tough guy..."
#        ir[14] "You definitely look down though... Did something happen?"
#    "\"Kind of...\"":
#        m "Kind of..."
#        ir[14] "........."
#        ir[12] "Old man, that's nasty... men don't cry."
#        m "I'm not crying... It's just..."
#        ir[14] "What is it then? Did someone spit in your eye or something?"
#        ir[14] "Because it kinda looks like--"
#        g4 "Enough! Know your place, girl!"
#        ir[1] "Hm... something is definitely wrong..."
#        ir[1] "Come on, tell me what happened."

m "It's a long story..."
ir[14] "I have time..."
ir[12] "Hey, the parade is pretty much over so what do you say we go hit a tavern or something?"
ir[17] "Or maybe the brothel?"
ir[16] "Today's spectacle was very exciting, wouldn't you say?"
hide image "wedding_g02.png"
ir[12] "Come on, you can tell me your story on the way there!"
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
hide image "wedding_g.png" with d5
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
j "Please love me..."
cr1 "Shut it whore!"
j "{size=-4}(Ah...{image=textheart.png} not again...{image=textheart.png}){/size}"
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
show blkfade with Dissolve(2)
hide image "04_pt/slavem/parade.jpg"
show image "04_pt/slavem/parade.jpg" behind blkfade
show con1 at right
show ctc7 at right
pause 
hide ctc7
hide blkfade with Dissolve(1)
show ctc7 at right
pause 
hide con1
hide ctc7
ir[14] "So tell me what happened?"
m "That's a long story, Iris..."
m "All I can say is I did a bad thing and there is no way I can set it right..."
ir[14] "Hm..."
ir[14] "Look at you! I never seen you like this before!"
stop music fadeout 1
ir[14] "Listen whatever your \"bad thing\" is, there's gotta be a way to undo it!"
m "No, you don't understand..."
play music "music/dice_game.MP3" fadein 1 fadeout 1  #DICE GAME2
ir[15] "I don't need to understand everything!"
ir[15] "I don't even need to know the details..."
m "Hm?"
ir[15] "I mean, I know you..."
ir[15] "You are a very, {size=+7}VERY{/size} capable man."
ir[15] "And whatever mess you managed to land yourself into, all that is most likely not your fault..."
m "Well--"
ir[11] "Let me, finish, old man!"
ir[15] "Like I said, whatever happened to you, you are still breathing, aren't you?"
ir[15] "Plus you can always count on my help, you know that, right?"
m "Iris..."
ir[14] "I do still owe you, you know."
ir[15] "And if my help alone won't cut it, I still have some connections in the underground world..."
ir[18] "I could introduce you to some pretty nasty characters..."
ir[14] "And my father of course - all his talk about retirement is pure crap!"
ir[18] "I assure you, the moment you mention that you need his help he will be on the bounce!"
ir[18] "And let me tell you, his friends are even nastier than mine!"
m "Hm..."
m "Maybe you're right..."
ir[17] "Of course I am..."
m "Maybe there is still a way...?"
ir[14] "Of course there is!"
m "This will take some planning though..."
m "And I will need money... a lot of money..."
m "And new connections..."
ir[18] "Now you're talking! That's the old man I know!"
m "Iris...."
ir[14] "Yes?"
m "Thank you..."
ir[17] "Heh! Are you gonna start crying again?"
g4 "\"Again\"? When did I ever--"
ir[13] "*chuckle*"
pause.5
show blkfade with Dissolve(2)
pause.5





show image "08_ending/e06.png" at Zoom((800, 600), (607, 263, 1409, 864), (591, 243, 800, 600), 0.0) with Dissolve(1.5)
show ctc7 at right
pause 
hide ctc7
iri "So..."
iri "To the brothel then?"
g3 "Well, alright, you evil little witch..."
iri "Tee-hee-hee."

show image "08_ending/e06.png" at Zoom((800, 600), (591, 243, 800, 600), (0, 0, 1600, 1200), 9)
show ctc7 at right
pause 
hide ctc7
show image "08_ending/e04.png" with Dissolve(1)











#show image "08_ending/e01.png" behind blkfade
#show ctc7 at right
#pause 
#hide ctc7
#hide blkfade with Dissolve(2)
#show ctc7 at right
#pause 
#hide ctc7
#show image "08_ending/e02.png" with Dissolve(1)
#show ctc7 at right
#pause 
#hide ctc7
#show image "08_ending/e03.png" with Dissolve(1)
#show ctc7 at right
#pause 
#hide ctc7
#show image "08_ending/e04.png" with Dissolve(1)
pause
hide blkfade
show blkfade with Dissolve(3)
pause(.3)
j "Please love me..."
j "{size=-4}(Ah...{image=textheart.png} I'm cumming again...{image=textheart.png}){/size}"
show ctc7 at right
pause 
hide ctc7
$ persistent.game_completed = True
pause 2
jump cr
centered "Thank you for playing. \nAKABUR 2014"





#                    m "Alright... So this world is not real... Or, even if it is, it's not my world."
#                    m "Me and princess Jasmine are not supposed to be here..."
#                    m "Princess Jasmine! Oh..."
#                    m "I did some pretty messed up things to her..."
#                    m "After I bring us back she will definitely have me beheaded..."
#                    m "Not the usual empty threats, but for real this time..."
#                    m "But I can think about it later... First I need to stop the wedding!"
#                    m "I don't have my full magic powers anymore, but I'm pretty sure I can still undo this spell, and that should set things right!"
#                    m "But I need to be close enough to the princess Jasmine to do that, otherwise she may get stuck here for good..."
                    




label lazy_or_not:
    show ctc7 at right
    pause 
    hide ctc7 
    a1 "Wait, a second. Let me check something..."
    "....................{w}............{w}............{w}............{w}............"
    show ctc7 at right
    pause 
    hide ctc7
    if quest1complete and quest2complete and quest3complete and quest4complete and quest5complete and quest6complete and quest7complete and quest8complete and quest9complete and quest10complete and quest11complete and quest12complete and quest13complete:
        a1 "You've completed all the quests in the game."
        a2 "Way to go!"
        a2 "Enjoy your \"cake\"!"
        jump the_cake
    else: 
        a6 "No cake for you!"
        pause 1
        return