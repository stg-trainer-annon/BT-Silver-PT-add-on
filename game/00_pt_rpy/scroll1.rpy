label ariel:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/spot01.png", "screens/spot01b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":     
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
    pause.05
    scene white
    pause.05
    scene bg meadow
    show ariel normal
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
    play music mrm fadein 3
    $ renpy.music.set_volume(0.5, .5, channel="music")
    pause 
    
    hide ariel normal
    show ariel mad
    with Dissolve(.1) 
    s "What is the meaning of this, mage!?"
    $ elena_pts += 1
    m "I guess this is not the right spell..."
    s "You think?! Look at me - I am a circus freak! Half-woman-half-fish! Undo your spell at once or you will be sorry!"
    m "Yes, your highness."
    menu:
        m "(Hm... Should I really undo the spell now...?)"
        "Yes. Undo the spell.":
            call masterstart
        "No. Not yet.":
            call arielnoundo
            
label arielnoundo: 
    pause
    $ renpy.play('sounds/boing.mp3')
    show ariel topless
    pause
    
    show ariel blush
    with Dissolve(.1)
    s "What are you doing, mage?! How dare you bare my breasts! I ordered you to undo the spell, not to humiliate me even more?!" 
    show arielscream
    with Dissolve(.1)
    hide ariel blush
    s "I will have you beheaded for this! Guards! Guar...."
    m "Your majesty, please, I just need to take some measurements. It will help me greatly to identify the correct spell."
    show asilent
    with Dissolve(.1)
    hide arielscream
    s "......................"
    m "Now, if you would be so kind to allow me to proceed, your majesty?..."
    show asulky
    with Dissolve(.1)
    s "Fine. Go ahead and feel me up, old man, but be quick about it!"
    pause
    $ renpy.play('sounds/boing02.mp3')
    $ renpy.play('sounds/boing03.mp3')
    show ariel groped
    pause
    show ariel groped
    $ renpy.play('sounds/boing02.mp3')
    pause.2
    $ renpy.play('sounds/boing03.mp3')
    pause
    m " It seems your-highness's breasts did become bigger in size so we are definitely going in the right direction... We need to proceed and try other combinations..."
label arielgrope:     
    s "............................."
    pause
    $ renpy.play('sounds/boing02.mp3')
    $ renpy.play('sounds/boing03.mp3')
    show ariel groped
    pause
    scene bg meadow
    show asilent
    pause
    
   
    s "That's enough, old man. Undo your spell at once."
    
    menu:
        m "(Maybe it is time to undo the spell, before I get myself in trouble...)"
        "Undo the spell.":
            call arielnogrope
        "Not yet":
            call arielgrope
label arielnogrope:        
    m "As you wish, your highness... "
    call masterstart
    
## THREE TITS


label threetits:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/spot07.png", "screens/spot07b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":

    scene white
    $ renpy.play('sounds/magic4.ogg')
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
    pause.05
    scene white
   
    pause.05
    scene bg meadow
    show threetits
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
    play music wnd fadein 3
    pause 
    
    s "I don't feel any different..." 
    show threenormal
    with Dissolve(.1)
    s "I hope not all of your spells are as useless as this one, mage."
    m "Hm..."
    $ elena_pts += 1
    menu:
        m "(I can not quite put my finger on it, but there is something different about the princess)."
        "Undo the spell.":
            call masterstart
        "Not just yet.":
            call threegoon
            
label threegoon:
    pause
    show three topless
    pause
    show threetitsmad
    with Dissolve(.1)
    pause
    show threetitsmad2
    with Dissolve(.1)
    pause
    show threetitsmad3
    with Dissolve(.1)
    s "W...{p} What...{p} What on earth is this!?"
    m "If I may, your excellency, this is not exactly what you requested of me, but might be this is a new look for you that, I have no doubt, your fiance would appreciate." 
    s "Is it all a joke to you, old man?"
    s "Because, if so I shall share a few jokes of my own! Right now, for example, I am thinking it would be particularly funny to behead someone!"
    m "Please, your highness... Your humble servant is merely trying to help..."
    show threetitsmad4
    with Dissolve(.1)
    s "By turning my beautiful royal breasts into this abomination?! They look like a cows udders!\nAm I a cow to you now?"
    m "{size=-8}Your highness, I merely...{/size}"
    s "{size=+12}Undo this vile spell of yours at once, or you will be sorry!{/size}"
    m "{size=-6}Your wish is my command, your highness.{/size}"
    menu:
        m "{size=-4}(I really  do not appreciate being threatened... Should I really undo the spell now?){/size}"
        "Undo the spell now":
            call masterstart
        "Refuse to undo the spell":
            call three_no_undo 

label three_no_undo:     
    scene bg meadow
    show threetitsmad3
    pause 
    hide threetitsmad3
    show three_nakid
    pause
    hide three_nakid
    show three_nakida
    pause
    s "Just touch me one more time, peasant, and I swear..."
    menu:
        m "Alright, maybe I am testing my luck here... Time to move on?"
        "Undo the spell now.":
            call three_obey
        "No. I am not done yet.":
            call three_no_undo
            
            
label three_obey:
    m "My humble apologies, your majesty..."
    s "....."
    call masterstart
    
## See Through

label seethroughj:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/spot03.png", "screens/spot03b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show see_through
    pause.05
    scene white
    pause.05
    scene bg meadow
    show see_through
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
    $ renpy.music.set_volume(0.5, .5, channel="music")
    play music freedom fadein 3
    pause 
    
    s "I don't feel any different...\nI hope not all of your spells are as useless as this one, mage."
    m "Yes, your majesty, this combination is obviously useless...{w} I mean, I can see it 
    pretty clear.\nWe shall try another one then?" 
label seetrough_gawking:   
    pause
    s "What are you looking at? You are testing my patience, old man! Try another combination already!"
    m "Er... Yes, of course, your Majesty."
    menu:
        m "{size=-4}(Now that's a neat spell.  I will make sure to remember this one for future use. He-he...).{/size}"
        "Time to undo the spell.":
            call masterstart
        "Not yet.":
            call seetrough_gawking
        
 
##SLAVE            
label slavej:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/spot02.png", "screens/spot02b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show slave
    pause.05
    scene white
    pause.05
    scene bg meadow
    show slave
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
    play music wnd fadein 3
    pause 
    s "How can I serve my master?"
    m "Your...{w} Highness...?"
    show slave02
    with Dissolve(.1)
    pause
    show slave03
    with Dissolve(.1)
    hide slave
    hide slave02
    pause
    show slave04
    with Dissolve(.1)
    s "...What is this ridiculous outfit?! Undo this spell immediately!"
    
    
    menu:
        m "{size=-4}(Fascinating...  How should I reply to that?){/size}"
        "Your wish is my command.":
            call obey_slave
        "(Slap her!).":
            call notobey_slave
    
label obey_slave:
    m "Your wish is my command."
    call masterstart
    
label notobey_slave:
    pause
    scene white
    pause.02
    scene bg meadow
    show slave04
    show slap
    $ renpy.play('sounds/slap.mp3')
    with hpunch
    show slave05
    pause
    s "!!!!!"
    m " Know your place, slave!"
    show slave
    s "Forgive me, master. I live to serve you...{p}...I mean...{p}...What is this?{w}I feel so conflicted!"
    scene bg meadow
    show slave04
    with Dissolve(.1)
    s "I am a princess of Agrabah, not some filthy slave-girl!" 
    show slave
    with Dissolve(.1)
    s "This spell...{p}It's...{w}confusing my thoughts..."
    s "Undo it! Undo this spell before it took me over completely! Hurry!"
    menu:
        m "{size=-4}(How should I reply to that?){/size}"
        "Your wish is my command.":
            call obey_slave
        "(Slap her again!).":
            call notobey_slave2
