

                
                
#############################################################################
############################ "MINI" GAME *laugh*########################################
#############################################################################

label slavetrainer:
$ mdaughterfriendship = 0
$ maslabfriendship = 0
$ day = 0
$ pthink = 0 #Must be 0.
$ gold = 0 # Must be 0. 
$ tired = 0
$ mtired = 0
$ outfits = 0
$ strength = 0 #Must be 0.
$ dayswithoutexercise = 0
$ courage = 0 #Must be 0.
$ obedience = 0 #Must be 0.
$ txt = ""
$ dancer = False
$ whore = False
$ taverngirl = False
$ peasant = False
$ slavegirl = False
$ parade = 0
###KISS MY ASS#######
$ kissmyass = True
####TITLES#####
$ myname = "Old man"
$ jasname = "Princess"
###QUESTS NAMES###
$ quest1 = "\"Food for the poor\""
$ quest2 = "\"family feud\""
$ quest3 = "\"Serving the people\""
$ quest4 = "\"the red phoenix rising\""
$ quest5 = "\"a friend in need...\""
$ quest6fix = "\"The dream job\""
$ quest7fix = "\"Pleasing the mother\""
$ quest8 = "\"Lola's new dress\""
$ quest9 = "\"Room 4 1 more\""
$ quest10 = "\"investments that bear fruit\""
$ quest11 = "\"no dancing allowed\""
$ quest12 = "\" to each his own... permit\""
$ quest13 = "\"the favorite customer\""
###DEFAULT OUTFITS#####
$ normalw2 = True
$ peasantw2 = False
$ tavernw2 = False
$ dancew2 = False
$ whorew2 = False
$ slavew2 = False
$ naked2 = False
$ naked_lolita = False
####OUTFITS TO WEAR####
$ dress01 = False
$ dress02 = False
$ dress03 = False
$ dress04 = False
#####QUESTS#########
$ storetopless = 0
$ storecomplete = False
$ storestarted2 = False
$ storestarted = True
#######MASTER QUESTS######
$ idlequest = True
$ onquest = False
$ quest100 = True
$ quest1start = False
$ quest1start2 = False
$ quest1complete = False
####NO NUMBER QUESTS######
$ awmaslab00 = True
$ awmaslab = False
$ awmaslabcomplete = False
$ meetlola00 = True
#######QUEST2##############
$ quest200 = True
$ quest2start = False
$ quest2start2 = False
$ quest2start3 = False
$ quest2start4 = False
$ quest2start5 = False
$ quest2complete = False
#######QUEST3#########
$ quest300 = True
$ quest3start = False
$ quest3start2 = False
$ quest3start3 = False
$ quest3start4 = False
$ quest3start5 = False
$ quest3complete = False
#######QUEST4#########
$ jafardays = 0
$ quest400 = True
$ quest4start = False
$ quest4start2 = False
$ quest4start3 = False
$ quest4complete = False
####QUEST5##########
$ balsamdays = 0
$ azaleadays = 0
$ quest5start = False
$ quest5start2 = False
$ quest5start3 = False
$ quest5start4 = False
$ quest5start5 = False
$ quest5start6 = False
$ quest5start7 = False
$ quest5complete = False
######QUEST6(EMPLOYING M.D.)#######
$ quest6 = 0
$ quest6complete = False
#################QUEST#7(LOLA)#####
$ lola00 = True
$ loladays = 0
$ quest7 = 0
$ quest7start = False
$ quest7balsam = True
$ quest7maslab = True
$ quest7maslab2 = False
$ quest7maslab3 = False
$ quest7thing = False
$ quest7food = False
$ quest7complete = False
$ quest7completefood = False
$ loladates = 0
$ quest7notcooking = True
#######QUEST#8########
$ quest8start00 = False
$ quest8start = False
$ quest8start2 = False
$ quest8start3 = False
$ quest8start4 = False
$ quest8start5 = False
$ quest8complete = False
$ loladressdays = 0
$ lolawhoredays = 0
######QUEST#9#######
$ quest900 = True
$ quest9start = False
$ quest9start2 = False
$ quest9start3 = False
$ quest9start4 = False
$ quest9start5 = False
$ quest9complete = False
$ quest9days = 0
$ quest9days2 = 0
$ lolamovedin = False #(By Default False)
$ emptyroom = True
$ jas_met_lola = False 
#############LOLA DATES#################
$ ldatemarket = True
$ ldatetavern = True
$ ldatebrothel = True
$ ldatestore = True
$ ldatecheapside = True
$ ldatepalace = True
$ lnightacademy = True
$ lnighttavern = True
$ lnightmarket = True
$ lolacomeatnight = False
$ lolawaitsforroom = False
###############################
$ lola_jas_makeover_talk = False #Lola takes Jas for a walk on a leash for the first time.
$ lola_walks_jasmine = False
####QUEST#10 FRUIT STAND#######
$ quest10fail = False
$ quest1000 = True
$ quest10start = False
$ quest10complete = False
$ quest10days = 0
$ fruitstand00 = True
$ standbought = False
$ fruitstandgold = 0
####QUEST#11 DANCING JOB#########
$ quest1100 = True
$ quest11start = False
$ quest11start2 = False
$ quest11start3 = False
$ quest11start4 = False
$ quest11complete = False
$ quest11days = 0
#####QUEST#12 WHORE JOB######
$ quest1200 = True
$ quest12start = False
$ quest12start2 = False
$ quest12start3 = False
$ quest12complete = False
$ quest12days = 0
####QUEST#13 AZALEA#######
$ quest13complete = False
########DREAM_FLAGS#################
$ watched_dream_01 = False
$ watched_dream_02 = False
$ watched_dream_03 = False
$ watched_dream_04 = False

#####################mini game INTRO##########################
show image "04_pt/slavem/mainbg00.jpg"


show image "interface/blackfade.png"
pause.2
scene blkfade
show image "04_pt/slavem/mainbg00.jpg" behind blkfade
hide blkfade with Dissolve(.3)
$ renpy.play('sounds/magic4.ogg')
scene white
pause.02
show magic5
pause.05
scene white
pause.05
pause.05
scene white
pause.05
show image "04_pt/slavem/mainbg00.jpg" 
show whitefade at basicfade, center
show magic at basicfade, center
show magic2 at basicfade2, center
show magic3 at basicfade3, center
show magic4 at basicfade4, center
hide magic
hide magic2
hide magic3
hide magic4
hide whitefade
show heal
stop music fadeout 1
play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
show con1 at right
show ctc7 at right
pause
hide con1
hide ctc7
jump smintro
################################################
label dayone:
###########################################
#######MESELENIOUS FLAGS#########
$ brothelnight = False
###########JOBS#######################
$ jonquest = False
$ jfruits = False
$ jhouse = False
$ jtavern = False
$ jdance = False
$ jwhore = False
$ jsob1 = False
$ jsob2 = False
$ jsob3 = False
$ jsmor1 = False
$ jsmor2 = False
$ jsmor3 = False
$ jptits1 = False
$ jptits2 = False
$ jpslave = False

$ loladaytime = True

$ day +=1
$ daytime = True
if quest2complete:
    $ dayswithoutexercise += 1
if quest4start2:
    $ jafardays += 1
if quest5start3:
    $ balsamdays += 1
if quest5start5:
    $ azaleadays += 1
if lola00 and quest4complete:
    $ loladays += 1
if quest8start2:
    $ loladressdays += 1
if quest8start5:
    $ lolawhoredays += 1
if quest9start:
    $ quest9days += 1
if quest9start3:
    $ quest9days2 += 1
if loladays >= 5 and quest7 == 0:
    $ lola00 = False
    $ lolaworks = renpy.random.randint(1, 2)  
else:
    $ lolaworks = 1
if quest10start:
    $ quest10fail = True
    $ quest10days += 1
if quest10days == 4:
    $ quest10fail = False
if standbought:
    $ fstandmademoney = renpy.random.randint(10, 30)
    $ fruitstandgold = fruitstandgold + fstandmademoney
if quest11start2:
    $ quest11days += 1
if quest12start2:
    $ quest12days += 1
    
$ dahliaworks = renpy.random.randint(1, 2)    
if quest6 == 3:
    $ daintavern = renpy.random.randint(2, 3)
       
$ tired = 0
$ jidle = True
stop music fadeout 1
play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1

scene blkfade
show image "04_pt/slavem/mainbg00.jpg" behind blkfade
if onquest:
    show image "04_pt/slavem/onaquest.png" behind blkfade
hide blkfade with Dissolve(.3)


    
if mtired >= 7:
    $ tired = 1
    ">Jasmine was working hard for many days in a row... She needs to take a break..."
"Day [day]. \nYou have [gold] gold."
if dayswithoutexercise >= 6 and quest2complete and strength >= 1:
    $ strength -= 1
    $ dayswithoutexercise = 0
    ">You did not exercise for many days in a row... \nYou feel your body got a bit weaker."
show rest03 with Dissolve(.3)


label mainmenu:
$ select = renpy.imagemap("04_pt/slavem/mainbg01.png", "04_pt/slavem/mainbg02.png", [
                                           (39, 325, 140, 412, "persona1"),
                                           (93, 446, 236, 552, "home"),
                                           (155, 368, 247, 444, "brothel"),
                                           (309, 371, 400, 512, "shop"),
                                           (407, 316, 519, 396, "market"),
                                           (531, 368, 621, 487, "tavern"),
                                           (693, 357, 774, 441, "school"),
                                           (532, 187, 594, 307, "jpalace"),
                                           (660, 470, 773, 573, "dayend")
                                           ])


    
if select == "dayend":
    jump dayends


if select == "jpalace":
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    $ normalw = False
    $ peasantw = False
    $ tavernw = False
    $ dancew = False
    $ whorew = False
    $ slavew = False
    
    sch4 "This is the royal palace."
    if jidle:
        sch4 "Princess Jasmine...???"
        sch13_2 "................"
        sch4 "*khem*..."
        label jpalace2:    
        menu:         
            sch4 "Err... Please state your business... "
            "-Pick up the whoring permit-" if quest12days >= 2:
                jump audijafar8
            "-Discuss the whore job with Jafar-" if quest12start:
                jump audijafar7
            "-Pick up the dancing permit-" if quest11days >= 1:
                jump audijafar6
            "-Discuss dancing job with Jafar-" if quest11start:
                jump audijafar5
            "-Discuss the wedding parade with Jafar-":
                jump audijafar
            "-Pick up the permit-" if quest9days2 >= 2 and quest9start3:
                jump quest9start3
            
            "-Discuss the house remodeling-" if quest9start2:
                jump quest9start2
            "-Discuss the \"Red Phoenix\" with Jafar-" if quest4start:
                jump audijafar3
            "-Pick up the permit-" if jafardays >= 3 and quest4start2:
                jump audijafar4
            "-Nevermind-":
                sch4 "Very well..."
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump mainmenu
    else:
        menu:
            sch4 "Please state your business... "
            "-Discuss dancing job with Jafar-" if quest11start:
                jump audijafar5
            "-Pick up the dancing permit-" if quest11days >= 1:
                jump audijafar6
            "-Discuss the wedding parade with Jafar-": 
                jump audijafar2
            "-Pick up the permit-" if quest9days2 >= 2 and quest9start3:
                jump quest9start3
            
            "-Discuss the house remodeling-" if quest9start2:
                jump quest9start2
            "-Discuss the \"Red Phoenix\" with Jafar-" if quest4start:
                jump audijafar3
            "-Nevermind-":
                sch4 "Oh, I see..."
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump mainmenu
        

###cheapside###
if select == "persona1":
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    label cheapside: 
                menu:
                    sch7 "Welcome to the cheapside, master. \nCoin for the poor?" 
                    "\"I have the permit!\"" if quest9start4:
                        jump quest9start4
                    "-About house remodeling...-" if quest9days >= 1 and quest9start:
                        jump quest9start
                    "-Quest: [quest9]-" if quest4complete and quest900:
                        jump quest8start6
                    "-Give fruits to the homeless crocus-" if quest1start2 and jidle:
                        sch7 "The kind master brought poor crocus food?"
                        show image "04_pt/slavem/masteritem.png" with Dissolve(.3)
                        show image "04_pt/slavem/boxfruits.png" with moveinleft
                        ">You hand over the fruits to the homeless old man."
                        hide image "04_pt/slavem/boxfruits.png" with moveoutright
                        hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                        ">He quickly hides them under a very ragget piece of cloth."
                        ">Doesn't look like his is hungry at all."
                        sch7 "{size=-4}(I will sell these back to balsam later...){/size}"
                        sch7 "*khem* I mean, poor crocus will eat the fruits later..."
                        sch7 "Thank you for bringing the food, kind master."
                        sch7 "hm..."
                        sch7 "The master's slave-girl has pretty eyes..."
                        show image "04_pt/jasmine/outfit/jas15.png" at right with Dissolve(.3)
                        j "Slave-girl?! How dare you, you filthy commoner!?"
                        hide image "04_pt/jasmine/outfit/jas15.png" at right with Dissolve(.3)
                        sch7 "And she's quite feisty too I see..."
                        sch7 "Hm..."
                        sch7 "Maybe the most kind of all masters could do poor, insignificant and lonely crocus one last favor?"
                        menu:
                            sch7 "Could master make his slave-girl show crocus her face?"
                            "-I brought you the food. That's enough-":
                                show image "04_pt/jasmine/outfit/jas15.png" at right with Dissolve(.3)
                                j "My thoughts exactly!"
                                hide image "04_pt/jasmine/outfit/jas15.png" at right with Dissolve(.3)
                                sch7 "Was it too much to ask...? My apologies, kind master."
                                sch7 "It's just that poor old crocus is so lonely sometimes..."
                            "-Take off your veil, girl-":
                                show image "04_pt/jasmine/outfit/jas15.png" at right with Dissolve(.3)
                                j "\"Girl\"? How dare you to address me in this manner?!"
                                j "......."
                                hide image "04_pt/jasmine/outfit/jas15.png" at right with Dissolve(.3)
                                sch7 "....."
                                show image "04_pt/jasmine/outfit/jas15.png" at right with Dissolve(.3)
                                j "er... Oh, well, who cares..."
                                j "There... have a feast for your eyes, you old bum."
                                show image "04_pt/jasmine/outfit/jas16.png" at right with Dissolve(.3)
                                hide image "04_pt/jasmine/outfit/jas15.png" 
                                show con1 at right
                                show ctc7 at right
                                pause
                                hide con1
                                hide ctc7
                                hide image "04_pt/jasmine/outfit/jas16.png" at right with Dissolve(.3)
                                sch8 "Oh! Oh! And what a feast that is!"
                                sch8 "Master's slave-girl is a beauty!"
                                show image "04_pt/jasmine/outfit/jas16.png" at right with Dissolve(.3)
                                j "Tsk..."
                                hide image "04_pt/jasmine/outfit/jas16.png" at right with Dissolve(.3)
                        
                        sch7 "Well, a deal is a deal. The kind master shall have my full cooperation from now on..."
                        hide image "04_pt/slavem/onaquest.png" with Dissolve(.3)
                        $ quest1complete = True
                        $ quest1start2 = False
                        $ onquest = False
                        $ renpy.play('sounds/win2.mp3')                        
                        show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
                        show con1 at right
                        show ctc7 at right
                        pause
                        hide con1
                        hide ctc7
                        "Congratulations! You just completed your first quest."
                        "From now on Princess Jasmine can make money by cleaning houses in the cheapside."
                        hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
                        hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                        ">It's getting late. You decide to head home."
                        jump dayends
                    "-Quest: [quest1]-" if peasant and quest100:
                        sch7 "Master is looking to employ his slave-girl?"
                        sch7 "Well, of course, poor crocus would be happy to assist the kind master."
                        sch7 "Poor old crocus knows everything about everyone around these parts."
                        sch7 "He could point the master directly to the houses currently looking to hire help."
                        sch7 "yes... poor crocus... he want's nothing else but to help the kind master..."
                        sch7 "But poor crocus is so hungry..."
                        menu:
                            sch7 "Could the kind master bring poor crocus something to eat first?"
                            "\"Alright, you lazy bum.\"":
                                sch7 "Thank you, kind master. Poor crocus will just wait here then."
                                $ quest1start = True
                                $ quest100 = False
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
                            "\"Not right now.\"":
                                sch7 "Oh... Crocus understands... \nThe kind master is a busy man..."
                                jump cheapside
                    "-Make Jasmine clean houses-" if quest1complete and jidle:   
                        if tired >= 2:
                            "Jasmine is too tired for that."
                            jump cheapside
                        else:
                            if peasant:
                                hide image "04_pt/slavem/bld.png" with Dissolve(.3)     
                                show cleaning with Dissolve(.3)
                                hide rest03
                                ">Jasmine tries to clean as many houses as she can..."
                                $ jhouse = True
                                $ jidle = False 
                                jump mainmenu                         
                                   
                            else:
                                "You need to buy a simple peasant robe before Jasmine can work here."
                                jump cheapside
                    "-Give crocus a few coins-" if gold >= 15 and peasant:
                        jump crocuscoins                
#                    "Talk to Crocus.":
#                        sch7 "Master is to kind to spent his time on poor useless Crocus."
#                        sch7 "This is residential area of Agarabah's lower class, also known as \"the cheapside\"."
#                        sch7 "Crocus lives here, on the street."
#                        sch7 "Yes, Crocus have no home and very a few possessions, but Crocus is good at listening..."
#                        sch7 "If Master wants to know what people on the streets are talking about, then Crocus could help."
#                        sch7 "Master could also find a job for his slave-girl here."
#                        jump cheapside
                    "-Leave-":
                        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                        jump mainmenu
elif select == "home":
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    $ renpy.play('sounds/door.mp3')
    label house:   
    menu:
        "Your home..."      
        
        "-Quest info-":
            jump questinfo    
        "-Personal requests-":
            label prequests2:
            menu:
                "You can order Princess Jasmine to..."
                                
                "...Expose her tits to complete strangers." if jidle:            
                    menu:
                        "-Wear a veil-":
                            if obedience >= 4:
                                if courage >= 3: 
                                    show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
                                    j "Fine... I'll do it..."
                                    hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
                                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)     
                                    show btits with Dissolve(.3)
                                    hide rest03
                                    ">Jasmine agrees to walk around the streets and expose her bare her tits before the commoners."
                                    $ jptits1 = True
                                    $ jidle = False 
                                    jump mainmenu
                                        
                                else:
                                    ">Jasmine agrees to expose her tits to complete strangers on the street. But her moral standards are too high to actually do that..."
                                    jump prequests2
                        
                            else:
                                show image "04_pt/jasmine/outfit/jas02.png" at right with Dissolve(.3)
                                j "You want me to do what?!"
                                show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
                                hide image "04_pt/jasmine/outfit/jas02.png" 
                                j "Forget it. I'm not doing that."
                                hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
                                ">Jasmine refuses to expose herself to complete strangers."
                                jump prequests2
                            
                        "-Do not wear a veil-": 
                            
                            if obedience >= 6:                
                                if courage >= 6:
                                    show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
                                    j "Fine... I'll do it..."
                                    hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
                                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                                    show btits2 with Dissolve(.3)
                                    hide rest03
                                    $ jptits2 = True
                                    $ jidle = False
                                    jump mainmenu                                  
                                else:
                                    ">Jasmine agrees to expose her tits to complete strangers on the street. But her moral standards are too high to actually do that..."
                                    jump prequests2
                            else:
                                show image "04_pt/jasmine/outfit/jas02.png" at right with Dissolve(.3)
                                j "You want me to do what?!"
                                show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
                                hide image "04_pt/jasmine/outfit/jas02.png" 
                                j "Forget it. I'm not doing that."
                                hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
                                "Jasmine refuses to expose herself to complete strangers."
                                jump prequests2
                                    
                        "-Cancel-":
                            jump prequests2
                            
                        
                "...Be lead around on a leash." if jidle:
                    if slavegirl:                        
                        if obedience >= 10:                
                            if courage >= 9:
                                $ jpslave = True
                                $ jidle = False
                                jump dayends
                            else:
                                "Jasmine agrees to follow you around Agrabah on a leash while wearing embarrassing outfit."
                                "But her moral standards are too high to actually do that..."
                                jump prequests2
                        else:
                            show image "04_pt/jasmine/outfit/jas02.png" at right with Dissolve(.3)
                            j "You want me to do what?!"
                            show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
                            hide image "04_pt/jasmine/outfit/jas02.png" 
                            j "Forget it. I'm not doing that."
                            hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
                            ">Jasmine refuses to be lead around the city on a leash."
                            jump prequests2
                    else:
                        ">You need to buy a slave-girl outfit in the shop first."
                        jump prequests2       
                "{color=#858585}...(LOCKED)...{/color}" if not lolamovedin:
                    ">You need to complete a correlating in-game quest to unlock this option."
                    jump prequests2
                "...Let Lola lead Jasmine on a leash." if lolamovedin and jidle:
                    if obedience >= 10 and courage >= 9:
                        if not lola_jas_makeover_talk:
                            play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1  #LOLA
                            show blkfade with d5
                            pause.5
                            hide blkfade with d5
                            lola[11] "Are you taking her for a walk? Can I do it? Can I do it?"
                            lola[11] "Please, pretty please?!"
                            jas[36] "What?!"
                            m "I don't think that's a good idea, Lola..."
                            lola[15] "Please... *sob!*"
                            m "well alright, but be careful."
                            jas[38] "Tsk..."
                            lola[71] "Yay!"
                            lola[71] "But first, she needs a makeover!"
                            jas[36] "What?!"
                            lola[71] "Oh, come on, this is gonna be fun!"
                            show blkfade with d5
                            show ctc7 at right
                            pause 
                            hide ctc7
                            hide blkfade with d5
                            lola[71] "Tad-dah!"
                            jas[67] "You can't be serious..."
                            lola[71] "I think you look hot."
                            jas[67] "I'm... naked. What kind of makeover is this?"
                            lola[13] "Hm....?"
                            lola[13] "Are you scared, or embarrassed, or what...?"
                            lola[13] "If it would make you feel any better..."
                            lola[13] "I could go like..."
                            lola[72] "This!"
                            jas[67] ".........."
                            m "Lola, no..."
                            lola[72] "I know, I know..."
                            lola[12] "You're no fun, old man..."
                            jas[67] ".........."
                            lola[71] "So? Ready to go?"
                            jas[67] "I suppose.........."
                            m "Have a fun day, girls..."
                            hide image "04_pt/slavem/bld.png" with Dissolve(.3)     
                            show leash_lola with Dissolve(.3)
                            hide rest03
                            $ lola_jas_makeover_talk = True
                            $ lola_walks_jasmine = True
                            $ jidle = False 
                            play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                            jump mainmenu

                        else:
                            lola[71] "Yay! Let's go!"
                            jas[67] "Alright, alright, you wicked child..."
                            lola[71] "Meh-he-he!"
                            hide image "04_pt/slavem/bld.png" with Dissolve(.3)     
                            show leash_lola with Dissolve(.3)
                            hide rest03
                            $ lola_walks_jasmine = True
                            $ jidle = False 
                            jump mainmenu
                    else:
                        show image "04_pt/jasmine/outfit/jas02.png" at right with Dissolve(.3)
                        j "You want me to do what?!"
                        show lola_f 6 at left with d3
                        sch1000 "Oh, come on! It's gonna be fun!"
                        show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
                        hide image "04_pt/jasmine/outfit/jas02.png" 
                        j "Out of question!"
                        show lola_f 4 at left with d3
                        sch1000 ".........."
                        hide lola with d3
                        hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
                        ">Jasmine refuses to be lead around the city on a leash by lola."
                        jump prequests2

                "Info.":
                    "Personal requests are the best way to lower the people's opinion about their precious Princess."
                    "You could order her to walk around the market square and randomly expose her breasts to complete strangers."
                    "Doing so without the veil on will increase the chances of success but it'll require higher levels of obedience and lower levels of morality."
                    "You can also lead her around the city on a leash. This will require the purchase of a special outfit and extremely high levels of obedience."
                    jump prequests2
                "Cheat.":
                    jump cheats_pt
                    
                "Cancel.":
                    jump house
        "-Status-":  
            show image "04_pt/status/statusbg.png" with Dissolve(.2)
            
            if courage >= 0 and courage <= 3:
                show image "04_pt/status/statusj1.png" with Dissolve(.2)
            elif courage >= 4 and courage <= 6:
                show image "04_pt/status/statusj2.png" with Dissolve(.2)
            elif courage >= 7 and courage <= 9:
                show image "04_pt/status/statusj3.png" with Dissolve(.2)
            elif courage == 10:
                show image "04_pt/status/statusj4.png" with Dissolve(.2)
            
            
            if tired >= 0 and tired < 1:                
                show image "04_pt/status/sen1.png" with Dissolve(.2)
            elif tired >= 1 and tired < 2:
                show image "04_pt/status/sen2.png" with Dissolve(.2)
            elif tired >= 2 and tired < 3:
                show image "04_pt/status/sen3.png" with Dissolve(.2)
            
            if obedience == 0:
                show image "04_pt/status/sob00.png" with Dissolve(.2)
            elif obedience == 1:
                show image "04_pt/status/sob01.png" with Dissolve(.2)          
            elif obedience == 2:
                show image "04_pt/status/sob02.png" with Dissolve(.2)
            elif obedience == 3:
                show image "04_pt/status/sob03.png" with Dissolve(.2)
            elif obedience == 4:
                show image "04_pt/status/sob04.png" with Dissolve(.2)
            elif obedience == 5:
                show image "04_pt/status/sob05.png" with Dissolve(.2)
            elif obedience == 6:
                show image "04_pt/status/sob06.png" with Dissolve(.2)
            elif obedience == 7:
                show image "04_pt/status/sob07.png" with Dissolve(.2)
            elif obedience == 8:
                show image "04_pt/status/sob08.png" with Dissolve(.2)
            elif obedience == 9:   
                show image "04_pt/status/sob09.png" with Dissolve(.2)
            elif obedience >= 10:
                show image "04_pt/status/sob10.png" with Dissolve(.2)
            
            
            if courage == 0:
                show image "04_pt/status/smor00.png" with Dissolve(.2)
            elif courage == 1:
                show image "04_pt/status/smor01.png" with Dissolve(.2)          
            elif courage == 2:
                show image "04_pt/status/smor02.png" with Dissolve(.2)
            elif courage == 3:
                show image "04_pt/status/smor03.png" with Dissolve(.2)
            elif courage == 4:
                show image "04_pt/status/smor04.png" with Dissolve(.2)
            elif courage == 5:
                show image "04_pt/status/smor05.png" with Dissolve(.2)
            elif courage == 6:
                show image "04_pt/status/smor06.png" with Dissolve(.2)
            elif courage == 7:
                show image "04_pt/status/smor07.png" with Dissolve(.2)
            elif courage == 8:
                show image "04_pt/status/smor08.png" with Dissolve(.2)
            elif courage == 9:   
                show image "04_pt/status/smor09.png" with Dissolve(.2)
            elif courage >= 10:
                show image "04_pt/status/smor10.png" with Dissolve(.2)
                
            show image "04_pt/status/smon.png" with Dissolve(.2)
            
            show screen gold_scr #Отображаем золото, сам экран описан в самом низу кода
            
            
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            
            hide screen gold_scr #Отображаем золото, сам экран описан в самом низу кода
            
            show image "interface/blackfade.png" with Dissolve(.3)
            hide image "04_pt/status/statusbg.png" 
            hide image "04_pt/status/statusj1.png" 
            hide image "04_pt/status/sen1.png"
            hide image "04_pt/status/sen2.png" 
            hide image "04_pt/status/sen3.png" 
            
            hide image "04_pt/status/smor00.png" 
            hide image "04_pt/status/smor01.png"
            hide image "04_pt/status/smor02.png"
            hide image "04_pt/status/smor03.png"
            hide image "04_pt/status/smor04.png"
            hide image "04_pt/status/smor05.png"
            hide image "04_pt/status/smor06.png"
            hide image "04_pt/status/smor07.png"
            hide image "04_pt/status/smor08.png"
            hide image "04_pt/status/smor09.png"
            hide image "04_pt/status/smor10.png"
            
            hide image "04_pt/status/sob00.png" 
            hide image "04_pt/status/sob01.png" 
            hide image "04_pt/status/sob02.png" 
            hide image "04_pt/status/sob03.png" 
            hide image "04_pt/status/sob04.png" 
            hide image "04_pt/status/sob05.png" 
            hide image "04_pt/status/sob06.png" 
            hide image "04_pt/status/sob07.png" 
            hide image "04_pt/status/sob08.png" 
            hide image "04_pt/status/sob09.png" 
            hide image "04_pt/status/sob10.png" 
            
            hide image "04_pt/status/smon.png"
            
            hide image "04_pt/status/statusj4.png" 
            hide image "04_pt/status/statusj3.png"
            hide image "04_pt/status/statusj2.png"
            hide image "04_pt/status/statusj1.png"
            
            hide image "interface/blackfade.png" with Dissolve(.3)
            jump house
        "-Leave-":   
            $ renpy.play('sounds/door2.mp3')
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            jump mainmenu
            
    
###BROTHEL#####
elif select == "brothel":
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    if quest4complete:
        $ renpy.play('sounds/door.mp3')
        jump brothelreopned
    else:
        ">The Brothel seems to be closed."
        ">There is a notice on the front door: \"Closed by Order of the Sultan.\"."
        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
        jump mainmenu
