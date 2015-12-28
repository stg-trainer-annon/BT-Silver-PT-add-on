
label food4lily:
    sch6 "Something delicious, huh?"
    sch6 "Wouldn't you rather have something disgusting? I have plenty of that left..."
    sch6 "Well, alright, alright, I will cook something nice for you..."
    sch6 "It shall be ready for you to pick up later tonight..."
    $ quest7maslab = False
    $ quest7maslab2 = True
    jump tavern2
label food4lily2:
    sch6 "I will get this cooked for ya. Come back later tonight."
    $ quest7maslab3 = True
    $ quest7notcooking = False
    jump tavern2


#######################
label jasminwaitreswork:
    if tired >= 2:
        "Jasmine is too tired for that."
        jump tavern2
    else:
        if taverngirl:                
            if obedience >= 3:
                ">Jasmine agrees to serve drinks in the local tavern..." 
                hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                show tavern with Dissolve(.3)  
                hide rest03
                $ jtavern = True
                $ jidle = False                    
                jump mainmenu                         
            else:
                show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
                j "Forget it. I'm not doing that."
                hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
                ">Jasmine refuses to serve drinks in the tavern."                    
                jump tavern2 
        else:
            ">You need to buy a \"Tavern Wench\" outfit first."
            jump tavern2
label jasminedanceork:
    if obedience >= 6:
        if courage >= 5:
            ">Jasmine works in the tavern dancing on the table and entertaining the patrons..."                                
            hide image "04_pt/slavem/bld.png" with Dissolve(.3)
            show dance with Dissolve(.3) 
            hide rest03
            $ jdance = True
            $ jidle = False                    
            jump mainmenu     
        else:
            ">Jasmine wants to obey your command, but she lacks the courage to dance on a table in the local tavern."
            jump tavern2
    else:
        show image "04_pt/jasmine/outfit/jas04.png" at right with Dissolve(.3)
        j "Forget it. I'm not doing that."
        hide image "04_pt/jasmine/outfit/jas04.png" with Dissolve(.3)
        ">Jasmine refuses to dance in the tavern."
        jump tavern2
  
#########################