label notobey_slave2:
    pause
    scene white
    pause.02
    scene bg meadow
    show slave04
    show slap
    $ renpy.play('sounds/slap.mp3')
    with hpunch
    show slave05
    s "!!!!!!!!!!!"
    m "Silence! Know your place, you insolent bitch, or I will punish you personally!"
    scene bg meadow
    show slave06
    with Dissolve(.1)
    s "Please, master, I beg you to forgive me..."
    m "(Hm... That felt good. Let's take it even further)."
    m "Is this how you beg? On your knees, whore!"
    s "As you wish, master."
    pause
    show blkfade
    with Dissolve(.9)
    pause
    m "Good... Now open your mouth!"
    s "..."
    pause
    $ renpy.play('sounds/slap.mp3')
    with hpunch
    m "Obey, me, slave!"
    s "Yes, master..."
    s "({i}Slurp... slurp... slurp...{/i})"
    show slavebj2 behind blkfade
    m "Oh...{p}Very good...{p}You are quite skilled for a princess..."
    pause
    hide blkfade
    with Dissolve(.7)
    pause
    show slavebj1
    with Dissolve(.1)
    pause
    s "{i}(Slurp?) A primphes? Buph I am noph a prinpheph,{p}(slurp), I am youph slaphe-phore,{/i} master..."
    m "He-he, yes you are! Keep sucking now!"
    hide slavebj1
    with Dissolve(.1)
    s "{i}(Slurp!){p}(Slurp!){p}(Slurp!){/i}{p}"
    m "(Hm... This is one powerful spell. I better remember this combination)."
    show slavebj1
    with Dissolve(.1)
    s "{i}(Slurp-gulp?){/i}"
    m "What? Just keep going!"
    hide slavebj1
    with Dissolve(.1)
    s "{i}(Slurp. Slurp...){/i}"
    pause
    show slavebj3
    with Dissolve(.4)
    s "{i}(Sob...){p}(Slurp, slurp...){p}(Sob, slurp...){/i}"
    m "Huh? Are you crying down there?"
    s "{i}(Slurp, sob, slurp.){/i} No, I do not, master, {i}(slurp. Sob.){/i}"
    m "Don't you lie to me, slave! Why are you crying?!"
    s "{i}(Slurp!){/i} I am not sure. {i}(Slurp){/i} I am so sorry, master. {i}(Sob.){/i} I know it is my rightful place to be my master's...\nslave-whore..."
    s "{i}(Sob... Slurp, slurp){/i}, but, for some reason I feel so embarrassed, humiliated and...{w} {i}(sob...){/i} ...Angry...{p}{i}(Slurp, sob, slurp, sob...){/i}"
    m "{size=-4}(Is the spell wearing off? I better hurry up!){/size}"
    s "{i}(Sob, sob, slurp...){/i}"
    m "Hey, whore, speed it up, would you!? I mean to fill your mouth with my cum before you get back to your senses."
    s "{i}(Slurp-slurp?){/i}"
    m "Never mind! Keep sucking!"
    show slavebj3
    with Dissolve(.4)
    s "{i}{size=+4}Slurp!\nSlurp!\nSlurp!{/size}{/i}"
    m "That's a good girl. Like this! Yes! Almost there!"
    s "{i}{size=+4}Slurp!!!\nSlurp!!!\nSlurp!!!{/size}{/i}"
    show slavebj4
    with flashbulb
    g4 "........!!!!!!!!!!!!! {size=+10}Arh! Take my cum, you royal whore! Gulp it all down!{/size}"
    s "{i}{size=+8}!!! Slurp! Gulp!... Gulp!.... Gulp!.......{/size}{/i}"
    s "{i}{size=+4}Gulp... Gulp...{p} ............Gulp.{/size}{/i}"
    s "{i}...Gulp...{/i}"
    pause
    show blkfade
    with Dissolve(.9)    
    m "...Oh, wow, that was great."
    s "...Thank you...{w} ...for feeding me your cum, master... \n(...sob...)"
    pause
    scene bg meadow
    show sylvie smile
    $ renpy.play('sounds/magic4.ogg')    
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
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
    pause
    show jascun1
    with Dissolve(.1)
    s "........"
    m "........"
    show jascun2
    with Dissolve(.1)
    s "...What just happened?"
    m "...I am afraid this was not the spell we are looking for, your highness..."
        
    s " ...What is this odd taste in my mouth?..."
    m "........."
    s "...It kind of tastes like sp..."
    show jascun3
    with Dissolve(.1)  
    s "...never mind. Let's try another spell. And hurry up, old man. I don't have all day!"
    m "Yes, your highness."
    jump masterstart2
    
##SLIME

label slime:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/spot04.png", "screens/spot04b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show slime1
    pause.05
    scene white
    pause.05
    scene bg meadow
    show slime1
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
    play music sillyc fadein 3
    pause 
    s "Squack-squack!!"
    m "...Oh no! What have I done?! I turned her highness, the princess of Agrabah, into a {p}...some kind of living slime creature?"
    s "Squack-squack!!"
    m "...I am afraid I can not understand what you are saying, your highness."
    s "Squack-squack!!Squack-squack!!Squack-squack!!"
    m "Yes, your highness, I shall return you to your normal royal self at once."
    s "Squack-squack!!Squack-squack!!Squack-squack!!Squack-squack!!Squack-squack!!Squack-squack!!"
    menu:
        m "(There is nothing left to do, really.\nIn this state she is simply repulsive)."
        "Undo the spell.":
            call masterstart
        
##NAKID

label nakidj:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/spot06.png", "screens/spot06b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show nakid1
    pause.05
    scene white
    pause.05
    scene bg meadow
    show nakid1
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
    $ renpy.music.set_volume(0.5, .5, channel="music")
    play music freedom fadein 3
    pause 
    s "What is the meaning of this, mage?!\nWhere did all my clothes go?"
    m "I am so terribly sorry, your highness. I think the spell backfired somehow, and as a result all your royal attire got vaporized..."
    s "!!! I could not care less for the reason behind this disgrace! Just set it right!"
    m "Yes, your highness, I shall do so at once!"
    s "You better! I can not be seen like this!\nNot by the likes of you!"
    m "Of course not, your highness!"
    m "......."
    m "...."
    s "Stop staring at me then, unless you want to lose those filthy eyes of yours."
    m "Yes, your highness, I mean, no. I mean I will fix everything at once, your majesty."
    menu:
        m "{size=-4}(She is naked...\nThe princess of Agrabah is fully naked in front of me... ){/size}"
        "Undo the spell.":
            call obey_slave
        "Not yet.":
            call nakidnobey
label nakidnobey:
    pause
    show nakid5
    with Dissolve(.1)
    s "Don't you dare touching me with your filthy claws, or I swear, you will lose them!"
    m "I did not mean to, I beg you to forgive me, your highness."
    hide nakid5
    with Dissolve(.1)
    s "Just fix your spell!"
    menu:
        m "(I guess I have to obey...)"
        "Obey.":
            call obey_slave
        "Disobey.":
            call nakidnobey
            
            
## LOVE POTION

label lpotion:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/spot09.png", "screens/spot09b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show lpotion01
    pause.05
    scene white
    pause.05
    scene bg meadow
    show lpotion01
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
    show bar01
    play music wnd fadein 3
    pause 
    s "It suddenly got hotter in here..." 
    m "It did, your highness?\nI did not notice..."
    s "Yeah... I feel so...{w} hot... and...{w} er...{w} never mind..."
    m "I need to know exactly what you feel, your majesty. It will help me to identify the spell faster." 
    s "I said never mind. I just need to... {image=textheart.png}Ah... {p}*pant*...{w} *pant*..."
    m "{size=-6}(Hm... Can it be that this combination of ingredients creates a \"love potion\" effect? Fascinating...){/size}"
    s "*pant* {image=textheart.png}Ah....{p}{image=textheart.png}Ah.... *pant*..."
    m "Your majesty do you feel any kind of excitement?" 
    s "What? I told you I am fine...{p}{image=textheart.png}Ah... I don't feel anything.{p}{image=textheart.png}Ah... {size=-10}(Especially not towards you, old man!){/size} {image=textheart.png}Ah..."
    m "Huh? Towards me, your highness?"
    s "Nothing! I did not say anything!\nThis spell is affecting me somehow...\nYou need to undo it before... {image=textheart.png}ah... I loose my mind...{p} {image=textheart.png}{image=textheart.png}Ahh..."
    show lpotion02
    with flashbulb
    hide lpotion01
    show bar02
    with Dissolve(.1)
    hide bar01
    pause
## CHOICE A 
label choicea:
    menu:
        m "Hm... Princess seem to be under influence of a \"love potion\" spell. If I play my cards right, it might be fun! What should I say now?"
        "\"Quiet, you filthy whore.\"":            
            m "Quiet, you filthy whore!"   
            jump gameover
        "\"We need to study the effects more.\"":
            m "Maybe it would be wise to study the effects a little more first, your highness."
            s "What are you blabbling about, old fool!? Undo your spell at once, that's an order!"
            m "...as you wish, your highness."
            jump choicea             
        "\"I shall undo the spell at once.\"":
            jump obey_slave
        "\"No. Tell me what do you feel.\"":
            m "I am afraid I have to insist your highness.\nTell me what do you feel."
            s "I did tell you already: I feel hot... {image=textheart.png}ah... and.. {image=textheart.png}ah... {w}exited... \nI want to... {image=textheart.png}Ahh!"
            jump choiceb
        "\"I think your breasts got a bit bigger.\"":
            m "Your highness, I think your breasts got a bit bigger."
            s "Ah... They did? Ah... Maybe you should examine them to be sure?"
            m "Certainly."
            pause
            s "!!! What are you doing?! Keep your hands away from me!"
            m "I am sorry, your highness. It's just you said that..."
            s "Did I say That you can fondle me at will? Geez... Get a hold of yourself, you peasant!"
            m "......................."
            jump choicea
            