#####SHOP#######
elif select == "shop":
    $ renpy.play('sounds/door.mp3')
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    label store2:
    if meetlola00 and quest2complete:
        show blkfade with d5
        pause.3
        hide blkfade with d5
        play music "music/silly_fun_loop.MP3" fadein 1 fadeout 1 #LOLA_THEME
        lola[0] "These designs are amazing, Azalea!"
        aza[1] "Well, thank you."
        lola[1] "Can I try one of these on?"
        aza[1] "Maybe next time."
        aza[3] "Although, I'm not sure you're old enough."
        lola[2] "Azalea!"
        aza[1] "Te-he-he. I'm just teasing you..."
        lola[3] "You..."
        aza[1] "Here are the dresses your mother ordered."
        lola[0] "Great. Thanks."
        lola[0] "I better hurry up now."
        aza[4] "Say \"hi\" to your mom from me."
        lola[0] "I will! See ya!"
        lola[5] "??!"
        show image "interface/white.jpg"
        with hpunch
        pause.3
        hide image "interface/white.jpg"
        ">The flamboyant young girl bumped into you."
        lola[4] "Ouch!"
        lola[4] "Sorry, mister."
        menu:
            "\"That's alright. No harm done.\"":
                lola[6] "Te-he-he! I'm sorry."
                lola[0] "Alright, Azalea, I'll see you later!"
                aza[1] "Take care now, girl."
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN THEME
            "-(Help her get up)-":
                lola[8] "Thank you...."
                lola[7] "........"
                lola[0] "Bye, Azalea..."
                aza[1] "See ya!"
                lola[7] "......."
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN THEME
            "\"Youngsters!!! Learn to respect the elderly!\"":
                stop music fadeout 2
                lola[9] "What? I'm sorry..."
                lola[10] "I just..."
                lola[10] "I have to go, excuse me!"
                ">The girl leaves in a hurry."
                aza[5] "Hey, what's the matter with you, old man? Snapping at the poor girl like that..."
                aza[1] "Oh, well, she'll live."
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN THEME
            "-(Stare at her with hatred)-":
                stop music fadeout 2
                lola[5] "..........?"
                lola[9] "I.... I'm so s-sorry..."
                lola[9] "Are you alright, mister?"
                lola[9] "I.... em... better go now."
                lola[9] "Bye, Azalea."
                aza[1] "Have a nice day, kiddo."
                lola[2] "Hey, don't call me \"kiddo\"! I'm almost as old as you are..."
                aza[3] "Whatever you say, kiddo..."
                lola[3] "...."
                ">The girl leaves."
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN THEME

        $ meetlola00 = False
        jump store2
    else:
        if storecomplete:
            aza[7] "Oh, it's you! Gimme a sec! Let me take this silly thing off."
            show blkfade with d3
            pause.5
            hide blkfade with d3
            label azalea_topless:
            aza[12] "Welcome to my store!"
            aza[12] "Only the best things for my favorite customer."   
        else:
            aza[1] "Something exotic or something trivial? No matter what, I have it all."
        menu:
            "-Pick up lola's dress-" if quest8start2 and loladressdays >= 3:
                jump quest8start2
            "-Order a dress for Lola-" if quest8start:
                jump quest8startass
            "-Pick up the dress-" if azaleadays >= 3 and quest5start5:
                jump pickupdress1
            "-Deliver the materials-" if quest5start4:
                jump delivermaterials
            "-Give Azalea Iris's dress designs-" if quest5start:
                show image "04_pt/slavem/masteritem.png" with moveinright
                show image "04_pt/slavem/boxirissketch.png" with moveinleft
                ">You hand over the sketches Iris gave you to Azalea."
                hide image "04_pt/slavem/boxirissketch.png" with moveoutright
                hide image "04_pt/slavem/masteritem.png" with moveoutleft
                aza[1] "What is this? A dress design?"
                aza[1] "Iris gave this to you?"
                aza[1] "This is one skimpy dress..."
                aza[1] "I love it!"
                aza[1] "Yes, I could create a dress based on these sketches..."
                aza[1] "As soon as you get me the required materials..."
                aza[1] "What? You didn't expect this to be too easy, did you?"
                aza[1] "Here is a list of things I will need..."
                aza[1] "As soon as I have the required materials I can start working..."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxlistmaterials.png" with moveinright
                ">You received a list of required materials..."
                hide image "04_pt/slavem/boxlistmaterials.png" with Dissolve(.4)
                hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                $ quest5start = False
                $ quest5start2 = True
                $ renpy.play('sounds/door2.mp3')
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump mainmenu
            "-Pay for the repairs-" if storestarted2:
                jump toplesspay
            "Quest: [quest13]." if storetopless >= 2 and storestarted:
                jump toplessstart
            "-Buy clothes-":
                jump buyingdresses
            "-Talk to Azalea-":
                if storecomplete:
                    aza[12] "You can... em... find all sorts of outfits in my store."
                    aza[12] "Hm...?"
                    aza[12] "I designed Everything you see here myself, meaning that every single item is of a topnotch quality." 
                    aza[12] "And quality does not come cheap, you understand that, don't you?"
                    aza[10] "Would stop staring at my breasts?!"
                    aza[2] "He-he...I'm kidding, look all you want."
                    aza[9] "But, you know, don't forget to buy something as well..."
                    jump azalea_topless
                else:
                    aza[1] "You can find all sorts of outfits for sale in my store. But my specialty are slave-girl garments."
                    aza[1] "I designed Everything you see here myself, meaning that every single item is of a topnotch quality." 
                    aza[1] "And quality does not come cheap, you understand that, don't you?"
                    aza[1] "Take a look around and let me know if you find something you like..."
                    jump store2
            "-Leave-":
                $ renpy.play('sounds/door2.mp3')
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump mainmenu
#############BUYING DRESSES#################
        label buyingdresses:
            show image "04_pt/slavem/shop01.png" with Dissolve(.3)
            if outfits >= 5:
                "You already own every single outfit this shop had to offer."
                hide image "04_pt/slavem/shop01.png" with Dissolve(.3)
                jump store2
                
            else: 
                label store3:
                $ select = renpy.imagemap("04_pt/slavem/shop01.png", "04_pt/slavem/shop02.png", [
                                               (74, 30, 267, 295, "peasant"),
                                               (320, 43, 491, 289, "tavern"),
                                               (526, 43, 693, 296, "dance"),
                                               (86, 296, 279, 550, "whore"),
                                               (313, 300, 490, 548, "slave"),
                                               (519, 302, 721, 557, "leave"),
                                               ])
                if select == "peasant":                    
                    if peasant:
                        "You already own this kind of dress."
                        jump store3
                    else:                        
                        menu:                            
                            "You currently have [gold] gold. \nWould you like to buy a simple peasant robe for 10 gold?"
                            "-Buy-":
                                if gold >= 10:
                                    $ gold -=10
                                    ">You bought one peasant robe."
                                    $ outfits +=1
                                    $ peasant = True
                                    jump store3                            
                                else:
                                    "You don't have enough gold to purchase this."
                                    jump store3
                            "-Do not buy-":
                                jump store3
                if select == "tavern":
                    if taverngirl:
                        "You already own this kind of dress."
                        jump store3
                    else:
                        menu:
                            "You currently have [gold] gold. \nWould you like to buy a \"tavern wench\" outfit for 70 gold?"                        
                            "-Buy-":                    
                                if gold >= 70:                                
                                    $ gold -=70
                                    ">You bought one Tavern girl outfit."
                                    $ outfits +=1
                                    $ taverngirl = True
                                    jump store3
                                else:
                                    ">You don't have enough gold to purchase this."
                                    jump store3
                            "-Do not buy-":
                                jump store3
                if select == "dance":
                    if dancer:
                        "You already own this kind of dress."
                        jump store3
                    else:
                        menu:
                            "You currently have [gold] gold. \nWould you like to buy a dacer-girl outfit for 150 gold?" 
                            "-Buy-":                      
                                if gold >= 150:                                    
                                    $ gold -=150
                                    ">You bought one Dancer attire."
                                    $ outfits +=1
                                    $ dancer = True
                                    jump store3
                                else:
                                    ">You don't have enough gold to purchase this."
                                    jump store3
                                 
                            "-Do not buy-":
                                jump store3
                if select == "whore":     
                    if whore:                        
                        "You already own this kind of dress."
                        jump store3
                    else:
                        menu:
                            "You currently have [gold] gold. \nWould you like to buy a Whore's outfit for 200 gold??" 
                            "buy":                                                  
                                if gold >= 200:
                                    $ gold -=200
                                    "You bought Whore's outfit."
                                    $ outfits +=1
                                    $ whore = True
                                    jump store3
                                else:
                                    "You don't have enough gold to purchase this."
                                    jump store3
                                              
                         
                            "do not buy.":
                                jump store3
                            
                if select == "slave":
                    if slavegirl:
                        "You already own this kind of dress."
                        jump store3
                    else:
                        menu:
                            "You currently have [gold] gold. \nWould you like to buy a royal slave outfit with a leash for 300 gold?"
                            "-Buy-":                        
                                if gold >= 300:                        
                                    $ gold -=300
                                    ">You bought one Slave-girl attire."
                                    $ outfits +=1
                                    $ slavegirl = True
                                    jump store3
                                else:
                                    "You don't have enough gold to purchase this."
                                    jump store3   
                            "-Do not buy-":
                                jump store3
                            
                if select == "leave":
                    hide image "04_pt/slavem/shop01.png" with Dissolve(.3)
                    jump store2
                    #################MARKET################
elif select == "market":
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    label market2:
        menu:
            sch5 "Welcome to the market, friend! \n*spit*"
            "-Buy a fruit stand-" if quest10complete and fruitstand00:
                jump fruitstand
            "-Quest: [quest10]-" if quest2complete and quest1000:
                jump quest10starts
            "-Quest [quest2]-" if quest200 and quest1complete:
                jump startquest2
            "-Pose as a rich customer-" if quest10days == 1:
                jump quest10day1
            "-Pose as a rich customer-" if quest10days == 2:
                jump quest10day2
            "-Pose as a rich customer-" if quest10days == 3:
                jump quest10day3
            "-Pose as a rich customer-" if quest10days == 4:
                jump quest10day4
            "-Pose as a rich customer-" if quest10days == 5:
                jump quest10day5
            "-Buy something nice for lily-" if quest7start and quest7balsam:
                jump buythinglily
            #"-Talk about Iris-" if quest6 == 1:
                #jump mdisneace
            "-Pick up the materials-" if balsamdays >= 2 and quest5start3:
                jump pickmaterials
            "-Buy the materials-" if quest5start2:
                jump buymaterials
            "-Talk about last night-" if quest2start3:
                jump aboutlastnight
            "-Sell fruits on the market-" if jidle:                     
                if peasant: 
                    if tired >= 2:
                        "Jasmine is too tired for that."
                        jump market2
                    else:
                        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                        hide rest03
                        show banana03 with Dissolve(.3)
                        ">Jasmine tries to sell as many fruits as she can..."                    
                        $ jfruits = True
                        $ jidle = False                    
                        jump mainmenu          
                else:
                    ">You need to buy a simple peasant robe before Jasmine could start working here."
                    jump market2
            "-Collect from your fruit stand-" if standbought and fruitstandgold >= 1:
                $ gold = gold + fruitstandgold
                sch5 "Here is your share. ([fruitstandgold] gold.)"
                $ fruitstandgold = 0
                jump market2
               
                
            "-Talk to Balsam-":  
                if quest1start:
                    if gold >= 50:
                        jump stupidfruits
                    else:
                        sch5 "You want to buy some fruits?"
                        sch5 "Of course, of course, only the best fruits for you, my friend!"
                        sch5 "That will be 50 gold coins."
                        ">You don't have enough gold."
                        jump market2
                    
                elif quest6 == 1:
                    jump mdisneace
                else:
                    jump balsam_talk
            "-Leave-":
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump mainmenu
           
    

###SCHOOL###
elif select == "school":    
    $ renpy.play('sounds/door.mp3')
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    label academy:
            menu:     
                ros[1] "Welcome to the \"JSGA\". \nThe Jafar's Slave-Girl Academy..."
                "-Make Jasmine take classes-" if jidle:            
                    if gold >= 50: 
                        if tired >= 1:
                            ">Jasmine is too tired for that."
                            jump academy
                        else:
                            menu:                    
                                "You have [gold] gold.\nWhat class would you want Princess Jasmine to attend?"
                                "-Obedience for beginners-":                    
                                    if obedience >= 10:                                
                                        ros[1] "Student Jasmine is completely obedient."
                                        ros[1] "She graduated our academy with honors, her devotion to her master is unparalleled."
                                        jump academy
                                    elif obedience >= 3 and obedience < 10:
                                        ros[1] "Your slave-girl already mastered this class. I suggest that you move on to the next one..."
                                        jump academy
                                    elif obedience >= 0 and obedience < 3:                            
                                        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                                        show obedience01b with Dissolve(.3)
                                        hide rest03
                                        ">Princess jasmine attends the \"Self-hatred 101\" class."
                                        $ gold -=50
                                        $ jsob1 = True
                                        $ jidle = False                    
                                        jump mainmenu         
                                "-advanced Obedience classes-":
                                    if gold >= 100:
                                        if obedience >= 10:
                                            ros[1] "Student Jasmine is completely obedient."
                                            ros[1] "She graduated our academy with honors, her devotion to her master is unparalleled."
                                            jump academy
                                        elif obedience >= 0 and obedience < 3:
                                            ros[1] "Hm... Doesn't look like she can take this one yet. I suggest that you try something less advanced."
                                            jump academy                                 
                                        elif obedience >= 6 and obedience < 10:
                                            ros[1] "Your slave-girl already mastered this class. I suggest that you move on to the next one..."
                                            jump academy
                                        elif obedience >= 3 and obedience < 6:                                
                                            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                                            show obedience02 with Dissolve(.3)
                                            hide rest03
                                            "Princess jasmine attends the \"Self-hatred 102\" class."
                                            $ gold -=100
                                            $ jsob2 = True
                                            $ jidle = False                    
                                            jump mainmenu    
                                    else:
                                        "You don't have enough gold to pay the tuition."
                                        jump academy
                                "-Obedience class for experts-":
                                    if gold >= 200:
                                        if obedience >= 10:
                                            ros[1] "Student Jasmine is completely obedient."
                                            ros[1] "She graduated our academy with honors, her devotion to her master is unparalleled."
                                            jump academy
                                        elif obedience >= 0 and obedience < 6:
                                            ros[1] "Hm... Doesn't look like she can take this one yet. I suggest that you try something less advanced."
                                            jump academy            
                                        elif obedience >= 6 and obedience < 10:
                                            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                                            show obedience03 with Dissolve(.3)
                                            hide rest03
                                            ">Princess jasmine attends the \"Self-hatred 103\" class."
                                            $ gold -=200
                                            $ jsob3 = True
                                            $ jidle = False                    
                                            jump mainmenu    
                                    else:
                                        "You don't have enough gold to pay the tuition."
                                        jump academy
                                "-Morality class for beginners-":                        
                                    if courage >= 10:
                                        ros[1] "The Student jasmine couldn't possibly have any lower moral standards than she already has."
                                        ros[1] "She graduated our academy with honors, and now has no shame whatsoever."
                                        jump academy
                                    elif courage >= 3 and courage < 10:
                                        ros[1] "Your slave-girl already mastered this class. I suggest that you move on to the next one..."
                                        jump academy
                                    elif courage >= 0 and courage < 3 and obedience >= 3:    
                                        hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                                        show courage with Dissolve(.3)
                                        hide rest03
                                        ">Princess jasmine attends the \"How to have no shame\" class."
                                        $ gold -=50
                                        $ jsmor1 = True
                                        $ jidle = False                    
                                        jump mainmenu 
                                    elif courage >= 0 and courage < 3:
                                        ros[1] "To attend this class your slave-girl need to complete \"Obedience for beginners\" first."
                                        jump academy
                                "-Advanced Morality class-":
                                    if gold >= 100:
                                        if courage >= 10:                            
                                            ros[1] "Student jasmine couldn't possibly have any lower moral standards than she already has."
                                            ros[1] "She graduated our academy with honors and now has no shame whatsoever."
                                            jump academy     
                                        elif courage >= 0 and courage < 3:
                                            ros[1] "Hm... Doesn't look like she can take this one yet. I suggest that you try something less advanced."
                                            jump academy 
                                        elif courage >= 6 and courage < 10:
                                            ros[1] "Your slave-girl already mastered this class. I suggest that you move on to the next one..."
                                            jump academy
                                        elif courage >= 3 and courage < 6: 
                                            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                                            show courage with Dissolve(.3)
                                            hide rest03
                                            ">Princess jasmine attends the \"Tricks to tame your embarrassment\" class."
                                            $ gold -=100
                                            $ jsmor2 = True
                                            $ jidle = False                    
                                            jump mainmenu 
                                    else:
                                        "You don't have enough gold to pay the tuition."
                                        jump academy
                                            
                                "-Morality class for experts-":
                                    if gold >= 200:
                                        if courage >= 10:                            
                                            ros[1] "Student jasmine couldn't possibly have any lower moral standards than she already has."
                                            ros[1] "She graduated our academy with honors, and now has no shame whatsoever."
                                            jump academy      
                                        elif courage >= 0 and courage < 6:
                                            ros[1] "Hm... Doesn't look like she can take this one yet. I suggest that you try something less advanced."
                                            jump academy     
                                        elif courage >= 6 and courage < 10:   
                                            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                                            show courage with Dissolve(.3)
                                            hide rest03
                                            "Princess jasmine attends the \"Shame is a lie\" class."
                                            $ gold -=200
                                            $ jsmor3 = True
                                            $ jidle = False                    
                                            jump mainmenu
                                    else:
                                        ">You don't have enough gold to pay the tuition."
                                        jump academy               
                                                
                                "-Cancel-":
                                    jump academy
                    else:
                        ">You don't have enough gold to pay the tuition."
                        jump academy
                "-Inquire about tuition prices-":
                    ros[1] "Tuition prices are as follows: 50 gold coins for the beginner classes."
                    ros[1] "100 gold coins to take an advanced class."
                    ros[1] "And 200 gold coins to take an expert class."
                    ">You currently have [gold] gold coins."
                    jump academy
                "-Talk to rose-":
                    jump rose_talk 
                "-Leave-":
                    $ renpy.play('sounds/door2.mp3')
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                    jump mainmenu
###TAVERN###
if select == "tavern":
    $ renpy.play('sounds/door.mp3')
    show image "04_pt/slavem/bld.png" with Dissolve(.3)
    label tavern2:
        if quest2start5:
            jump wasscared
        else:            
            menu:
                sch6 "Welcome to \"The blue bull\" tavern...\n*spit*"
                "-Bring jasmine to Maslab-" if quest11start4 and jidle and dancer:
                    jump quest11start4
                "-Give Maslab the dancing permit-" if quest11start3:
                    jump quest11start3
                "Quest: [quest11]." if quest4complete and quest1100 and quest3complete and obedience >= 6 and courage >= 5:
                    if maslabfriendship >= 2:
                        jump quest1100
                    else:
                        jump notafriendyet
                "-Buy something delicious-" if quest7completefood and quest7notcooking and not quest7food:
                    if quest7food:
                        "You have one portion of that food already."
                        jump tavern2
                    else:
                        jump food4lily2
                "-Buy something delicious-" if quest7start and quest7maslab:
                    jump food4lily
                "-Finish the waitress training-" if quest3start4 and jidle:
                    jump waitressfinish
                "-Take waitress training again-" if quest3start3 and jidle:
                    jump waitresstrain2
                "-Take waitress training-" if quest3start2 and jidle:
                    if obedience >= 3:
                        jump waitresstrain
                    else:
                        show image "04_pt/jasmine/outfit/jas04.png" at right with d3
                        j "......"
                        j "No... I'm not going to do that..."
                        hide image "04_pt/jasmine/outfit/jas04.png" at right with d3
                        jump tavern2
                "Quest: [quest3]." if quest300 and obedience >= 2 and quest2complete:
                    jump quest3starts
                "-Order Jasmine to serve drinks here-" if quest3complete and jidle:
                    jump jasminwaitreswork
                "-Order Jasmine to work as a dancer-" if quest11complete and jidle:
                    jump jasminedanceork
                "-Talk to Maslab-":
                    if quest2start:
                        jump boxdelievered
                    else:
                        jump maslab_talk
                "-Leave-":
                    $ renpy.play('sounds/door2.mp3')
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                    jump mainmenu 
#################EVENING##################################       
        
label dayends:
    #play music "music/Ozone.ogg" fadein 1 fadeout 1
    play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1
    hide image "04_pt/slavem/onaquest.png" with Dissolve(.3)
    
if quest10fail:
    show image "04_pt/slavem/qfailed.png" with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    hide image "04_pt/slavem/qfailed.png" with Dissolve(.3)
    $ quest10fail = False
    $ quest1000 = True
    $ quest10start = False
    $ quest10days = 0
    $ onquest = False
    
    jump dayends

if jonquest: 
    show image "04_pt/slavem/night.jpg" with fade   
    ">It's evening and Princess Jasmine returns from performing a quest related activity."
    show image "04_pt/jasmine/outfit/jas11.png" at right with Dissolve(.3)
    ">Jasmine is tired."
    show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
    hide image "04_pt/jasmine/outfit/jas11.png" at right with Dissolve(.3)
    pause 1
    hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
    $ tired +=2
    $ jonquest = False

#####################______FRUITS_______#####################################
if jfruits: 
    $ mtired +=1
    hide banana03 with Dissolve(.3)
    $ fruits = renpy.random.randint(1, 10)    
    if fruits <= 5:                                          
        show image "04_pt/slavem/night.jpg" with fade   
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)          
        $ fruitsgold = renpy.random.randint(10, 30)
        $ tired +=1
        $ gold = gold + fruitsgold
        ">Jasmine is a little tired but she brought home [fruitsgold] gold." 
        $ jfruits = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "I managed to sell plenty of fruits. Balsam said I was a big help..."
                m "I see... Alright, go to your room..."
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
        
    elif fruits == 6:                                          
        show image "04_pt/slavem/night.jpg" with fade   
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas11.png" at right with Dissolve(.3)          
        $ fruitsgold = renpy.random.randint(8, 20)
        $ tired +=1
        $ gold = gold + fruitsgold
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
        hide image "04_pt/jasmine/outfit/jas11.png" at right with Dissolve(.3)     
        ">Jasmine is a little tired but she brought home [fruitsgold] gold." 
        $ jfruits = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "I kneed one of the customers in the groin."
                g4 "You did what?!"
                j "Not my fault! He got handy with me!"
                j "He said he was just reaching out of the melon and garbed my breast by an accident, but he was lying..."
                j "He knew exactly what he was doing, and he got what he deserved..."
                j "Although, Balsam got a bit mad with me, that's why I brought a bit less gold tonight..."
                m "I see... Well, nothing we could do now I suppose. Just try to restrain yourself in the future..."
                j "Hmph..."
                m "Alright, off you go then..."
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
        
    elif fruits == 7:                                          
        show image "04_pt/slavem/night.jpg" with fade   
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)          
        $ fruitsgold = renpy.random.randint(20, 40)
        $ tired +=1
        $ gold = gold + fruitsgold
        ">Jasmine is a little tired but she brought home [fruitsgold] gold." 
        $ jfruits = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Good."
                j "Balsam said that I could eat as many bananas as I want absolutely free... So I ate quite a few of them..."
                j "I'm not sure how is this related but today we had twice us many customers..."
                j "some of them would even leave after they made a purchase... They would just stand watch me eat..."
                j "Men are weird..."
                m "Yes, yes, we are nothing but a bunch of weirdos. Off you go now..."
                j "............................."
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
    
    elif fruits == 8:                                          
        show image "04_pt/slavem/night.jpg" with fade   
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)          
        $ fruitsgold = renpy.random.randint(10, 30)
        $ tired +=1
        $ gold = gold + fruitsgold
        ">Jasmine is a little tired but she brought home [fruitsgold] gold." 
        $ jfruits = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Well, we got a new shipment of figs this morning. A really good one too. Maybe I should bring you some next time?"
                m "I don't care for figs. All I need you to bring me is gold, [jasname]."
                j "Alright, alright..."
                m "Go to your room..."
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
    
    elif fruits == 9:                                          
        show image "04_pt/slavem/night.jpg" with fade   
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)          
        $ fruitsgold = renpy.random.randint(10, 30)
        $ tired +=1
        $ gold = gold + fruitsgold
        ">Jasmine is a little tired but she brought home [fruitsgold] gold." 
        $ jfruits = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Well... Did you know that Balsam is one of the official palace fruit suppliers?"
                j "This serving girl was buying fruits for that dirt-bag of a sultan from us today."
                j "She recognized me and tried to kneel, but I gave her a cold stare and she understood..."
                j "She made her purchases but right before she left she slipped me this little pouch with gold..."
                j "What a nice girl... And I used to think that all the palace serving girls are good-for-nothing sluts."
                j "Here it is..."
                $ fruitsgold = renpy.random.randint(20, 40)
                $ gold = gold + fruitsgold
                $ renpy.play('sounds/win2.mp3')   
                ">You received [fruitsgold] gold."
                m "Very good. We could always use extra gold."
                m "Alright, you can go to your room now..."
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
        
    elif fruits == 10:                                          
        show image "04_pt/slavem/night.jpg" with fade   
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)          
        $ fruitsgold = renpy.random.randint(10, 30)
        $ tired +=1
        $ gold = gold + fruitsgold
        ">Jasmine is a little tired but she brought home [fruitsgold] gold." 
        $ jfruits = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "I'm glad you asked!"
                j "When I was working today, I saw this girl, she was wearing this ridiculously distressful burqa..."
                j "I mean, it was purple and with some white ornament... Some women just have now class whatsoever."
                j "I'm pretty sure she were fat and ugly under that thing..."
                j "And then there was this other girl... Her burqa wasn't that bad I suppose, but her shoes... I mean speaking of wasted money!"
                j "Oh, oh, wait! Then, there was this other one, she had such an ugly veil--"
                with hpunch
                g4 "Woman!"
                j "Huh?"
                m "To your room!"
                m "Hmph! You never have time for me!"
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
        
    
   
