
image bgpalace = "palace.jpg"
image bgroom = "room.jpg"

image su01 = "04_pt/slavem/sultan01.png"
image su02 = "04_pt/slavem/sultan02.png"

image ext01 = "04_pt/extras/ext01.jpg"
image ext02 = "04_pt/extras/ext02.jpg"
image ext03 = "04_pt/extras/ext03.jpg"
image ext04 = "04_pt/extras/ext04.jpg"
image ext05 = "04_pt/extras/ext05.jpg"
image ext06 = "04_pt/extras/ext06.jpg"
image ext07 = "04_pt/extras/ext07.jpg"
image ext08 = "04_pt/extras/ext08.jpg"
image ext09 = "04_pt/extras/ext09.jpg"
image ext10 = "04_pt/extras/ext10.jpg"
image ext11 = "04_pt/extras/ext11.jpg"

image slbg = "04_pt/slavem/mainbg00.jpg"


#####CHARACTER IMAGES###########
init python:
    # lola 1 to 31
    for i in range(1,31):
        renpy.image("lola " + str(i), "04_pt/lola_dates/l" + str(i) + ".png")
    for i in range(1,31):# flip
        renpy.image("lola_f " + str(i), im.Flip("04_pt/lola_dates/l" + str(i) + ".png", horizontal=True))
        
    # lily 1 to 5
    for i in range(1,5):
        renpy.image("lily " + str(i), "04_pt/quest05/lily" + str(i) + ".png")
    for i in range(1,5):# flip
        renpy.image("lily_f " + str(i), im.Flip("04_pt/quest05/lily" + str(i) + ".png", horizontal=True))
    
    # iris 1 to 106
    for i in range(1,106):
        renpy.image("iris " + str(i), "04_pt/iris/q5/iris" + str(i) + ".png")
    for i in range(1,106):# flip
        renpy.image(("iris " + str(i) + "f"), im.Flip("04_pt/iris/q5/iris" + str(i) + ".png", horizontal=True))
    
    # jas 1 to 31
    for i in range(1,32):
        renpy.image("jas " + str(i), "04_pt/jasmine/q1/jas" + str(i) + ".png")
    for i in range(1,31):# flip
        renpy.image("jas_f " + str(i), im.Flip("04_pt/jasmine/q1/jas" + str(i) + ".png", horizontal=True))
    
    # dahlia 1 to 5
    for i in range(1,6):
        renpy.image("dahlia " + str(i), "04_pt/dahlia/d" + str(i) + ".png")
    
    # maslab 1 to 8
    for i in range(1,8):
        renpy.image("maslab " + str(i), "04_pt/quest01/maslab" + str(i) + ".png")
    
    
image side jaf1 = "04_pt/jaffar/jaf1.png"
image side jaf2 = "04_pt/jaffar/jaf2.png"
image side jaf3 = "04_pt/jaffar/jaf3.png"
image side jaf4 = "04_pt/jaffar/jaf4.png"
image side jaf5 = "04_pt/jaffar/jaf5.png"
image side jaf6 = "04_pt/jaffar/jaf6.png"
image side jaf7 = "04_pt/jaffar/jaf7.png"
image side jaf8 = "04_pt/jaffar/jaf8.png"
image side jaf9 = "04_pt/jaffar/jaf9.png"
image side jaf10 = "04_pt/jaffar/jaf10.png"
image side jaf11 = "04_pt/jaffar/jaf11.png"
image side jaf12 = "04_pt/jaffar/jaf12.png"
image side jaf13 = "04_pt/jaffar/jaf13.png"
image side jaf14 = "04_pt/jaffar/jaf14.png"
image side jaf15 = "04_pt/jaffar/jaf15.png"

image side jaf8b = "04_pt/jaffar/jaf8b.png"
image side jaf9b = "04_pt/jaffar/jaf9b.png"
image side jaf10b = "04_pt/jaffar/jaf10b.png"
image side jaf8c = "04_pt/jaffar/jaf8c.png"
image side jaf9c = "04_pt/jaffar/jaf9c.png"
image side jaf10c = "04_pt/jaffar/jaf10c.png"

image side jaf8n = "04_pt/jaffar/jaf8n.png"
image side jaf9n = "04_pt/jaffar/jaf9n.png"
image side jaf10n = "04_pt/jaffar/jaf10n.png"