label choiceb:
    hide lpotion02
    show lpotion03
    with flashbulb
    show bar03
    with Dissolve(.1)
    hide bar02
    pause
    
label choiceb2: 
    
    menu:
        "\"You have such beautiful eyes.\"":
            m "Did anyone ever tell you that you have the most beautiful eyes, your highness?"
            s "Yes, my fiance, Aladdin, did on countless occasions.\nEnough with this nonsense, old man! Undo the spell!"
            jump choiceb2
        "\"Describe exactly what you feel, princess.\"":
            m "I am not going to undo this spell until you describe exactly what you feel, princess."
            s "I told you already! I feel a heat allover my body...\nBut not the kind of heat you usually feel under the desert sun. {w}The other kind..."
            m "Other kind, your highness?"
            s "Yes! Other kind! You are so dull! I am speaking of sexual desire. It fills my body with wants and my mind with thoughts...{w} Naughty thoughts... {w}{image=textheart.png}Ah..."
            jump choicec
        "\"You slut, all you need is a big cock.\"":
            m "Just admit it, you slut, all you need is a big cock."
            jump gameover
        "\"Akabur secretly rules the world.\"":
            m "They say Akabur secretly rules the world."  
            s "Yes, I heard the rumors."
            jump choiceb2            
        "\"Will you let me squeeze your breasts?\"":
            m "Please will you let me squeeze your breasts, your highness. Just once."
            s "Have you completely lost it, old fool? Get a hold of yourself!"
            s "I am a member of a royal family! It is unthinkable to let some filthy peasant touch me. To let him fondle my breasts." 
            s "Or maybe even surrender to his will completely, let him have his way with me, treat me like a market street whore...?"
            m "What? No, you highness, all I wanted was...{p} I would never..."
            s "Let him manhandle me. Here, on this dirty floor... It would be so not princess-like... {w}So depraved... {w}So... {image=textheart.png}Ah.... {image=textheart.png}AH!!!!"
            jump choicec
            
label choicec:
    hide lpotion03
    show lpotion04
    with flashbulb
    show bar04
    with Dissolve(.1)
    hide bar03
    pause
    
label choicec2:
    
    menu:
        "\"Shut up an show me your tits, whore!\"":
            m "Shut up and show me your tits, whore!"
            s "Insolent peasant! How dare you to speak to your princess in this manner!? I will have you beheaded for this!"
            m "Just admit it, you are nothing but a common slut after all!" 
            s "Fucking bastard... {w}{image=textheart.png}ah... {w}{image=textheart.png}ah... {w}\nHow dare you... {w}{image=textheart.png}ah..."
            m "Princess of Agarabah? Ha! Looks more like a common whore to me!"
            s "Ah.. Ah.. Stop, saying such things, {image=textheart.png}{image=textheart.png}ah..."
            jump choiced
        "\"What are you thinking about?\"":
            m "I need to know exactly what are you thinking about, princess."
            s "How many times should I tell you the same thing, old man?"
            s "Your stupid spell is playing tricks with my mind! All I can think about is...{w}is... {w}all I want is to..." 
            m "Yes your highness?"
            s "All I want is to lay with a man, alright?!! And I can't fight it! I imagine you, old man, grabbing me and fucking me right here, right now."
            s "I am picturing you releasing your vile seed right in my face, treating me like a worthless whore that I am! {image=textheart.png}Ah!"
            m "Oh, your majesty if you would only allow me, I would gladly..."
            s "No! Stay away from me, peasant! STAY THE HELL AWAY, YOU HEAR ME?!!! Undo this spell, I am ordering you to! Undo your spell before it's to late!"
            m "Tsk... {size=-4}(As if...){/size}"
            jump choicec2
        "\"Teenage mutant ninja turtles...\"":
            m "Teenage mutant ninja turtles..."
            s "{size=+2}Teenage mutant ninja turtles...{/size}"
            m "{size=+4}Teenage mutant ninja turtles!{/size}"
            s "{size=+6}Heroes in a half-shell!{/size}"
            m "{size=+8}Turtle power!!!{/size}"
            s "................."
            m "..............."
            jump choicec2
        "\"People say you lay with your pet tiger.\"":
            m "Word on the street is, you lay with your pet tiger, princess."
            jump gameover
        "\"I have a present for you (My dick).\"":
            m "Your highness I have a present for you!" 
            s "A present?... *pant*" 
            m "Yes! My rock-hard cock! Would you like to see it?"
            s "You are testing my patience, old man!"
            jump choiceb2
            
label choiced:
    hide lpotion04
    show lpotion05
    with flashbulb
    show bar05
    with Dissolve(.1)
    hide bar04
    pause
    
label choiced2:
   
    menu:
        "\"Pull down those pants now, slut.\"":
            m "That's enough slut. Pull down those pants and spread your legs!"
            jump gameover
        "\"They canceled \"Firefly\"...\"":
            m "They should have never canceled \"Firefly\"..." 
            s "No, they should have not. But that's what makes those fifteen episodes that much more precious..."
            jump choiced2
        "\"Repeat after me: \"I am a dirty whore.\"":
            m "Repeat after me now, princess: \"I am a dirty whore\"."
            s "What? How dare you?!"
            m "You need to repeat it after me in order to undo this spell, your highness."
            s "....*pant* {image=textheart.png}Ah... {image=textheart.png}Ah...   {w}Fine.... {w}I am a dirty whore... {image=textheart.png}Ah..."
            m "(I can't believe she is buying it. Alright then.) Now say: \"I love to suck cock\"."
            s "... {image=textheart.png}Ah...{w} I love to... {w}I love to... suck... {w}cock... {image=textheart.png}Ah...{w} {image=textheart.png}AH!"
            m "\"I am a worthless cock sucker, my only purpose of existence is to gulp down cum\"."
            s "{image=textheart.png}Ah...{w} My only... {w}Purpose... {w}is... {w}{image=textheart.png}Ah... {image=textheart.png}Ah... {w}Cum... {w}I gulp down cum and suck cocks, because that's what I am good at! I am a worthless WHORE!!! {image=textheart.png}{image=textheart.png}{image=textheart.png}AHHH{image=textheart.png}!!!!"
            m "(Wow, she has completely succumbed to the spells effect. Or is it just her true nature? )"
            jump choicee
        "\"So, Aladdin's harem starts with you then?\"":
            m "So, Aladdin's harem starts with you then, your highness?" 
            s "....................................."
            m "I wonder what his next wife will look like... A shorter hair maybe? Or longer legs?"
            m "Or bigger breasts perhaps? Is this why you are looking for this spell, your highness? A desperate attempt to postpone the enviable?" 
            s "You bore me old man... Stop saying nonsense and undo this spell."
            jump choicec2
        "\"I need to squeeze one of your tits.\"":
            m "To undo this spell I need to squeeze one of your tits, your highness."
            s "Do you think I am that stupid, old man?  I would never let some filthy peasant touch me"
            m "......"
            jump choicec2
    
label choicee:
    hide lpotion05
    show lpotion06
    with flashbulb
    show bar06
    with Dissolve(.1)
    hide bar05
    pause
    
label choicee2:
    
    menu:
        "\"You OK? Should I call for guards?\"":
            jump choicesfinal
        "\"Your highness, you are so beautiful.\"":
            m "Your highness. you are so beautiful."
            s "Yes, I know. Now stop saying obvious things to me and undo your spell."
            jump choiced2        
        "\"So... do you swallow?\"":
            m "So... Do you swallow?"
            s "What? What kind of question is that? of course I swallow. Who in this day and age doesn't?"
            m "Fair enough..."
            jump choicee2
        "\"In brightest day, in blackest night...\"":
            m "In brightest day, in blackest night, No evil shall escape my sight."
            s "Let those who worship evil's might, Beware my power, Green Lantern's light!!!"
            m "...."
            s "...."
            s "Please stop saying random thing like this..."
            m "...Yes, your highness."
            jump choicee2
        "\"Dirty fucking whore you are!\"":
            m "Dirty fucking whore you are!"
            s "...................."
            s "...."
            jump choicee2
            
