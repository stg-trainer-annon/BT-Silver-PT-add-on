label foursome3:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with d3
    pause.7
    show dahlia 2 at right behind blkfade
    hide blkfade with d3
    sch900 "Hello, darling..."
    show iris_f 86 at left with d5
    sch1100 "Oh, it's you... What are you doing here?"
    hide dahlia with d3
    show dahlia 4 at right with d3
    sch900 "I think it's pretty obvious dear..."
    sch900 "The man is looking for some company..."
    show jas 22 at Position(xpos=200, ypos=0, xanchor=0, yanchor=0) with Dissolve(.3)
    j "Old man? I mean, master? I mean... "
    j "What are you doing here?"
    hide dahlia with d3
    show dahlia 5 at right with d3
    sch900 "Well now, dear, is this really the way to greet a client?"
    hide jas with d3
    show jas 22 at Position(xpos=200, ypos=0, xanchor=0, yanchor=0) with d3
    j "A client?"
    hide jas with d3
    show jas 23 at Position(xpos=200, ypos=0, xanchor=0, yanchor=0) with d3
    j "Oh, right..."
    j "Welcome to the \"Red Phoenix\".... s-sweetheart..."
    hide dahlia with d3
    show dahlia 1 at right with d3
    sch900 "Yes, much better..."
    hide dahlia with d3
    show dahlia 4 at right with d3
    sch900 "If you do in fact want to get close and personal with all three of us, you better be ready to pay a good coin..."
    sch900 "This kind of service is premium and it doesn't come cheap..."
    menu: 
        "You currently have [gold] gold. \nWould you like to give 400 gold to Dahlia?"
        "\"Yes.\"":
            if gold >= 400:
                $ gold -=400
                ">You give 400 gold coins to Dahlia."
                hide dahlia with d3
                show dahlia 4 at right with d3
                sch900 "Follow me then. You too girls..."
                hide dahlia
                hide iris 
                with d3
                show iris_f 83 at left with d3
                sch1100 "Alright!"
                hide iris 
                hide jas 
                with d3
                show jas 21 at Position(xpos=200, ypos=0, xanchor=0, yanchor=0) with d3
                j "................................."
                hide jas with d3
                pass
            else:
                ">You don't have 400 gold."
                play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                jump nogold44some
        "\"Not today.\"":
            label nogold44some:
            hide dahlia with d3
            show dahlia 2 at right with d3
            dah "Well, we don't work for free honey. Come back when you change your mind."
            hide iris with d3
            show iris_f 89 at left with d3
            sch1100 "Tsk................."
            hide jas with d3
            show jas 24 at Position(xpos=200, ypos=0, xanchor=0, yanchor=0) with d3
            j "......................."
            play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
            show blkfade with d3
            pause.7
            hide dahlia
            hide jas
            hide iris
            hide blkfade with d3
            jump brothelmain

    
    
    
    
    
    
    
    show blkfade with d3
    show asssome behind blkfade
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    
    ">You follow the girls upstairs."
    ">The room Dahlia brought you to is rather spacious, with a huge bed taking up the greater part of it..."
    ">Jasmine and Iris sit down on opposite sides of the bed and give each other a glare..."
    ">Dahlia appears to be very calm and professional, like a seasoned whore such as she is expected to behave..."

    dah[3] "Well, alright girls, to make this work you will need to follow my lead..."
    ir[2] "Of course, Dahie..."
    jas[43] ".............................."
    dah[3] "So, girls, there is just one of him, and three of us..."
    dah[2] "Again, keep in mind, that this is your job. It's not about having fun, it's about pleasuring the client."
    menu:
        "\"Exactly!\"":
            dah[1] "Right..."
            dah[2] "Don't worry, dear, they know their stuff, this is just a recap..."
        "\"I would disagree.\"":
            dah[3] "Oh, really?"
            dah[2] "Well, girls, you are in luck. Our customer wants you to have fun as well..."
            ir[2] "The other day you said that although some of them might say that, in truth it always must still be about pleasuring the customer first."
            dah[2] "Exactly. Good girl, Iris. You learn fast."
            jas[47] "Tsk....."

        
       
    
    
    
    
    
    dah[2] "Now, just follow my example, girls..."
    ">Suddenly Dahlia pulls her pants down and lifts up her skirts..."
    ">Then she climbs on the bed and goes on all fours..."
    dah[2] "What are you waiting for, girls?"
    dah[3] "Come on, don't be shy... We need to give our man here easy access..."
    ir[1] "A-alright..."
    ">It takes Iris a second to compose herself..."
    ">You see how she is doing her best to try and look professional and all business-like mimicing Dahlia." 
    ">Iris also pulls her pants down and climbs on the bed from the opposite side to Dahlia..."
    jas[47] ".................................."
    ">Princess Jasmine gives you a look that is quite difficult to decipher..."
    ">Then pulls down her pants as well and squeezes herself in-between the girls..."
    play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    $ girlsfight = True

        

    hide blkfade with d3
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch900 "Do you like what you see, dear?"
    sch900 "For the next few hours we are all yours..."
    j "Hmph....."
    label choiceschoices:
    sch900 "So, who would you like to start with?"
    $ promised_to_cum_on_face = False #Genie promises Iris to cum on Jasmine's face.
#######################