########################________HOUSE___CLEAN_________################################        
elif jhouse:
    $ mtired +=1
    hide cleaning with Dissolve(.3)                           
    $ clean = renpy.random.randint(1, 10)
    ### Usual.
    if clean <= 5:                           
        show image "04_pt/slavem/night.jpg" with fade       
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)                                         
        $ cleangold = renpy.random.randint(20, 60)
        $ tired +=2
        $ gold = gold + cleangold
        ">She feels very tired, but she made some money. \n>Jasmine brought home [cleangold] gold."
        $ jhouse = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "I've been dusting, sweeping and moping... \nSo, in short: very boring and tiresome..."
                m "I see... Go have some rest then."
                j "Thank you..."
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
    
    ### The Owner got suspicious.
    elif clean == 6:                           
        show image "04_pt/slavem/night.jpg" with fade       
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)                                         
        $ cleangold = renpy.random.randint(20, 60)
        $ tired +=2
        $ gold = gold + cleangold
        ">She feels very tired, but she made some money. \n>Jasmine brought home [cleangold] gold."
        $ jhouse = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Well... This one owner of one of the houses I worked at today..."
                j "I think he had his suspicions about my true identity..."
                j "But he didn't say anything so I didn't even have to lie to him..."
                j "So basically nothing exciting happened. Just another day..."
                m "I see. Well, go have some rest now."
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
    
    ### Broke a vase.
    elif clean == 7:                           
        show image "04_pt/slavem/night.jpg" with fade       
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)                                         
        $ cleangold = renpy.random.randint(5, 20)
        $ tired +=2
        $ gold = gold + cleangold
        ">She feels very tired, but she made some money. \n>Jasmine brought home [cleangold] gold."
        $ jhouse = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "Only [cleangold] gold coins? are you kidding me?"
                j "Yes... I was cleaning this one house and accidentally broke some stupid old jar..."
                j "Apparently it was not a jar but some expensive vase... I had to pay for the damage with the money I made..."
                j "So frustrating..."
                m "Be careful next time. You know we need money..."
                j "Yes, I know. Sorry, [myname]."
                m "Off you go then."       
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
    
    ### Bonus 1 coin
    elif clean == 8:                           
        show image "04_pt/slavem/night.jpg" with fade       
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)                                         
        $ cleangold = renpy.random.randint(20, 60)
        $ tired +=2
        $ gold = gold + cleangold
        ">She feels very tired, but she made some money. \n>Jasmine brought home [cleangold] gold."
        $ jhouse = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Well... Pretty generic I suppose. But there was this one house..."
                m "Yes? What about it?"
                j "Well the owner asked me to sweep the floors... {w}n-naked."
                m "I see... What did you tell him?"
                j "I refused of course..."
                j "But then he promised to pay me 300 gold coins..."
                g4 "And!?"
                j "300 gold coins is a big sum of money... I couldn't say \"no\" to such offer..."
                g9 "Atta girl! Come on, give me the money!"
                j "Here..."
                ">You recieve...{w}........{w}............{w} 1 gold coin."
                $ gold +=1
                g4 "Wait! What?"
                j "Yeah, he didn't actually pay me, that sleaze bag!"
                j "When I was done sweeping the floors he just gave me this one gold coin." 
                m "That's why you should always ask to see the money first before you get naked, girl."
                j "Right... I'll remember that... Sorry..."
                m "No harm done. Off you go then..."
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
        
    ### Watched man jerkoff
    elif clean == 9:                           
        show image "04_pt/slavem/night.jpg" with fade       
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)                                         
        $ cleangold = renpy.random.randint(20, 60)
        $ tired +=2
        $ gold = gold + cleangold
        ">She feels very tired, but she made some money. \n>Jasmine brought home [cleangold] gold."
        $ jhouse = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Well..."
                m "What? What is it?"
                j "This one merchant I was cleaning the house for..."
                j "He recognized me somehow... I'm not sure how, but he did."
                j "He called me by my name and said that he will keep my secret in exchange for..."
                m "Hm?"
                j "Well...."
                m "What is it? What did he want?"
                j "He kind of made me watch him touch himself..."
                j "It was very disturbing, but at least I didn't have to actually clean the house."
                j "All he asked me to do after was to mop up the puddle of semen he made on the floor."
                j "What a disgusting man..."
                m "Well, as long as you get paid, we have no problem."
                j "Y-yes... I think so too..."
                m "Alright. You can go to your room now."
                
        hide image "04_pt/jasmine/outfit/jas14.png" at right with Dissolve(.3)
  
    elif clean == 10:                           
        show image "04_pt/slavem/night.jpg" with fade       
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/q1/jas25.png" at right with Dissolve(.3)                                         
        $ cleangold = renpy.random.randint(20, 60)
        $ tired +=2
        $ gold = gold + cleangold
        ">She feels very tired, but she made some money. \n>Jasmine brought home [cleangold] gold."
        $ jhouse = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Huh? Oh, well, quite usual I suppose..."
                m "There is something on your hip there..."
                j "What? Wait! Is it...?"
                j "When did he?"
                j "That vile man! I knew it! He was touching himself while I was moping the floors!"
                m "What?"
                j "No, no. It's nothing..."
                j "Can I go now? I need to take this robe off..."
                m "Em... Sure. You can go..."
        hide image "04_pt/jasmine/q1/jas25.png" at right with Dissolve(.3)
        
#######JASMINE-WAITRESS#######################################################___WAITRESS___####################     
elif jtavern:
    $ mtired +=1
    hide tavern with Dissolve(.3)
    $ maid = renpy.random.randint(1, 10)
    
    ### Nothing happened
    if maid <= 5:
        show image "04_pt/slavem/night.jpg" with fade                
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)                       
        $ tired +=1
        $ maidgold = renpy.random.randint(50, 90)
        $ gold = gold + maidgold        
        ">Jasmine is tired but she brought home [maidgold] gold."       
        $ jtavern = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "I did my best... Flirted... Nobody recognized me."
                m "I see. Go to your room..."
        hide image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)
    
    ### Recognized    
    elif maid == 6:
        show image "04_pt/slavem/night.jpg" with fade                
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)
        $ tired +=1
        $ pthink +=2
        $ maidgold = renpy.random.randint(30, 70)
        $ gold = gold + maidgold        
        ">Jasmine is tired but she brought home [maidgold] gold. \n>Rumors are spreading."       
        $ jtavern = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "A customer recognized me. I had to let him grope me. And I gave him some money too."
                m "You think that will keep quiet?"
                j "I don't think so..."
                g4 "Why give him money, then, you silly [jasname]?!"
                j "I'm sorry, [myname]..."
                m "Go to your room..."
        hide image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)
    
    ### Triped. Paid less.
    elif maid == 7:
        show image "04_pt/slavem/night.jpg" with fade                
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)
        $ tired +=1
        $ pthink +=2
        $ maidgold = renpy.random.randint(40, 80)
        $ gold = gold + maidgold        
        ">Jasmine is tired but she brought home [maidgold] gold."       
        $ jtavern = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Well...."
                j "I tripped while I was dancing... so I got paid less today."
                m "Too bad... Be more careful next time."  
                j "Yes, [myname]."
        hide image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)
    
    ### Fight with Iris.
    elif maid == 8:
        show image "04_pt/slavem/night.jpg" with fade                
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)                       
        $ tired +=1
        $ maidgold = renpy.random.randint(50, 90)
        $ gold = gold + maidgold        
        ">Jasmine is tired but she brought home [maidgold] gold."       
        $ jtavern = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "That filthy peasant attacked me!"
                m "What? Who was it? Why didn't Maslab protect you?!"
                g4 "I will need to have a talk with him about this..."
                j "It was Iris..."
                m "What? Oh, so you got in a fight with her..."
                m "Well, cat-fights are not a big deal..."
                j "It is to me! Do I have to return to that despicable excuse for a tavern tomorrow?"
                m "We'll see... Just take some rest for now..."
                j ".................."
        hide image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)
      
    ### Groped. Apologized.
    elif maid == 9:
        show image "04_pt/slavem/night.jpg" with fade                
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)                       
        $ tired +=1
        $ maidgold = renpy.random.randint(50, 90)
        $ gold = gold + maidgold        
        ">Jasmine is tired but she brought home [maidgold] gold."       
        $ jtavern = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Well, this one brutish peasant tried to grope me..."
                j "So i slapped him..."
                j "..........................."
                m "And?"
                j "Tsk... Then I had to apologize and let him grope me anyway..."
                m "I see. Go to your room..."
        hide image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)
    
    ### Back alley handjob
    elif maid == 10:
        show image "04_pt/slavem/night.jpg" with fade                
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)                       
        $ tired +=1
        $ maidgold = renpy.random.randint(50, 90)
        $ gold = gold + maidgold        
        ">Jasmine is tired but she brought home [maidgold] gold."       
        $ jtavern = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "I don't want to talk about it..."
                m "Jasmine?"
                j "................"
                j "Well, alright..."
                j "This one ugly, pig-like customer recognized me..."
                j "...but, em, I convinced him to keep his mouth shut..."
                m "................."
                m "What did he ask for in exchange for his silence?"
                j ".................."
                j "He... em... well..."
                j "He took me to the back alley and... em..."
                j "He made jerk his filthy cock..."
                m "I see..."
                j "Can I go now? I want to wash my hands... again..."
                m "By all means... Just don't touch me..."  
                j "...................."
        hide image "04_pt/jasmine/outfit/jas08.png" at right with Dissolve(.3)
    
    
    
    
####################______DANCER__________#####################################
elif jdance:
    $ mtired +=1
    hide dance with Dissolve(.3)
    $ dancep = renpy.random.randint(1, 10)
    ### Nothing happened.
    if dancep <= 5:                            
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
        $ tired +=1
        $ dancegold = renpy.random.randint(70, 90)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."  
        $ jdance = False        
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "The Usual... Nothing out of the ordinary happened tonight..."
                m "I see..." 
        hide image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
        
    ###  gold 70, 90   
    elif dancep == 6:                            
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
        $ tired +=1
        $ dancegold = renpy.random.randint(70, 90)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."  
        $ jdance = False        
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "I did my best and even bared my tits a few times."
                j "Two dirty peasants recognized her."
                j "She let one of them play with her tits a little and let the other one one stick his tongue in her mouth."
                j "They promised to keep her secret... But it's very unlikely that they'll keep their word."
                j "There is a rumor that Princess Jasmine dances in the local tavern now."
                j "Jasmine's reputation dropped a little."    
                j "Jasmine is a little tired."
        hide image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
    
    ### gold 110, 140
    elif dancep == 7:                            
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
        $ tired +=1
        $ pthink +=2
        $ dancegold = renpy.random.randint(110, 140)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."  
        $ jdance = False        
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Well... I did my best..."
                j "I even bared my breasts a couple of times."
                g9 "Very good..."
                j "Yes... There was a big crowd in the tavern today."
                j "My performance was a great success actually."
                j "Although I thought I heard someone from the crowd call my name."
                j "But that can't be true because I was wearing the veil the whole time."
                g9 "Even when your naked tits were bouncing all over the place?"
                j "Don't be so vulgar, [myname]. But yes, even then..."
                m "Hm..."
                m "Well, alright. Go have some rest."
        hide image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
    
    ### Tripped. Paid less. Gold 50, 70
    elif dancep == 8:                            
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
        $ tired +=1
        $ dancegold = renpy.random.randint(50, 70)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."  
        $ jdance = False        
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "I tripped while I was dancing... so I got paid a bit less..."
                m "I see. be more careful next time." 
                j ".................."
        hide image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
        
    elif dancep >= 9:                            
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/q1/jas26.png" at right with Dissolve(.3)
        $ tired +=1
        $ dancegold = renpy.random.randint(70, 90)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."  
        $ jdance = False        
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was--"
                g4 "Eeww! What happened to you!?"
                j "Oh... Don't worry that's just honey mixed with some white wine..."
                m "Is it now?"
                m "Any particular reason why your entire body is covered with it?"
                j "Well, we tried this new thing tonight at the tavern..."
                j "With dancing, honey and, well, wine..."
                j "But it didn't work out the way we thought it would..."
                m "Alright, your explanations don't make this any less weird."
                m "Just go clean yourself up."
                j "Of course, [myname]..."
        hide image "04_pt/jasmine/q1/jas26.png" at right with Dissolve(.3)

        #################___IN PROGRESS___________###################
    elif dancep >= 10:                            
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
        $ tired +=1
        $ dancegold = renpy.random.randint(70, 90)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."  
        $ jdance = False        
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "Usual..."
                m "I see..." 
        hide image "04_pt/jasmine/outfit/jas09.png" at right with Dissolve(.3)
        
############_____WHORE___________##########################
elif jwhore:
    $ mtired +=1
    hide whore with Dissolve(.3)
    $ whoring = renpy.random.randint(1, 8) 
    if whoring ==1:
        show image "04_pt/slavem/night.jpg" with fade                               
        "It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
        $ tired +=2
        $ dancegold = renpy.random.randint(170, 190)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."
        $ jwhore = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "What? Oh... em... Well..."
                m "What is it?"
                j "One of the clients recognized me... But I said that I'm just a Princess Jasmine lookalike..."
                j "Because the real Princess Jasmine wouldn't be caught working in a brothel.... *sight*" 
                m "I don't think you should hide you true identity from the clients..."
                j "If they knew who you are they would pay more..."
                j "I know... It's just... never mind..."
                m "Alright. You can go now."
                j "................"
        hide image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
        
    if whoring ==2:
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
        $ tired +=2
        $ dancegold = renpy.random.randint(170, 190)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."
        $ jwhore = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "What? Oh... em... Nothing special really..."
                m "Alright then, off you go."
        hide image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
        
    if whoring ==3:
        show image "04_pt/slavem/night.jpg" with fade  
        hide whore
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas06.png" at right with Dissolve(.3) 
        $ tired +=2
        $ pthink +=5
        $ dancegold = renpy.random.randint(200, 350)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold.\n>Rumors about Princees Jasmine working in a brothel are spreading..."
        $ jwhore = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "What the hell happened to you?!"
                j "What? Oh... yeah..."
                j "One of the clients recognized me today..."
                j "So a whole bunch of those peasants decided to have their way with me all together... Ah...{image=textheart.png}"
                j "They did pay me extra, but I think they may brag to their friends about today..."
                j "I'm sorry, can I go to my room now? My legs are still shaking... {image=textheart.png}{image=textheart.png}{image=textheart.png}" 
                m "Sure... Go take a bath or something..."
                j "{size=-5}(ah... those dirty peasnts...){/size}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide image "04_pt/jasmine/outfit/jas06.png" at right with Dissolve(.3) 
    
    if whoring ==4:
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
        $ tired +=2
        $ dancegold = renpy.random.randint(90, 130)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."
        $ jwhore = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "What? Oh... em... Nothing special..."
                j "The bussness was a bit slow actually..."
                m "I see... Well, off you go..."
        hide image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
    
    if whoring ==5:
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
        $ tired +=2
        $ dancegold = renpy.random.randint(170, 190)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."
        $ jwhore = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day?"
                j "What? Oh... em..."
                j "Just another day at the brothel I guess..."
                j "Although there was this one fat and ugly merchant..."
                j "Apparently he likes it when women humiliate him and treat him like dirt..."
                j "I made him cry..."
                g4 "Did I really need to know this?"
                j "You asked about me day..."
                g4 "Go to your room, [jasname]!"
                j "Yes, you worthless worm! Oh, sorry, I meant to say [myname] of course."
        hide image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
        
    if whoring ==6:
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
        $ tired +=2
        $ dancegold = renpy.random.randint(170, 190)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."
        $ jwhore = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "What happened to your clothes?"
                j "Iris said I'm not brave enough to do something like this. I had to prove her wrong!"
                m "To do something like what? Get raped on the way home? How did you even get here in one piece?"
                j "I ran... Some naughty street urchins started to chase me but I outran them..."
                m "Foolish little [jasname]..."
                j "Em... I'm brave, right?"
                m "Oh, yes, yes. That proved your point, I'm sure... Go to your room now..."
                j "................."
        hide image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
    
    if whoring ==7:
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from work."
        show image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
        $ tired +=2
        $ dancegold = renpy.random.randint(200, 210)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."
        $ jwhore = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day, [jasname]?"
                j "*burp*!"
                j "Excuse me..."
                j "Today was an \"all in one bucket special\" day... I feel so full..."
                menu:
                    "-What's \"all in one bucket special\" day?":
                        j "You don't know?"
                        j "It's that event they hold in the \"Phoenix\" sometimes..."
                        j "At the beginning of the shift one girl is chosen at random to be this day's \"bucket\"..."
                        j "After that business goes as usual with one little difference: the \"bucket-girl\" can not be chosen by clients anymore..."
                        j "She just sits and waits..."
                        j "And whenever any of the working girls make a client cum the \"bucket-girl\" must interfere..."
                        j "So basically, for this entire day every ounce of cum produced goes inside one woman... *burp!*"
                        m "So I'm guessing you were the \"bucket-girl\" this time?"
                        j "Yes... em... if you don't mind I think I will skip dinner tonight...*burp!*"
                        m "Sure... You can go now..."
                        j "(Oh... So full...)"
                    "-I see... Go take a rest-":
                        j "*Burp!* Excuse me..."
        hide image "04_pt/jasmine/outfit/jas05.png" at right with Dissolve(.3) 
    
    
    if whoring ==8:
        show image "04_pt/slavem/night.jpg" with fade                               
        "It's evening and Princess Jasmine returns from work." 
        show image im.Flip("04_pt/jasmine/q1/jas07.png", horizontal=True) at right with d3
        $ tired +=2
        $ dancegold = renpy.random.randint(170, 190)
        $ gold = gold + dancegold
        ">Jasmine brought home [dancegold] gold."
        $ jwhore = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "How was your day, [jasname]?"
                g4 "Wait, why are you wearing your usual attire?"
                j "................"
                j "I don't want to talk about it..."
                menu:
                    "-Pressure the matter-":
                        hide image im.Flip("04_pt/jasmine/q1/jas07.png", horizontal=True) at right with d3
                        show image im.Flip("04_pt/jasmine/q1/jas12.png", horizontal=True) at right with d3
                        j "ah... but it's so embarrassing..."
                        m "What is? What happened?"
                        j "Well, alright..."
                        j "There was this one guy...."
                        j "........................"
                        m "Yes? What about him?"
                        j "He recognized me... Apparently his father used to work as a royal gardener at the palace..."
                        m "He recognized you? So what? I think by now everyone knows who you really are..."
                        j "Not true... There are rumors of course, but that's not the same..."
                        j "Well in any case, apparently he knew for a while now... and he brought this outfit with him..."
                        j "He made me put it on and then..."
                        hide image im.Flip("04_pt/jasmine/q1/jas12.png", horizontal=True) at right with d3
                        show image im.Flip("04_pt/jasmine/q1/jas05.png", horizontal=True) at right with d3
                        j "................"
                        m "[jasname]!!"
                        hide image im.Flip("04_pt/jasmine/q1/jas05.png", horizontal=True) at right with d3
                        show image im.Flip("04_pt/jasmine/q1/jas12.png", horizontal=True) at right with d3
                        j "He had me service him and his buddies..."
                        j "At first they pretended to be courteous and would only address me as \"Majesty\" or \"Your highness\"..."
                        j "And then they just overpowered me and had their way with me, one after another..."
                        j "And throught the whole thing they would keep calling me \"Princess Jasmine\" and \"Your royal highness\"."
                        hide image im.Flip("04_pt/jasmine/q1/jas12.png", horizontal=True) at right with d3
                        show image im.Flip("04_pt/jasmine/q1/jas04.png", horizontal=True) at right with d3
                        j "It was so humiliating..."
                        j "................................"
                        m "..............................."
                        m "You enjoyed it, didn't you?"
                        hide image im.Flip("04_pt/jasmine/q1/jas04.png", horizontal=True) at right with d3
                        show image im.Flip("04_pt/jasmine/q1/jas15.png", horizontal=True) at right with d3
                        j "I didn't have such strong orgasms in my entire life...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                        hide image im.Flip("04_pt/jasmine/q1/jas15.png", horizontal=True) at right with d3
                        show image im.Flip("04_pt/jasmine/q1/jas06.png", horizontal=True) at right with d3
                        j "I think I even passed out a couple of times..."
                        m "Good. You're almost ready..."
                        hide image im.Flip("04_pt/jasmine/q1/jas06.png", horizontal=True) at right with d3
                        show image im.Flip("04_pt/jasmine/q1/jas10.png", horizontal=True) at right with d3
                        j "Oh, and they also left me a personal tip, which actually never happens..."
                        j "Here..."
                        $ renpy.play('sounds/win2.mp3')
                        ">You received 50 gold coins."
                        $ gold +=50
                        m "not bad..."
                        m "OK, you can go now..."
                        hide image im.Flip("04_pt/jasmine/q1/jas10.png", horizontal=True) at right with d3
                        show image im.Flip("04_pt/jasmine/q1/jas06.png", horizontal=True) at right with d3
                        j ".................{image=textheart.png}"
                        hide image im.Flip("04_pt/jasmine/q1/jas06.png", horizontal=True) at right with d3
                    "-Let it go-":
                        m "Fine... Go to your room then..."
                        hide image im.Flip("04_pt/jasmine/q1/jas07.png", horizontal=True) at right with d3
                    
              

####______GRADUATION_IN_OBEDIENCE_____####
elif jsob1:
    $ mtired +=1
    hide obedience01b with Dissolve(.3)
    $ train = renpy.random.randint(1, 10)
    if train >= 3:
        show image "04_pt/slavem/night.jpg" with fade
        ">It's evening and Princess Jasmine returns from school."
        $ obedience +=1
        $ tired +=2
        if obedience >= 10:
            show image "quest/jas07.png" at right with Dissolve(.3)
            ">Princess Jasmine successfully graduated in the \"JSGA\" today with an \"I live to serve my master\" major."
            ">She is very proud of her achievement."
            ">There was a graduation party of course."
            ">And the party was for the teachers, of course."
            ">All the graduates had to wear skimpy outfits and serve drinks to the guests."
            ">Later on the party kinda turned into an all-out orgy, with teachers dominating their students."
            ">Jasmine had a great time though."
            $ jsob1 = False
            hide image "04_pt/jasmine/outfit/jas07.png" at right with Dissolve(.3)
        else:
            show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
            ">Rose the teacher was able to explain to Jasmine why she deserves no respect."
            ">Princess Jasmine became more obedient."
            $ jsob1 = False
            hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
    else:
        show image "04_pt/slavem/night.jpg" with fade
        ">It's evening and Princess Jasmine returns from the Academy."
        show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
        ">Jasmine now understands better why she should always only blame herself for everything."
        ">But it seems that she will have to attend a few more classes before she could learn to be more obedient."
        ">Jasmine feels tired."
        $ tired +=2
        $ jsob1 = False
        hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
       
                        
elif jsob2:
    $ mtired +=1
    hide obedience02 with Dissolve(.3)
    $ train = renpy.random.randint(1, 10)
    if train >= 3:
        show image "04_pt/slavem/night.jpg" with fade
        ">It's evening and Princess Jasmine returns from school."
        $ obedience +=1
        $ tired +=2
        if obedience >= 10:
            show image "04_pt/jasmine/outfit/jas07.png" at right with Dissolve(.3)
            "Princess Jasmine successfully graduated in the \"JSGA\" today with an \"I live to serve my master\" major."
            "She is very proud of her achievement."
            "There was a graduation party of course."
            "And the party was for the teachers, of course."
            "All the graduates had to wear skimpy outfits and serve drinks to the guests."
            "Later on the party kinda turned into an all-out orgy, with teachers dominating their students."
            "Jasmine had a great time though."
            $ jsob2 = False
            hide image "04_pt/jasmine/outfit/jas07.png" at right with Dissolve(.3)
        else:
            show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
            ">Rose the teacher was able to explain to Jasmine why \"Respectful love-making\" is a myth."
            ">Princess Jasmine became more obedient."
            $ jsob2 = False
            hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
    else:
        show image "04_pt/slavem/night.jpg" with fade
        hide obedience03
        "It's evening and Princess Jasmine returns from the Academy."
        show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
        "Jasmine now understands better why she deserves to be treated like crap." 
        "But it seems that she will have to attend a few more classes before she will learn to be more obedient."
        ">Jasmine feels tired."
        $ tired +=2
        $ jsob2 = False

        