label choicesfinal:
   
    m "Are you feeling alright, princess?"
    s "Yes, I am feeling great... {image=textheart.png}Ah... I mean no, I told you already: I am not in control of my body anymore..."
    m "Should I call for the guards?"
    s "What? No! Have you lost your mind, old man?  No one shall see me like this! No one! Do you understand me, mage?... {image=textheart.png}Ah..." 
    m "..........."
    menu:
        m "(Do I understand...?)"
        "\"Of course, I understand, your highness.\"":
            jump choicee2
        "\"I think I should call the guards.\"":
            m "I think I should call the guards nevertheless, your highness." 
            s "No! I told you, no one should see me in this state! Don't you dare to call anyone that's an order."
            m "But what if I did call for them? And they would rush in here, and see their beloved princess all hot and sweaty..."
            s "{image=textheart.png}Ah... {image=textheart.png}ah..."
            m "Sitting here, half naked, touching herself..."
            s "{image=textheart.png}Yes... {image=textheart.png}Yes..."
            show lpotion07
            with flashbulb
            
            m "And some dirty peasant jerking off his cock right in front of her... Maybe she even starts to suck on the peasant's cock?"
            s "{image=textheart.png}Ah... {image=textheart.png}Ah... {image=textheart.png}ah...  {w}{image=textheart.png}A slut..."
            m "Yes, yes, she is a dirty slut, that princess is. \nAnd the guards see her, and they can not believe their eyes... And they..."
            s "{image=textheart.png}Ah! What? What do they do with that whore!? {image=textheart.png}AH!"
            m "They grab her, toss her on the ground, pull out their cocks and start raping her like animals!!!"
            hide lpotion07
            with Dissolve(.1)
            s "I'm cuming?!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            hide lpotion07
            hide lpotion06
            show lpotion08
            with flashbulb
            show bar08
            with Dissolve(.1)
            hide bar07
            s "{image=textheart.png}A-{image=textheart.png}A-{image=textheart.png}A-{image=textheart.png}A-{image=textheart.png}A-{image=textheart.png}A-{image=textheart.png}A-{image=textheart.png}AH!"
            show lpotion08
            with flashbulb           
            s "I'M CUUUUUUUMING!!!{image=textheart.png}"
            show lpotion08
            with flashbulb
            show lpotion08
            with flashbulb
            s "{image=textheart.png}Ah! {image=textheart.png}Ah! {image=textheart.png}Ah!"
            stop music fadeout 3
            s "........"
            s "......"
            s "...."
            s "..."
            m "Your highness, I am sorry, this was the only way to lift the spell. I hope you are alright?"
            show lpotion09
            with Dissolve(.5)
            hide lpotion08
            $ renpy.music.set_volume(0.3, .5, channel="music")
            play music mark fadein 3
            s "More then just alright, old man. This was heavenly! You are good with your words, you old prick." 
            m "I am good with my spells, your highness..."
            s "{image=textheart.png}Ah... Yes you are. And I am good with mine."
            m "???"
            s "I am feeling generous today. Tell you what: I will let you take your dick out and jerk it off in front of me, how about that?"
            m "Your highness..."
            s "Just make sure that vile thing does not touch me." 
            m "Of course, your highness."
            pause
            show blkfade
            with Dissolve(.5)
            pause.2
            scene bg lp
            hide blkfade
            with Dissolve(.5)
            pause
            s "So tell me what do you feel, you old pervert. I bet never did you dream to see me in this position."
            m "...well, I did fantasize about this..."
            show blkfade
            with Dissolve(.5)
            pause.2
            show lpfinal01
            hide blkfade
            with Dissolve(.5)
            pause
            s "Oh... Do tell... And don't forget to jerk that big cock of yours. Do it harder!" 
            m "...oh, your highness!"
            show lpfinal02
            with Dissolve(.3)
            hide lpfinal01
            s "Yes, I am your princess whore today! Come on! Cum! Spray me with your nasty seed! Cover my face with semen!"
            m "YOUR MAJESTY!"
            show lpfinal03
            with Dissolve(.3)
            hide lpfinal02
            s "Oh, right, I forgot to mention: don't you dare to actually come on my face though..."
            m "Your Majesty?"
            s "Yes, we are playing this little game here, but last thing I want is your filthy sperm anywhere on me. \"Look. but don't touch\", you understand me?"
            menu:
                m "It is so tempting. What should I do?"
                "Hold it and listen.":
                    s "Jerk it off all you want, but make sure you do not cum anywhere on me."
                    m "As you wish, your highness..."
                    s "What? You think I want this? Alright, alright, I gotta admit I do find some odd pleasure in this depravity..."
                    s "Come on now, release your seed! I want to see you cum!"
                    m "Yes!"
                    s "YES! COME FOR YOUR PRINCESS! COME FOR YOUR WHORE{image=textheart.png}!"
                    g4 "CUMMING! ARGH!"
                    show lpfinal09
                    with Dissolve(.3)
                    hide lpfinal03
                    pause
                    s "Now that's a good peasant!"
                    g4 "ARGH!!!"
                    show lpfinal10
                    with flashbulb
                    show lpfinal10
                    with flashbulb
                    hide lpfinal09
                    pause 
                    s "That's a lot of cum. Were you saving it for me? Were you saving it for your princess-whore?"
                    s " Imagine releasing all this amount in my mouth! I would most certainly choke."
                    g4 "{size=+6}AAAAAAAARGH!!!!!{/size}" 
                    show lpfinal11
                    with flashbulb
                    show lpfinal11
                    with flashbulb
                    hide lpfinal10
                    pause
                    s "{size=+6}!?{/size}"
                    s "This is the longest orgasm I have ever seen a man have... How long has it been since you last time had sex, you old pervert?"
                    show blkfade
                    with Dissolve(1)
                    pause.9
                    show lpfinal12
                    hide blkfade
                    with Dissolve(1)
                    pause
                    m "Your highness.... *pant*"
                    s "This was truly magical, I had a great time..." 
                    s "But should you say a single word about this to anyone I will have you beheaded and feed your headless corpse to my tiger Rajah."
                    m "I'm not sure what you are talking about, your highness, because I do not recall anything out of the ordinary happening today..."
                    s "That's a good peasant."
                    m "{size=-6}(Then again, seeing you behave like a common whore is not an unordinairy thing...).{/size}" 
                    s "Did you say something, Mage?"
                    m "Yes, your highness, I said if you do not mind we shall proceed with our experiments..."
                    s "Yes, indeed, and hurry it up, would you? I don't have all day..." 
                    pause
                    show lpfinal13
                    with Dissolve(.2)
                    hide lpfinal12
                    pause
                    s "Oh, and would you clean up that mess you did on the floor? I don't want to step into \"it\" by accident."
                    m "Of course..."  
                    pause
                    show blkfade
                    with Dissolve(1)
                    pause.9
                    jump masterstart 
                "Cum straight in her face.":
                    play music wnd fadein 3
                    $ renpy.music.set_volume(1.0, .5, channel=7)
                    show lpfinal04
                    with flashbulb
                    m "{size=+6}Arg!!!{/size}"
                    s "!!!!!!!!!"
                    m "{size=+4}Yes!!!{/size}"
                    show lpfinal05
                    with flashbulb
                    show lpfinal05
                    with flashbulb
                    hide lpfinal04
                    pause
                    s "What are you...? Didn't you hear me saying that I..."
                    g4 "Oh, yes! Yes! Take it, you whore!"
                    s "!!!!!!!"
                    show lpfinal06
                    with flashbulb
                    show lpfinal06
                    with flashbulb
                    hide lpfinal05
                    pause
                    s "Stop it! Stop cumming on your princess's face while she is talking to you!"
                    g4 "Yes, you slut take it! Yes!"
                    s "!!!"
                    show lpfinal07
                    with flashbulb
                    hide lpfinal06
                    pause
                    g4 "!!!!!!!!!!!!!"
                    s "..........."
                    show lpfinal08
                    with flashbulb
                    hide lpfinal07
                    pause
                    s "Alright, you filthy peasant, have it your way..."  
                    m "Oh, I think this was the last of it..."
                    s "Yeah, whatever, you freak, just give me something to wipe my face..."
                    m "Of course your highness. I hope you will not have me beheaded for this."
                    s "Have you beheaded for ignoring my direct order and defiling me with your vile semen? Of course not." 
                    m "Er...{w} Thank you... {w} ...your highness."
                    s "Although, shall you fail to find the correct spell to satisfy my need, I will have you castrated, and will feed your testicles to my pet monkey, Abu." 
                    m "Of course, your highness, as you wish. But I assure you, the right combination is somewhere among these scrolls and ingredients."
                    s "Hurry up and try another spell already, you old prick. I don't have all day."
                    m "Of course, your majesty..."
                    pause
                    show blkfade
                    with Dissolve(1)
                    pause.9
                    jump masterstart
                    
## APPLE

label apple:
        scene bg meadow
        show sylvie smile