menu:
    "-Start with Dahlia-":
        jump round01_dahlia
    "-Start with Jasmine-":
        jump round01_jasmine
    "-Start with Iris-":
        jump round01_iris
    
label label_round02:
    menu:
        "-Proceed with Dahlia-":
            jump round02_dahlia
        "-Proceed with Jasmine-":
            jump round02_jasmine
        "-Proceed with Iris-":
            jump round02_iris
            
label label_round03:
    menu: 
        "-Finish with Dahlia-":
            jump round03_dahlia
        "-Finish with Jasmine-":
            jump round03_jasmine
        "-Finish with Iris-":
            jump round03_iris

##################################

















#########################################
label round01_dahlia:
    sch900 "An obvious choice I suppose..."
    sch900 "Now you girls watch me work and make sure you learn..."
    sch1100 "Alright!"
    j "Hmph!"
    show blkfade with Dissolve(.7)
    pause.7
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show image "01_foursome/4some_08.png" behind blkfade
    ">Your cock enters Dahlia with an audible \"squeesh\". Her wet pussy simply swallows your dick whole..." 
    sch900 "Yes...{image=textheart.png}"
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide blkfade with Dissolve(.7)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch900 "Yes....{image=textheart.png} Oh, yes...{image=textheart.png} Please, keep going...{image=textheart.png}"
    show image "01_foursome/4some_09.png" with d3
    sch900 "By the great desert sands! Your cock is so big!"
    sch900 "You gonna tear me apart! The pleasure is unbearable!!!"
    ">Dahlia seems to enjoy being fucked by you, quite a lot."
    show image "01_foursome/4some_10.png" with d3
    sch900 "You see what I did there, girls?"
    ">Or is she? Suddenly her tone is all matter-of-fact like again..."
    sch900 "In one simple phrase and in a very subtle way..."
    sch900 "I both let the client know that I'm having a great time and complemented the size of his manhood."
    g4 "(\"Subtle\" my ass! What's going on here?)"
    sch1100 "Amazing! You're so cool, Dahlia!"
    j "Hm....... Interesting..."
    show image "01_foursome/4some_11.png" with d3
    sch900 "Why did you stop, dear? Keep going! You are the best!"
    hide image "01_foursome/4some_09.png"
    show image "01_foursome/4some_09.png" with d5
    sch900 "Yes!{image=textheart.png} Yes!{image=textheart.png} Pound me like a whore I am!"
    sch900 "Yes!{image=textheart.png} Like that!{image=textheart.png} Give me more!{image=textheart.png}"
    m "Er... I'm not moving..."
    hide image "01_foursome/4some_08.png"
    show image "01_foursome/4some_08.png" with d5
    sch900 "Oh, sorry..."
    sch900 "It seems having your huge fat cook inside of me made me lose my mind..."
    m "Right..."
    sch900 "Please, start moving, start fucking me! I'm so horny!"
    m "......................"
    jump label_round02
label round02_dahlia:
    show blkfade with d3
    hide image "01_foursome/4some_08.png"
    show image "01_foursome/4some_08.png" behind blkfade
    sch900 "ah...{image=textheart.png}"
    sch900 "yes...{image=textheart.png}"
    sch900 "Yes...{image=textheart.png} Yes...{image=textheart.png} Thank you..."
    sch900 "Oh wow, girls, his dick is amazing!"
    hide blkfade with d5
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch900 "Yes...{image=textheart.png} Yes! Keep pounding my ass like that! Oh, this is too good!"
    sch900 "ah...{image=textheart.png} I had sex with so many men, but..."
    sch900 "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
    sch900 "But you are something else! Ah!{image=textheart.png} Yes!"
    g9 "(Alright! Time to show you my moves.)"
    ">You squeeze Dahlia's butt even harder and pick up the pace...."
    sch900 "Oh my god! What are you doing?!"
    sch900 "Not so hard! Oh, this is so amazing! Ah!{image=textheart.png} Ah!{image=textheart.png}"
    g4 "Yes, you whore! Just like that! And some more!"
    sch900 "Ah!{image=textheart.png} Oh my god! Oh my god! If you keep it up like that...."
    sch900 "I think I'm gonna...{image=textheart.png} Ah...{image=textheart.png} ah...{image=textheart.png}"
    g4 "Yes, whore?"
    sch900 "I'm gonna cum!!!!!!!!!"
    g4 "Yes! You cum away, you slut!"
    with hpunch
    hide image "01_foursome/4some_09.png"
    show image "01_foursome/4some_09.png" with d3
    sch900 "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    sch900 "I'm cumming!{image=textheart.png} I'm cumming!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    g4 "Yes, yes! Cum you whore! Cum!!!"
    sch900 "Ahhhh!{image=textheart.png}{image=textheart.png}{image=textheart.png} This is too much!!!"
    g11 "You silly slut!"
    m "(Well, this was easy... I guess she {size=+5}is{/size} a professional.)"
    sch900 "I just came, and you keep fucking me! This is just too much!"
    hide image "01_foursome/4some_10.png"
    show image "01_foursome/4some_10.png" with d3
    sch900 "Alright, girls, did you see what I did there?!"
    with hpunch
    g4 "(What the hell?!)"
    sch900 "Not only I \"came\" before the customer did..."
    sch900 "But I also let him think that he is special, that nobody makes me cum the way he does..."
    sch1100 "Oh, I see..."
    j "Very interesting..."
    with hpunch 
    g4 "{size=+7}I'm right here!!!{/size}"
    hide image "01_foursome/4some_11.png"
    show image "01_foursome/4some_11.png" with d3
    sch900 "Well, of course, you are dear. Where else would you be? Keep going please, you are the best!"
    g4 "*Growl*"
    sch1100 "I have a question..."
    hide image "01_foursome/4some_10.png"
    show image "01_foursome/4some_10.png" with d3
    sch900 "Go ahead."
    sch1100 "How do you make him believe that you did actually cum?"
    sch900 "Oh, you just say that you did..."
    sch1100 "And that's all?"
    sch900 "Yes, men are not very bright, you know..."
    sch900 "Not you darling, obviously, you are an exception."
    m "Yeah, whatever..."
    sch1100 "So I don't have to cum every time I have sex?"
    sch900 "Of course not."
    sch900 "It is really important to stroke a man's ego, you see..."
    sch900 "But that's an easy job, really..."
    sch900 "All you have to do is say that he is the best..."
    sch900 "And make sure to fake an orgasm every time you have sex with him, and everyone will be happy..."
    sch1100 "I see..."
    j "Wow, I had no idea..."
    g4 "(Unbelievable... What is this \"Whoring 101\"? I don't remember signing up for this class!)"
    jump label_round03
