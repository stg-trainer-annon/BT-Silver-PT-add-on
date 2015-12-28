screen jasmine_sprite_room:
    if normalw2:
        add "04_pt/jasmine/outfit/jas01.png" at right
    elif peasantw2:
        add "04_pt/jasmine/outfit/jas14.png" at right
    elif tavernw2:
        add "04_pt/jasmine/outfit/jas08.png" at right
    elif dancew2:
        add "04_pt/jasmine/outfit/jas09.png" at right
    elif whorew2:
        add "04_pt/jasmine/outfit/jas05.png" at right
    elif slavew2:
        add "04_pt/jasmine/outfit/jas12.png" at right
    elif naked2:
        add "04_pt/jasmine/outfit/jas17.png" at right
    elif naked_lolita:
        add "04_pt/jasmine/outfit/jas18.png" at right

label set_jas_clothes(str):
    $ normalw2 = False
    $ peasantw2 = False
    $ tavernw2 = False
    $ dancew2 = False
    $ whorew2 = False
    $ slavew2 = False
    $ naked2 = False
    $ naked_lolita = False
    
    if str == "normal":
        $ normalw2 = True
    elif str == "peasant":
        $ peasantw2 = True
    elif str == "tavern":
        $ tavernw2 = True
    elif str == "dance":
        $ dancew2 = True
    elif str == "whore":
        $ whorew2 = True
    elif str == "slave":
        $ slavew2 = True
    elif str == "naked":
        $ naked2 = True
    elif str == "naked_lolita":
        $ naked_lolita = True
return

label jas_change_clothes(str):
    hide screen jasmine_sprite_room
    with d3
    
    "Princess Jasmine quickly changes."
    
    $ normalw2 = False
    $ peasantw2 = False
    $ tavernw2 = False
    $ dancew2 = False
    $ whorew2 = False
    $ slavew2 = False
    $ naked2 = False
    $ naked_lolita = False
    
    if str == "normal":
        $ normalw2 = True
    elif str == "peasant":
        $ peasantw2 = True
    elif str == "tavern":
        $ tavernw2 = True
    elif str == "dance":
        $ dancew2 = True
    elif str == "whore":
        $ whorew2 = True
    elif str == "slave":
        $ slavew2 = True
    elif str == "naked":
        $ naked2 = True
    elif str == "naked_lolita":
        $ naked_lolita = True
    
    show screen jasmine_sprite_room
    with d3
return