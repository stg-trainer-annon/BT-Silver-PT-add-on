init python:
    # Character tables
    
    ros = [""]
    for i in range(1,6):
        ros.append("")
        ros[i] = Character("Rose the teacher", color="#402313", window_right_padding=240, show_side_image=Image("04_pt/rose/rose" + str(i) + ".png", xalign=0.985, yalign=0.98), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")
    
    aza = [""]
    for i in range(1,13):
        aza.append("")
        aza[i] = Character("Azalea the store owner", color="#402313", window_right_padding=240, show_side_image=Image("04_pt/azalea/school" + str(i) + ".png", xalign=0.985, yalign=0.98), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")

    lola = [""]
    for i in range(0,73):
        lola.append("")
        lola[i] = Character("Lola", color="#402313", window_right_padding=270, show_side_image=Image("04_pt/lola/school00_" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")
    
    ir = [""]
    for i in range(1,32):
        ir.append("")
        ir[i] = Character("Iris", color="#402313", window_right_padding=270, show_side_image=Image("04_pt/iris/ih" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")
    
    jas = [""]
    for i in range(1,68):
        jas.append("")
        jas[i] = Character("Jasmine", color="#402313", window_right_padding=270, show_side_image=Image("04_pt/jasmine/j" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")
    
    
    dah = [""]
    for i in range(1,14):
        dah.append("")
        dah[i] = Character('Dahlia',color="#402313",window_right_padding=270,show_side_image=Image("04_pt/dahlia/dh" + str(i) + ".png", xalign=1.0, yalign=0.0),show_two_window=True,show_who_xalign=0.5,ctc="ctc3",ctc_position="fixed")
    
    
    aka = ["",""]
    for i in range(1,8): #Jew
        aka.append("")
        #aka[i] = Character(None, window_left_padding=220, image="aka"+str(i), color="#402313", ctc="ctc3", ctc_position="fixed")
        #tb_c_bj[i] = Character("Evil Jasmine", color="#402313", window_right_padding=270, show_side_image=Image("03_hp/25_ue/goodevil/bh" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc4", ctc_position="fixed")

    
    jaf = [""]
    jaf_b = [""]
    jaf_c = [""]
    jaf_n = [""]
    for i in range(1,16): #Jaffar
        jaf.append("")
        jaf_b.append("")
        jaf_c.append("")
        jaf_n.append("")
        if i >= 8 and i <= 10:
            jaf[i] = Character(None, window_left_padding=330, image="jaf"+str(i), color="#402313", ctc="ctc3", ctc_position="fixed")
            jaf_b[i] = Character(None, window_left_padding=330, image="jaf"+str(i)+"b", color="#402313", ctc="ctc3", ctc_position="fixed")
            jaf_c[i] = Character(None, window_left_padding=330, image="jaf"+str(i)+"c", color="#402313", ctc="ctc3", ctc_position="fixed")
            jaf_n[i] = Character(None, window_left_padding=330, image="jaf"+str(i)+"n", color="#402313", ctc="ctc3", ctc_position="fixed")
        else:
            jaf[i] = Character(None, window_left_padding=260, image="jaf"+str(i), color="#402313", ctc="ctc3", ctc_position="fixed")
            jaf_b[i] = Character(None, window_left_padding=260, image="jaf"+str(i), color="#402313", ctc="ctc3", ctc_position="fixed")
            jaf_c[i] = Character(None, window_left_padding=260, image="jaf"+str(i), color="#402313", ctc="ctc3", ctc_position="fixed")
            jaf_n[i] = Character(None, window_left_padding=260, image="jaf"+str(i), color="#402313", ctc="ctc3", ctc_position="fixed")
    
    w_jas_a = [""]
    w_jas_b = [""]
    w_jas_c = [""]
    w_jas_n = [""]
    for i in range(1,22):
        w_jas_a.append("")
        w_jas_b.append("")
        w_jas_c.append("")
        w_jas_n.append("")
        if i < 15:
            w_jas_a[i] = Character(None, window_left_padding=260, image="jas"+str(i), color="#402313", ctc="ctc3", ctc_position="fixed")
            w_jas_b[i] = Character(None, window_left_padding=260, image="jas"+str(i)+"b", color="#402313", ctc="ctc3", ctc_position="fixed")
            w_jas_c[i] = Character(None, window_left_padding=260, image="jas"+str(i)+"c", color="#402313", ctc="ctc3", ctc_position="fixed")
            w_jas_n[i] = Character(None, window_left_padding=260, image="jas"+str(i)+"n", color="#402313", ctc="ctc3", ctc_position="fixed")
        else:
            w_jas_a[i] = Character(None, window_left_padding=330, image="jas"+str(i), color="#402313", ctc="ctc3", ctc_position="fixed")
            w_jas_b[i] = Character(None, window_left_padding=330, image="jas"+str(i)+"b", color="#402313", ctc="ctc3", ctc_position="fixed")
            w_jas_c[i] = Character(None, window_left_padding=330, image="jas"+str(i)+"c", color="#402313", ctc="ctc3", ctc_position="fixed")
            w_jas_n[i] = Character(None, window_left_padding=330, image="jas"+str(i)+"n", color="#402313", ctc="ctc3", ctc_position="fixed")
    
    iri = Character('Iris', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    la = Character('Lara Croft', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    j = Character('Jasmine', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr1 = Character('Somebody from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr2 = Character('Another voice from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr3 = Character('female voice', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr4 = Character('somebody named mustafa', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr5 = Character('the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr6 = Character('many voices at once', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ej = Character('Evil Jasmine', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    gj = Character('Good Jasmine', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    a = Character('Aladdin', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ali = Character('Prince Ali', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sul = Character('Sultan', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    g3 = Character('Genie', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ras = Character('Rasul', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    jaf1 = Character('Jafar', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ia = Character('Iago', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    raj = Character('Rajah', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    rajl = Character('Little Rajah', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    patron = Character('Tavern patron', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    patron2 = Character('Another patron', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    par = Character('A Parrot', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    urc = Character('Street Urchin', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    nob = Character('Nobleman', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    lol = Character('Lola', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sch9 = Character('Dahlia', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")

    
define sch3 = Character('Fat Lilly',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school3.png", xalign=0.985, yalign=0.98),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch300 = Character('Fat Lilly',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch4 = Character('Rasul captain of the guard',
    color="#402313",
    window_right_padding=300,
    show_side_image=Image("04_pt/slavem/school4.png", xalign=0.985, yalign=0.98),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch5 = Character('Balsam the merchant',
    color="#402313",
    window_right_padding=300,
    show_side_image=Image("04_pt/slavem/school5.png", xalign=1.0, yalign=0.98),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch600 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch6 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school6.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch6_2 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school9_2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch6_3 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school9_3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch6_4 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school9_4.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch62 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school9.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch6_5 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school9_5.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch6_6 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school9_6.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch7 = Character('Crocus the homeless',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school7.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch8 = Character('Crocus the homeless',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school8.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
    
define aka1 = Character('none',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/aka1.png", xalign=0.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

    
define sch1000 = Character('Lola',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

    
define iris = Character(None, window_left_padding=250, image="test/sch11_2.png", color="#402313", ctc="ctc3", ctc_position="fixed")

define sch1100 = Character('Iris',
    color="#402313",
    window_right_padding=90,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch11 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school11.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch11_2 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school11_2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch11_3 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school11_3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch11_3 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school11_3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch11_4 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school11_4.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch11_5 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("test/sch11_1.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch11_62 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school11_6.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch11_6 = Character(None,
    color="#402313",
    window_right_padding=70,
    window_left_padding=230,
    show_side_image=Image("test/sch11_2.png", xalign=0.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sch11_7 = Character(None,
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school11_5.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

    
#SPSG'S Iris Defines
define iri32 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/iris/q1/iris08_bust.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")
define iri33 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/iris/q1/iris08_bust_2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")
define iri34 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/iris/q1/iris08_bust_3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")
define iri35 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/iris/q1/iris08_bust_4.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")
define iri36 = Character('Iris',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/iris/q1/iris08_bust_5.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

#End SPSG's Defines


define sch12 = Character('Madder the City Guard',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school12.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch12_2 = Character('Madder the City Guard',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/school12_2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

    
define sch13 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/jasmine/school13.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch13_2 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/jasmine/school13_2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch14 = Character(None,
    color="#402313",
    window_right_padding=70,
    window_left_padding=250,
    show_side_image=Image("test/jas01.png", xalign=0.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch900 = Character('Dahlia the whore',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah = Character('Dahlia',
    color="#402313",
    window_right_padding=90,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

########################################################################

define ali01 = Character('Prince Ali',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/al01.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define ali02 = Character('Aladdin',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/al02.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define ali03 = Character('Prince Ali',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/al03.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define ali04 = Character('Aladdin',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/al04.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")


define sul03n = Character('Sultan',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/sultan03.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define sul04n = Character('Sultan',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/sultan04.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define ia01 = Character('Iago',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/iago01.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define ia02 = Character('Iago',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/iago02.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define ia03 = Character('Iago',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/iago03.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")


define raj01 = Character('Little Rajah',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/rajah01.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")


define raj02 = Character('Rajah',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("04_pt/slavem/rajah02.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")
    