elif jsob3:
    $ mtired +=1
    hide obedience01b with Dissolve(.3)                         
    $ train = renpy.random.randint(1, 10)
    if train >= 4:
        show image "04_pt/slavem/night.jpg" with fade
        ">It's evening and Princess Jasmine returns from school."
        $ obedience +=1
        $ tired +=2
        if obedience >= 10:
            ">Princess Jasmine successfully graduated the \"JSGA\" today with an \"I live to serve my master\" major."
            show image im.Flip("04_pt/jasmine/q1/jas30.png", horizontal=True) at right with d3 
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            ">She is very proud of her achievement."
            ">There was a graduation party of course."
            ">And the party was for the academy staff, of course."
            ">All the graduates had to wear skimpy outfits and serve drinks to the guests."
            ">Later on the party kinda turned into an all-out orgy, with teachers dominating their students."
            ">Jasmine had a great time though."
            $ jsob3 = False
            hide image im.Flip("04_pt/jasmine/q1/jas30.png", horizontal=True) at right with d3
        else:
            show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
            ">Rose the teacher has been able to explain to Jasmine how to properly enjoy hateful sex."
            ">Princess Jasmine became more obedient."
            $ jsob3 = False
            hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
    else:
        show image "04_pt/slavem/night.jpg" with fade
        ">It's evening and Princess Jasmine returns from the Academy."
        show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
        ">Jasmine understands better now why she should always swallow."
        ">But it seems that she will have to attend a few more classes before she will learn to be more obedient."
        ">Jasmine feels tired."
        $ tired +=2
        $ jsob3 = False
        hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)

elif jsmor1:
    $ mtired +=1
    hide courage with Dissolve(.3)
    $ train = renpy.random.randint(1, 10)
    if train >= 3:                            
        $ courage +=1
        $ tired +=2
        show image "04_pt/slavem/night.jpg" with fade
        ">It's evening and Princess Jasmine returns from the Academy."
        if courage >= 10:
            show image "04_pt/jasmine/outfit/jas07.png" at right with Dissolve(.3)
            "Princess Jasmine successfully graduated in the \"JSGA\" today. She got a \"Shameless whore\" diploma."
            "Jasmine is very proud of her achievement."
            "There was a graduation party of course."
            "And All the graduates had to walk the streets of agrabah fully naked, showing off their diplomas while trying not to blush."
            "She had a great time."
            "Many people saw her happily prancing around naked and without a shred of shame."
            "Jasmine's reputation among people of Agrabah suffered a devastating blow today."
            $ pthink +=7
            $ jsmor1 = False
            hide image "04_pt/jasmine/outfit/jas07.png" at right with Dissolve(.3)
        else:  
            show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
            ">Rose the teacher taught her how to succesfully ignore embarassment."
            ">Jasmine became more shameless." 
            $ jsmor1 = False
            hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
    else: 
        show image "04_pt/slavem/night.jpg" with fade
        "It's evening and Princess Jasmine returns from the Academy."
        show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
        "Jasmine understands a bit better now, why having high moral standards is bad for a woman."
        "But it seems that she will have to attend a few more classes before she will learn to be more shameless."
        "Jasmine is very tired."
        $ tired +=2
        $ jsmor1 = False
        hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
        
elif jsmor2:
    $ mtired +=1
    hide courage with Dissolve(.3)
    $ train = renpy.random.randint(1, 10)
    if train >= 3:                            
        $ courage +=1
        $ tired +=2
        show image "04_pt/slavem/night.jpg" with fade
        ">It's evening and Princess Jasmine returns from the Academy."
        if courage >= 10:
            show image "04_pt/jasmine/outfit/jas07.png" at right with Dissolve(.3)
            ">Princess Jasmine successfully graduated in the \"JSGA\" today. She got a \"Shameless whore\" diploma."
            ">She is very proud of her achievement."
            ">There was a graduation party of course."
            ">All the graduates had to walk the streets of agrabah completely naked, showing off their diplomas while trying not to blush."
            ">Jasmine had a great time."
            ">Many people saw her happily prancing around naked and without a shred of shame."
            ">Jasmine's reputation among people of Agrabah suffered a devastating blow today."
            $ pthink +=7
            $ jsmor2 = False
            hide image "04_pt/jasmine/outfit/jas07.png" at right with Dissolve(.3)
        else:  
            show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
            ">Rose the teacher was able to explain to Jasmine why she should always try and expose her breasts in public."
            ">Jasmine became more shameless."
            $ jsmor2 = False
            hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
    else: 
        show image "04_pt/slavem/night.jpg" with fade
        ">It's evening and Princess Jasmine returns from the Academy."
        show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
        ">Jasmine understands a bit better now, why it's important to never interrupt people when they grope you."   
        ">But it seems that she will have to attend a few more classes before she will learn to be more shameless."
        ">Jasmine is very tired."
        $ tired +=2
        $ jsmor2 = False
        hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)

elif jsmor3:
    $ mtired +=1
    hide courage with Dissolve(.3)
    $ train = renpy.random.randint(1, 10)
    if train >= 4:                            
        $ courage +=1
        $ tired +=2
        show image "04_pt/slavem/night.jpg" with fade
        ">It's evening and Princess Jasmine returns from the Academy."
        if courage >= 10:
            ">Princess Jasmine successfully graduated the \"JSGA\" today. She got a \"Shameless whore\" diploma."
            show image im.Flip("04_pt/jasmine/q1/jas31.png", horizontal=True) at right with d3 
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            ">She is very proud of her achievement."
            ">There was a graduation party of course."
            ">After which all the graduates were required to walk the streets of Agrabah topless showing off their diplomas, while trying not to blush."
            ">Jasmine had a great time."
            ">Many people saw her happily prancing around half-naked and without a shred of shame."
            ">Jasmine's reputation among people of Agrabah suffered a devastating blow today."
            $ pthink +=7
            $ jsmor3 = False
            hide image im.Flip("04_pt/jasmine/q1/jas31.png", horizontal=True) at right with d3 
        else:  
            show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
            ">Rose the teacher was able to explain to Jasmine  how to completely suppress any embarrassment."
            ">Jasmine became more shameless."
            $ jsmor3 = False
            hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
    else: 
        show image "04_pt/slavem/night.jpg" with fade
        hide courage
        ">It's evening and Princess Jasmine returns from the Academy."
        show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
        ">Jasmine understands a bit better now, why it's important to always be submissive."
        ">But it seems that she will have to attend a few more classes before she will learn to be more shameless."
        ">Jasmine is very tired."
        $ tired +=2
        $ jsmor3 = False
        hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
   
elif jidle:
    hide rest03 with Dissolve(.3)
    show image "04_pt/slavem/night.jpg" with fade                               
    ">Jasmine been idle today."
    show image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
    ">Jasmine feels refreshed."
    hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)
    $ mtired = 0
    $ tired = 0
    
    
elif lola_walks_jasmine:
    show image "04_pt/slavem/night.jpg" with fade
    ">It's evening and both Princess Jasmine and Lola return home from performing your personal request."
    show image "04_pt/lola/q5/lola03.png" 
    show image "lola_dates/cum.png" 
    with d5
    lol "Were're home!"
    show image "04_pt/jasmine/outfit/jas19.png" at right with d5
    show ctc7 at right
    pause
    hide ctc7
    j ".................."
    m "Did you girls have fun?"
    lol "Tons!!!"
    j "................."
    m "Jasmine are you alright?"
    j "What? Oh.... I..."
    j "I'm sorry, I just want to be alone for a while..."
    hide image "04_pt/jasmine/outfit/jas19.png" at right with d5
    lol "Let's do this again sometime!"
    hide image "04_pt/lola/q5/lola03.png" 
    hide image "lola_dates/cum.png" 
    with d5
    ">Jasmine is very tired..."
    ">And depressed..."
    ">And could be pregnant now..."
    $ tired +=2
    $ pthink +=5
    $ lola_walks_jasmine = False
    hide image "04_pt/jasmine/outfit/jas03.png" at right with Dissolve(.3)

    
    
elif jptits1:
    if storestarted: #By default is True. This flags only porpoise is to purpose is to stop storetopless +=1. 
        $ storetopless +=1 
    hide btits with Dissolve(.3)
    $ whoring = renpy.random.randint(1, 10)
    if whoring >= 4:
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from performing your personal request."
        show image im.Flip("04_pt/jasmine/q1/jas27.png", horizontal=True) at right with d3                                      
        ">The People of Agrabah respect their princess a little less now..."
        $ tired +=1
        $ jptits1 = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "So... How did it go?"
                j ".................................."
                m "Did you do what I told you to do?"
                j "Y-yes..."
                m "Did you expose yourself in front of your people..."
                j "Yes... I did..."
                j "I just don't understand why I have to do this...?"
                m "Never mind that. It's part of your training."
                j "............"
                m "How many people saw your tits today?"
                j "I... I d-don't know..."
                m "Take a wild guess then."
                j "A few dozen maybe..."
                m "How many of them recognized you?"
                j "I don't know... I don't think any of them did..."
                m "What? That's not good at all."
                m "Maybe next time you should leave your veil at home..."
                j "....................."
                j "Can I go now? I want to be alone for a while..."
                m "Sure, sure, go have some rest..."
        hide image im.Flip("04_pt/jasmine/q1/jas27.png", horizontal=True) at right with d3 
    else:
        show image "04_pt/slavem/night.jpg" with fade                               
        ">It's evening and Princess Jasmine returns from performing your personal request."
        show image im.Flip("04_pt/jasmine/q1/jas27.png", horizontal=True) at right with d3 
        ">The People of Agrabah respect their princess a little less now..."
        $ tired +=1
        $ pthink +=2 
        $ jptits1 = False
        menu:
            "-Send Jasmine to her room-":
                pass
            "-Inquire about her day-":
                m "So... How did it go?"
                j ".................................."
                m "Did you do what I told you to do?"
                j "Y-yes..."
                m "Did you expose yourself in front of your people..."
                j "Yes... I did..."
                j "I just don't understand why I have to do this...?"
                m "Never mind that. It's part of your training."
                j "............"
                m "How many people saw your tits today?"
                j "I... I d-don't know..."
                m "Take a wild guess then."
                j "A few dozen maybe..."
                m "How many of them recognized you?"
                j "I don't know... Not too many... One or two maybe..."
                m "That's not enough..."
                m "Maybe next time you should leave your veil at home..."
                j "....................."
                j "Can I go now? I want to be alone for a while..."
                m "Sure, sure, go have some rest..."
        hide image im.Flip("04_pt/jasmine/q1/jas27.png", horizontal=True) at right with d3

elif jptits2:
    if storestarted:
        $ storetopless +=1 
    hide btits2 with Dissolve(.3)
    show image "04_pt/slavem/night.jpg" with fade                               
    ">It's evening and Princess Jasmine returns from performing your personal request."
    show image im.Flip("04_pt/jasmine/q1/jas28.png", horizontal=True) at right with d3 
    ">Many people saw her tits today and most of them recognized her as their Princess."
    $ tired +=1    
    $ pthink +=4   
    $ jptits2 = False
    menu:
        "-Send Jasmine to her room-":
            pass
        "-Inquire about her day-":
            m "So... How did it go?"
            j ".................................."
            m "Did you do what I told you to do?"
            j "Y-yes..."
            m "Did you expose yourself in front of your people..."
            j "Yes... I did..."
            j "I just don't understand why I have to do this...?"
            m "Never mind that. It's part of your training."
            j "............"
            m "How many people saw your tits today?"
            j "I... I d-don't know..."
            m "Take a wild guess then."
            j "I don't know... A lot... Much more than a few dozen..."
            m "How many of them recognized you?"
            j ".........................."
            m "How many of them recognized you, girl?"
            hide image im.Flip("04_pt/jasmine/q1/jas28.png", horizontal=True) at right with d3 
            show image im.Flip("04_pt/jasmine/q1/jas29.png", horizontal=True) at right with d3 
            j "Every single one of them...*sob!*"
            m "Very good..."
            j "Can I please go now? *sob!*..."
            m "Sure, sure, go have some rest..."
    hide image im.Flip("04_pt/jasmine/q1/jas29.png", horizontal=True) at right with d3
    hide image im.Flip("04_pt/jasmine/q1/jas28.png", horizontal=True) at right with d3
    
elif jpslave:
    show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
    j "Fine... I'll do it..."
    hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
    ">Jasmine agrees to put on an embarrassing outfit and follow you around the city as a common slave-girl." 
    call jas_on_a_leesh
">Jasmine leaves for her room."
$ renpy.play('sounds/door2.mp3')    
    
####DAY ENDS#######    
label dayended: 
    $ daytime = False
    
    
menu:      
    "What would you like to do now?"
    "-Check Status-":  
        show image "04_pt/status/statusbg.png" with Dissolve(.2)
        if courage >= 0 and courage <= 3:
            show image "04_pt/status/statusj1.png" with Dissolve(.2)
        elif courage >= 4 and courage <= 6:
            show image "04_pt/status/statusj2.png" with Dissolve(.2)
        elif courage >= 7 and courage <= 9:
            show image "04_pt/status/statusj3.png" with Dissolve(.2)
        elif courage == 10:
            show image "04_pt/status/statusj4.png" with Dissolve(.2)
        
        if tired >= 0 and tired < 1:                
            show image "04_pt/status/sen1.png" with Dissolve(.2)
        elif tired >= 1 and tired < 2:
            show image "04_pt/status/sen2.png" with Dissolve(.2)
        elif tired >= 2 and tired < 3:
            show image "04_pt/status/sen3.png" with Dissolve(.2)
        
        if obedience == 0:
            show image "04_pt/status/sob00.png" with Dissolve(.2)
        elif obedience == 1:
            show image "04_pt/status/sob01.png" with Dissolve(.2)          
        elif obedience == 2:
            show image "04_pt/status/sob02.png" with Dissolve(.2)
        elif obedience == 3:
            show image "04_pt/status/sob03.png" with Dissolve(.2)
        elif obedience == 4:
            show image "04_pt/status/sob04.png" with Dissolve(.2)
        elif obedience == 5:
            show image "04_pt/status/sob05.png" with Dissolve(.2)
        elif obedience == 6:
            show image "04_pt/status/sob06.png" with Dissolve(.2)
        elif obedience == 7:
            show image "04_pt/status/sob07.png" with Dissolve(.2)
        elif obedience == 8:
            show image "04_pt/status/sob08.png" with Dissolve(.2)
        elif obedience == 9:   
            show image "04_pt/status/sob09.png" with Dissolve(.2)
        elif obedience >= 10:
            show image "04_pt/status/sob10.png" with Dissolve(.2)
        
        
        if courage == 0:
            show image "04_pt/status/smor00.png" with Dissolve(.2)
        elif courage == 1:
            show image "04_pt/status/smor01.png" with Dissolve(.2)          
        elif courage == 2:
            show image "04_pt/status/smor02.png" with Dissolve(.2)
        elif courage == 3:
            show image "04_pt/status/smor03.png" with Dissolve(.2)
        elif courage == 4:
            show image "04_pt/status/smor04.png" with Dissolve(.2)
        elif courage == 5:
            show image "04_pt/status/smor05.png" with Dissolve(.2)
        elif courage == 6:
            show image "04_pt/status/smor06.png" with Dissolve(.2)
        elif courage == 7:
            show image "04_pt/status/smor07.png" with Dissolve(.2)
        elif courage == 8:
            show image "04_pt/status/smor08.png" with Dissolve(.2)
        elif courage == 9:   
            show image "04_pt/status/smor09.png" with Dissolve(.2)
        elif courage >= 10:
            show image "04_pt/status/smor10.png" with Dissolve(.2)
            
        show image "04_pt/status/smon.png" with Dissolve(.2)
        
        show screen gold_scr #Отображаем золото, сам экран описан в самом низу кода
        
        
        show con1 at right
        show ctc7 at right
        pause 
        hide con1
        hide ctc7
        
        hide screen gold_scr #Отображаем золото, сам экран описан в самом низу кода
        
        show image "interface/blackfade.png" with Dissolve(.3)
        hide image "04_pt/status/statusbg.png" 
        hide image "04_pt/status/statusj1.png" 
        hide image "04_pt/status/sen1.png"
        hide image "04_pt/status/sen2.png" 
        hide image "04_pt/status/sen3.png" 
        
        hide image "04_pt/status/smor00.png" 
        hide image "04_pt/status/smor01.png"
        hide image "04_pt/status/smor02.png"
        hide image "04_pt/status/smor03.png"
        hide image "04_pt/status/smor04.png"
        hide image "04_pt/status/smor05.png"
        hide image "04_pt/status/smor06.png"
        hide image "04_pt/status/smor07.png"
        hide image "04_pt/status/smor08.png"
        hide image "04_pt/status/smor09.png"
        hide image "04_pt/status/smor10.png"
        
        hide image "04_pt/status/sob00.png" 
        hide image "04_pt/status/sob01.png" 
        hide image "04_pt/status/sob02.png" 
        hide image "04_pt/status/sob03.png" 
        hide image "04_pt/status/sob04.png" 
        hide image "04_pt/status/sob05.png" 
        hide image "04_pt/status/sob06.png" 
        hide image "04_pt/status/sob07.png" 
        hide image "04_pt/status/sob08.png" 
        hide image "04_pt/status/sob09.png" 
        hide image "04_pt/status/sob10.png" 
        
        hide image "04_pt/status/smon.png"
        
        hide image "04_pt/status/statusj1.png"
        hide image "04_pt/status/statusj2.png"
        hide image "04_pt/status/statusj3.png"
        hide image "04_pt/status/statusj4.png"
        
        hide image "interface/blackfade.png" with Dissolve(.3)
        jump dayended
    
    "-Jasmine's room-":
        if obedience >= 1:
            jump jasminsroom
        else: 
            $ renpy.play('sounds/door3.mp3')
            "*Knock-knock-knock*"
            pause.8
            "...."
            ".........................................."
            j "Go away..."
            ">The door seems to be locked from the inside."
            jump dayended
   
    "-Lola's room-" if lolamovedin:
        jump lolasroom
    "-Empty room-" if quest9complete and emptyroom:
        jump quest9complete
    "-Visit the tavern-" if quest2start2:
        show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
        ">Princess jasmine goes to bed... \nAfter that you leave the house..."
        show sleeping2 with Dissolve(.3)
        jump quest2night1
    "-Go to the market-" if quest2start4:
        show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
        ">Princess jasmine goes to bed... After that you leave the house..."
        show sleeping2 with Dissolve(.3)
        jump quest2night2
    
    "-Take Jasmine to Maslab-" if quest3start:
        $ quest3start = False
        $ quest3start2 = True
        jump waitress01
    
    "-Quest info-":
        jump questinfo
    "-Take a walk outside-" if quest2complete:
        $ loladaytime = False
        $ dahliaworks = renpy.random.randint(1, 2)
        if quest6 == 3:
            $ daintavern = renpy.random.randint(1, 3)
        else:
            $ daintavern = renpy.random.randint(1, 2)
        if loladays >= 5 and quest7 == 0:
            $ lola00 = False
            $ lolaworks = renpy.random.randint(1, 2) 
        show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
        play music "music/Ozone.ogg" fadein 1 fadeout 1
        ">Princess jasmine goes to bed... \nAfter that you leave the house..."
        show sleeping2 with Dissolve(.3)
        jump nightwalk        
    "-Call it a day-":
        if lolawhoredays >= 7 and quest8start5:
            jump quest8start5
        else:
            show image "04_pt/slavem/night2.jpg" with Dissolve(.3)
            show sleeping with Dissolve(.3)
            ">Jasmine goes to bed ...."
            jump jasdreams
########################
########################
###LAST DAY#############
            
label lastday:
hide rest03 with Dissolve(.3)
hide image "04_pt/slavem/bld.png" with Dissolve(.3)
$ cheapside = False 
$ redphoenix = False
$ finaldaystore = False
$ finaldaymarket = False
$ finaldaytavern = False

play music "music/The_calm_before_by_Calamaistr.mp3" fadein 1 fadeout 1
label lastday2:
    

$ select = renpy.imagemap("04_pt/slavem/mainbg01.png", "04_pt/slavem/mainbg02.png", [
                                       (39, 325, 140, 412, "persona1"),
                                       (93, 446, 236, 552, "home"),
                                       (155, 368, 247, 444, "brothel"),
                                       (309, 371, 400, 512, "shop"),
                                       (407, 316, 519, 396, "market"),
                                       (531, 368, 621, 487, "tavern"),
                                       (693, 357, 774, 441, "school"),
                                       (532, 187, 594, 307, "jpalace")
                                       ])


if select == "persona1":
    if cheapside:
        ">The Cheapside is as busy and noisy as ever..."
        ">You have no business here..."
        jump lastday2
    else:
        ">The Cheapside is as busy and noisy as ever..."
        menu:
            "-Take a walk-":
                $ cheapside = True 
                ">You take a walk through the narrow streets of the cheapside..."
                show blkfade with d3
                pause.5
                hide blkfade with d3
                sch8 "Good master... How are you doing today?"
                sch8 "Did you hear the big news?"
                sch8 "Our Princess is too be wed tomorrow..."
                sch8 "A big wedding parade is to be held!"
                sch8 "Oh, Crocus is not missing that one!"
                sch8 "Crocus wants to take one more look at \"The Whore Princess\"."
                m "You take a good care of yourself, old crow..."
                sch7 "Huh? Of course, crocus always does."
                show blkfade with d3
                pause.5
                hide blkfade with d3
                ">It feels like ages ago that Jasmine was working here cleaning houses..."
                "......."
                "..."
                ">The Streets are full of people as always..."
                ">News spread fast, and citizens already anticipate tomorrows wedding parade..."
                "....."
                "..."
                ">You recall sending Jasmine here with a task to simply walk around and bare her tits in front of complete strangers..."
                ">and reminisce about \"the good old days\" for a while..."
                "....."
                "..."
                ".."
                ">There is nothing left for you here. You decide to leave."
                jump lastday2
            "-Leave-":
                jump lastday2
    
if select == "home":
    $ renpy.play('sounds/door.mp3')
    
    show blkfade with d5
    pause.5
    show image "04_pt/slavem/bld.png" behind blkfade
    hide blkfade with d5
    menu:
        "Your house..."
        "-Stay here till the evening...-":
            ">The Wedding Parade is going to take place tomorrow."
            ">Today is your last chance to explore the city and say your goodbyes..."
            menu:
                "Are you sure you want to spend the rest of the day in your house?"
                "\"No, not yet.\"":
                    show blkfade with d5
                    pause.5
                    hide image "04_pt/slavem/bld.png" 
                    hide blkfade with d5
                    jump lastday2
                "\"Yes, stay home.\"":                            
                    ">You decide to spend the rest of the day at home..."
                    ">The house feels quiet and empty today..."
                    ">You think about the days you spent here with princess Jasmine..."
                    ">You did do a great job... You turned her into a perfect whore, just like the Sultan Jafar ordered you to do, but..."
                    ">But what is that feeling...? None of this feels quite right... Why...?"
                    ">Why do you follow Jafar's orders so blindly?"
                    ">Well, because he is the Sultan of course..."
                    ">But who are you then?..."
                    ">You try to recall your past but everything seems to be so fuzzy..."
                    ">You try to reason with yourself back and forth, but can't get rid of an odd feeling that you are forgetting something important..."
                    ">You lose track of time and suddenly realize that it's already pretty late..."
                    show image "04_pt/slavem/night.jpg" with fade           
                    play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1   
                    ">You decide to go to bed early today..."
                    ">but you're having troubles falling asleep..."
                    ">A feeling of unease is not leaving you..."
                    "........."
                    ">Maybe you will see another one of those odd dreams tonight?"
                    show image "interface/blackfade.png" with Dissolve(.5)
                    hide image "04_pt/slavem/night.jpg" 
#                    show ctc7 at right
#                    pause 
#                    hide ctc7
#                    "......"
#                    "..."
#                    ".."

#                    show image im.Alpha("04_pt/jasmine/outfit/jas09.png", 0.5) with Dissolve(.3)
#                    j "I am home master..."
#                    m "Jasmine...?"
#                    hide image im.Alpha("04_pt/jasmine/outfit/jas09.png", 0.5) with Dissolve(.3)
#                    "....."
#                    show image im.Alpha("intro/al03.png", 0.5) with Dissolve(.3)
#                    a "Oh, look at the way you're dressed!"
#                    hide image im.Alpha("intro/al03.png", 0.5) with Dissolve(.3)
#                    show image im.Alpha("intro/jas02.png", 0.5) with Dissolve(.3)
#                    j "What is wrong with the way I dress?"
#                    show image im.Alpha("intro/al03.png", 0.5) with Dissolve(.3)
#                    hide image im.Alpha("intro/jas02.png", 0.5) with Dissolve(.3)
#                    a "Nothing! For a dancing slave girl, but you are a princess! You're supposed to set an example! But what do you do? You fly around the city half-naked in the company of some \"street rat\"..."
#                    m "Who... Who is that guy?..."
#                    hide image im.Alpha("intro/al03.png", 0.5) with Dissolve(.3)
#                    "......"
#                    show image im.Alpha("intro/sultan02.png", 0.5) with Dissolve(.3)
#                    sul "Jasmine, my dear. Aladdin has a point!"
#                    hide image im.Alpha("intro/sultan02.png", 0.5) with Dissolve(.3)
#                    show image im.Alpha("intro/jas04.png", 0.5) with Dissolve(.3)
#                    j "Don't you take his side, father!"
#                    hide image im.Alpha("intro/jas04.png", 0.5) with Dissolve(.3)
#                    show image im.Alpha("intro/sultan02.png", 0.5) with Dissolve(.3)
#                    sul "But dear, people are starting to talk."
#                    "....."
#                    m "That old guy...."
#                    m "The sultan...?"
#                    m "No... jafar is the sultan..."
#                    hide image im.Alpha("intro/sultan02.png", 0.5) with Dissolve(.3)
#                    "...."
#                    show image im.Alpha("lpotion/lpfinal00.jpg", 0.5) with Dissolve(.3)
#                    j "Can I suck your cock now please?"
#                    hide image im.Alpha("lpotion/lpfinal00.jpg", 0.5) with Dissolve(.3)
#                    show image im.Alpha("lpotion/lpotion07.png", 0.5) with Dissolve(.3)
#                    j "I am your slut, i am your whore..."            
#                    j "I want you to fuck me, to use me..."
#                    hide image im.Alpha("lpotion/lpotion07.png", 0.5) with Dissolve(.3)
#                    show image "intro/jas14.png" with Dissolve(.3)
                    