$ select = renpy.imagemap("screens/spot08.png", "screens/spot08b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":
        $ renpy.play('sounds/magic4.ogg')
        scene white
        pause.02
        scene bg meadow
        show magic5
        pause.05
        scene white
        pause.05
        scene bg meadow
        show apple01
        pause.05
        scene white
        pause.05
        scene bg meadow
        show apple01
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
        play music wnd fadein 3
        pause
        m "Your Majesty? Princess Jasmine? Where did she go?" 
label appleleave:        
        pause
        menu:
            m "Oh, look, an apple! Goody! I love apples!"
            "\"Leave it be.\"":
                jump appleleave
            "\"Have a bite.\"":                
                "*Crunch!*"
                $ renpy.play('sounds/crunch.wav')
                show apple02
                with Dissolve(.1)
                hide apple01
                m "Oh, this apple is delicious!" 
                pause
                $ renpy.play('sounds/crunch.wav')
                show apple03
                with Dissolve(.1)
                hide apple02
                pause.3
                with Dissolve(.1)
                $ renpy.play('sounds/crunch.wav')
                m "*Crunch!* *Crunch!* Delicious indeed. Kind of tastes like a chicken..."
                m "I wonder where the majesty disappeared to though..."
                m "Wait a second...{w} Her highness disappeared, and this apple manifested in her place..."
                m "No... "
                m "This can't be!"
                m "{size=+4}No!....................{/size}"
                show blkfade
                with Dissolve(.5)
                show apple04 behind blkfade
                pause.9
                play music galm fadein.1
                hide blkfade
                with Dissolve(.5)
                
                pause
                show blkfade
                with Dissolve(3)
                jump finalgover
                
            "\"Undo the spell.\"":
                jump masterstart
                
                
label loli:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/spot10.png", "screens/spot10b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show loli1
    pause.05
    scene white
    pause.05
    scene bg meadow
    show loli1
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
    play music mark fadein 3
    
    pause
    m "...Er... Is this you, your highness?"
    show lolismile
    with Dissolve(.2)
    s "Yes, yes! Her highness Little Princess! That's me!" 
    s "You are so nice to call me that, grandpa."
    hide lolismile
    with Dissolve(.2)
    s "Hm... You are much older then any of the people that usually molest me..."
    s "But since you called me a princess I shall let you do things to me."
    m "...I am not sure what is going on here..."
    m "......"
    s "Huh? Oh, come on, grandpa, don't you want to touch me?" 
    m "{size=-2}(What is she exactly, I wonder? New form of princess Jasmine or a completely different being from another dimension? If so, where did princess Jasmine go?){/size}"
    s "Oh, come on, old man, I am not getting any younger here. Well actually I am not getting any older either..."
    show loliangry
    with Dissolve(.1)
    hide loli1
    s "You see, I am a fruit of fiction, meaning that I am not an actual real-life girl. But people are just so fucking stupid sometimes!"
    show loliangry2
    with Dissolve(.1)
    hide loliangry
    s "You hear me, you fucktards? I hate that I have to stoop to your level and explain obvious things to you."
    s "I am not underage, but even if I were I still would be a fictional character, you dumbasses!"
    s "........................"
    show loliangry3
    with Dissolve(.1)
    hide loliangry2
    s "Wow, for a second there I sounded just like my father."
    m "Who are you talking to?"
    show loli1
    with Dissolve(.1)
    hide loliangry3
    s "Oh, gramps, does it matter? Just go ahead and start groping me already."
    menu:
        m "What to do, what to do...?"
        "Expose her tits.":
            jump loli2
        "Undo the spell.":
            m "I am sending you back where you came from."
            show loliangry
            with Dissolve(.1)
            s "No fun..."
            jump masterstart
            
label loli2:            
    m "Oh, alright then, I guess I do need to examine you in the interest of science." 
    stop music fadeout 4
    show lolismile
    with Dissolve(.2)
    s "Yes, yes, examine me, grandpa!"
    
    pause    
    hide loli01
    show ltopless
    play music wnd fadein 3
label exam2:    
    pause
    hide lolisups
    hide ltopless
    show ltopless2
    pause
    show ltopless2
    pause
    show lolisups
    with Dissolve(.2)
    s "Huh? Is the examination over? So fast? :("
    menu:
        "\"No. Not yet.\"":
            jump exam2
        "\"Yes, it is over.\"":
            jump loli3
label loli3:
    hide lolisups
    s "OK, what's next? What's next?"
    m "I guess I need to undo the spell now..."
    s "A spell? Awesome! What does it mean exactly..."
    m "It means that you will be sent back to where ever you came from..."
    show lolisulk
    with Dissolve(.1)
    s "What? No fun! :("
    hide lolisulk
    with Dissolve(.1)
    s "Come on! Do more naughty things to me instead!"
    m "Are you sure you are not princess Jasmine?"
    s "Absolutely sure! I don't even know who that is... Although... Is it that Arab princess girl from that old cartoon?"
    m "Alright, as long as you are not her it should be safe for me."
    show lolisups
    with Dissolve(.2)
    hide lolisulk
    with Dissolve(.2)
    
    s "Huh?"
    m "Go down on your knees, girl, and open your mouth!"
    hide lolisulk
    with Dissolve(.2)
    hide lolisups
    with Dissolve(.2)
    s "Fun! Yes, tell me what to do."
    m "I already did! Go down on you knees and open your mouth!"
    s "Yes, yes! Like this?"
    show blkfade
    with Dissolve(.7)
    pause
    m "Perfect. Now just hold still..."
    m "Look at me!"
    
    scene lolifin00
    show blkfade
    pause.3
    hide blkfade
    with Dissolve(.3)
    pause
    s "Like this?"
    show lani
    with Dissolve(.3)
    pause
    m "Yes, yes... You dirty girl."
    s "He-he, that's me!"
    m "Yes, yes... Just keep your mouth wide open like that and keep looking in my eyes..."
    s "Fun! Fun! I think I know what's gonna happen next. It's called \"bukkake\" right?"
    m "A book of what?"
    s "\"Bukkake\", it means that you will come all over my face."
    m "Oh, You are just the cutest thing, aren't you?"
    s "Yes, I am. I think that is why people always try to touch me."
    s "That one time these guys started to touch me, and then they stuck a lollipop in my butt, and then they took it out and put it in my mouth instead and ..."
    
    g4 "Argh! Here it comes!"
    show lolifin02
    with flashbulb
    with hpunch
    
    show lolifin03
    with flashbulb
    g4 "Argh! You little whore!"
    show lolifin04
    with flashbulb
    g4 "Yes! Oh, yes!!!"
    
    s "Gulp! This is delicious! I want more!"
    g4 "Here you go, you little slut, all over your face!"
    show lolifin05
    with flashbulb
    
    s "Some old man I don't even know is coming on my face! Father would be so proud!"
    m "There! Some more for you!"
    show lolifin06
    with flashbulb
    s "Ah?!{image=textheart.png} Gulp! Gulp! Gulp!..."
    m "...well, I think this was the last of it."
    show lolifin07
    with flashbulb
    s "Ah, your sperm is so hot..."
    s "Thank you for cumming on my face."
    m "Yeah, whatever. Time for you to get the fuck out of here!"
    s "What?"
    
    jump masterstart

## GHOST
label ghostl:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/spot05.png", "screens/spot05b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            ])     
    
    
if select == "no":
    jump fromcsoon
if select == "yes":
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show ghostan
    pause.05
    scene white
    pause.05
    scene bg meadow
    show ghostan
    show tbl behind ghostan
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
    play music xf fadein 3
    $ renpy.music.set_volume(0.5, .5, channel="music")
    pause
    s "........."
    m "Your Highness?" 
    s "It's so cold in here.. Am I.... floating?"
    m "Hm... Seems to be that this particular combination of ingredients turns the subject into a...{w}  ...ghost."
    s "A ghost? So that's what I am?... I see..."
    m "You are not mad at me, your Majesty?"
    s "Why would I be mad at you, mage? I have no wants, no desires... Endless darkness and cold engulfs me..."
    s "I am finally at peace..."
    g4 "Oh, dear... Did I just murder the princess? Crap! I must undo the spell at once!"
label ghostmenu:  
    pause
    menu:
        
        "Undo the spell.":
            jump masterstart
        "Not yet.":
            pause
            s "I feel so peaceful... I think I am ready to leave this mortal plane and move on to my afterlife..."
            g4 "Hold that thought, your highness! I will bring you back to life these instance!!"
            jump ghostmenu

        
    
#################################
label faq:
    play music galm fadeout 1
    scene title2
    with flashbb
    a1 "Hello. My name is Akabur. I am the creator of this game and I'm here to answer your questions." 