label round03_dahlia: 
    show blkfade with d5
    pause.5
    dah[1] "Another thing to remember girls is always to--"
    with hpunch
    show image "01_foursome/4some_12b.png" with flashbulb
    hide blkfade 
    sch900 "!!!!!!!!!!!!!!?"
    sch900 "What are you doing?! Not so hard!"
    g4 "Shut up, whore!"
    sch900 "Oh...{image=textheart.png} m-my g-god, such r-rough power..."
    with hpunch
    sch900 "What's gotten into you?!"
    g4 "Are you ready to cum yet?"
    sch900 "What? What are...{w} you...{w} talking...{w} about...?"
    g11 "*Growl-growl*"
    ">You focus all your energy and strength on giving Dahlia a fuck she would not be forgetting anytime soon."
    sch900 "No, no, stop it... No one had taken me like this in years!"
    sch900 "I can't think straight! What are you doing to me?!"
    g11 "Shut the fuck up! Shut the fuck up! *growl*"
    sch1100 "Oh, wow, old man, you could be really scary..."
    show image "01_foursome/4some_13b.png" with flashbulb
    sch900 "I can't...{image=textheart.png} anymore...{image=textheart.png} I...{image=textheart.png}"
    j "Is this another one of your tricks, Dahlia?"
    g11 "Is it?! Answer the question, whore!"
    with hpunch
    sch900 "I...{image=textheart.png} what's going on...{image=textheart.png} I.. ah...{image=textheart.png} what?"
    sch900 "I can't...{image=textheart.png} any more...{image=textheart.png} I...{image=textheart.png}"
    sch900 "....................."
    show image "01_foursome/4some_14b.png" with flashbulb
    with hpunch
    sch900 "{size=+9}I'm cumming!!!?{/size}"
    g11 "{size=+5}You sound surprised, you whore!{/size}"
    g11 "{size=+9}Take it all, you slut!!!{/size}"
    show image "01_foursome/4some_15.png" with flashbulb
    with hpunch
    sch900 "{size=+9} I'm cumming!!! I...{image=textheart.png} Ah....{image=textheart.png} Yaaaaah!{image=textheart.png}{/size}"
    g11 "*Growl*"
    g11 "Fucking whore! How about it? Am I man enough for you now?"
    sch900 "You...{image=textheart.png} don't...{image=textheart.png} ah...{image=textheart.png} understand...{image=textheart.png}"
    sch900 "I haven't been able to come like this since my teenage years..."
    sch900 "Here comes another wave...{image=textheart.png} ah, i'm cumming again.{image=textheart.png}"
    g11 "You cum, whore! You cum! No more of your stupid mind games!" 
    show blkfade with d5
    show image "01_foursome/4some_16.png" behind blkfade
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    m "Ah...{image=textheart.png} That was good..."
    dah[6] "................"
    if promised_to_cum_on_face:
        ir[9] "I was hoping you would cum on Jasmine's face to teach her a lesson..."
        ir[10] "But I'm glad you made Dahie happy instead..."
    jas[56] "Dahlia?"
    hide blkfade with Dissolve(1)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    
    sch1100 "Dahie? Are you alright?"
    sch900 "I'm fine... It's just because of my line of work..."
    sch900 "I forgot how good this could feel... *sob*"
    sch900 "Sorry, I want to be alone now...*sob*"
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show blkfade with Dissolve(.7)
    ">You leave the brothel."
    hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
    if brothelnight:
        ">You return home and go to sleep."
        show image "interface/blackfade.png" with Dissolve(.3)
        pause 1
        jump dayone
    else:            
        ">It's getting late. You decide to head home."
        jump dayends