#                    j "What the hell do you think you are doing, peasant?!"
#                    j "I will have you beheaded for this!!!"
#                    with hpunch
#                    g4 "{size=+4}PRINCESS JASMINE?!?!{/size}"
#                    show whitefade with Dissolve(.4)
#                    show image "interface/white.jpg" with Dissolve(.4)
#                    m "????"
#                    stop music fadeout 1
#                    show image "04_pt/slavem/parade.jpg" behind whitefade
#                    hide image "interface/blackfade.png" with Dissolve(.5)
#                    hide image "intro/jas14.png" with Dissolve(.3)
#                    hide whitefade with Dissolve(.5)
#                    hide image "interface/white.jpg" with Dissolve(.5)
#                    "You wake up covered in cold sweat."
#                    g5 "But of course! The real Agrabah, aladdin, carpet, abu and the real sultan!"
#                    g5 "The magic shop..."
#                    play music "music/EasternJourneybyPike270.mp3" fadein 1 fadeout 1
#                    g5 "It's all coming back to me now! How could I forget my entire life?!"
#                    m "Alright... So this world is not real... Or even if it is, it's not my world."
#                    m "Me and princess Jasmine are not supposed to be here..."
#                    m "Princess Jasmine! Oh..."
#                    m "I did some pretty messed up things to her..."
#                    m "After I bring us back she will definitely have me beheaded..."
#                    m "Not the usual empty threats, but for real this time..."
#                    m "But I can think about it later... First I need to stop the wedding!"
#                    m "I don't have my magic powers anymore, but I'm pretty sure I can still undo this spell, and that should set things right!"
#                    m "But I need to be close enough to the princess Jasmine to do that, otherwise she may get stuck here for good..."
                    
                    "...........{w}.............{w}.............{w}............."
                    show whitefade with Dissolve(.4)
                    show image "interface/white.jpg" with Dissolve(.4)
                    stop music fadeout 1
                    show image "04_pt/slavem/parade.jpg" behind whitefade
                    hide image "interface/blackfade.png" with Dissolve(.5)
                    hide whitefade with Dissolve(.5)
                    hide image "interface/white.jpg" with Dissolve(.5)
                    play music "music/EasternJourneybyPike270.mp3" fadein 1 fadeout 1
                    ">It's morning..."
                    ">You wake up covered in cold sweat, you heart is racing..."
                    ">You don't remember seeing any dreams this time though..."
                    ">But the feeling of unease is not leaving you... If anything it's gotten even worse..."
                    ">The sound of music and royal fanfares comes from the outside."
                    m "The parade! I better hurry up!"
                    
                    #########################################################################################
                    show con1 at right
                    show ctc7 at right
                    pause 
                    hide con1
                    hide ctc7
                    show image "04_pt/slavem/dark.jpg" with Dissolve(.3)
                    ">The central street of Agrabah is packed with people..."
                    ">It's nearly impossible to get close enough to even see what's going on..."
                    ">Looks like the main platform with Princess Jasmine and Jafar is yet to show up."
                    ">All you can see are rows of camels and some elephants decorated with all sorts of feathers and golden trinkets."
                    ">You have no interest in any of that."
                    stop music fadeout 3
                    ">Finally you hear screams of excitement from your right!"
                    ">This has got to be the main platform!"                    
                    ">And it is... Just a few minutes later it shows up and moves slowly right beside you..."
                  
        ##############################################################
                    play music "music/JafarsHour.mp3" fadein 1 fadeout 1
                    if dress01: 
                        
                        show image "04_pt/slavem/wedding10.jpg" with fade
                        hide image "04_pt/slavem/dark.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        w_jas_c[2] "........."
                        w_jas_c[4] "........."
                        "Princess jasmine is wearing a wedding dress that leaves no room for imagination."
                        "Her shapely tits are are completely visible through the transparent fabric of the dress."
                        "You hear that the people around you are starting to take notice of that."
                        cr1 "look, look at the princess... She is... Her... Her dress... I think I can see her tits..."
                        cr2 "I can see her breasts too! And her nipples!"
                        w_jas_c[4] "........."
                        cr3 "Did Jafar force her to wear that vulgar outfit?"
                        cr2 "Doesn't look like it. She is smiling..."
                        cr2 "It's almost as if she is enjoying parading herself shamelessly before us like this?"                     
                        cr1 "What a disgusting whore! Is she mocking us!?"

                        "The platform stops. Looks like the Sultan wants to address the people."
                        show image "04_pt/slavem/wedding01.jpg" with fade
                        hide image "04_pt/slavem/wedding10.jpg" 
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        jaf[4] "People of Agrabah."
                        jaf[4] "My loyal subjects."
                        jaf[4] "Thank you for attending our wedding parade today."
                        

                        cr1 "Shut your mouth, Jafar! You suck!"
                        stop music 
                        $ renpy.play('sounds/scratch.wav')
                        
                        jaf[5] "........."
                        jaf[3] "(You filthy peasants... How dare you....?)"
                        play music "music/Marketplace.mp3" fadein 1 fadeout 1
                        cr2 "My camel shits turds that are prettier than your face, jafar!"
                        cr1 "Ha-ha-ha! That's a good one, Mustafa!"
                        cr4 "Shut up you idiot, don't say my name."

                        
                        jaf[3] "Without further ado let me present you my bride..."
                        jaf[4] "Jasmine, the princess of agrabah!"
                        w_jas_c[2] "H-Hello everyone..."
                        cr1 "Filthy slut! Whore!"
                        w_jas_c[3] "................."
                        cr2 "Hey, princess I can see your tits!"
                        w_jas_c[4] "(ah.........)"
                        cr1"Hey, Princess jasmine, nice dress! Would you shake those jugs a bit for us? Ha-ha-ha!"
                        w_jas_c[9] "(ah... ah.........)"
                        cr3"Princess Jasmine, your highness, I beg you, please cover yourself! This is disgraceful!"

                        cr2 "Quiet wench! Clearly this one has no shame!"
                        cr1 "But, she is mocking us with her vulgarity!"

                        jaf[1] "(Go on with your speech, \"my love\"...)"
                        w_jas_c[3] "(Yes, master...)"

                        w_jas_c[5] "People of agrabah, thank you for showing up today..."
                        cr1 "You suck, you filthy slut!"
                        w_jas_c[4] "....."
                        cr2 "Yeah, shut your whore-mouth! you betrayed Agrabah! you betrayed us all!"
                        cr1 "Traitor! Traitor! You will pay for this!!!"
                        w_jas_c[8] "???"
                        w_jas_c[6] "{size=-4}(I'm sorry...){/size}"

                        jaf[6] "(Keep going, slave...)"
                        w_jas_c[5] "...."
                        w_jas_c[5] "As a wedding present to you all I am wearing this humiliating outfit, to let all of you see me for what I am..."
                        cr1"A filthy whore!"
                        cr2 "Well said, Mustafa!"
                        cr4 "Shut up! Or I'll cut your ear off, I swear!"
                        cr1 "sorry..."
                        stop music fadeout 1
                        w_jas_c[5] "Y-yes... I am a..."
                        w_jas_c[5] "a..."
                        w_jas_c[9] "...a filthy whore..."
                        w_jas_c[5] "...Please look at me..."
                        play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1
                        cr1 "Huh..?"
                        w_jas_c[5] "Look at me... Shame me..."
                        w_jas_c[5] "I stand before you today, and I allow you all to marvel at my poorly covered body..."
                        w_jas_c[5] "This is the only way I could show my appreciation and love to you..."
                        cr1 "Is she insane...?"
                        w_jas_c[5] "Please.... Look at me, all of you..."
                        w_jas_c[6] "I am your shameless princess..."
                        cr5 "........."
                        cr5 "...."
                        w_jas_c[4] "......."
                        cr1 "What is going on here?"
                        cr2 "I can't believe this! What is she saying?!"
                        cr1 "Whore! Slut! Stone her to death!"
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        jaf[1] "(he-he. Splendid. But that's not all.)"
                        jaf[6] "(Keep going, slut.)"
                        w_jas_c[7]  "......"
                        w_jas_c[5] "Now I would like to present to you my beloved fiancee Jafar."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_c[5] "I... I ask you to accept him as... your..."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_c[9] "........"
                        w_jas_c[5] "As your rightful ruler... and... and..."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_c[5] "And... I..."
                        jaf[6] "(what's the matter, slut? Keep going!)"
                        w_jas_c[4] "I... I can't... everyone is looking at me..."
                        w_jas_c[4] "My... my body is on display..."
                        w_jas_c[4] "Everyone can see me in this embarrassing garment..."
                        jaf[6] "(So what? I said, keep talking, slave!)"
                        w_jas_c[5] "I... I can't... I'm almost... I'm about to..."                        
                        w_jas_c[8] "oh No!"
                        w_jas_c[8] "no. Not now, please..."
                        w_jas_c[8] "no... No... ....."
                        jaf[6] "(What are you talking about, slut?)"
                        stop music fadeout 10
                        w_jas_c[9] "(I'm cumming... Jafar, oh my god, I'm cumming!)"
                        w_jas_c[9] "(Please, don't let them see me like that!)"            
                        jaf[7] "(You're what?!)"
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        jaf[3] "(You worthless piece of camel shit! You're gonna ruin everything!)"
                        w_jas_c[9] "(No... I'm sorry.)"
                        w_jas_c[9] "(Please, don't talk to me like that, it only makes me come harder! Please, I can't hold it...)"
                        w_jas_c[9] "(I can't stop!)"
                        w_jas_c[11] "Here comes another one... Ah..."
                        w_jas_c[10] "(No, no... Not like this, not in front of all of these people!)"
                        w_jas_c[10] "ah... ah..."
                        play music "music/The_calm_before_by_Calamaistr.mp3" fadein 2 fadeout 1
                        cr6 "Princess whore! Princess Whore! Princess Wh--"
                        show image "04_pt/slavem/wedding14c.jpg" with Dissolve(.3)
                        hide image "04_pt/slavem/wedding01.jpg"                        
                        cr1 "Huh? Hey, what is wrong with the princess!"                        
                        w_jas_c[13] "Ah... (Jafar, I'm begging you. Save me form this! Don't let them realize what's going on!) ah..."
                        cr1 "Is she sick or something? look at her..."
                        jaf[3] "(You fucking bitch, now I have to fix this mess!)"
                        jaf[4] "Khem..."
                        jaf[4] "Ladies and gentlemen. Can i have your attention for a second!?"
                        w_jas_c[12] "(Thank you Jafar! Thank you, thank you! I'm ... ah...)"
                        jaf[3] "If you would, please take a closer look at your beloved princess now!"
                        w_jas_c[11] "(What? No, Jafar, no, don't...)"
                        jaf[3] "At this very moment she is cumming violently!"
                        cr1 "What?"
                        cr2 "Is he serious?!"
                        jaf[3] "She is trying to hide it, but she is cumming like a filthy pig, again and again!"
                        w_jas_c[13] "No! Why... ah.... No..."
                        w_jas_c[11] "I'm cumming again!"
                        jaf[3] "You see? I guess showing off her body shamelessly like that just got our little princess a bit too exited..."
                        cr1 "I can not believe this..."
                        cr2 "Such a disgrace..."
                        w_jas_c[11] "I'M CUMMING AGAIN! I CAN'T STOP! EVERYONE FORGIVE ME! I'M CUMMING!"
                        jaf[3] "Isn't she a filthy animal?"
                        jaf[3] "I know! She deserves to be punished!"
                        cr1 "Yes! She is disgusting!"
                        cr2 "You shame agrabah, you filthy slut!"
                        w_jas_c[14] "Ohhh! This is unbearable! I can't stop..."
                        cr1 "Shut up you whore!"
                        cr3 "Stone her! Stone that bitch!"
                        cr2 "Throw her into the dungeons! She deserves no mercy!"
                        jaf[2] "(Great! They are all mine now!)"
                        jaf[4] "People of agrabah, What would you say if I were to punish her right here, in front of you!?"
                        w_jas_c[13] "ah.. What?"
                        cr1 "Yeah! Punish her!"
                        cr2 "Punish the bitch! Punish the bitch!"
                        jaf[3] "Come, here you slut!"
                        w_jas_c[13] "What?"
                        w_jas_c[13] "What are you...?"
                        show image "04_pt/slavem/wedding04.jpg" with fade
                        with hpunch
                        hide image "04_pt/slavem/wedding14c.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        cr5 "yes! Fuck her, jafar! Fuck that slut!"
                        w_jas_c[15] "AAAAAAAAH!!!"
                        w_jas_c[16] "NoOOOOOO! I...! I'm cumming!"
                        jaf_c[8] "That's just a begging, whore!"
                        cr1 "Hey? Can you hear me slut!? You whore! I wish i could fuck you too!"
                        cr2 "yeah! Fuck that bitch!"
                        w_jas_c[16] "No, don't fuck me like that!"
                        w_jas_c[16] "Not infront ..."
                        w_jas_c[16] "Of everyone! I will go insane..."
                        w_jas_c[16] "I can't stop cumming... I never came... like that ever... please... I ... no.... no..."
                        cr1 "Ha-ha-ha! Look at those udders fly!"
                        cr2 "Ha-ha-ha, you're right! Those are the royal tits my friend!"
                        cr1 "Look at them bounce!"
                        w_jas_c[17] "No, please stop saying such things... or I'll..."
                        w_jas_c[17] "............"
                        w_jas_c[17] "........"
                        w_jas_c[17] "..."
                        jaf_c[8] "Let me guess, whore. You're cumming again."
                        w_jas_c[16] "y-y-yeeeeeeees!!!!!!!!!!!"
                        jaf_c[8] "Are you done, whore?"
                        jaf_c[8] "You did not finish your speech, did you?"
                        w_jas_c[18] "what?... I... ah..."
                        w_jas_c[18] "No, you must be kidding...:"
                        jaf_c[8] "I said, finish your speech, whore!"
                        w_jas_c[18] "While... you're...."
                        w_jas_c[17] "........"
                        w_jas_c[18] "Fucking me... and I keep on cumming uncontrollably???..."
                        jaf_c[8] "I said, start talking, you whore!"
                        w_jas_c[17] "AH! I can't I'm cumming again!"
                        w_jas_c[17] "....."
                        jaf_c[8] "Do You disobey me?"
                        w_jas_c[18] "No, no, I'm sorry... I will try..."
                        w_jas_c[17] "......"
                        w_jas_c[19] "People ah... of.... ah... A-Agrabah... ah..."
                        cr1 "What is she blathering there?"
                        w_jas_c[19] "I ask ...ah... you to accept... jafar ... as... ah..."
                        w_jas_c[17] "....."
                        w_jas_c[16] "Sorry...."
                        w_jas_c[16] "Again..."
                        w_jas_c[16] "I'm sorry! I'm so sorry! I'M CUUUMING!"
                        cr3 "She is disgusting!"
                        cr5 "filthy Princess whore! filthy Princess whore!"
                        w_jas_c[19] "And Er ... ah... I'm sure... that... ah..."
                        w_jas_c[18] "no, not so hard!"
                        w_jas_c[16] "i'm cumming..."
                        w_jas_c[15] "I... I'm sure that sultan Jafar will bring..."
                        w_jas_c[19] "ah... prosperity to A-agrabah... ah..."
                        w_jas_c[19] "...and I w-will give him a healthy baby-boy to inherit the t-throne..."
                        jaf_c[8] "Yup! We gonna make one here today, you whore!"
                        cr1 "ha-ha-ha! never thought I'd become a part of the royal honey moon!"
                        cr2 "Ha-ha-ha! Look at her silly face! You keep fucking that whore, jafar!"
                        cr1 "Yeah! Show her who's the sultan!"
                        w_jas_c[19] "And ah... the prosperity... ah..."
                        w_jas_c[19] "orgasm... and... ah... the royal pussy, I mean family..."
                        w_jas_c[17] "ah... cumming... ah... peasants are watching... ah... my sultan jafar... ah..."
                        w_jas_c[17] "and please... ah... whore... ah cumming again..."
                        cr1 "What is she talking about now? Can you understand what she's saying?"
                        
                        cr2"Can you make any sense of what she is saying, Mustafa?"
                        cr4"Alright, that does it, come here, you fool!"
                        cr2"Ah, no, not my ear! Get off me! NOT MY EAR!"
                        cr1 "I think she just  went mad from experiencing too many orgasms at once..."
                        w_jas_c[16] "Ah... blah... slut... whore..."
                        w_jas_c[16] "I'm a whore.. look at me... I'm cumming..."
                        w_jas_c[16] "Can't stop cumming... I..."
                        w_jas_c[16] "ah.... Princess...filthy slut..."
                        jaf_c[8] "What is it, whore? About to pass out, are you?"
                        jaf_c[8] "Not yet! I'm still fucking ya sorry ass!"
                        jaf_c[8] "Now be a good whore  and show some respect to all those nice people!"
                        jaf_c[8] "Look at them while I'll be filling you with my cum!"
                        jaf_c[8] "And don't forget to smile too!"
                        show image "04_pt/slavem/wedding16c.jpg" with Dissolve(.3)
                        hide image "04_pt/slavem/wedding06.jpg"
                        w_jas_c[20] "Ah... blah... Blah... cum... hah... blah..."
                        cr2 "ha-ha-ha! look at her silly face!"
                        cr1 "I think she completely lost it!"
                        cr3 "Such a disgrace! Never thought I will live to see anything like that."
                        cr4 "Shame... Such a shame... I used to be a big fan of the Princess Jasmine you know, but after today's shameless display..."
                        jaf_c[8] "And now to the grand finale! I'm about to cum!"
                        jaf_c[8] "Are you ready, whore???"
                        w_jas_c[20] "Blah, blah... Imha cumminga..."
                        cr1 "She is ready!"
                        cr4 "Yeah! Fill that cunt with cum, Jafar! Make yourself a little prince!!! ha-ha-ha!"
                        cr1 "Yeah, impregnate that bitch! Cum inside of her!"
                        cr5 "Cum! Cum! Cum! Cum!"
                        jaf_c[8] "The people have spoken, my love."
                        w_jas_c[20] "Blah... Blah..."
                        jaf_c[8] "Here it comes then!"
                        w_jas_c[20] "!!!!!???????????????"
                        jaf8b "Argh! Take it all you whore!!!!"
                        show image "04_pt/slavem/wedding15c.jpg" with Dissolve(.3)
                        with hpunch
                        hide image "04_pt/slavem/wedding16c.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7            
                        w_jas_c[21] "AAAAAAHHHH!!!"
                        stop music fadeout 5
                        jaf[8] "Alright, slave, my last wish..."
                        jaf[8] "I wish for you to become human!"
                        with hpunch
                        g4 "What did he just say?" 
                        show whitefade with Dissolve(.4)
                        jaf[1] "I wish for you to become human!"
                        with hpunch
                        g4 "Argh! My head..."
                        g4 "I refuse to obey..."
                        show image "interface/white.jpg" with Dissolve(.4)
                        jump dream_04
                    
                    if dress02: 
                        show image "04_pt/slavem/wedding11.jpg" with fade
                        hide image "04_pt/slavem/dark.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        w_jas_b[2] "........."
                        w_jas_b[4] "........."
                        "Princess jasmine is wearing a wedding dress that leaves no room for imagination."
                        "Her shapely tits are in a plain view."
                        "You hear that people around you are starting to take notice of that."

                        cr1 "look, look at the princess... She is... Her... Her tits are just hanging out there!"
                        cr1 "I can see her breasts! I can see her breasts!"
                        w_jas_b[4] "........."
                        cr3 "Did Jafar force her to wear that vulgar outfit?"
                        cr2 "Doesn't look like it. She is smiling..."
                        cr2 "It's almost as if she is enjoying parading her naked tits shamelessly before us?"                     
                        cr1 "What a disgusting whore! She is mocking us!"

                        "The platform stops. Looks like the Sultan wants to address the people."
                        show image "04_pt/slavem/wedding02.jpg" with fade
                        hide image "04_pt/slavem/wedding11.jpg" 
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        jaf[4] "People of Agrabah."
                        jaf[4] "My loyal subjects."
                        jaf[4] "Thank you for attending our wedding parade today."

                        cr1 "Shut your mouth, Jafar! You suck!"                       
                        stop music 
                        $ renpy.play('sounds/scratch.wav')
                        jaf[5] "........."
                        jaf[3] "(You filthy peasants... How dare you....?)"
                        play music "music/Marketplace.mp3" fadein 1 fadeout 1
                        cr2 "My camel shits turds that are prettier than your face, jafar!"
                        cr1 "Ha-ha-ha! That's a good one, Mustafa!"
                        cr4 "Shut up you idiot, don't say my name."

                        
                        jaf[3] "Without further ado let me present you my bride..."
                        jaf[4] "Jasmine, the princess of agrabah!"
                        w_jas_b[2] "H-Hello everyone..."
                        cr1 "Filthy slut! Whore!"
                        w_jas_b[3] "................."
                        cr2 "Hey, princess I can see your tits!"
                        w_jas_b[4] "(ah.........)"
                        cr1"Hey, Princess jasmine, nice dress! Would shake you those jugs a bit for us? Ha-ha-ha!"
                        w_jas_b[9] "(ah... ah.........)"
                        cr3"Princess Jasmine, your highness, I beg you, please cover yourself! This is disgraceful!"

                        cr2 "Quiet wench! Clearly this one has no shame!"
                        cr1 "But, she is mocking us with her vulgarity!"

                        jaf[1] "(Go on with your speech, \"my love\"...)"
                        w_jas_b[3] "(Yes, master...)"

                        w_jas_b[5] "People of agrabah, thank you for showing up today..."
                        cr1 "You suck, you filthy slut!"
                        w_jas_b[4] "....."
                        cr2 "Yeah, shut your mouth! you betrayed Agrabah! you betrayed us all!"
                        cr1 "Traitor! Traitor! You will pay for this!!!"
                        w_jas_b[8] "???"
                        w_jas_b[6] "{size=-4}(I'm sorry...){/size}"

                        jaf[6] "(Keep going, slave...)"
                        w_jas_b[5] "...."
                        w_jas_b[5] "As a wedding present to you all I am wearing this humiliating outfit, to let all of you see me for what I am..."
                        cr1"A filthy whore!"
                        cr2 "Well said, Mustafa!"
                        cr4 "Shut up! Or I'll cut your ear off, I swear!"
                        cr1 "sorry..."
                        stop music fadeout 1
                        w_jas_b[5] "Y-yes... I am a..."
                        w_jas_b[5] "a..."
                        w_jas_b[9] "...a filthy whore..."
                        w_jas_b[5] "...Please look at me..."
                        cr1 "Huh..?"
                        w_jas_b[5] "Look at me... Shame me..."
                        w_jas_b[5] "I stand before you today, and present to you my bare tits."
                        w_jas_b[9] "And I allow you all to marvel at my poorly covered body..."
                        w_jas_b[5] "This is the only way I could show my appreciation and love to you..."
                        cr1 "Is she insane...?"
                        play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1
                        w_jas_b[5] "Please.... Look at me, all of you..."
                        
                        w_jas_b[6] "I am your shameless princess..."
                        cr5 "........."
                        cr5 "...."
                        w_jas_b[4] "......."
                        cr1 "What is going on here?"
                        cr2 "I can't believe this! What is she saying?!"
                        cr1 "Whore! Slut! Stone her to death!"
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        jaf[1] "(he-he. Splendid. But that's not all.)"
                        jaf[6] "(Keep going, slut.)"
                        w_jas_b[7]  "......"
                        w_jas_b[5] "Now I would like to present to you my beloved fiancee Jafar."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_b[5] "I... I ask you to accept him as... your..."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_b[9] "........"
                        w_jas_b[5] "As your rightful ruler... and... and..."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_b[5] "And... I..."
                        jaf[6] "(what's the matter, slut? Keep going!)"
                        w_jas_b[4] "I... I can't... everyone is looking at me..."
                        w_jas_b[4] "My... my body is on display..."
                        w_jas_b[4] "Everyone can see me in this embarrassing garment..."
                        jaf[6] "(So what? I said, keep talking, slave!)"
                        w_jas_b[5] "I... I can't... I'm almost... I'm about to..."                        
                        w_jas_b[8] "oh No!"
                        w_jas_b[8] "no. Not now, please..."
                        w_jas_b[8] "no... No... ....."
                        jaf[6] "(What are you talking about, slut?)"
                        stop music fadeout 10
                        w_jas_b[9] "(I'm cumming... Jafar, oh my god, I'm cumming!)"
                        w_jas_b[9] "(Please, don't let them see me like that!)"            
                        jaf[7] "(You're what?!)"
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        jaf[3] "(You worthless piece of camel shit! You're gonna ruin everything!)"
                        w_jas_b[9] "(No... I'm sorry.)"
                        w_jas_b[9] "(Please, don't talk to me like that, it only makes me come harder! Please, I can't hold it...)"
                        w_jas_b[9] "(I can't stop!)"
                        w_jas_b[11] "Here comes another one... Ah..."
                        w_jas_b[10] "(No, no... Not like this, not in front of all these people!)"
                        w_jas_b[10] "ah... ah..."
                        play music "music/The_calm_before_by_Calamaistr.mp3" fadein 2 fadeout 1
                        cr6 "Princess whore! Princess Whore! Princess Wh--"
                        show image "04_pt/slavem/wedding14b.jpg" with Dissolve(.3)
                        hide image "04_pt/slavem/wedding02.jpg"
                        cr1 "Huh? Hey, what is wrong with the princess!"                        
                        w_jas_b[13] "Ah... (Jafar, I'm begging you. Save me form this! Don't let them realize what's going on!) ah..."
                        cr1 "Is she sick or something? look at her..."
                        jaf[3] "(You fucking bitch, now I have to fix this mess!)"
                        jaf[4] "Khem..."
                        jaf[4] "Ladies and gentlemen. Can i have your attention for a second!?"
                        w_jas_b[12] "(Thank you Jafar! Thank you, thank you! I'm ... ah...)"
                        jaf[3] "If you would, please take a closer look at your beloved princess now!"
                        w_jas_b[11] "(What? No, Jafar, no, don't...)"
                        jaf[3] "At this very moment she is cumming violently!"
                        cr1 "What?"
                        cr2 "Is he serious?!"
                        jaf[3] "She is trying to hide it, but she is cumming like a filthy pig, again and again!"
                        w_jas_b[13] "No! Why... ah.... No..."
                        w_jas_b[11] "I'm cumming again!"
                        jaf[3] "You see? I guess showing off her body shamelessly like that just got our little princess a bit too exited..."
                        cr1 "I can not believe this..."
                        cr2 "Such a disgrace..."
                        w_jas_b[11] "I'M CUMMING AGAIN! I CAN'T STOP! EVERYONE FORGIVE ME! I'M CUMMING!"
                        jaf[3] "She's a filthy animal, isn't she??"
                        jaf[3] "I know! She deserves to be punished!"
                        cr1 "Yes! She is disgusting!"
                        cr2 "You shame agrabah, you filthy slut!"
                        w_jas_b[14] "Ohhh! This is unbearable! I can't stop..."
                        cr1 "Shut up you whore!"
                        cr3 "Stone her! Stone that bitch!"
                        cr2 "Throw her into the dungeons! She deserves no mercy!"
                        jaf[2] "(Great! They are all mine now!)"
                        jaf[4] "People of agrabah, What would you say if I were to punish her right here, infront of you!?"
                        w_jas_b[13] "ah.. What?"
                        cr1 "Yeah! Punish her!"
                        cr2 "Punish the bitch! Punish the bitch!"
                        jaf[3] "Come, here you slut!"
                        w_jas_b[13] "What?"
                        w_jas_b[13] "What are you...?"
                        show image "04_pt/slavem/wedding06.jpg" with fade
                        with hpunch
                        hide image "04_pt/slavem/wedding14b.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        cr5 "yes! Fuck her, jafar! Fuck that slut!"
                        w_jas_b[15] "AAAAAAAAH!!!"
                        w_jas_b[16] "NoOOOOOO! I...! I'm cumming!"
                        jaf_b[8] "That's just a begging, whore!"
                        cr1 "Hey? Can you hear me slut!? You whore! I wish i could fuck you too!"
                        cr2 "yeah! Fuck that bitch!"
                        w_jas_b[16] "No, don't fuck me like that!"
                        w_jas_b[16] "Not in front ..."
                        w_jas_b[16] "Of everyone! I will go insane..."
                        w_jas_b[16] "I can't stop cumming... I never came... like that ever... please... I ... no.... no..."
                        cr1 "Ha-ha-ha! Look at those udders fly!"
                        cr2 "Ha-ha-ha, you're right! Those are the royal tits my friend!"
                        cr1 "Princess's tit's those are! Look at them bounce!"
                        w_jas_b[17] "No, please stop saying such things... or I'll..."
                        w_jas_b[17] "............"
                        w_jas_b[17] "........"
                        w_jas_b[17] "..."
                        jaf_b[8] "Let me guess, whore. You're cumming again."
                        w_jas_b[16] "y-y-yeeeeeeees!!!!!!!!!!!"
                        jaf_b[8] "Are you done, whore?"
                        jaf_b[8] "You did not finish your speech, did you?"
                        w_jas_b[18] "what?... I... ah..."
                        w_jas_b[18] "No, you must be kidding...:"
                        jaf_b[8] "I said, finish your speech, whore!"
                        w_jas_b[18] "While... you...."
                        w_jas_b[17] "........"
                        w_jas_b[18] "Fucking me... and I keep cumming uncontrollably???..."
                        jaf_b[8] "I said, start talking, you whore!"
                        w_jas_b[17] "AH! I can't I'm cumming again!"
                        w_jas_b[17] "....."
                        jaf_b[8] "Do You disobey me?"
                        w_jas_b[18] "No, no, I'm sorry... I will try..."
                        w_jas_b[17] "......"
                        w_jas_b[19] "People ah... of.... ah... A-Agrabah... ah..."
                        cr1 "What is she blathering there?"
                        w_jas_b[19] "I ask ...ah... you to accept... jafar ... as... ah..."
                        w_jas_b[17] "....."
                        w_jas_b[16] "Sorry...."
                        w_jas_b[16] "Again..."
                        w_jas_b[16] "I'm sorry! I'm so sorry! I'M CUUUMING!"
                        cr3 "She is disgusting!"
                        cr5 "filthy Princess whore! filthy Princess whore!"
                        w_jas_b[19] "And Er ... ah... I'm sure... that... ah..."
                        w_jas_b[18] "no, not so hard!"
                        w_jas_b[16] "i'm cumming..."
                        w_jas_b[15] "I... I'm sure that sultan Jafar will bring..."
                        w_jas_b[19] "ah... prosperity to A-agrabah... ah..."
                        w_jas_b[19] "...and I w-will give him a healthy baby-boy to inherit the t-throne..."
                        jaf_b[8] "Yup! We gonna make one here today, you whore!"
                        cr1 "ha-ha-ha! never thought I will be a part of the royal honey moon!"
                        cr2 "Ha-ha-ha! Look at her silly face! You keep fucking that whore, jafar!"
                        cr1 "Yeah! Show her who's the sultan!"
                        w_jas_b[19] "And ah... the prosperity... ah..."
                        w_jas_b[19] "orgasm... and... ah... the royal pussy, I mean family..."
                        w_jas_b[17] "ah... cumming... ah... peasants are watching... ah... my sultan jafar... ah..."
                        w_jas_b[17] "and please... ah... whore... ah cumming again..."
                        cr1 "What is she talking about now? Can you understand what she's saying?"
                        
                        cr2"Can you make any sense of what she is saying, Mustafa?"
                        cr4"Alright, that does it, come here, you fool!"
                        cr2"Ah, no, not my ear! Get off me! Not my ear!"
                        cr1 "I think she just  went mad from having too many orgasms at once..."
                        w_jas_b[16] "Ah... blah... slut... whore..."
                        w_jas_b[16] "I'm a whore.. look at me... I'm cumming..."
                        w_jas_b[16] "Can't stop cumming... I..."
                        w_jas_b[16] "ah.... Princess...filthy slut..."
                        jaf_b[8] "What is it, whore? About to pass out, are you?"
                        jaf_b[8] "Not yet! I'm still fucking ya sorry ass!"
                        jaf_b[8] "Now be a good whore  and show some respect to all these nice people!"
                        jaf_b[8] "Look at them while I will be filling you with my cum!"
                        jaf_b[8] "And don't forget to smile too!"
                        show image "04_pt/slavem/wedding16b.jpg" with Dissolve(.3)
                        hide image "04_pt/slavem/wedding06.jpg"
                        w_jas_b[20] "Ah... blah... Blah... cum... hah... blah..."
                        cr2 "ha-ha-ha! look at her silly face!"
                        cr1 "I think she completely lost it!"
                        cr3 "Such a disgrace! Never thought I will live to see anything like that."
                        cr4 "Shame... Such a shame... I used to be a big fan of the Princess Jasmine you know, but after today's shameless display..."
                        jaf_b[8] "And now to the grand finale! I'm about to cum!"
                        jaf_b[8] "Are you ready, whore???"
                        w_jas_b[20] "Blah, blah... Imha cumminga..."
                        cr1 "She is ready!"
                        cr4 "Yeah! Fill that cunt with cum, Jafar! Make yourself a little prince!!! ha-ha-ha!"
                        cr1 "Yeah, impregnate that bitch! Cum inside of her!"
                        cr5 "Cum! Cum! Cum! Cum!"
                        jaf_b[8] "The people have spoken, my love."
                        w_jas_b[20] "Blah... Blah..."
                        jaf_b[8] "Here it comes then!"
                        w_jas_b[20] "!!!!!???????????????"
                        jaf_b[8] "Argh! Take it all you whore!!!!"
                        show image "04_pt/slavem/wedding15b.jpg" with Dissolve(.3)
                        with hpunch
                        hide image "04_pt/slavem/wedding16b.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7            
                        w_jas_b[21] "AAAAAAHHHH!!!"
                        stop music fadeout 5
                        jaf_b[8] "Alright, slave, my last wish..."
                        jaf_b[8] "I wish for you to become human!"
                        g4 "What did he just say?" 
                        show whitefade with Dissolve(.4)
                        jaf[1] "I wish for you to become human!"
                        with hpunch
                        g4 "Argh! My head..."
                        g4 "I refuse to obey..."
                        show image "interface/white.jpg" with Dissolve(.4)
                        jump dream_04

                    if dress03:
                        show image "04_pt/slavem/wedding12.jpg" with fade
                        hide image "04_pt/slavem/dark.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        w_jas_a[2] "........."
                        w_jas_a[4] "........."
                        "Princess jasmine is wearing a wedding dress that leaves no room for imagination."
                        "Her shapely tits are barely covered by thin lines of fabric."
                        "You hear that people around you are starting to take notice of that."

                        cr1 "look, look at the princess... She is... Her... Her tits are barely covered..."
                        cr1 "I think I can see her left nipple!"
                        w_jas_a[4] "........."
                        cr3 "Did Jafar force her to wear that vulgar outfit?"
                        cr2 "Doesn't look like it. She is smiling..."
                        cr2 "It's almost like if she is enjoying parading her half-naked tits shamelessly before us like that?!"                     
                        cr1 "What a disgusting whore! She is mocking us!"

                        "The platform stops. Looks like the Sultan wants to address the people."
                        show image "04_pt/slavem/wedding03.jpg" with fade
                        hide image "04_pt/slavem/wedding12.jpg" 
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        jaf[4] "People of Agrabah."
                        jaf[4] "My loyal subjects."
                        jaf[4] "Thank you for attending our wedding parade today."

                        cr1 "Shut your mouth, Jafar! You suck!"
                        stop music 
                        $ renpy.play('sounds/scratch.wav')
                        jaf[5] "........."
                        jaf[3] "(You filthy peasants... How dare you....?)"
                        play music "music/Marketplace.mp3" fadein 1 fadeout 1
                        cr2 "My camel shits turds that are prettier than your face, jafar!"
                        cr1 "Ha-ha-ha! That's a good one, Mustafa!"
                        cr4 "Shut up you idiot, don't say my name, you fool."

                        
                        jaf[3] "Without further ado let me present you my bride..."
                        jaf[4] "jasmine, the princess of agrabah!"
                        w_jas_a[2] "H-Hello everyone..."
                        cr1 "Filthy slut! Whore!"
                        w_jas_a[3] "................."
                        cr2 "Hey, princess show us your tits!"
                        w_jas_a[4] "........."
                        cr1"I can almost see her bush too, I'm not complaining! Ha-ha-ha!"
                        cr3"That's because you're a simpleminded idiot! This kind of behavior is unacceptable!"
                        cr2"Yes! She has no shame! She is mocking us with her vulgarity!"

                        jaf[1] "(Go on with your speech, \"my love\"...)"
                        w_jas_a[3] "(Yes, master...)"

                        w_jas_a[5] "People of agrabah, thank you for showing up today..."
                        cr1 "You suck, you filthy slut!"
                        cr2 "Yeah, shut your mouth! you betrayed Agrabah! you betrayed us all!"

                        jaf[6] "(Keep going, slave...)"
                        w_jas_a[5] "As a wedding present to you all I am wearing this humiliating outfit, to let all of you see me for what I am..."
                        cr1"A filthy whore!"
                        cr2 "Well said, Mustafa!"
                        cr4 "Shut up! Or I'll cut your ear off, I swear!"
                        cr1 "sorry..."
                        stop music fadeout 1
                        w_jas_a[5] "Y-yes... I am a filthy whore..."
                        w_jas_a[5] "Please look at me..."
                        cr1 "Huh..?"
                        play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1
                        w_jas_a[5] "Look at me... Shame me..."
                        w_jas_a[5] "I stand before you today, and allow you all to look at my poorly covered body..."
                        w_jas_a[5] "This is the only way I could show my appreciation and love to you..."
                        cr1 "Is she insane...?"
                        w_jas_a[5] "Please.... Look at me, all of you..."
                        w_jas_a[6] "I am your shameless princess..."
                        cr5 "........."
                        cr5 "...."
                        w_jas_a[4] "......."
                        cr1 "What is going on here?"
                        cr2 "I can't believe this! What is she saying?!"
                        cr1 "Whore! Slut! Stone her!"
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        jaf[1] "(he-he. Splendid. But that's not all.)"
                        jaf[6] "(Keep going, slut.)"
                        w_jas_a[7]  "......"
                        w_jas_a[5] "Now I would like to present to you my beloved fiancee, Jafar."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_a[5] "I... I ask you to accept him as... your..."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_a[5] "As your rightful ruler... and... and..."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_a[5] "And... I..."
                        jaf[6] "(what's the matter, slut? Keep going!)"
                        w_jas_a[4] "I... I can't... everyone is looking at me..."
                        w_jas_a[4] "My... my body is on display..."
                        w_jas_a[4] "Everyone can see me in this embarrassing garment..."
                        jaf[6] "(So what? I said, keep talking, slave!)"
                        w_jas_a[5] "I... I can't... I'm almost... I'm about to..."
                        w_jas_a[8] "oh No!"
                        w_jas_a[8] "no. Not now, please..."
                        w_jas_a[8] "no... No... ....."
                        jaf[6] "(What are you talking about, slut?)"
                        stop music fadeout 10
                        w_jas_a[9] "(I'm cumming... Jafar, oh my god, I'm cumming!)"
                        w_jas_a[9] "(Please, don't let them see me like that!)"            
                        jaf[7] "(You're what?!)"
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        jaf[3] "(You worthless piece of camel shit! You gonna ruin everything!)"
                        w_jas_a[9] "(No... I'm sorry.)"
                        w_jas_a[9] "(Please, don't talk to me like that, it only makes me come harder! Please, I can't hold it...)"
                        w_jas_a[9] "(I can't stop!)"
                        w_jas_a[11] "Here comes another one... Ah..."
                        w_jas_a[10] "(No, no... Not like this, not in front of all these people!)"
                        w_jas_a[10] "ah... ah..."
                        play music "music/The_calm_before_by_Calamaistr.mp3" fadein 2 fadeout 1
                        cr6 "Princess whore! Princess Whore! Princess Wh--"
                        show image "04_pt/slavem/wedding14.jpg" with Dissolve(.3)
                        hide image "04_pt/slavem/wedding03.jpg"
                        cr1 "Huh? Hey, what is wrong with the princess!"
                        w_jas_a[13] "Ah... (Jafar, I'm begging you. Save me form this! Don't let them realize what's going on!) ah..."
                        cr1 "Is she sick or something look at her..."
                        jaf[3] "(You fucking bitch, now I have to fix this mess!)"
                        jaf[4] "Khem..."
                        jaf[4] "Ladies and gentlemen. Can i have your attention for a second!?"
                        w_jas_a[12] "(Thank you Jafar! Thank you, thank you! I'm ... ah...)"
                        jaf[3] "If you would, please take a closer look at your beloved princess now!"
                        w_jas_a[11] "(What? No, Jafar, no, don't...)"
                        jaf[3] "At this very moment she is cumming violently!"
                        cr1 "What?"
                        cr2 "Is he serious?!"
                        jaf[3] "She is trying to hide it, but she is cumming like a filthy pig, again and again!"
                        w_jas_a[13] "No! Why... ah.... No..."
                        w_jas_a[11] "I'm cumming again!"
                        jaf[3] "You see? I guess showing off her body shamelessly like that just got our little princess a bit too exited..."
                        cr1 "I can not believe this..."
                        cr2 "Such a disgrace..."
                        w_jas_a[11] "I'M CUMMING AGAIN! I CAN'T STOP! EVERYONE FORGIVE ME! I'M CUMMING!"
                        jaf[3] "She's a filthy animal, isn't she?"
                        jaf[3] "I know! She deserves to be punished!"
                        cr1 "Yes! She is disgusting!"
                        cr2 "You shame agrabah, you filthy slut!"
                        w_jas_a[14] "Ohhh! This is unbearable! I can't stop..."
                        cr1 "Shut up you whore!"
                        cr3 "Stone her! Stone that bitch!"
                        cr2 "Throw her into the dungeons! She deserves no mercy!"
                        jaf[2] "(Great! They are mine now!)"
                        jaf[4] "What would you say if I were to punish her right here, in front of you!?"
                        w_jas_a[13] "ah.. What?"
                        cr1 "Yeah! Punish her!"
                        cr2 "Punish the bitch! Punish the bitch!"
                        jaf[3] "Come, here you slut!"
                        w_jas_a[13] "What?"
                        w_jas_a[13] "What are you...?"
                        show image "04_pt/slavem/wedding08.jpg" with fade
                        with hpunch
                        hide image "04_pt/slavem/wedding14.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        cr5 "yes! Fuck her, jafar! Fuck that slut!"
                        w_jas_a[15] "AAAAAAAAH!!!"
                        w_jas_a[16] "NoOOOOOO! I...! I'm cumming!"
                        jaf[8] "That's just a begging, whore!"
                        cr1 "You hear me slut! You whore! I wish i could fuck you!"
                        cr2 "yeah! Fuck that bitch!"
                        w_jas_a[16] "No, don't fuck me like that!"
                        w_jas_a[16] "Not in front ..."
                        w_jas_a[16] "Of everyone! I will go insane..."
                        w_jas_a[16] "I can't stop cumming... I never came... like that ever... please... I ... no.... no..."
                        cr1 "Ha-ha-ha! Look at those udders fly!"
                        cr2 "Ha-ha-ha, you're right! Those are the royal tits my friend!"
                        cr1 "Princess's tit's those are! Look at them bounce!"
                        w_jas_a[17] "No, please stop saying such things... or I'll..."
                        w_jas_a[17] "............"
                        w_jas_a[17] "........"
                        w_jas_a[17] "..."
                        jaf[8] "Let me guess, whore. You're cumming again."
                        w_jas_a[16] "y-y-yeeeeeeees!!!!!!!!!!!"
                        jaf[8] "Are you done, whore?"
                        jaf[8] "You did not finish your speech, did you?"
                        w_jas_a[18] "what?... I... ah..."
                        w_jas_a[18] "No, you must be kidding...:"
                        jaf[8] "I said, finish your speech, whore!"
                        w_jas_a[18] "While... you...."
                        w_jas_a[17] "........"
                        w_jas_a[18] "Fucking me... and I keep cumming uncontrollably???..."
                        jaf[8] "I said, start talking, you whore!"
                        w_jas_a[17] "AH! I can't I'm cumming again!"
                        w_jas_a[17] "....."
                        jaf[8] "You disobey me?"
                        w_jas_a[18] "No, no, I'm sorry... I will try..."
                        w_jas_a[17] "......"
                        w_jas_a[19] "People ah... of.... ah... A-Agrabah... ah..."
                        cr1 "What is she blathering there?"
                        w_jas_a[19] "I ask ...ah... you to accept... jafar ... as... ah..."
                        w_jas_a[17] "....."
                        w_jas_a[16] "Sorry...."
                        w_jas_a[16] "Again..."
                        w_jas_a[16] "I'm sorry! I'm so sorry! I'M CUUUMING!"
                        cr3 "She is disgusting!"
                        cr5 "filthy Princess whore! filthy Princess whore!!"
                        w_jas_a[19] "And Er ... ah... I'm sure... that... ah..."
                        w_jas_a[18] "no, not so hard!"
                        w_jas_a[16] "i'm cumming..."
                        w_jas_a[15] "I... I'm sure that sultan Jafar will bring..."
                        w_jas_a[19] "ah... prosperity to A-agrabah... ah... and I w-will give him a healthy baby-boy to inherit the t-throne..."
                        jaf[8] "Yup! We gonna make one here today, you whore!"
                        cr1 "ha-ha-ha! never thought I will be a part of the royal honey moon!"
                        cr2 "Ha-ha-ha! Look at her silly face! You keep fucking that whore, jafar!"
                        cr1 "Yeah! Show her who's the sultan!"
                        w_jas_a[19] "And ah... the prosperity... ah..."
                        w_jas_a[19] "orgasm... and... ah... the royal pussy, I mean family..."
                        w_jas_a[17] "ah... cumming... ah... all is watching... ah... my sultan jafar... ah..."
                        w_jas_a[17] "and please... ah... whore... ah cumming again..."
                        cr1 "What is she talking about now? Can you understand what she's saying?"
                        cr2 "I think she just went mad from experiencing so many orgasms at once..."
                        w_jas_a[16] "Ah... blah... slut... whore..."
                        w_jas_a[16] "whore.. look at me... I'm cumming..."
                        w_jas_a[16] "Can't stop cumming... I..."
                        w_jas_a[16] "ah.... Princess...filthy slut..."
                        jaf[8] "What is it, whore? About to pass out, are you?"
                        jaf[8] "Not yet! I'm still fucking ya sorry ass!"
                        jaf[8] "Now be a good whore  and show some respect to all those nice people!"
                        jaf[8] "Look at them while I'll be filling you with my cum!"
                        jaf[8] "And don't forget to smile too!"
                        show image "04_pt/slavem/wedding16.jpg" with Dissolve(.3)
                        hide image "04_pt/slavem/wedding14.jpg"
                        w_jas_a[20] "Ah... blah... Blah... cum... hah... blah..."
                        cr2 "ha-ha-ha! look at her silly face!"
                        cr1 "I think she completely lost it!"
                        cr3 "Such a disgrace! Never thought I will live to see anything like that."
                        cr4 "Shame... Such a shame... I used to be a big fan of the Princess jasmine you know, but after today's shameless display..."
                        jaf[8] "And now to the grand finale! I'm about to cum!"
                        jaf[8] "Are you ready, whore???"
                        w_jas_a[20] "Blah, blah... Imha cumminga..."
                        cr1 "She is ready!"
                        cr4 "Yeah! Fill that cunt with cum, Jafar! Make yourself a little prince!!! ha-ha-ha!"
                        cr1 "Yeah, impregnate that bitch! Cum inside of her!"
                        cr5 "Cum! Cum! Cum! Cum!"
                        jaf[8] "The people have spoken, my love."
                        w_jas_a[20] "Blah... Blah..."
                        jaf[8] "Here it comes then!"
                        w_jas_a[20] "!!!!!???????????????"
                        jaf[8] "Argh! Take it all you whore!!!!"
                        show image "04_pt/slavem/wedding15.jpg" with Dissolve(.3)
                        with hpunch
                        hide image "04_pt/slavem/wedding16.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7            
                        w_jas_a[21] "AAAAAAHHHH!!!"
