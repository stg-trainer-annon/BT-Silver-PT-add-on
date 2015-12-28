label hulk:
    scene bg meadow
    show sylvie smile
$ select = renpy.imagemap("screens/s2pot03.png", "screens/s2pot03b.png", [                                            
                                            (492, 400, 637, 600, "no"),
                                            (647, 400, 799, 600, "yes"),
                                            (1, 1, 800, 80, "dahr"),
                                            ])     


if select == "dahr":
    jump dahr
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
    show hulk1
    pause.05
    scene white
    pause.05
    scene bg meadow
    show hulk1
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
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    
play music "music/Marketplace.mp3" fadein 2 fadeout 2
j "!!!!!!!!!!!!!!!!?"
j "............"
j "What...."
j "What have you done?!"
show image "01hulk/hulk05.png" with Dissolve(.3)
hide hulk1
with vpunch
j "{size=+5}What have you done to me, old man!?{/size}"
g4 "Y-your highness, my apologies. This is not the spell we are looking for..."
with vpunch
j "{size=+7}You think?!{/size}"
g4 "Yes, this is obviously a wrong spell, but we are definitely getting closer to the right combination, because..."
g4 "Well, because, as you can see, your highness, you did become bigger in size... and... your...em..."
j "{size=+5}What are you going on about, old fool!?{/size}"
j "{size=+5}Undo this spell at once!!!{/size}"
g4 "But, your majesty, can't you see? You breasts did become bigger!"
g4 "I think we need to examine--"
with hpunch
with vpunch
j "I said undo this vile spell {size=+7}at once!!!{/size}" 
j "Or, I swear, I will not bother calling for guards, I'm gonna behead you with my bare hands!"
g4 "Please calm down, your Highness,  I shall undo the spell immediately."
menu:
    m "I think in this state she could actually hurt me. \nI need to undo the spell."
    "Undo the spell":
        call masterstart


    
    
    
########################################


label dahr:
    a1 "The following combination was generously donated by Dahr. You can get in touch with him through his website. {a=http://dahr.ru/}Just click here.{/a}"
    jump hulk
    