label faq2:    
    menu:
        "How can I show my support?":
            a1 "Well, there are few ways to do that..."  
            a1 "The easiest way would be to contact me (akaburfake2@yahoo.com) and let me know that you enjoyed the game."
            a1 "Or you could contact contact me (akaburfake2@yahoo.com) personally and support me with a donation."
            a1 "PayPal, WebMoney, CrediCard, YandexMoney... Whichever way you are more comfortable with..."
            a1 "For an independent artist like myself every buck counts..."
            a1 "The Best way to support me though would be to follow this link: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a} and join the site, because \"hentai united\" is my main source of my income."
            a1 "Make sure you follow the link though, That's the only way you will be counted as \"akabur's follower\" by the site's system."
            a1 "And also, don't unsubscribe the moment I take a little break in-between updates to work on a bigger project (like this game for example)."
            label payments:
            menu:
                "-WebMoeny info-":
                    a1 "My RUBLES WebMoney purse: R133931000745"
                    a1 "My USD WebMoney purse: Z319925489258"
                    a1 "My EURO WebMoney purse: E800599783938"
                    jump payments
                "-YandexMoney Info-":
                    a1 "My Yandex Purse Number: 41001849167270"
                    jump payments
                "-PayPal Info-":
                    a1 "Contact me via email and i will give you my PayPal."
                    jump payments
                "-Credit Card-":
                    a1 "Here: {a=http://www.test.akabur.com/donate}how to donate with Credit Card.{/a}"
                    jump payments
                "-Cancel-":
                    jump faq2
        
        "How to stay tuned?":
            a1 "Well, follow this link: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a} and subscribe. Or visit my site: {a=http://akabur.com}akabur.com{/a} and follow me on twitter or something."
            jump faq2
        "I have another question.":
            a1 "If you have a question that is not covered in this \"F.A.Q.\", feel free to email it to me: akaburfake2@yahoo.com"
            a1 "Or ask your question here: {a=http://ask.fm/AKABUR}ask.fm/AKABUR{/a}"
            jump faq2
        "I want to report a bug/error.":
            a1 "This game has been tested many many many times, but the best testers are always the players."
            a1 "So if you did encounter a bug, typo or even a grammatical error - feel free to contact me (akaburfake2@yahoo.com) and I will fix the problem in the next version of the game."
            jump faq2
        "Who helped you create this game?":
            show image "09_gallery/ext38.jpg" with d5
            a1 "Nobody... except my AWESOME PET FOX PLUSHY."   
            hide image "09_gallery/ext38.jpg" with d5
            a1 "But I would never (EVER) be able to complete this game if not for the support people keep showing me, of course."
            a1 "It is great to have full creative freedom, but it comes with a price: every project takes me a very long time to finish."
            a1 "So thank you for your understanding folks. Thank you for keeping your Hentiunited subscriptions going and feeding me..."
            jump faq2
        "Is it OK to hack and translate this game?":
            a1 "..."
            a1 "..."
            a3 "no."
            a6 "Just want all the volunteer translators out there to know this..."
            a7 "I absolutely {size=+5}do not{/size} give you my permission to hack this game and translate it to Chinese, Spanish, Russian or any other language."
            a1 "If this game ever gets translated into any other language, you should know that it happened without my consent."
            a6 "I know you (my dear translator fucks) must have your terribly misguided reasons to put in hours of work into translating of tons of in-game text."
            a7 "Maybe you even think that you actually help me to reach wider audience or something."
            a7 "But I don't care what motivates you! Simply don't!"
            a1 "So I'm saying it again:..."
            a7 "{size=+6}I DO NOT GIVE YOU MY PERMISSION TO TRANSLATE THIS GAME!{/size}"
            a7 "{size=+6}I DO NOT WANT YOU TO DO THAT!{/size}"
            a6 "If you do it then know that you are going against my will..."
            a1 "And Santa will most certainly put you on a \"naughty kids list\" for doing so." 
            jump faq2

        "Nevermind. Let me out of here!":
            return

    
    return
    
label gallery:
    play music galm fadeout 1
    scene title2
    with flashbb
    menu:
        a1 "Welcome to the \"Princess Trainer\" gallery. Here you can have a look at some of the production artwork."
        "-Gallery volume 01-":
            jump volone
            
        "-Gallery volume 02-":
            jump volumetwo
        
        "-Gallery volume 03-":
            jump volume_three
            
        "-Cancel-":
            return 
        
label volone:    
    show image "09_gallery/ext01.jpg"
    with flashbb
    a1 "A bunch of different dress designs for Iris created by Dahr."
    a1 "I didn't ask for this many of course..."
    a2 "But Dahr felt like drawing a few different versions and I figured the more the merrier..."
    a1 "Only one made it into the final version of the game though..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext02.jpg"
    with flashbb
    a1 "The one on your left is the first version of Iris that Dahr drew for me."
    a2 "I loved it!"
    a1 "But I thought that it would be better if we could replace the piece of meat on her tray with a pint of wine..."
    a1 "Because big portion of the game-play will be about drinking wine and not about eating meat..."
    a1 "I also thought that her top was way too revealing, so I asked Dahr to fix those things if possible..."
    a2 "Which he did."
    a1 "The one on the right is the version of Iris you see in the final game."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext03.jpg"
    with flashbb
    a2 "A whole bunch of cute chibi-drawings Dahr created for me..."
    a1 "As you can see one of them even features Iris taking Jasmine for a walk..."
    a1 "Sadly this one didn't make it into the final game... Purely because of the harsh time limitations I had to work with."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext04.jpg"
    with flashbb
    a2 "Variety of emotions for Rose the teacher..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext06.jpg"
    with flashbb
    a2 "All sorts of in-game items created by Dahr."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext07.jpg"
    with flashbb
    a1 "My second draft of Loli... *khem* I mean Lola."
    a1 "Don't have much to say about this one..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext13.jpg"
    with flashbb
    a1 "First version of the \"whore outfit\" for Lola..."
    a1 "I didn't like it much..."
    a1 "I think my main problem with it was that it didn't fit Lola's flamboyant personality well..."
    a1 "Later on a created a new one... (Which fits her even less... heh)."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext14.jpg"
    with flashbb
    a1 "Undone raincoat and transparent rain coat... Just for fun."
    a1 "And \"face-fuck aftermath\" of her whore costume that I created but never had a chance to incorporate into the final game..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext15.jpg"
    with flashbb
    a2 "And this is my first version of lola..."
    a2 "I tried to give her a somewhat Arabic look..."
    a1 "As a result I got some girl that not only looks nothing like Lola..."
    a1 "But also, for some unknown reason had a very \"anime look\" to her."
    a1 "I tried to fix her eyes but it didn't made me dislike this version of her any less..."
    a1 "I drew another one later... The one you see in the game."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext16.jpg"
    with flashbb
    a1 "I also thought that maybe at some point in the game she would decide to get her body pierced..."
    a1 "That's how this abomination happened..."
    show ctc7 at right
    pause 
    hide ctc7
    show blkfade with d5
    a1 "This concludes volume one of the gallery."
    pause 1   
    stop music fadeout 1
    jump gallery
    

    
    

label volumetwo:
    show image "09_gallery/ext17.jpg"
    with flashbb
    a1 "I knew the game would need a way to keep track of your quest completion progress..."
    a1 "I thought it would be cool to create a little badge for every quest and make them appear in the \"Quest progress menu\"."
    a1 "Sort of like archivements in the modern games..."
    a1 "Later on I created a simple temporary draft just to test the system..."
    a1 "For that temporary draft I just used lines of text instead of (super cool) badges..."
    a1 "Eventually (because of the lack of time) I gave up and the temporary draft turned into permanent one..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext18.jpg"
    with flashbb
    a2 "Chibis...."
    a2 "Man, I love these things..."
    a2 "I love drawing them, I love animating them, I love seeing them in the final game..."
    a1 "How could anyone prefer boring, full screen SG's..."
    a2 "To this awesome little things..."
    a7 "...Is simply beyond me!!!"
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext19.jpg"
    with flashbb
    a1 "This strong, independent and successful woman was in charge of the \"JSGA\" before lovely Rose came along..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext21.jpg"
    with flashbb
    a1 "Just another costume that I spent hours developing and ended up not using..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext22.jpg"
    with flashbb
    a2 "Now this is interesting!"
    a1 "At first I wanted every sex scene in the game to be represented through adorable chibi-animations..."
    a1 "This is how I imagined the sex encounter between Genie, Jasmine and Iris would look like."
    show ctc7 at right
    pause 
    hide ctc7
    show blkfade with d5
    a1 "This concludes volume two of the gallery."
    pause 1  
    stop music fadeout 1
    jump gallery
    
    