#######################################################
                        stop music fadeout 5
                        jaf[8] "Alright, slave, my last wish..."
                        jaf[8] "I wish for you to become human!"
                        g4 "What did he just say?" 
                        show whitefade with Dissolve(.4)
                        jaf[1] "I wish for you to become human!"
                        with hpunch
                        g4 "Argh! My head..."
                        g4 "I refuse to obey..."
                        show image "interface/white.jpg" with Dissolve(.4)
                        jump dream_04
                        
                    if dress04:
                        show image "04_pt/slavem/wedding12n.jpg" with fade
                        hide image "04_pt/slavem/dark.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        w_jas_n[2] "........."
                        w_jas_n[1] "........."
                        "Princess jasmine is fully naked."
                        "Her shapely tits are in the plan view."
                        "The crowd around suddenly turns silent..."

                        cr1 "She's..."
                        cr1 "She's naked..."
                        cr1 "Look, look at the princess!"
                        cr1 "I can see her tits!"
                        cr2 "Forget her tits! I can see her pussy!"
                        w_jas_n[4] "........."
                        cr3 "Did Jafar force her to do this?"
                        cr2 "Doesn't look like it. She is smiling..."
                        cr2 "It's almost like if she is enjoying parading her naked tits shamelessly before us like that?!"                     
                        cr1 "What a disgusting whore! She is mocking us!"

                        ">The platform stops. Looks like the Sultan wants to address the people."
                        show image "04_pt/slavem/wedding14n.jpg" with fade
                        hide image "04_pt/slavem/wedding12n.jpg" 
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        jaf[4] "People of Agrabah."
                        jaf[4] "My loyal subjects."
                        jaf[4] "Thank you for attending our wedding parade today."

                        cr1 "Shut your mouth, Jafar! You suck!"
                        stop music 
                        $ renpy.play('sounds/scratch.wav')
                        jaf[5] "........."
                        jaf[3] "(You filthy peasants... How dare you....?)"
                        play music "music/Marketplace.mp3" fadein 1 fadeout 1
                        cr2 "My camel shits turds that are prettier than your face, jafar!"
                        cr1 "Ha-ha-ha! That's a good one, Mustafa!"
                        cr4 "Shut up you idiot, don't say my name, you fool."

                        
                        jaf[3] "Without further ado let me present you my bride..."
                        jaf[4] "Jasmine, the princess ofAgrabah!"
                        w_jas_n[2] "H-Hello everyone..."
                        cr1 "Shameless slut! Whore!"
                        w_jas_n[3] "................."
                        cr2 "Hey, princess, nice tits!"
                        w_jas_n[4] "........."
                        cr1 "I can see her bush too, I'm not complaining! Ha-ha-ha!"
                        cr3 "That's because you're a simpleminded idiot! This kind of behavior is unacceptable!"
                        cr2 "Yes! She has no shame! She is mocking us with her nakedness!"

                        jaf[1] "(Go on with your speech, \"my love\"...)"
                        w_jas_n[3] "(Yes, master...)"

                        w_jas_n[5] "People of Agrabah, thank you for showing up today..."
                        cr1 "You suck, you filthy slut!"
                        cr2 "Yeah, shut your mouth! you betrayed Agrabah! you betrayed us all!"

                        jaf[6] "(Keep going, slave...)"
                        w_jas_n[5] "As a wedding present to you all I am letting you see my naked body, to let all of you understand what I really ma..."
                        cr1"A filthy whore!"
                        cr2 "Well said, Mustafa!"
                        cr4 "Shut up! Or I'll cut your ear off, I swear!"
                        cr1 "sorry..."
                        stop music fadeout 1
                        w_jas_n[5] "Y-yes... I am a filthy whore..."
                        w_jas_n[5] "Please look at me... Look at my naked body..."
                        cr1 "Huh..?"
                        play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1
                        w_jas_n[5] "Look at me... Shame me..."
                        w_jas_n[5] "I stand before you today, and allow you all to look at my bare tits..."
                        w_jas_n[5] "This is the only way I could show my appreciation and love to you..."
                        cr1 "Is she insane...?"
                        w_jas_n[5] "Please.... Look at me, all of you..."
                        w_jas_n[6] "I am your shameless princess..."
                        cr5 "........."
                        cr5 "...."
                        w_jas_n[4] "......."
                        cr1 "What is going on here?"
                        cr2 "I can't believe this! What is she saying?!"
                        cr1 "Whore! Slut! Stone her!"
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        jaf[1] "(he-he. Splendid. But that's not all.)"
                        jaf[6] "(Keep going, slut.)"
                        w_jas_n[7]  "......"
                        w_jas_n[5] "Now I would like to present to you my beloved fiancee, Jafar."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_n[5] "I... I ask you to accept him as... your..."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_n[5] "As your rightful ruler... and... and..."
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        w_jas_n[5] "And... I..."
                        jaf[6] "(what's the matter, slut? Keep going!)"
                        w_jas_n[4] "I... I can't... everyone is looking at me..."
                        w_jas_n[4] "My... my body is on display..."
                        w_jas_n[4] "Everyone can see me in this embarrassing garment..."
                        jaf[6] "(So what? I said, keep talking, slave!)"
                        w_jas_n[5] "I... I can't... I'm almost... I'm about to..."
                        w_jas_n[8] "oh No!"
                        w_jas_n[8] "no. Not now, please..."
                        w_jas_n[8] "no... No... ....."
                        jaf[6] "(What are you talking about, slut?)"
                        stop music fadeout 10
                        w_jas_n[9] "(I'm cumming... Jafar, oh my god, I'm cumming!)"
                        w_jas_n[9] "(Please, don't let them see me like that!)"            
                        jaf[7] "(You're what?!)"
                        cr6 "Princess whore! Princess Whore! Princess Whore!"
                        jaf[3] "(You worthless piece of camel shit! You gonna ruin everything!)"
                        w_jas_n[9] "(No... I'm sorry.)"
                        w_jas_n[9] "(Please, don't talk to me like that, it only makes me come harder! Please, I can't hold it...)"
                        w_jas_n[9] "(I can't stop!)"
                        w_jas_n[11] "Here comes another one... Ah..."
                        w_jas_n[10] "(No, no... Not like this, not in front of all these people!)"
                        w_jas_n[10] "ah... ah..."
                        play music "music/The_calm_before_by_Calamaistr.mp3" fadein 2 fadeout 1
                        cr6 "Princess whore! Princess Whore! Princess Wh--"
                        cr1 "Huh? Hey, what is wrong with the princess!"
                        w_jas_n[13] "Ah... (Jafar, I'm begging you. Save me form this! Don't let them realize what's going on!) ah..."
                        cr1 "Is she sick or something look at her..."
                        jaf[3] "(You fucking bitch, now I have to fix this mess!)"
                        jaf[4] "Khem..."
                        jaf[4] "Ladies and gentlemen. Can i have your attention for a second!?"
                        w_jas_n[12] "(Thank you Jafar! Thank you, thank you! I'm ... ah...)"
                        jaf[3] "If you would, please take a closer look at your beloved princess now!"
                        w_jas_n[11] "(What? No, Jafar, no, don't...)"
                        jaf[3] "At this very moment she is cumming violently!"
                        cr1 "What?"
                        cr2 "Is he serious?!"
                        jaf[3] "She is trying to hide it, but she is cumming like a filthy pig, again and again!"
                        w_jas_n[13] "No! Why... ah.... No..."
                        w_jas_n[11] "I'm cumming again!"
                        jaf[3] "You see? I guess showing off her body shamelessly like that just got our little princess a bit too exited..."
                        cr1 "I can not believe this..."
                        cr2 "Such a disgrace..."
                        w_jas_n[11] "I'M CUMMING AGAIN! I CAN'T STOP! EVERYONE FORGIVE ME! I'M CUMMING!"
                        jaf[3] "She's a filthy animal, isn't she?"
                        jaf[3] "I know! She deserves to be punished!"
                        cr1 "Yes! She is disgusting!"
                        cr2 "You shame agrabah, you filthy slut!"
                        w_jas_n[14] "Ohhh! This is unbearable! I can't stop..."
                        cr1 "Shut up you whore!"
                        cr3 "Stone her! Stone that bitch!"
                        cr2 "Throw her into the dungeons! She deserves no mercy!"
                        jaf[2] "(Great! They are mine now!)"
                        jaf[4] "What would you say if I were to punish her right here, in front of you!?"
                        w_jas_n[13] "ah.. What?"
                        cr1 "Yeah! Punish her!"
                        cr2 "Punish the bitch! Punish the bitch!"
                        jaf[3] "Come, here you slut!"
                        w_jas_n[13] "What?"
                        w_jas_n[13] "What are you...?"
                        show image "04_pt/slavem/wedding04n.jpg" with fade
                        with hpunch
                        hide image "04_pt/slavem/wedding14n.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7
                        cr5 "yes! Fuck her, jafar! Fuck that slut!"
                        w_jas_n[15] "AAAAAAAAH!!!"
                        w_jas_n[16] "NoOOOOOO! I...! I'm cumming!"
                        jaf_n[8] "That's just a begging, whore!"
                        cr1 "You hear me slut! You whore! I wish i could fuck you!"
                        cr2 "yeah! Fuck that bitch!"
                        w_jas_n[16] "No, don't fuck me like that!"
                        w_jas_n[16] "Not in front ..."
                        w_jas_n[16] "Of everyone! I will go insane..."
                        w_jas_n[16] "I can't stop cumming... I never came... like that ever... please... I ... no.... no..."
                        cr1 "Ha-ha-ha! Look at those udders fly!"
                        cr2 "Ha-ha-ha, you're right! Those are the royal tits my friend!"
                        cr1 "Princess's tit's those are! Look at them bounce!"
                        w_jas_n[17] "No, please stop saying such things... or I'll..."
                        w_jas_n[17] "............"
                        w_jas_n[17] "........"
                        w_jas_n[17] "..."
                        jaf_n[8] "Let me guess, whore. You're cumming again."
                        w_jas_n[16] "y-y-yeeeeeeees!!!!!!!!!!!"
                        jaf_n[8] "Are you done, whore?"
                        jaf_n[8] "You did not finish your speech, did you?"
                        w_jas_n[18] "what?... I... ah..."
                        w_jas_n[18] "No, you must be kidding...:"
                        jaf_n[8] "I said, finish your speech, whore!"
                        w_jas_n[18] "While... you...."
                        w_jas_n[17] "........"
                        w_jas_n[18] "Fucking me... and I keep cumming uncontrollably???..."
                        jaf_n[8] "I said, start talking, you whore!"
                        w_jas_n[17] "AH! I can't I'm cumming again!"
                        w_jas_n[17] "....."
                        jaf_n[8] "You disobey me?"
                        w_jas_n[18] "No, no, I'm sorry... I will try..."
                        w_jas_n[17] "......"
                        w_jas_n[19] "People ah... of.... ah... A-Agrabah... ah..."
                        cr1 "What is she blathering there?"
                        w_jas_n[19] "I ask ...ah... you to accept... jafar ... as... ah..."
                        w_jas_n[17] "....."
                        w_jas_n[16] "Sorry...."
                        w_jas_n[16] "Again..."
                        w_jas_n[16] "I'm sorry! I'm so sorry! I'M CUUUMING!"
                        cr3 "She is disgusting!"
                        cr5 "filthy Princess whore! filthy Princess whore!!"
                        w_jas_n[19] "And Er ... ah... I'm sure... that... ah..."
                        w_jas_n[18] "no, not so hard!"
                        w_jas_n[16] "i'm cumming..."
                        w_jas_n[15] "I... I'm sure that sultan Jafar will bring..."
                        w_jas_n[19] "ah... prosperity to A-agrabah... ah... and I w-will give him a healthy baby-boy to inherit the t-throne..."
                        jaf_n[8] "Yup! We gonna make one here today, you whore!"
                        cr1 "ha-ha-ha! never thought I will be a part of the royal honey moon!"
                        cr2 "Ha-ha-ha! Look at her silly face! You keep fucking that whore, jafar!"
                        cr1 "Yeah! Show her who's the sultan!"
                        w_jas_n[19] "And ah... the prosperity... ah..."
                        w_jas_n[19] "orgasm... and... ah... the royal pussy, I mean family..."
                        w_jas_n[17] "ah... cumming... ah... all is watching... ah... my sultan jafar... ah..."
                        w_jas_n[17] "and please... ah... whore... ah cumming again..."
                        cr1 "What is she talking about now? Can you understand what she's saying?"
                        cr2 "I think she just went mad from experiencing so many orgasms at once..."
                        w_jas_n[16] "Ah... blah... slut... whore..."
                        w_jas_n[16] "whore.. look at me... I'm cumming..."
                        w_jas_n[16] "Can't stop cumming... I..."
                        w_jas_n[16] "ah.... Princess...filthy slut..."
                        jaf_n[8] "What is it, whore? About to pass out, are you?"
                        jaf_n[8] "Not yet! I'm still fucking ya sorry ass!"
                        jaf_n[8] "Now be a good whore  and show some respect to all those nice people!"
                        jaf_n[8] "Look at them while I'll be filling you with my cum!"
                        jaf_n[8] "And don't forget to smile too!"
                        show image "04_pt/slavem/wedding16n2.jpg" with Dissolve(.3)
                        hide image "04_pt/slavem/wedding04n.jpg"
                        w_jas_n[20] "Ah... blah... Blah... cum... hah... blah..."
                        cr2 "ha-ha-ha! look at her silly face!"
                        cr1 "I think she completely lost it!"
                        cr3 "Such a disgrace! Never thought I will live to see anything like that."
                        cr4 "Shame... Such a shame... I used to be a big fan of the Princess Jasmine you know, but after today's shameless display..."
                        jaf_n[8] "And now to the grand finale! I'm about to cum!"
                        jaf_n[8] "Are you ready, whore???"
                        w_jas_n[20] "Blah, blah... Imha cumminga..."
                        cr1 "She is ready!"
                        cr4 "Yeah! Fill that cunt with cum, Jafar! Make yourself a little prince!!! ha-ha-ha!"
                        cr1 "Yeah, impregnate that bitch! Cum inside of her!"
                        cr5 "Cum! Cum! Cum! Cum!"
                        jaf_n[8] "The people have spoken, my love."
                        w_jas_n[20] "Blah... Blah..."
                        jaf_n[8] "Here it comes then!"
                        w_jas_n[20] "!!!!!???????????????"
                        jaf_n[8] "Argh! Take it all you whore!!!!"
                        show image "04_pt/slavem/wedding16n.jpg" with Dissolve(.3)
                        with hpunch
                        hide image "04_pt/slavem/wedding16n2.jpg"
                        show con1 at right
                        show ctc7 at right
                        pause 
                        hide con1
                        hide ctc7            
                        w_jas_n[21] "AAAAAAHHHH!!!"