image side jas1 = "04_pt/jasmine/jas1.png"
image side jas2 = "04_pt/jasmine/jas2.png"
image side jas3 = "04_pt/jasmine/jas3.png"
image side jas4 = "04_pt/jasmine/jas4.png"
image side jas5 = "04_pt/jasmine/jas5.png"
image side jas6 = "04_pt/jasmine/jas6.png"
image side jas7 = "04_pt/jasmine/jas7.png"
image side jas8 = "04_pt/jasmine/jas8.png"
image side jas9 = "04_pt/jasmine/jas9.png"
image side jas10 = "04_pt/jasmine/jas10.png"
image side jas11 = "04_pt/jasmine/jas11.png"
image side jas12 = "04_pt/jasmine/jas12.png"
image side jas13 = "04_pt/jasmine/jas13.png"
image side jas14 = "04_pt/jasmine/jas14.png"
image side jas15 = "04_pt/jasmine/jas15.png"
image side jas16 = "04_pt/jasmine/jas16.png"
image side jas17 = "04_pt/jasmine/jas17.png"
image side jas18 = "04_pt/jasmine/jas18.png"
image side jas19 = "04_pt/jasmine/jas19.png"
image side jas20 = "04_pt/jasmine/jas20.png"
image side jas21 = "04_pt/jasmine/jas21.png"
image side jas1b = "04_pt/jasmine/jas1b.png"
image side jas2b = "04_pt/jasmine/jas2b.png"
image side jas3b = "04_pt/jasmine/jas3b.png"
image side jas4b = "04_pt/jasmine/jas4b.png"
image side jas5b = "04_pt/jasmine/jas5b.png"
image side jas6b = "04_pt/jasmine/jas6b.png"
image side jas7b = "04_pt/jasmine/jas7b.png"
image side jas8b = "04_pt/jasmine/jas8b.png"
image side jas9b = "04_pt/jasmine/jas9b.png"
image side jas10b = "04_pt/jasmine/jas10b.png"
image side jas11b = "04_pt/jasmine/jas11b.png"
image side jas12b = "04_pt/jasmine/jas12b.png"
image side jas13b = "04_pt/jasmine/jas13b.png"
image side jas14b = "04_pt/jasmine/jas14b.png"
image side jas15b = "04_pt/jasmine/jas15b.png"
image side jas16b = "04_pt/jasmine/jas16b.png"
image side jas17b = "04_pt/jasmine/jas17b.png"
image side jas18b = "04_pt/jasmine/jas18b.png"
image side jas19b = "04_pt/jasmine/jas19b.png"
image side jas20b = "04_pt/jasmine/jas20b.png"
image side jas21b = "04_pt/jasmine/jas21b.png"
image side jas1c = "04_pt/jasmine/jas1c.png"
image side jas2c = "04_pt/jasmine/jas2c.png"
image side jas3c = "04_pt/jasmine/jas3c.png"
image side jas4c = "04_pt/jasmine/jas4c.png"
image side jas5c = "04_pt/jasmine/jas5c.png"
image side jas6c = "04_pt/jasmine/jas6c.png"
image side jas7c = "04_pt/jasmine/jas7c.png"
image side jas8c = "04_pt/jasmine/jas8c.png"
image side jas9c = "04_pt/jasmine/jas9c.png"
image side jas10c = "04_pt/jasmine/jas10c.png"
image side jas11c = "04_pt/jasmine/jas11c.png"
image side jas12c = "04_pt/jasmine/jas12c.png"
image side jas13c = "04_pt/jasmine/jas13c.png"
image side jas14c = "04_pt/jasmine/jas14c.png"
image side jas15c = "04_pt/jasmine/jas15c.png"
image side jas16c = "04_pt/jasmine/jas16c.png"
image side jas17c = "04_pt/jasmine/jas17c.png"
image side jas18c = "04_pt/jasmine/jas18c.png"
image side jas19c = "04_pt/jasmine/jas19c.png"
image side jas20c = "04_pt/jasmine/jas20c.png"
image side jas21c = "04_pt/jasmine/jas21c.png"

image side jas1n = "04_pt/jasmine/jas1n.png"
image side jas2n = "04_pt/jasmine/jas2n.png"
image side jas3n = "04_pt/jasmine/jas3n.png"
image side jas4n = "04_pt/jasmine/jas4n.png"
image side jas5n = "04_pt/jasmine/jas5n.png"
image side jas6n = "04_pt/jasmine/jas6n.png"
image side jas7n = "04_pt/jasmine/jas7n.png"
image side jas8n = "04_pt/jasmine/jas8n.png"
image side jas9n = "04_pt/jasmine/jas9n.png"
image side jas10n = "04_pt/jasmine/jas10n.png"
image side jas11n = "04_pt/jasmine/jas11n.png"
image side jas12n = "04_pt/jasmine/jas12n.png"
image side jas13n = "04_pt/jasmine/jas13n.png"
image side jas14n = "04_pt/jasmine/jas14n.png"
image side jas15n = "04_pt/jasmine/jas15n.png"
image side jas16n = "04_pt/jasmine/jas16n.png"
image side jas17n = "04_pt/jasmine/jas17n.png"
image side jas18n = "04_pt/jasmine/jas18n.png"
image side jas19n = "04_pt/jasmine/jas19n.png"
image side jas20n = "04_pt/jasmine/jas20n.png"
image side jas21n = "04_pt/jasmine/jas21n.png"
## CHARACTERS