label volume_three:
    show image "09_gallery/ext23.jpg"
    with flashbb
    a1 "The foursome CG. Pretty much self-explanatory...." 
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext24.jpg"
    with flashbb
    a1 "My first go at the game logo..."
    a1 "It was alright... But not great..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext25.jpg"
    with flashbb
    a1 "I guess you could call this one \"Concept art\"."
    a2 "Dahr is responsible for this one..."
    a1 "He sent it to me back when the game was on a very (VERY!) early stages of development..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext26.jpg"
    with flashbb
    a1 "Yeah, there were a few variations..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext27.jpg"
    with flashbb
    a1 "..........................."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext28.jpg"
    with flashbb
    a2 "Heh... This one is my favorite..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext29.jpg"
    with flashbb
    a1 "Jasmine's slave-girl outfits..."
    a1 "I drew the girl, Dahr drew the costumes..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext30.jpg"
    with flashbb
    a1 "And some more variations..."
    a2 "I like second form your left..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext31.jpg"
    with flashbb
    a1 "The threesome scene..."
    a1 "I thought it was very important to bring the conflict between Jasmine and Iris into the bedroom..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext32.jpg"
    with flashbb
    a1 "The sex scene...."
    a1 "I really wish you guys would let me draw those cool chibi animations instead of this..."
    a5 "Oh well..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext33.jpg"
    with flashbb
    a1 "The game logo..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext34.jpg"
    with flashbb
    a2 "Chibis!"
    a2 "I created this set before the complains about my chibi anmations and lack of full screen SG's started to pile up..."
    a1 "So the rest of the sex scenes are told through full-screen illustrations..."
    a2 "But visiting Dahlia in the brothel is still one of my favorite things to do in the game..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext35.jpg"
    with flashbb
    a1 "Weird-ass, anime-lola again..."
    a1 "I did put a lot of effort into this one..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext36.jpg"
    with flashbb
    a1 "{size=+5}A LOT{/size} of effort..."
    show ctc7 at right
    pause 
    hide ctc7
    show image "09_gallery/ext37.jpg"
    with flashbb
    a1 "And the logo I ended up not using..."
    show blkfade with d5
    a1 "This concludes volume three of the gallery."
    pause 1   
    stop music fadeout 1
    lola[35] "Thank you for supporting us and make this game happen!"
    jump gallery
    
    
    
    
    
    
    
###########How To Play#############
label howtoplay:
    play music galm fadeout 1
    a1 "Alright then."
    a1 "First, let me quickly go over some usefull keyboard commands."
    a1 "\"CTRL\" - hold it to make ren'py skip the text you've already read."
    a1 "\"H\" - hit that key if you want to hide the text box. (\"H\" stand for \"hide\" of course... clever.)"
    a1 "And don't forget about \"AUTO\" (hands-free) option. The button is at the top right corner of the screen..."
    a1 "And that's that. Now to the game mechanics..."
    a1 "I will try to make this short."
    a5 "And I'll also use some graphs provided by the almighty Dahr."
    a1 "Before we proceed, I ask everyone to take a minute and heil Dahr for helping me out."
    a1 "........"
    a1 "Ok, with this out of the way, let's start with the tutorial."
    show image "04_pt/slavem/tut01.png" with Dissolve(.4)
    a1 "In this game your main objective is to turn princess Jasmine from a disobedient, brat-like Princess into an obedient slave-girl that follows your every order."
    a5 "Your secondary objective is to unravel the mystery of Genie becoming human, losing his memory..."
    a1 "Jasmine has two major characteristics: \"Obedience\" and \"Moral Standards\"."
    a5 "Leveling up her obedience will make her more obedient and will unlock new actions."
    a1 "Leveling up (or rather lowering down) her moral standards will lower Jasmine's shame threshold. And will let her do more embarrassing things."
    a1 "To improve Jasmine's \"Obedience\" and \"Moral Standards\" characteristics you need to send her to the \"JSGA\" - \"Jafar's Slave-Girl Academy."
    show image "04_pt/slavem/tut02.png" with Dissolve(.4)
    hide image "04_pt/slavem/tut01.png" 
    a1 "Then there is \"energy\"..."
    a1 "Every morning the Princess will wake up full of energy, but depending on what you make her do during the day her energy will go down (naturally)."
    a1 "To let her rest simply don't assign her any tasks during the day..."
    a1 "She will also get tired if you make her work for too many days in a row..."
    a1 "The Next one is her reputation."
    a5 "You need to make sure that the people of Agrabah lose their faith in Princess Jasmine..."
    a1 "Some jobs may help with that."
    a1 "For example, making Jasmine work as a dancer will spread all sorts of rumors."
    a5 "But the best and quickest way to tarnish her reputation would be the \"Personal Requests\" accessible from your house during the daytime."
    a5 "To check Jasmine's reputation talk to the homeless old man in the Cheapside district of the city."
    a1 "And finally, the jobs..."
    show image "04_pt/slavem/tut03.png" with Dissolve(.4)
    hide image "04_pt/slavem/tut02.png" 
    a5 "You will need gold to finance the wedding parade."
    a1 "To acquire the necessary sum money you will have to send princess jasmine on all sorts of jobs around agrabah."
    a1 "Every job has its own requirements that need to be met and its own payoffs."
    show image "qchecklist/qbg.png" with d5
    hide image "04_pt/slavem/tut03.png" 
    a1 "And now to my favorite thing..."
    a2 "The quests..."
    a1 "The game has 13 quests. Only half of them are mandatory..."
    a1 "But completing all of them will help you experience the game-world more fully..."
    a1 "Some of them will unblock new action as well..."
    hide image "qchecklist/qbg.png" with Dissolve(.4)
    a1 "And this concludes the tutorial. I promised to make it short, didn't i?"
    a5 "The game is really simple, I would even say basic, so it shouldn't take you long to figure out what's what..."
    a1 "And there is no time limit, so you can't really lose in this game. But it may require some grinding."
    a2 "Have fun."
    stop music fadeout 1
    return


################About This Game###############################
label abouttrainer:
    a1 "Alright then, let me say a few words about this beast of a game..."
    show image "04_pt/slavem/tut04.png" with Dissolve(.4)
    a1 "It has an official name now: \"The Princess Trainer\"."
    a1 "This one is a product of love, no doubt about it."
    a1 "I always wanted to do something like this..."
    a1 "Does anyone here remember the \"Broken Heart Bordello\"?"
    a1 "But even years before the \"BHB\" happened, I already had that idea in my mind."
    a2 "I remember back when I was a kid I made my own monopoly-like table game where you had to buy and manage strip-clubs and brothels."
    a1 "Yeah... I've been showing a lot of promise since my very early years..."
    show image "04_pt/slavem/tut05.png" with Dissolve(.4)
    hide image "04_pt/slavem/tut04.png"
    a1 "Thankfully my family wasn't paying much attention to my activities, otherwise I might have been sent to an institution..."
    a2 "Heh... But, you know, who of us didn't draw boobs and dicks on pieces of paper when they were growing up?"
    a1 "I just enjoy taking stuff to another level I guess..."
    a1 "Anyway, before I digress too much, I had a blast working on the \"Princess Trainer\"."
    show image "04_pt/slavem/tut06.png" with Dissolve(.4)
    hide image "04_pt/slavem/tut05.png"
    a1 "I Never dreamed of such an opportunity..." 
    a1 "Many things came together to make this dream a reality for me."
    a1 "First of all the \"Ren'Py\" software of course... It's so perfect for my needs that I can't even believe it sometimes."
    a1 "Then there's this guy called \"Xaljio\", who I bothered a lot throughout the game development with all sorts of \"Ren'Py\" related questions."
    a1 "And he was always super nice and taught me all sorts of neat \"Ren'Py\" tricks."
    a2 "Thank you, Xalijo, dude. You rock!"
    show image "04_pt/slavem/tut07.png" with Dissolve(.4)
    hide image "04_pt/slavem/tut06.png"        
    a1 "And then there is my idol - dahr of course. Who not only provided me with some kick-ass illustrations for the game, but also fed me quite a few great ideas."
    a1 "And last, but not least is everyone who supported me with their $$$ of course."
    a1 "I would never be able to successfully ignore my family, friends and the entire outside world and fully consentrate on the game if not for you."         
    a1 "When I know that I have enough cash to pay the rent this month and buy groceries, I really don't give a damn about anything else anymore. All I want is to work for you guys."
    a2 "So thank you everyone who joined \"HU\" under my link and those of you who sent me all sorts of donations via PayPal."
    a2 "Thank you guys, really."
    show image "04_pt/slavem/tut08.png" with Dissolve(.4)
    hide image "04_pt/slavem/tut07.png"
    a1 "......"
    a1 "This game is my first attempt at something that epic."
    a1 "A test run, if you will."
    a1 "Keep in mind that I'm just one guy... And I do everything... "
    a1 "Writing, drawing, planning, endless lines of codes and testing, it's all on me and takes enormous amounts of time."
    a1 "So naturally I had to sacrifice a lot of ideas for time's sake..."
    show image "04_pt/slavem/tut09.png" with Dissolve(.4)
    hide image "04_pt/slavem/tut08.png"
    a1 "Like I said, many people showed their support, and have been pretty patient with me."
    a1 "But not everyone..."
    a1 "There are also people who keep on bugging me, complain and demand that I release the game \"Right now!\"."
    hide image "04_pt/slavem/tut09.png" with Dissolve(.4)
    a1 "But it's all behind us now. The game is finally finished..."
    a1 "Next step for me will be to finish working on the \"Magic Shop\"."
    a2 "And after that... the sky is the limit."
    a1 "Ok, that's enough talking I think."
    a1 "Enjoy the game now, you deserved it."
    stop music fadeout 1
    return