#######################################################
                        stop music fadeout 5
                        jaf_n[8] "Alright, slave, my last wish..."
                        jaf_n[8] "I wish for you to become human!"
                        g4 "What did he just say?" 
                        show whitefade with Dissolve(.4)
                        jaf[1] "I wish for you to become human!"
                        with hpunch
                        g4 "Argh! My head..."
                        g4 "I refuse to obey..."
                        show image "interface/white.jpg" with Dissolve(.4)
                        jump dream_04
        



            
            
            
            


        "-Leave...-":
            show blkfade with d5
            pause.5
            hide image "04_pt/slavem/bld.png" 
            hide blkfade with d5
            jump lastday2
            jump lastday2
    
    
        
if select == "brothel":
    
    
    if redphoenix:
        "\"The Red Phoenix\" brothel....."
        "The place is closed for today..."
        jump lastday2        
    else:
        "\"The Red Phoenix\" brothel....."
        menu:
            "-Enter the building-":
                $ renpy.play('sounds/door.mp3')
                show blkfade with d3
                pause.5
                show bld behind blkfade
                hide blkfade with d3
                sch3 "Hi there, handsome."
                sch3 "I'm afraid we are closed today..."
                sch3 "Haven't you heard? The royal wedding is tomorrow!"
                sch3 "Everybody is so exited about the upcoming wedding parade..." 
                sch3 "To be honest I can barely contain the excitement myself!"
                show blkfade with d3
                pause.5
                hide blkfade with d3
                ">\"The Red Phoenix\" brothel....."
                ">Jasmine used to work here..."
                ">You remember how she would come from work all sweaty and covered in cum, but satisfied and with a good sum of money..."
                "......"
                ">For some reason you don't feel like spending too much time in lily's company and decide to leave..."
                $ redphoenix = True
                $ renpy.play('sounds/door2.mp3')
                hide bld with d3
                jump lastday2
                                                                                                                  

            "-Never mind...-":
                
                jump lastday2
                
    
    

if select == "shop":    
    if finaldaystore:
        ">The store is closed for today..."
        jump lastday2        
    else:
        ">The store is closed for today..."
        menu:
            "There is a sign on the door: \"Closed for today due to upcoming parade\"."
            "-Enter the store-":
                $ renpy.play('sounds/door.mp3')
                show blkfade with d5
                pause.5
                show image "04_pt/slavem/bld.png" behind blkfade
                hide blkfade with d5
                aza[3] "Well, If it isn't my favorite customer!"
                aza[1] "My store is closed for today, sweetie."
                lola[11] "Haven't you heard, old man? Our slave-princess is getting married tomorrow."
                m "Lola?"
                lola[13] "Yo!"
                aza[1] "...."
                aza[1] "I've been hearing all sorts of rumors about the Princess lately..."
                lola[12] "All of which are true!"
                aza[1] "Hm..."
                aza[5] "She used to be my idol, but now I'm not sure what to think anymore..."
                aza[1] "Nevertheless, I can't wait to see what Princess Jasmine is going to wear for her wedding."
                lola[11] "Me too! Me too!"
                menu:
                    m "Hm..."
                    "\"I could give you a hint.\"":
                        aza[6] "Really?! Tell me!"
                        aza[3] "Although, no wait. I would rather see for myself."
                    "\"Why aren't you topless?\"" if storecomplete:
                        aza[7] "Aw... You miss them already, sweetie?"
                        aza[1] "My store is closed for today, so that's why."
                        aza[1] "But don't worry. Come back on a business day and I will greet you the usual way!"
                    "\"I'm glad I got to know you, Azalea.\"":
                        aza[11] "Huh? You talk like you are about to go far away..."
                        aza[11] "But I will see you after the parade, right?"
                lola[11] "This is so exiting..."
                aza[1] "Princess Jasmine is getting married..."                           
                aza[1] "Make sure you drop by after the parade is over, I might have some new dresses to offer."
                m "You take care, Azalea."
                aza[1] "You too, love."
                lola[11] "Bye, Azalea!"
                m "Lola, I think maybe you should spend tonight here, if it's alright with Azalea."
                aza[1] "Sure, I don't mind."
                lola[70] "Really?"
                lola[71] "Slumber-party!!!"
                m "Look after her for me, alright?"
                aza[1] "Sure..."
                ">You leave the store."
                $ renpy.play('sounds/door2.mp3')
                show blkfade with d5
                pause.5
                hide image "04_pt/slavem/bld.png" 
                hide blkfade with d5
                $ finaldaystore = True
                jump lastday2           
            "-Leave-":
                jump lastday2
                
#        else:
#            "The store is closed for today..."
#            menu:
#                "There is a sign on the door: \"Closed for today due to upcoming parade\"."
#                "Enter the store.":
#                    $ renpy.play('sounds/door.mp3')
#                    aza[1] "Well, If it isn't my favorite customer!"
#                    aza[1] "My store is closed for today, sweetie."
#                    aza[1] "Haven't you heard? Princess Jasmine is getting married tomorrow."
#                    aza[1] "...."
#                    aza[1] "I've been hearing all sorts of rumors about her lately..."
#                    aza[1] "She used to be my idol, but now I'm not sure what to think anymore..."
#                    aza[1] "Nevertheless, I can't wait to see what Princess Jasmine is going to wear for her wedding."
#                    menu:
#                        m "Hm..."
#                        "I could give you a hint.":
#                            aza[1] "Really?! Tell me then!"
#                            aza[1] "Although, no wait. I would rather see for myself."                        
#                        "I'm glad I got to know you, Azalea.":
#                            aza[1] "Huh? You talk like you are about to go far away..."
#                            aza[1] "But I will see you after the parade, right?"
#                    aza[1] "This is so exiting..."
#                    aza[1] "Princess Jasmine is getting married!"                           
#                    aza[1] "Make sure you drop by after the parade is over, I might have some new dresses to offer."
#                    m "You take care, Azalea."
#                    aza[1] "You too, love."
#                    "You leave the store."
#                    $ renpy.play('sounds/door2.mp3')
                     #$ finaldaystore = True
                    #jump lastday2
                #"Leave.":
                   # jump lastday2
            

        
        
        

    
if select == "market":    
    if finaldaymarket:
        ">The market square is busy and full of people..."
        ">You have no business here..."
        jump lastday2        
    else:
        menu:
            "The market square..."
            "-Take a walk-":
                            $ finaldaymarket = True
                            show blkfade with d5
                            pause.5
                            show image "04_pt/slavem/bld.png" behind blkfade
                            hide blkfade with d5
                            ">You take a walk around the market square..."
                            ">The place is very noisy and full of people as usual..."
                            ">Fat merchants are shouting out prices of their merchandise..."
                            ">Some of them recognize you and greet you with a smile, others with a cold stare..."
                            ">Of course... You used to parade Princess Jasmine on a leash around this area like a common slave-girl..."
                            ">Some people enjoyed the spectacle... Others hated you for doing that, for working for Jafar..."
                            ">You see balsam among the merchants."
                            ">He greet's you with his usual smile, but you can't say if it's genuine..."
                            sch5 "Always nice to see you, friend!"
                            sch5 "I'm having a \"Wedding day sale\" today, my friend! Bananas and dates are half price!"
                            ">Suddenly the place feels too noisy for your taste... You decide to leave..."
                            show blkfade with d5
                            pause.5
                            hide image "04_pt/slavem/bld.png" 
                            hide blkfade with d5
                            jump lastday2

            "-Never mind...-":
                jump lastday2
    
    
    
if select == "tavern":    
    if finaldaytavern:
        ">You have no business left here..."
        jump lastday2        
    else:
        menu:
            "\"The blue bull\" tavern..."
            "-Go in...-":
                show blkfade with d5
                pause.5
                show image "04_pt/slavem/bld.png" behind blkfade
                hide blkfade with d5
                $ renpy.play('sounds/door.mp3')
                $ finaldaytavern = True
                ">You enter the building..."
                show bld with d3
                ">The tavern is packed with people, much more than usual."
                ">You almost have to squeeze in..."
                ">Every single table seems to be taken... And some people are even standing..."
                ">You wonder what's the reason behind this gathering..."
                ">You see quite a few tavern wenches dancing on the tables and on the floor among patrons..."
                ">Most of them are already topless..."
                ">There is something strange going on here... At first you can't quite put your finger on in, but then you realize it..."
                ">Every single wench in the building is a princess Jasmine impersonator..."
                ">None of them look much like jasmine, but all of them are dressed like her, and have their hair fashioned in a similar manner..."
                $ conversationflag01 = True
                $ conversationflag02 = True
                ">You see maslab behind the counter, energetic as ever."
                sch6 "Welcome to \"THE BLUE BULL\", my friend! *spit*."
                label lastmaslab:
                menu:
                    sch6 "......"
                    "\"What's going on here?\"" if conversationflag02:
                        sch6 "You Like what you see, huh?"  
                        $ conversationflag02 = False
                        jump lastmaslab
                    "\"Hello Maslab.\"" if conversationflag01:
                        sch6 "Always a pleasure to have you here, my friend!"
                        $ conversationflag01 = False
                        jump lastmaslab
                    "\"Can I get a pint of wine?\"":
                        sch6 "Here you go, my friend. On the house!"
                        ">Maslab pours you a pint of a very cheap vine..."
                        ">You empty the pint in a few gulps, but the nasty drink doesn't improve your mood at all..."
                
                sch6 "In honor of the upcoming parade today we have a \"Princess day\" in the Blue Bull!"
                sch6 "You want princess jasmine? I've got a dozen for you! Ha-ha-ha!"     
                ">One of the nearby topless wenches gives you a smile and starts to shake her tits violently."
                show blkfade with d3
                pause.5
                hide blkfade with d3
                sch11_4 "All the girls are dressed like that princess whore of ours..."
                sch11_3 "But not me of course... Father wouldn't let me..."
                sch11_3 "Not that I wanted to..."
                sch11_4 "Hey, don't just stay there! Grab that girl's tit, she wants it."
                sch11 "If you won't, I will!"
                sch11_4 "So, our princess is to be wed tomorrow, huh?"
                sch11_3 "I can't wait to see the parade..."
                sch11_3 "That, whore! I think I will try and throw a rotten peach at her or something!"
                show blkfade with d3
                pause.5
                hide blkfade with d3
                ">Heh... The days when Princess herself used to work here are done."
                ">This is Maslab's last desperate attempt to make some extra gold at Jasmine's expense..."
                ">Well it seems to be working just fine..."
                ">The building is packed with people, but most of them were probably expecting the actual Princess Jasmine to dance for them..."
                ">Another dancing wench gives you a smile... This particular one kinda looks like Jasmine actually..."
                ">You don't feel like staying here any longer..."
                ">You say goodbye to Maslab..."
                sch6 "Leaving so soon?"
                ir[12] "Hey, come on, stick around a bit longer..."
                m "I'm glad I got to know you, Iris..."
                ir[15] "Old man? What's the matter?"
                m "Take care of your father, alright?"
                ir[14] "............."
                ir[15] ".............?"
                ">You leave the building..."
                $ renpy.play('sounds/door2.mp3')
                show blkfade with d5
                pause.5
                hide image "04_pt/slavem/bld.png" 
                hide blkfade with d5
                hide bld2 with d3
                hide bld with d3
                jump lastday2 

            "-Never mind...-":
                jump lastday2 
                
            
        
    
if select == "school":    
    ">The \"JSGA\"..."
    ">Due to the upcoming parade there are no classes held today..."
    jump lastday2
    
        
if select == "jpalace":
    ">You have no business at this palace anymore..."
    jump lastday2
    

    
#################################
##GOLD SCREEN################
########################

screen gold_scr: #более подробно см. здесь http://www.renpy.org/doc/html/screens.html
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 10 xpos 490 ypos 530#отступ для текста, если надо прямо в левом углу — убираем его        
        text "{size=+7}[gold] gold{/size}" #сумма текстом

     
  
############################       
    
###########MARKET LABELS##########################
label buythinglily:
    sch5 "You want something nice? Oh, snap. I'm out of someting nice."
    sch5 "Yeah, imagine that!"
    sch5 "So, you will have to come back in five days - I will restock."
    sch5 "..............."
    sch5 "........"
    sch5 "He-he... I'm kidding! You should've seen your face!"
    sch5 "Here is something nice for you. That will be 50 gold."
    menu:
        "You currently have [gold] gold. \nWould you like to buy something nice for 50 gold?"
        "\"Yes please.\"":
            if gold >= 50: 
                $ gold -=50
                $ quest7balsam = False
                $ quest7thing = True
                ">You paid Balsam 50 gold coins."
                sch5 "Thank you for your purchase."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxnice.png" with moveinright
                ">You received something nice."
                hide image "04_pt/slavem/boxnice.png" with Dissolve(.4)
                hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                jump market2
            else:
                sch5 "Not enough gold? That's alright. Come back when you are ready. I'll put the something nice aside for you."
                jump market2
        "\"No, thank you.\"":
            sch5 "Suit yourself."
            jump market2
label mdisneace:
    show blkfade with Dissolve(.3)
    pause.5
    hide blkfade with Dissolve(.3)
    sch5 "Hello, friend. What can I do for you today?"
    sch5 "Huh...?"
    sch5 "Yes, yes, Iris is my niece..."
    sch5 "She is what?! She wants to work in a brothel against her father's will?"
    sch5 "This is great news indeed!"
    sch5 "Huh? It's not going to happen unless she gets the approval from a male member of her family?"
    sch5 "No problem! I love that bitch... er, that girl so much! And I think she deserves something0 better than the life of a waitress!"
    sch5 "Just let me know where to sign!"
    show image "04_pt/slavem/masteritem.png" with moveinleft
    $ renpy.play('sounds/win2.mp3')
    show image "04_pt/slavem/boxpermission.png" with moveinright
    ">You acquired a written permission and a blessing for Iris to start working as a whore signed by Balsam."
    hide image "04_pt/slavem/boxpermission.png" with Dissolve(.4)
    hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
    sch5 "If only I could see my brother's face when he finds out!"
    sch5 "Don't worry though, I'm not going to tell him... Not right away atleast..."
    $ quest6 += 1
    show blkfade with Dissolve(.3)
    pause.5
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    hide blkfade with Dissolve(.3)
    jump mainmenu
label pickmaterials:
    sch5 "Yes, yes, your materials have been delivered last night..."
    sch5 "Everything on your list is right here..."
    sch5 "That will be 200 gold coins."
    menu:
        "You currently have [gold] gold. \nWould you like to buy the materials for 200 gold?"
        "\"Yes please.\"":
            if gold >= 200: 
                $ gold -=200
                $ quest5start3 = False
                $ quest5start4 = True
                sch5 "Here is your stuff. Thank you for the purchase..."
                show image "04_pt/slavem/masteritem.png" with moveinleft
                $ renpy.play('sounds/win2.mp3')
                show image "04_pt/slavem/boxmaterials.png" with moveinright
                ">You receive the materials Azalea's been asking for..."
                hide image "04_pt/slavem/boxmaterials.png" with Dissolve(.4)
                hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                jump mainmenu
            else:
                sch5 "Not enough gold? That's alright. Come back when you are ready. I'll put the material aside for you."
                jump market2
        "\"Maybe later.\"":
            sch5 "Come back whenever you're ready. I'll put the materials aside for you."
            jump market2
label buymaterials:
    show image "04_pt/slavem/masteritem.png" with moveinright
    show image "04_pt/slavem/boxlistmaterials.png" with moveinleft
    ">You hand over the list of required materials to the merchant..."
    hide image "04_pt/slavem/boxlistmaterials.png" with moveoutright
    hide image "04_pt/slavem/masteritem.png" with moveoutleft
    sch5 "What is this? Hm... Some fabric, some beads..."
    sch5 "Yeah, I usually have all of these things in stock..."
    sch5 "Not this time though..."
    sch5 "What? You didn't expect this to be that easy, did you?"
    sch5 "I'm expecting another shipment soon..."
    sch5 "Come back in a couple of days, I will restock by then..."
    $ quest5start2 = False
    $ quest5start3 = True
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    jump mainmenu