#######
label round01_jasmine:
    show blkfade with Dissolve(.7)
    pause.7
    hide image "01_foursome/4some_19.png"
    show image "01_foursome/4some_19.png" behind blkfade
    ir[8] "Her? But why?"
    jas[46] "Shut it, you wench."
    dah[1] "Jasmine is right, Iris."
    dah[1] "The customer made his choice. Be a little bit more professional about it, alright?"
    ir[9] "Alright....."
    hide blkfade with Dissolve(.7)
    j "ah....{image=textheart.png}"
    j "Ah...{image=textheart.png} ah...{image=textheart.png}"
    j "Ah...{image=textheart.png} Ah...{image=textheart.png} Yes...{image=textheart.png}"
    sch900 "Now, Jasmine, don't forget to thank him for choosing you?"
    hide image "01_foursome/4some_20.png"
    show image "01_foursome/4some_20.png" with d3
    j "Ah...{image=textheart.png} Ah...{image=textheart.png} what? Do I really have to?"
    sch900 "Of course. It's the basic etiquette."
    j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
    j "alright...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
    j "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
    sch900 "Jasmine?"
    hide image "01_foursome/4some_19.png"
    show image "01_foursome/4some_19.png" with d3
    j "Fine, fine. Thank you for choosing me old man! Ah...{image=textheart.png} ah...{image=textheart.png}"
    sch900 "Much better..."
    hide image "01_foursome/4some_20.png"
    show image "01_foursome/4some_20.png" with d3
    j "ah...{image=textheart.png} it feels so good... ah...{image=textheart.png} yes..."
    sch900 "Very nice. Now complement the size of his manhood."
    j "Ah...{image=textheart.png} ah...{image=textheart.png}"
    j "Ah, do I really have to? ah...{image=textheart.png} ah...{image=textheart.png}"
    hide image "01_foursome/4some_21.png"
    show image "01_foursome/4some_21.png" with d3
    sch1100 "Yes, you spoiled bitch! You are getting paid for this! Do your job!"
    hide image "01_foursome/4some_19.png"
    show image "01_foursome/4some_19.png" with d3
    j "Shut up, Iris, ah...{image=textheart.png} ah...{image=textheart.png} you are just jealous because he chose me..."
    sch1100 "Am not!"
    sch900 "Girls, girls, what did I tell you? We never quarrel in front of a client."
    sch1100 "Sorry, Dahlia..."
    j "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} Yes... yes... oh, yes...{image=textheart.png}"
    sch900 "Jasmine? Go ahead and complement the client, dear." 
    hide image "01_foursome/4some_20.png"
    show image "01_foursome/4some_20.png" with d3
    j "ah...{image=textheart.png} {w}ah...{image=textheart.png}{w} old man... your cock is...{w} em...{w} ah...{image=textheart.png}{w} good."
    m "(heh... Ok...)"
    sch900 "Not bad... But you could do better..."
    j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
    j "Yes... oh, yes...{image=textheart.png} feels so good, feels so... ah...{image=textheart.png}"
    jump label_round02
label round02_jasmine:
    show blkfade with Dissolve(.7)
    pause.7
    hide image "01_foursome/4some_18.png" 
    show image "01_foursome/4some_18.png" behind blkfade
    jas[50] "Ah...{image=textheart.png}"
    jas[51] "He is fucking {size=+9}me{/size}..."
    jas[51] "M-my master...{image=textheart.png} yes...{image=textheart.png}"
    g9 "(Heh...)"
    hide image "01_foursome/4some_19.png"
    show image "01_foursome/4some_19.png" behind blkfade
    hide blkfade with Dissolve(.7)
    j "Ah...{image=textheart.png} ah...{image=textheart.png} I knew he would prefer me to you...{image=textheart.png}"
    j "Ah...{image=textheart.png} ah...{image=textheart.png} A-after all... I am... a... ah...{image=textheart.png}"
    j "I am a princess... ah...{image=textheart.png}"
    sch1100 "Not anymore, you're not, you nasty whore."
    j "Shut up, you disgusting wench. ah...{image=textheart.png} ah...{image=textheart.png}"
    j "What do you know about being a princess!?"
    j "I'm still a well educated... ah...{image=textheart.png} and ah...{image=textheart.png} I..."
    j "Oh, my god, his cock reaches so deep... ah...{image=textheart.png}"
    sch1100 "Yup, nothing but a shameless whore now..."
    j "ah... I hadn't expected you'd understand, ah...{image=textheart.png} with that tiny brain of yours...ah...{image=textheart.png}"
    j "Being a royalty is in my blood... ah...{image=textheart.png} ah...{image=textheart.png}"
    j "Nothing could ever change that... ah...{image=textheart.png}"
    sch1100 "Yeah, right."
    hide image "01_foursome/4some_21.png"
    show image "01_foursome/4some_21.png" with d3
    sch1100 "Hey, old man, when you're done fucking her royal highness..."
    sch1100 "You think you could do me a favour and cum all over her ugly face?"
    sch1100 "I want her to give me that lecture on being a princess, with cum and tears running down her cheeks."
    menu:
        "\"Not a problem.\"":
            m "Not a problem..."
            sch1100 "Thanks."
            j "Why everybody is always against me? I'm a princess!"
            j "Ah...{image=textheart.png} yes, like this! Please don't stop fucking me!"
            $ promised_to_cum_on_face = True
        "\"Be quiet Iris.\"":
            sch1100 "What? I'm just saying..."
            sch1100 "Whatever, old man, side with her if you will, but you know I'm right."
            sch1100 "This little pretentious slut maybe used to be a princess, but now she is not different from any other whore in this brothel..."
            j "Thank you for sticking up for me... ah... old man..."
            j "Ah...{image=textheart.png} yes...{image=textheart.png} ah...{image=textheart.png}"
        "\"..................\"":
            sch1100 "I take your silence as a \"yes\"."
            j "Ah...{image=textheart.png} ah...{image=textheart.png} this feels so good...."

        

        

       
    jump label_round03