######################################################################
label cr:
    #play music "music/Real Talk by Brix.MP3" fadein 1 fadeout 1 
    play music "music/03_2_Voicemail Freestyle Mike Wiebe.mp3" fadein 3 fadeout 1  
    scene image "08_ending/e05.png" with Dissolve(2)
    show akaani with d5

    
    centered "{cps=20}{size=+5}{color=#ea91b0}-The Princess Trainer-{/color}{/size}\n\n
    {size=+5}{color=#e5e297}-Producer-{/color}{/size}\n{color=#cbcbcb}AKABUR{/color}\n\n
    {size=+5}{color=#e5e297}-Head programmer-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
    {size=+5}{color=#e5e297}-Writer-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
    {size=+5}{color=#e5e297}-Artwork-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
    {size=+5}{color=#e5e297}-Additional Artwork-{/color}{/size}\n     {color=#cbcbcb}DAHR{/color}\n\n
    {size=+5}{color=#e5e297}-Sound Effects-{/color}{/size}\n    {color=#cbcbcb}http://www.freesound.org/{/color}\n\n
    {size=+5}{color=#e5e297}-MUSIC-{/color}{/size}\n\n

    {color=#e5e297}(From \"NEWGROUNDS\")\n
    {color=#e5e297}\"Eastern Journey\" {/color}{color=#cbcbcb}by Pike270.{/color}\n
    {color=#e5e297}\"Grape Soda Is Fucking Raw\"{/color} {color=#cbcbcb}by jrayteam6.{/color}\n
    {color=#e5e297}\"The Eastern Wind\"{/color} {color=#cbcbcb}by roensb.{/color}\n
    {color=#e5e297}\"Silly Cat\" {/color}{color=#cbcbcb}by Maverlyn.{/color}\n
    {color=#e5e297}\"Kabul Flight\" {/color}{color=#cbcbcb}by Jumpstart.{/color}\n
    {color=#e5e297}\"Sleep Walking\" {/color}{color=#cbcbcb}by hektikmusic.{/color}{/cps}"
    nvl clear
    hide akaani
    show akaani2
#{color=#e5e297}\"Real Talk by Brix\" {color=#cbcbcb}By CARTEL.{/color}\n\n\n    
#{color=#e5e297}\"S.W.A.T. feat. Real\" {color=#cbcbcb} by Eins Zwei Polizei (Radio Edit).{/color}\n   
    centered "{cps=20}{size=+5}{color=#e5e297}-MUSIC-{/size}\n{color=#e5e297}(From other sources.)\n
    {color=#e5e297}\"Roll In the Leaves\" {color=#cbcbcb}Xena OST.{/color}\n
    {color=#e5e297}\"Going to Kill Me\" {color=#cbcbcb}Xena OST.{/color}\n
    {color=#e5e297}\"Jafar's Hour\" {color=#cbcbcb}Aladdin OST.{/color}\n
    {color=#e5e297}\"Marketplace\" {color=#cbcbcb}Aladdin OST.{/color}\n
    {color=#e5e297}\"Freedom\" {color=#cbcbcb}Outlaw Star OST.{/color}\n
    {color=#e5e297}{size=-2}\"Voicemail Freestyle Mike Wiebe\" {color=#cbcbcb}By Astronautalis.{/size}{/color}\n\n\n
              
              
              
              
    {size=+5}-Game Engine-{/size}\n{color=#cbcbcb}Ren'Py\nhttp://renpy.org/{/color}\n\n
    {size=+5}-Testers-{/size}\n{color=#cbcbcb}Silentchill\nBookfisher\nXaljio\nAKABUR{/color}\n\n{/cps}"
    nvl clear
    hide akaani2
    show akaani
    
    centered "{cps=20}{size=+5}{color=#e5e297}-CREATOR OF THIS GAME WOULD ALSO LIKE TO PERSONALLY THANK-{/color}{/size}\n\n{color=#cbcbcb}
    {size=+5}Dahr{/size}{/color}\n{color=#e5e297}for helping me out in all sorts of ways with\nthe \"Princess Trainer\"{/color}\n\n
    {color=#cbcbcb}{size=+5}Xaljio{/size}{/color}\n{color=#e5e297} for not only being my personal \"Ren'Py\" consultant but also an extremely thorough game-tester.\n {size=-5}(Who wouldn't let me rest until every single bug has been eradicated.){/size}{/color}\n\n
    {color=#cbcbcb}{size=+5}Lyk.D9 (a.k.a. Silentchill){/size}{/color}\n {color=#e5e297}for fixing my terrible grammar.{/color}\n\n
    {color=#cbcbcb}{size=+5}Bookfisher{/size}{/color}\n{color=#e5e297}For everything.\n\nAlso{/color} {color=#cbcbcb}Jashinslayer, Urban, Jason, Lucius, Dorago, Largo_Leet{/color}\n{color=#e5e297}And many others who supported this game with \ndonations but chose to stay anonymous.{/color}\n\n
    {color=#cbcbcb}A bunch of other people who helped me with development of this game in one way or another,\n but whom I forgot to mention.{/color}\n
    {color=#cbcbcb}And of course to everyone else who supports me.\n\n\n
    {size=+5}Thank you for playing.{/size}{/color}\n\n
    {color=#e5e297}AKABUR 2014{/color}{/cps}"
    stop music fadeout 1
    show blkfade
    with Dissolve(.5)
    jump lazy_or_not
    if not persistent.game_completed:
        $ renpy.play('sounds/win2.mp3')
        centered "Gallery unlocked in the \"extras\" menu."
label assmenu:
    return
    
label htp:
    scene title2
    with flashbb
    a1 "This is your basic visual novel kind of game, so I don't think any additional explanations are necessary."
    a1 "A hint though: there is a tiny  \"Skip\" button at the upper right corner of the screen."
    a1 "You can also access the skip mode by holding down the ctrl-button on your keyboard."
    a1 "Don't worry about missing out on things in the skip mode, because ren'py is smart and will only skip parts that you have already seen."
    a1 "Also, to access the option screen you can hit the esc-key on your keyboard or just right-click with your mouse anywhere on the game-screen."
    a1 "That's all I have to say. Go play the game now."
    return
    
label updatem:
    scene title2
    with flashbb
    a1 "Go {a=http://akabur.hentaiunited.com}here.{/a} to get latest version of the game."
    $ renpy.full_restart()

label whatsnew:
    scene title2
    with flashbb
    a1 "This is \"1.1\" version of the game."
    a1 "3 new combinations have been added.\nA new scroll and a potion selection screen have been added."
    a1 "The quick menu buttons were relocated to the upper right corner of the screen."
    a1 "A few new pics were added to the gallery."
    a1 "The Akabur-logo intro has been shortened, it only takes 3 seconds now."
    a1 "And many, many minor changes and improvements have been made, which you won't even notice."
    a1 "Enjoy the game now."
    return
    

    
## GAME OVER
label gameover:
    s "Insolent peasant! How dare you to speak to your princess in this manner!? I will have you beheaded for this!"
    m "Just admit it, you are nothing but a common slut after all!" 
    s "!!! YOU...{p}YOU!!!!{p}GUARDS! GUARDS!!!!"
    show blkfade
    with Dissolve(.5)
    show gover behind blkfade
    pause.2
    hide blkfade
    with Dissolve(.5)
    pause
    show blkfade
    with Dissolve(.9)
    
label finalgover:    
    
    
    
    
label gallery_locked:
    "Beat the game to unlock the gallery."
    return