label startquest2:
    sch5 "Hello, friend."
    menu:
        sch5 "Do you know my brother Maslab?"
        "\"I know him.\"":
            sch5 "Good then."
        "\"You have a brother?\"":
            sch5 "Yes, unfortunately I do... I mean, I sure do."
            sch5 "He owns a tavern not far from here called \"The Blue Bull\"."
    sch5 "You think you could do me a little favor?"
    sch5 "Could you take this little box to him for me?"
    sch5 "I would do it myself but I can't stand the man *spit*."
    sch5 "Er... I mean, I can't leave my fruit stand unattended."
    sch5 "Anyway, the contents of this box are very fragile, so you will have to be very careful with it."
    label keepingup:
    menu:
        sch5 "Also you will have to promise not to open this box yourself."
        "\"What's in it for me?\"":
            sch5 "Nothing."
            sch5 "It's not for you, it's for my brother. Try to keep up, friend. *spit*"
            jump keepingup
        "\"What's inside?\"":
            sch5 "A present for my dear brother..."
            sch5 "So, what do you say? Will you help me out, friend? *spit*"
            jump keepingup
        "\"Sounds dangerous. No thank you.\"":
            sch5 "Oh... I see..."
            sch5 "Well, maybe I will ask one those urchin kids to help me out then..."
            jump market2
        "\"I promise.\"":
            sch5 "Great! Here it is."
            show image "04_pt/slavem/masteritem.png" with moveinleft
            $ renpy.play('sounds/win2.mp3')
            show image "04_pt/slavem/boxtrick.png" with moveinright
            "You receive a small wooden box from Balsam the merchant."
            sch5 "You do know the way, don't you?"
            sch5 "Just take it to \"The Blue Bull\" tavern and give it to my brother."
            hide image "04_pt/slavem/boxtrick.png" with Dissolve(.4)
            hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
            sch5 "Oh, and one more thing: don't tell him it's from me, alright? I want it to be a surprise. *spit*"
            sch5 "Thank you for helping me out, friend."
            $ quest200 = False
            $ quest2start = True
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
            ">You leave the market square."
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            show con1 at right
            show ctc7 at right
            pause
            hide con1
            hide ctc7
            ">On your way to the tavern you can't help but start wondering about the contents of the mysterious box."
            show image "04_pt/slavem/bld.png" with Dissolve(.3)
            label kissmyass:
            menu:
                "Should you open it and take a peek inside?"
                "-Carefully examine it without opening-" if kissmyass:
                    ">You carefully examine the box..."
                    ">It's a really plain, almost cheap looking little box, made of wood."
                    ">It doesn't seem to have locks, seals or any other means of protection from being opened."
                    ">In fact for a box that is not meant to be opened it's almost asking for the opposite."
                    $ kissmyass = False
                    jump kissmyass
                "-Open the lead a little and take a peek-":
                    ">Carefully you lift the lid of the box up."
                    ">You hear something click inside of it and then a light cracking sound."
                    ">Suddenly the box spits out some sort of slimy liquid right in your face."
                    ">Your eyes are starting to burn, and a truly terrible stench fills up your nostrils."
                    ">What is this awful stench? It smells like..."
                    ">Rotten eggs...?"
                    ">Suddenly the realization comes: a trick-box. \nA trick-box loaded with rotten eggs."
                    ">You should't have opened it..."
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                    ">You wipe your face clean with a sleeve but it doesn't help against the stench."
                    ">You take the box back to the Balsam."
                    show image "04_pt/slavem/bld.png" with Dissolve(.3)
                    sch5 "What happened, friend?"
                    sch5 "Didn't I ask you to not to open it?"
                    sch5 "Oh well... I will reload it, but this time make sure you do not open it yourself, promise?"
                    sch5 "Hm... I don't have any rotten eggs left to load it with..."
                    sch5 "Would you mind coming back tomorrow?"
                    ">You leave the market square."
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                    show image "04_pt/slavem/qfailed.png" with Dissolve(.3)
                    show con1 at right
                    show ctc7 at right
                    pause
                    hide con1
                    hide ctc7
                    "You failed this quest."
                    hide image "04_pt/slavem/qfailed.png" with Dissolve(.3)
                    ">It's getting late. You decide to head home."
                    $ onquest = False
                    $ quest200 = True
                    $ quest2start = False
                    jump dayends
                    
                "-Keep your promise. Do not open it-":
                    "You decide to keep your promise and leave the box be."
                    ">You continue on your way."
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                    jump mainmenu

            

label stupidfruits:
    sch5 "You need to buy some fruits?"
    menu:
        "You currently have [gold] gold. \nWould you like to buy a bunch of fruits for 50 gold?"
        "\"Yes please.\"":
            $ gold -=50
            $ quest1start = False
            $ quest1start2 = True
            sch5 "Only the best fruits, for you, my friend."
            show image "04_pt/slavem/masteritem.png" with moveinleft
            $ renpy.play('sounds/win2.mp3')
            show image "04_pt/slavem/boxfruits.png" with moveinright
            ">You bought some fruits."
            sch5 "Thank you for your purchase."
            hide image "04_pt/slavem/boxfruits.png" with Dissolve(.4)
            hide image "04_pt/slavem/masteritem.png" with Dissolve(.4)
            jump market2
        "\"Not right now.\"":
            jump market2
######################CROCUS COINS################
label crocuscoins:
        $ cleangold = renpy.random.randint(2, 14)                
        $ gold = gold - cleangold
        $ renpy.play('sounds/coins.mp3')
        ">You give the homeless [cleangold] gold coins."
        sch7 "Thank you, kind master."
        
        if pthink >= 0 and pthink < 6:
            sch7 "People of agrabah love and adore princess Jasmine, you know."
        elif pthink >= 6 and pthink < 11:
            sch7 "People say that sultan Jafar is planning a wedding between him and our Princess Jasmine..."
            sch7 "But that can't be true, can it?"
        elif pthink >= 11 and pthink < 16:
            sch7 "Crocus heard the most peculiar rumor about princess Jasmine the other day..."
            sch7 "But that's just a rumor, Crocus won't to bother the master with silly rumors..."
        elif pthink >= 16 and pthink < 21:
            sch7 "crocus hears people of agrabah talk a lot about Princess Jasmine lately..."
            sch7 "They seem to feel sorry for her..."
            sch7 "Crocus does too..."
        elif pthink >= 21 and pthink < 26:
            sch7 "Crocus sits here all day... People barely notice him... But he hears when they talk about all sorts of things..."
            sch7 "People exchange all sorts of bizarre rumors about Princess Jasmine lately..."
            sch7 "Crocus sure, none of them are true."                     
        elif pthink >= 26 and pthink < 31:
            sch7 "People say Princess Jasmine is behaving very strange lately..."
            sch7 "But they also say there's gotta to be a good reason for her to behave the way she does..."
        elif pthink >= 31 and pthink < 41:
            sch7 "People on the streets exchange all sorts of rumors about Princess Jasmine..."
            sch7 "Crocus is starting to think that some of those rumors might be true..."
        elif pthink >= 41 and pthink < 51:
            sch7 "People of agrabah seem to be very confused about the way their princess behaves lately..."
            sch7 "Crocus is confused too..."
        elif pthink >= 51 and pthink < 61:                        
            sch7 "From what Crocus can hear, people of agrabah don't like princess Jasmine much anymore..."
            sch7 "They say she has no shame..."
            sch7 "Crocus doesn't care... he doesn't believe what people say about his princess..."
        elif pthink >= 61 and pthink < 71:
            sch7 "People are very angry with Princess jasmine."
            sch7 "They call her \"filthy-princess-whore\" now..."
            sch7 "When crocus asked why, they said because she is working in the brothel as a whore now..."
            sch7 "But that can't be true...."
            sch7 "Can it?"
            sch7 "If it is, then Crocus will have to visit that brothel too... He saved quite a few coins lately, thanks to the master."
        elif pthink >= 71 and pthink < 81:
            sch7 "People talk about Princess Jasmine all the time..."
            sch7 "They say she's been seen dancing on a table in the \"Blue Bull\" like a common tavern wench."
            sch7 "Some people even say they saw her walking around the streets with her tits completely naked..."
            sch7 "Royal tits... Crocus would love to see them..."
        elif pthink >= 81 and pthink < 91:
            sch7 "Master, master..."
            sch7 "Crocus has something special to tell you today..."
            sch7 "Not rumors, no... Crocus saw it himself this time..."
            sch7 "Princess Jasimine walked right by poor old crocus the other day."
            sch7 "She was wearing so little clothing that poor old crocus almost lost his consciousness..."
            sch7 "Some guy was leading the her on a leash like a common slave-girl..."
            sch7 "Come to think of it he was wearing the same cloak master always does..."
        elif pthink >= 91 and pthink < 101:
            sch8 "Why poor old Crocus is smiling today, master asks? Because Crocus been to the \"Red Phoenix\" last night..."
            sch8 "At first that fat pig of a woman lily didn't want to let Crocus in, but after he showed her how much gold he has, she had no choice..."
            sch8 "Crocus spent all his gold to pay for a handjob from the Princess..."
            sch8 "It was the best handjob Crocus had in his entire life..."
            sch8 "These wonderful memories will keep Crocus warm during cold winter nights, that's for sure..."
            sch8 "Crocus still loves Princess Jasmine... But he has no respect for her anymore..."
            sch8 "Princess Jasmine is a filthy whore..."
            sch8 "Now, if master doesn't mind, Crocus wants to be alone for a while..."
        elif pthink >= 101 and pthink < 10001:
            sch7 "Crocus still loves Princess Jasmine even though she literally is a whore now..."
            sch7 "But people seem to despise their princess for betraying Agrabah by whoring herself out and acting like a slut without any shame."  
            sch7 "They are very angry. Crocus doesn't think Jasmine's reputation could get any worse..."
        jump cheapside
         

#################################AUDIENCE WITH JAFAR#####
label audijafar:
$ parade = 0
play music "music/JafarsHour.mp3" fadein 1 fadeout 1
sch4 "I see... Follow me please..."
label jafaroutfits:
menu:                
    "Choose the outfit that you'd want to present Princess Jasmine in."
    "-Usual outfit-":
        call set_jas_clothes("normal")
        $ normalw = True
        ">Princess Jasmine agrees to wear that outfit in front of Jafar."
    "-Peasant robe-":
        if peasant:
            if obedience >= 2:
                call set_jas_clothes("peasant")
                $ peasantw = True
                ">Princess Jasmine agrees to wear this outfit in front of Jafar."
            else:
                ">Princess refuses to wear this outfit in front of her sworn enemy."
                jump jafaroutfits
        else:
            ">You don't own this outfit yet."
            jump jafaroutfits
    "-Tavern girl-":
        if taverngirl:
            if obedience >= 4:
                call set_jas_clothes("tavern")
                $ tavernw = True
                ">Princess Jasmine agrees to wear this outfit in front of Jafar."             
            else:
                ">Princess refuses to wear this outfit in front of her sworn enemy."
                jump jafaroutfits
        else:
            ">You don't own this outfit yet."
            jump jafaroutfits
    "-Dancer-":
        if dancer:
            if obedience >= 6:
                call set_jas_clothes("dancer")
                $ dancew = True
                ">Princess Jasmine agrees to wear this outfit in front of Jafar."
                
            else:
                ">Princess refuses to wear this outfit in front of her sworn enemy."
                jump jafaroutfits
        else:
            ">You don't own this outfit yet."
            jump jafaroutfits
    "-Brothel whore-":
        if whore:
            if obedience >= 9:
                call set_jas_clothes("whore")
                $ whorew = True
                "the Princess Jasmine agrees to wear this outfit in front of Jafar."
                
            else:
                ">Princess refuses to wear this outfit in front of her sworn enemy."
                jump jafaroutfits
        else:
            ">You don't own this outfit yet."
            jump jafaroutfits
    "-Slave-girl on a leash-":
        if slavegirl:
            if obedience >= 10:
                call set_jas_clothes("slave")
                $ slavew = True
                ">Princess Jasmine agrees to wear this outfit in front of Jafar."
            else:
                "> Princess refuses to wear this outfit in front of her sworn enemy."
                jump jafaroutfits
        else:
            "You don't own this outfit yet."
            jump jafaroutfits
    "-Cancel-":
        play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
        jump jpalace2
    
show blkfade with d3
pause.7
hide rest03
hide blkfade with d3
sch4 "Your majesty... Please, forgive my intrusion, but there is someone here to see you..."
jaf[2] "Huh? Oh, it's you, old man..."            
jaf[2] "What? What is it? Make it quick, I'm busy."
jaf[2] "Is it time to start the final preparations for the Wedding Parade?"
jaf[2] "Let's see..."
if gold <= 2000:
    jaf[2] "How much money did you make so far?"
    jaf[2] "Hm..."
    jaf[2] "You have [gold] gold coins? No, that's not enough..."
else:
    jaf[2] "How much money did you make so far?"
    jaf[2] "Hm..."
    jaf[1] "Looks like you have more than enough gold to finance the whole thing. Good job!"
    $ parade +=1
if pthink <= 100:
    jaf[2] "Now, about Jasmine's reputation..."
    jaf[2] "Hm..."
    jaf[2] "My spies tell me that she still has some supporters left among the commoners..."
    jaf[3] "This is unacceptable..."
    jaf[3] "I need those filthy peasants to hate the princess! Every single one of them..."
    jaf[3] "Otherwise the crowd could turn on me during the wedding ceremony..."
    jaf[2] "No, we can't have that..."
    jaf[2] "Do whatever you deem necessary to turn every single one of them against her."
else: 
    jaf[2] "Now, about Jasmine's reputation..."
    jaf[2] "Hm..."
    jaf[2] "My spies tell me that she doesn't have any supporters left among the citizens of Agrabah..."
    jaf[1] "\"The Princess Whore\" they call her now."
    jaf[1] "\"betrayer of Agrabah\", and \"Jasmine the Shameless Slut\"."
    jaf[1] "This is perfect. You did a great job, old man." 
    $ parade +=1
jaf[1] "And now for the final prize... The most delicious, princess jasmine."
jaf[1] "Please, come forward."

show screen jasmine_sprite_room
with d3

        
if obedience >= 0 and obedience < 3:   
    j "Burn in hell, you son of a jackal!"
    j "You will pay for what you've done!"
    jaf[2] "Starting a conversation with insults?"
    jaf[2] "Have you forgotten all of your courtesies, my princess?"
    j "......."
    
    hide screen jasmine_sprite_room
    with d3
    
    jaf[2] "Oh, my... That's not good at all... She is still disobedient."
    jaf[2] "You better get back to work, old man."
    sch4 "I will show you out. Follow me..."
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    show rest03 with d3
    jump mainmenu
                                               
elif obedience >= 3 and obedience < 6:
    j "Jafar..."
    jaf[1] "My dear princess. Come here and give me a kiss."
    j "How about I spit in your ugly face instead?"
    
    hide screen jasmine_sprite_room
    with d3
    
    jaf[2] "Oh, my... That's not good at all... She is still disobedient."
    jaf[2] "You better get back to work, old man."
    sch4 "I will show you out. Follow me..."
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    show rest03 with d3
    jump mainmenu
elif obedience >= 6 and obedience < 8:
    j "Jafar..."
    jaf[1] "My dear princess. Come here and give me a kiss."
    j "I am not going to do that!"
    j "Never..."
    j "......"
    
    hide screen jasmine_sprite_room
    with d3
    
    jaf[2] "Oh, my... That's not good at all... She is still disobedient."
    jaf[2] "You better get back to work, old man."
    sch4 "I will show you out. Follow me..."
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    show rest03 with d3
    jump mainmenu
elif obedience >= 8 and obedience < 10:
    j "Jafar..."
    jaf[1] "My dear princess. Come here and give me a kiss."
    j "I..."
    jaf[1] "Oh, come on, it's just a kiss."
    j "....alright. If it's just a kiss...."
    
    hide screen jasmine_sprite_room
    with d3
    
    "Jasmine briefly kisses Jafar on the lips. She seems very conflicted."
    jaf[1] "This is great!"
    jaf[1] "You did a great job old man!"
    jaf[1] "Now, Jasmine, I want you to dance for me!"
    
    show screen jasmine_sprite_room
    with d3
    
    j "......"
    jaf[2] "Did you hear what I said?"
    jaf[2] "I want you to dance for me. And make sure you shake those tits of yours enough."
    j "no..."
    jaf[3] "What did you say?"
    j "No... I... I'm not going to do that..."
    
    hide screen jasmine_sprite_room
    with d3
    
    jaf[2] "Oh, my... That's not good at all... She is still disobedient."
    jaf[2] "You better get back to work."
    sch4 "I will show you out. Follow me..."
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    show rest03 with d3
    jump mainmenu
elif obedience >= 10:
    j "Jafar..."
    jaf[1] "My dear princess. Come here and give me a kiss."
    j "I..."
    jaf[1] "Oh, come on, it's just a kiss."
    j "As you wish...."
    hide screen jasmine_sprite_room
    with d3
    ">Jasmine gives Jafar a deep kiss on a lips, She seems to be enjoying it."
    jaf[1] "This is great!"
    jaf[1] "You did a great job old man!"
    jaf[1] "Now, Jasmine, I want you to dance for me!"
    show screen jasmine_sprite_room
    with d3
    j "......"
    jaf[2] "Did you hear what I said?"
    jaf[1] "I want you to dance for me. And make sure you shake those tits of yours enough."
    j "As you wish..."
    hide screen jasmine_sprite_room
    with d3
    ">Jasmine is starting to dance. She is giving it all she's got."    
    ">You notice that she is making a lot of unnecessary and awkward movements to make sure her tits bounce and jiggle enough."
    ">Jafar seems to be pleased."
    jaf[1] "Good, good. This is good!"
    jaf[1] "She is definitely ready!"
    jaf[1] "You did a great job, old man."
    $ parade +=1
    
    
if parade >=3:
    jaf[1] "Well, it seems that all the requirements have been met."
    menu:
        
        jaf[1] "What do you think, old man? Should we proceed with the wedding?"
        "\"Yes. Proceed with the wedding.\"":
            play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
            jaf[1] "Alright then."
            jaf[1] "The preparations will take some time, so for now you can return to the house I assigned for you."
            jaf[1] "The princess will be staying in the palace starting tonight."
            jaf[1] "oh, and one more thing, before you go."
            jaf[1] "I have a few designs for the wedding dresses here."
            show image "04_pt/slavem/wedding13.jpg" with Dissolve(.3)
            jaf[1] "Take a look and tell me what you think."
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            
            menu:
                "No good. These are way too revealing.":
                    jaf[1] "But that's the whole point."
                    jaf[1] "I think they are great!"
                "The Princess will be as good as naked!":
                    jaf[1] "Exactly!"
                    jaf[1] "The ceremony will be a spectacle to remember, that's for sure!"
                "Those are too risky. People might revolt.":
                    jaf[1] "Well that's why I made you to work so hard on her reputation."
                    jaf[1] "If all goes well people will aim all of their hatred towards the princess. (Not me.)"
                    jaf[1] "And it will make it much easier for them to accept me as their rightful ruler."
                "Can princess stay with me tonight?":
                    jaf[2] "What?"
                    jaf[2] "Don't be ridiculous, old man."
                    jaf[2] "Did you form some sort of weird attachment to her?"
                    jaf[2] "Old man, you should be smarter than that."
                    jaf[2] "Hm..."
                    jaf[2] "Hey, slave... err, I mean, my wife-to-be..."
                    show screen jasmine_sprite_room
                    with d3 
                    j "I am here, masters..."
                    jaf[3] "Masters?"
                    jaf[2] "No, no, no."
                    jaf[2] "Master. Singular. Just me."
                    j "I understand, master."
                    jaf[2] "Good."
                    hide screen jasmine_sprite_room
                    with d3
                    jaf[2] "Alright, let's carry on then."
            jaf[2] "You know what? I think I will let you decide which dress princess jasmine should wear during the parade."
            jaf[2] "So take a good look and tell me which one she should wear."
            show con1 at right
            show ctc7 at right
            pause 
            hide con1
            hide ctc7
            label letscarryon:
            menu:
                "The one on the left.":
                    $ dress01 = True
                    jaf[2] "The one one the left then?"
                    jaf[1] "Good choice. I think it will look great on her."
                    jaf[2] "Alright now, this would be all for today."
                    jaf[2] "You can enjoy your free time in the city now. And make sure that you don't miss the parade tomorrow."
                    jaf[2] "My bride?"
                    show screen jasmine_sprite_room
                    with d3
                    j "Yes, master..."
                    jaf[2] "Say good-bye to the old man."
                    j "Good bye, master..."
                    jaf[3] "I told you already that I am your master now."
                    j "I'm sorry master..."
                    jaf[3] "You are so stupid."
                    j "....."
                    hide screen jasmine_sprite_room
                    with d3
                    "You leave the palace."
                    hide image "04_pt/slavem/wedding13.jpg" with Dissolve(.3)
                    jump lastday
                "The one in the middle.":
                    $ dress02 = True
                    jaf[2] "The one one in the middle then?"
                    jaf[1] "Good choice. I think it will look great on her."
                    jaf[2] "Alright now, this would be all for today."
                    jaf[2] "You can enjoy your free time in the city now. And make sure that you don't miss the parade tomorrow."
                    jaf[2] "My bride?"
                    show screen jasmine_sprite_room
                    with d3
                    j "Yes, master..."
                    jaf[2] "Say good-bye to the old man."
                    j "Good bye, master..."
                    jaf[3] "I told you already that I am your master now."
                    j "I'm sorry master..."
                    jaf[3] "You are so stupid."
                    j "....."
                    hide screen jasmine_sprite_room
                    with d3
                    "You leave the palace."
                    hide image "04_pt/slavem/wedding13.jpg" with Dissolve(.3)
                    jump lastday
                "The one one the right.":
                    $ dress03 = True
                    jaf[2] "The one on the right?"
                    jaf[1] "Good choice. I think it will look great on her."
                    jaf[2] "Alright now, this would be all for today."
                    jaf[2] "You can enjoy your free time in the city now. And make sure that you don't miss the parade tomorrow."
                    jaf[2] "My bride?"
                    show screen jasmine_sprite_room
                    with d3
                    j "Yes, master..."
                    jaf[2] "Say good-bye to the old man."
                    j "Good bye, master..."
                    jaf[3] "I told you already that I am your master now."
                    j "I'm sorry master..."
                    jaf[3] "You are so stupid."
                    j "....."
                    hide screen jasmine_sprite_room
                    with d3
                    "You leave the palace."
                    hide image "04_pt/slavem/wedding13.jpg" with Dissolve(.3)
                    jump lastday
                "Can't she just be naked instead?":
                    if quest1complete and quest2complete and quest3complete and quest4complete and quest5complete and quest6complete and quest7complete and quest8complete and quest9complete and quest10complete and quest11complete and quest12complete and quest13complete:
                        $ dress04 = True
                        jaf[2] "Naked? Well, that could work too!"
                        jaf[1] "Good choice."
                        jaf[2] "Alright now, this would be all for today."
                        jaf[2] "You can enjoy your free time in the city now. And make sure that you don't miss the parade tomorrow."
                        jaf[2] "My bride?"
                        show screen jasmine_sprite_room
                        with d3
                        j "Yes, master..."
                        jaf[2] "Say good-bye to the old man."
                        j "Good bye, master..."
                        jaf[3] "I told you already that I am your master now."
                        j "I'm sorry master..."
                        jaf[3] "You are so stupid."
                        j "....."
                        hide screen jasmine_sprite_room
                        with d3
                        ">You leave the palace."
                        hide image "04_pt/slavem/wedding13.jpg" with Dissolve(.3)
                        jump lastday
                    else:
                        jaf[2] "Naked? Well, that could work too I suppose..."
                        a1 "(Maybe if you were to complete all the in-game quests...)"
                        jaf[2] "Huh? Did you say something..."
                        jaf[2] "Never mind, let's carry on..."
                        jump letscarryon
                "Princess Jasmine should decide.":
                    $ dress02 = True
                    jaf[2] "What? I should Let jasmine decide?"
                    jaf[1] "But of course!"
                    jaf[1] "Hey, slut, er, I mean, my bride, come here."
                    show screen jasmine_sprite_room
                    with d3
                    j "Yes, master..."
                    jaf[1] "Look at those designs and tell me which one you would rather wear for your wedding parade tomorrow!"
                    j "....."
                    j "I...."
                    jaf[1] "It's alright. Take your time."
                    j "......"
                    j "..."
                    jaf[2] "So?"
                    hide screen jasmine_sprite_room
                    with d3
                    "Jasmine inspects the designs carefully..."
                    show screen jasmine_sprite_room
                    with d3
                    
                    j "...the one in the middle..."
                    jaf[1] "What? really? This is the one you'd like to go with?"
                    j "Yes..."
                    jaf[1] "But, look at it. Your tits will be in plain sight!"
                    jaf[1] "Do you know how many people will gather tomorrow to see the parade?"
                    jaf[1] "If you wear this, all of them will see your naked tits!"
                    j "That's... That's alright... I want them to see..."
                    jaf[1] "What? Do you have no shame, slut?!"
                    j "I am sorry, master..."
                    jaf[1] "No, no, there's nothing you should be sorry for."
                    j "I am happy to hear that..."
                    hide screen jasmine_sprite_room
                    with d3
                    jaf[1] "Old man, you did an excellent job with this one."
                    jaf[1] "Not only is she fully obedient, but she is also a complete slut now."
                    jaf[1] "Amazing. Just amazing..."
                    jaf[1] "Alright now, this would be all for today."
                    jaf[2] "You can enjoy your free time in the city now. And make sure that you don't miss the parade tomorrow."
                    jaf[2] "My bride?"
                    show screen jasmine_sprite_room
                    with d3
                    j "Yes, master..."
                    jaf[2] "Say good-bye to the old man."
                    j "Good bye, master..."
                    jaf[3] "I told you already that I am your master now."
                    j "I'm sorry master..."
                    jaf[3] "You are so stupid."
                    j "....."
                    hide screen jasmine_sprite_room
                    with d3
                    "You leave the palace."
                    hide image "04_pt/slavem/wedding13.jpg" with Dissolve(.3)
                    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                    jump lastday
                
        "\"Not yet, I need more time.\"":
            jaf[2] "No? OK, you are the expert here."
            jaf[2] "Everything is ready on my end though, so just give me the signal when we should start."
            sch4 "I will take you to the exit. Follow me..."
            show blkfade with d3 
            show rest03 behind blkfade
            play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            hide blkfade with d3
            jump mainmenu
            
else: 
    jaf[2] "Well, we can't proceed with the wedding preparations until all three conditions are met." 
    jaf[2] "Princess Jasmine should be well trained and fully obedient."
    jaf[2] "The People of Agrabah should not have any respect or love for their princess left."
    jaf[2] "And the money of course. You should provide me with enough gold to finance the wedding parade."
    jaf[2] "Come back when you're ready."
    sch4 "I will take you to the exit. Follow me..."  
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    jump mainmenu
        
#####AUDI JAFAR2#
label audijafar2:
    play music "music/JafarsHour.mp3" fadein 1 fadeout 1
    sch4 "I see... Follow me please..."
    show blkfade with d3
    pause.7
    hide blkfade with d3
    sch4 "Your majesty... Please, forgive my intrusion, but there is someone here to see you..."
    jaf[2] "Huh? Oh, it's you, old man..."            
    jaf[2] "What? What is it? Make it quick, I'm busy."
    jaf[2] "Is it time to start the final preparations for the Wedding Parade?"
    jaf[2] "huh? Why are you alone? Where is the princess?"
    jaf[2] "I need to see that she is ready before we can proceed with the parade preparations."
    jaf[2] "Next time make sure you bring her along."
    jaf[4] "Now leave. I am a busy man."
    sch4 "I will take you to the exit. Follow me..."  
    show blkfade with d3
    pause.7
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    hide blkfade with d3
    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1
    jump mainmenu


    

#########################################################