label round03_jasmine:
    show blkfade with Dissolve(.7)
    pause.7
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    show image "01_foursome/4some_18.png" behind blkfade
    jas[50] ".........."
    jas[51] "ah.....{image=textheart.png}"
    jas[51] "ah...{image=textheart.png} ah...{image=textheart.png} yes....{image=textheart.png}"
    jas[51] "Yes...{image=textheart.png} yes...{image=textheart.png}"
    jas[51] "{image=textheart.png} ah...{image=textheart.png} yes...{image=textheart.png}"
    jas[51] "Yes...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
    dah[1] "Jasmine, my dear, you need to be a bit more vocal..."
    ir[8] "Yeah, this is getting boring..."
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    hide blkfade with Dissolve(.7)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    j "What? ah...{image=textheart.png} {w}but... what is there to say? Ah...{image=textheart.png}"
    sch1100 "Say \"I'm a stupid spoiled whore, and I love to get fucked!\""
    hide image "01_foursome/4some_19.png" 
    show image "01_foursome/4some_19.png" with d5
    j "Ah...{image=textheart.png} be quiet, you nasty, vulgar girl."
    sch900 "Well, actually something along those lines would work quite well..."
    hide image "01_foursome/4some_20.png" 
    show image "01_foursome/4some_20.png" with d5
    j "ah...{image=textheart.png} ah...{image=textheart.png} w-what?"
    hide image "01_foursome/4some_21.png" 
    show image "01_foursome/4some_21.png" with d5
    sch1100 "Say it, you whore! Say it!"
    j "What? Ah...{image=textheart.png} but this is... ah...{image=textheart.png}"
    j "Oh, it's getting so hard to concentrate..."
    j "ah...{image=textheart.png} alright, if I must..."
    j "Em...{w} ah...{image=textheart.png} {w}ah...{image=textheart.png}"
    j "I'm a spoiled... ah...{image=textheart.png} w-whore... and ah...{image=textheart.png}"
    j "I love to... ah...{image=textheart.png} get f-fucked... {size=+7}YES!{/size}{image=textheart.png}{image=textheart.png}{image=textheart.png} Oh yes!"
    j "Yes! Please keep going!"
    sch1100 "You forgot \"stupid\"."
    hide image "01_foursome/4some_19.png" 
    show image "01_foursome/4some_19.png" with d5
    j "W-what?"
    sch1100 "You said \"spoiled whore\" instead of \"Stupid spoiled whore\"."
    j "W-what? Do I have to repeat then ah...{image=textheart.png} Well, alright...{image=textheart.png} ah...{image=textheart.png} oh yes...{image=textheart.png}"
    g4 "OK, enough of this nonsense! Are you ready to cum, sluts?"
    show blkfade with Dissolve(.7)
    pause.7
    show image "01_foursome/4some_22.png" behind blkfade
    g4 "I know I am!"
    jas[49] "!!!!!!!!!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    dah[8] "Oh, my...{image=textheart.png}"
    ir[6] "Ah...{image=textheart.png} Yes...{image=textheart.png}"
    g4 "Here we go then! Like that! Like that!"
    hide blkfade with Dissolve(.7)
    with hpunch
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    sch900 "Oh... Not bad at all... yes...{image=textheart.png}"
    sch1100 "Old man?! ah...{image=textheart.png} ah...{image=textheart.png}"
    j "Ah...{image=textheart.png} I think I'm about to... ah...{image=textheart.png} ah...{image=textheart.png} harder!"
    g4 "Argh!"
    j "Yes! Yes! Harder!"
    sch900 "Ah...{image=textheart.png} ah...{image=textheart.png} Oh my, you sure do know how to use your fingers..."
    sch1100 "Ah...{image=textheart.png} ah...{image=textheart.png} yes...{image=textheart.png} Keep it up, old man, oh yes!"
    show image "01_foursome/4some_23.png" with d3
    j "Harder! I said fuck me harder, you peasant!"
    g4 "Argh! Shut it, you whore!"
    hide image "01_foursome/4some_23.png" with d3
    j "I'm about to... ah....{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    j ".................{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    show image "01_foursome/4some_24.png" with d5
    j "I'm cumming....{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    hide image "01_foursome/4some_19.png" 
    show image "01_foursome/4some_19.png" with d5
    j "You made me cum, you peasant!"
    g4 "Finally! Here! Take this then!"
    if promised_to_cum_on_face:
        sch1100 "On her face, old man! You promised!"
        g4 "Shut it, Iris... I'm... argh!"
    hide image "01_foursome/4some_22.png" 
    show image "01_foursome/4some_22.png" with d5
    j "?!!!!!!"
    show white 
    pause.2
    hide white
    pause.3
    show white 
    pause .1
    hide white
    show image "01_foursome/4some_25.png" with d5
    with hpunch 
    g4 "{size=+7}Argh! Y-yes!{/size}"
    j "AAAAAAAH!{image=textheart.png}{image=textheart.png}{image=textheart.png} I'm cumming!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    j "No, stop ah...{image=textheart.png} you're cumming inside of me...{image=textheart.png} it's so...{image=textheart.png}"
    j "ah...{image=textheart.png}{w} I...{w} what...{w} ah...{image=textheart.png}{w} I'm cumming.... "
    sch1100 "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
    sch900 "Well, now, this is quite lovely..."
    j "ah...{image=textheart.png} ah......{image=textheart.png}"
    show white with Dissolve(2)
    show ctc7 at right
    pause 
    hide ctc7
    show image "01_foursome/4some_26.png" behind white
    hide white with Dissolve(2)
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    j "..............................."
    j "*Sob-sob*....."
    j "Why?........................."
    sch900 "Why what, dear?"
    j "Why......."
    show image "01_foursome/4some_27.png" with d3
    j "{image=textheart.png}Why does this feel so right?{image=textheart.png}"
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

    
    
#############
label round01_iris:
    show blkfade with Dissolve(.7)
    pause.7
    show image "01_foursome/4some_28.png" behind blkfade
    ir[5] "Me? Really?"
    dah[1] "Why do you sound so surprised, dear?"
    jas[46] "Because she knows she is nothing but a worthless peasant wench, and doesn't deserve to go first." 
    hide blkfade with Dissolve(.7)
    sch1100 "Ah...{image=textheart.png} ah...{image=textheart.png} oh, yes...{image=textheart.png}"
    j "Didn't you hear what I just said, you nasty woman?"
    sch1100 "ah...{image=textheart.png} yes...{image=textheart.png} like this...{image=textheart.png} oh, yes...{image=textheart.png}"
    j "What's the matter with you? Can't you hear me?"
    sch1100 "Oh, I heard you alright... ah...{image=textheart.png}"
    sch1100 "But it's difficult to ah...{image=textheart.png} get mad at you ah...{image=textheart.png} when, I've been chosen over you ah...{image=textheart.png}"
    sch1100 "And there is nothing you can do about it, ex-princess... ah...{image=textheart.png}"
    sch1100 "All there is left for you... ah...{image=textheart.png}"
    sch1100 "Is to feel jealous of me for once ..."
    sch1100 "All I feel for you right now is pity... Oh, yes, like this... ah...{image=textheart.png}"
    j "P-pity?!"
    sch1100 "Oh, old man... You are fucking me... I will never get used to this sensation..."
    j "H-how dare you?!"
    sch1100 "Ah...{image=textheart.png} Yes... Oh, yes...{image=textheart.png}"
    sch1100 "Harder, do it harder! Yes, fuck me!"
    hide image "01_foursome/4some_29.png" 
    show image "01_foursome/4some_29.png" with d3
    j "Tsk... whatever...."
    jump label_round02
label round02_iris:
    show blkfade with Dissolve(.7)
    pause.7
    hide image "01_foursome/4some_29.png"
    show image "01_foursome/4some_29.png" behind blkfade
    ir[1] "ah...{image=textheart.png} ah...{image=textheart.png}"
    jas[46] "Tsk..."
    ir[1] "Ah...{image=textheart.png} yes...{image=textheart.png}"
    hide blkfade with Dissolve(.7)
    sch1100 "This feels soooooo good... Dahlia, what am I to do now?"
    sch1100 "I forgot everything you taught me."
    sch900 "My dear, the things I teach you are not carved in stone."
    sch900 "Sometimes it's alright to just listen to your heart."
    sch900 "Just enjoy yourself, my girl."
    sch1100 "ah...{image=textheart.png} alright...{image=textheart.png}"
    j "........................................................"
    sch1100 "Ah...{image=textheart.png} yes...{image=textheart.png} Ah....{image=textheart.png}"
    hide image "01_foursome/4some_30.png"
    show image "01_foursome/4some_30.png" with d3
    sch1100 "Oh, Forgive me, daddy... ah...{image=textheart.png}"
    hide image "01_foursome/4some_31.png"
    show image "01_foursome/4some_31.png" with d3
    sch1100 "And, ah...{image=textheart.png} Old man, thank you for making this happen for me... ah...{image=textheart.png}"
    sch1100 "If not for you I would still be waiting tables... ah...{image=textheart.png}"
    menu:
        "\"And now you're a whore.\"":
            m "And now you are a whore."
            hide image "01_foursome/4some_32.png"
            show image "01_foursome/4some_32.png" with d3
            sch1100 "Yes! Yes! I am a whore!"
            hide image "01_foursome/4some_30.png"
            show image "01_foursome/4some_30.png" with d3
            sch1100 "Since I got my scar I never thought this could be possible... Ah...{image=textheart.png}"
            sch1100 "Thank you! Thank you! Please, I'm begging you, fuck me harder now!"
            m "No problem..."
            hide image "01_foursome/4some_29.png"
            show image "01_foursome/4some_29.png" with d3
            sch1100 "Ahhh!{image=textheart.png} YES!{image=textheart.png}"

        "\"Shut up and take my dick, Iris.\"":
            m "Shut up and take my dick, Iris."
            hide image "01_foursome/4some_29.png"
            show image "01_foursome/4some_29.png" with d3
            sch1100 "Yes! YES! Oh YES! Talk to me like you would to any other whore!"
            sch1100 "Forget that I'm your friend's daughter! Just fuck me!"
            g11 "You slut!"
            sch900 "Very, very nice, Iris."
            sch1100 "Ah...{image=textheart.png} ah...{image=textheart.png} Just keep fucking me!"
        "\"You owe me a big one.\"":
            m "You owe me a big one for this, Iris."
            hide image "01_foursome/4some_29.png"
            show image "01_foursome/4some_29.png" with d3
            sch1100 "I do, I know. And I always... ah...{image=textheart.png} "
            sch1100 "Always return my debts! Ah, yes...{image=textheart.png}"
            sch1100 "But for now... just fuck me..."
            sch1100 "Make me feel like a dirty whore, please...{image=textheart.png}"
            j "Tsk... Make you feel? You are one, no doubt about it..."
            sch1100 "Ah...{image=textheart.png} ah....{image=textheart.png} ah...{image=textheart.png} I'm so happy...."
    jump label_round03
    
label round03_iris:
    show blkfade with Dissolve(.7)
    pause.7
    hide image "01_foursome/4some_32.png"
    show image "01_foursome/4some_32.png" behind blkfade
    ir[7] "Yes.....{image=textheart.png}"
    ir[7] "Ah...{image=textheart.png} ah...{image=textheart.png}"
    dah[1] "Iris, dear, do you like the feeling of his cock inside of you?"
    ir[6] "Ah...{image=textheart.png} Like it? I love it! Ah...{image=textheart.png} Every time it enters me it takes my breath away. Ah...{image=textheart.png}"
    dah[2] "Good. Tell us more..."
    hide blkfade with Dissolve(.7)
    sch1100 "I love it! Love it! Love the way he fucks me! ah!{image=textheart.png}"
    sch1100 "Love the way he impales me on his dick, that from how it feels it might as well be an iron rod!"
    sch900 "Splendid, my dear."
    j "Tsk... Nothing special... I could've said better." 
    sch1100 "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
    sch900 " Keep going, dear."
    sch1100 "Yes! Old man! Fuck me! Fuck me!"
    hide image "01_foursome/4some_34.png"
    show image "01_foursome/4some_34.png" with d3
    sch1100 "Make me a real whore! Make my stupid father cry with anger and envy..."
    sch1100 "Yes! Yes! That's what's happening to your dear Iris, father! Ah!{image=textheart.png}"
    sch1100 "She is being fucked like a cheap whore!"
    sch900 "Am... er... ok, this would work as well, I guess, but--"
    hide image "01_foursome/4some_36.png"
    show image "01_foursome/4some_36.png" with d3
    sch1100 "Yes! Yes! Fuck me! Stub me with your hard cock like you would stub a sheep with a dagger if you were to gut it!"
    j ".................?"
    sch900 "Dear, I think you are taking a wrong direction with this--"
    hide image "01_foursome/4some_35.png"
    show image "01_foursome/4some_35.png" with d3
    sch1100 "Stub me with your cock! Stub me! Slaughter me! Yes!"
    sch1100 "Fuck me and then murder me!"
    j "(What is wrong with her?)"
    sch1100 "Yes! Yes! Like that! I'm getting close! Yes!{image=textheart.png}"
    sch1100 "Come on, old man, do it harder! Rip me apart with your hard cock!"
    sch1100 "Yes! Yes! Yes...{image=textheart.png}"
    g4 "agh... I'm getting close..."
    sch1100 "Yes, yes! Pummel me with your cock!"
    sch1100 "Kill me and fill my corpse up with your hot semen...{image=textheart.png}"
    g4 "Shut up, Iris, your weird-ass commentaries are not helping!"
    hide image "01_foursome/4some_37.png"
    show image "01_foursome/4some_37.png" with d3
    sch1100 "What? But Dahlia said men love to hear such things from women when they fuck them?"
    sch900 "I said no such thing, dear."
    sch900 "Try to concentrate a little harder on being dominated and on submitting to the man..."
    sch900 "And little less on odd rape-murder talks..."
    hide image "01_foursome/4some_38.png"
    show image "01_foursome/4some_38.png" with d3
    sch1100 "Oh, OK."
    sch1100 "Yeah, sure... I mean, I totally only said those things because I thought that that's what I was supposed to say..."
    j "Right..."
    j "What a weirdo..."
    hide image "01_foursome/4some_40.png"
    show image "01_foursome/4some_40.png" with d3
    sch1100 "Shut up, you bitch, I'm so tired of your crap!"
    sch1100 "At least I'm not secretly fantasizing about sex with freaking tigers!"
    hide image "01_foursome/4some_41.png"
    show image "01_foursome/4some_41.png" with d3
    j "What? Sex with.... t-tigers..."
    j "How did you...?"
    sch1100 "Yeah, you talk in your sleep. \"Rajah, Rajah, my dear tiger! Mount me! Mount you tigress!\""
    j "B-but those, are just nicknames of course... I would never.. ehm..."
    sch1100 "Yeah, whatever...."
    with hpunch
    g11 "{size=+7}THAT'S ENOUGH!{/size}"
    g11 "I've had enough of your bullshit! All of you, shut up and let me cum in peace!"
    hide image "01_foursome/4some_39.png"
    show image "01_foursome/4some_39.png" with d3
    j "You see what you did? You can't even be a proper whore!"
    sch1100 "..................."
    hide image "01_foursome/4some_42.png"
    show image "01_foursome/4some_42.png" with d3
    sch1100 "You're right... *sob-sob*..."
    sch1100 "I feel his dick got all soft... I ruined everything..."
    sch1100 "*Sob-sob-sob*... I knew all this was too good to be true..."
    g4 "No, no, don't you fucking dare to start crying again!"
    hide image "01_foursome/4some_43.png"
    show image "01_foursome/4some_43.png" with d3
    sch1100 "I'm so-o-o-orry!"
    hide image "01_foursome/4some_44.png"
    show image "01_foursome/4some_44.png" with d3
    sch900 "Everything will be alright."
    sch900 "Jasmine I need you to be quiet for a while..."
    j "Hmph........"
    sch900 "Iris, repeat after me: \"I love cock... I love licking it... I love sucking on it...\""
    sch1100 "*sob-sob* I... I love cock... I love sucking on it and licking it..."
    sch900 "\"I l-love when men put their cocks between my tits and in my pussy...\""
    sch1100 "*Sob* I love it when men fuck me in my pussy and in-between my tits..."
    sch900 "\"B-but most of all I love a feeling of another hard cock entering my tiny asshole...\""
    sch1100 "But most of all I love to be fucked up my ass..."
    hide image "01_foursome/4some_32.png"
    show image "01_foursome/4some_32.png" with d3
    sch1100 "Hey, it's working! I can feel it getting super hard again..."
    g4 "................."
    sch900 "\"But nothing compares to the sensation of hot cum covering my cute little face...\""
    sch900 "\"I always try to swallow it all though, because I love the taste of cum even more...\""
    sch1100 "But I love the taste of cum the most... And I love the feeling of it on my face.... ah..."
    g4 "Yes, you slut, yes..."
    sch1100 "Ah...{image=textheart.png} ah...{image=textheart.png} Yes, fuck me, fuck me!"
    sch1100 "Oh, my god! How did you do that, Dahie?"
    j "Hm... This was... most impressive indeed."
    sch900 "Enough, talks, girls. Time to bring this party to a worthy conclusion."
    g4 "*Panting*"
    sch900 "How, are you doing there, sweetheart?"
    g4 "I'm good. I'm good."
    sch900 "Do you enjoy this cute little whore's pussy?"
    g4 "Yes... Yes!"
    sch1100 "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} so hard!"
    sch900 "You know, the other day she told me that more than anything she loves to get fucked!"
    g4 "*Panting*"
    sch900 "She said that if she could she would fuck for free..."
    sch900 "She would just go outside and give a blowjobs to the first guy she would see."
    g4 "*Growl*"
    sch900 "And then another to the next guy..."
    sch900 "And then just go to the market square with her face all covered in cum and let every man there use her at will!"
    sch1100 "Ah...{image=textheart.png} what? I never--"
    g4 "WHAT A WHORE!"
    sch900 "Yes, she is a whore! A nasty little slut!"
    with hpunch
    g4 "{size=+9}ARGH!!!!!!!!!!!{/size}"
    with hpunch
    g11 "{size=+9}I'm CUMMING!{/size}"
    show white
    pause.2
    hide white
    g11 "{size=+9}Take it all, you whore!{/size}"
    show white 
    pause.2
    hide white
    pause.3
    show white 
    pause .1
    hide white
    show image "01_foursome/4some_45.png" with d5
    with hpunch 
    sch1100 "{size=+9}AAAAAAAAAAAAAAAAAAAAAAAAAAAH!{image=textheart.png}{image=textheart.png}{image=textheart.png}{/size}"
    g4 "Fucking whore! And some more for you!"
    with hpunch
    show image "01_foursome/4some_46.png" with d3
    sch1100 "Ahh!{image=textheart.png} It's so hot! I'm cumming!"
    sch1100 "I'm cumming!{image=textheart.png} Yes, old man!{image=textheart.png} Cum!{image=textheart.png} Cum in my pussy!{image=textheart.png}"
    hide image "01_foursome/4some_46.png" 
    show image "01_foursome/4some_45.png" with d3
    sch1100 "My father would go insane if he knew...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
    sch1100 "Ah, daddy, I'm cumming again...{image=textheart.png} sorry, daddy, but this feels too good."
    show white with Dissolve(2)
    show image "01_foursome/4some_47.png" behind white
    pause.5
    dah[1] "Well, this was a close call, but it's all good for as along as the client is satisfied..."
    dah[3] "And you are, aren't you, sweetheart..."
    g9 "Oh, yes..."
    dah[1] "Good..."
    jas[59] "Still, the way you salvaged the situation after the \"murder my corpse\" fiasco Iris brought upon us, was quite amazing..."
    dah[1] "Thank you dear. I've been in this business for quite a while, you know..." 
    ir[9] "*Sob-sob*"
    dah[3] "Iris? Are you alright dear?"
    dah[2] "It's normal to get a bit emotional after the sex. Just let it out..."
    hide white with Dissolve(1)
    sch1100 "It's not that, Dahie... It's just....*sob*"
    sch900 "Dear?"
    sch1100 "I'm so happy.........................."
    if promised_to_cum_on_face:
        sch1100 "I was hoping he would cum on Jasmine's face to teach her a lesson..."
        sch1100 "But this way is so much better..."
        sch1100 "I am full of cum again..."
        j "Who is the slut now?"
        sch1100 "I am... *sob*"
    show ctc7 at right
    pause 
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