###############################SHOP########################
label toplessstart:
    if onquest:
        "You need to complete your current quest first in order to take on a new one."
        jump store2
    else:
        show blkfade with d3
        pause.5
        hide blkfade with d3
        aza[1] "Hey, you got a second, sweetie?"
        aza[1] "I need 200 gold coins to make some repairs around the shop."
        menu:
            aza[1] "You think you could help a girl out?"
            "\"Sure, no problem.\"":
                aza[1] "Really? Thank you, sweetie! I knew there was something special about you!"
                aza[1] "And, hey, I will make it worth your while!"
                jump quest13start
            "\"Are you insane? 200 gold coins is a lot!\"":
                aza[1] "Hey, I'm not asking you to just hand me over the gold."
                aza[1] "I will make it worth your while, I promise!"
                menu: 
                    "\"Well, alright...\"":
                        aza[1] "Really? Thank you, sweetie! I knew there was something special about you!"
                        aza[1] "And, hey, I will make it worth your while!"
                        jump quest13start
                    "\"Nah, I don't think so...\"":
                        aza[1] "Oh, I see... well, let me know if you change your mind..."
                        jump store2
            "\"Maybe later.\"":
                aza[1] "Oh, OK. Whenever you're ready, sweetie. I'm not going anywhere."
                jump store2
    #####QUEST TAKEN####
label quest13start:
        aza[1] "How about, if you do help to finance the repairs of my shop, as a thank you, from that point on..."
        aza[1] "I will always..."
        aza[1] "Greet you topless whenever you visit my store!! Huh? How about that?!"
        aza[1] "Yes! Just like princess Jasmine!"
        aza[1] "People say that sometimes she can be seen walking around the cheapside with her tits completely bared, you know!"
        menu:
            aza[1] "So, how about that?!"
            "\"You have a deal!\"":
                aza[1] "Fantastic! Just let me know when you have the money!"
                aza[1] "Until next time then."
            "\"I would rather have a discount.\"":
                aza[1] "A discount? Where is fun in that!"
                aza[1] "I would rather copy the princess and go topless for you!"
                aza[1] "Just let me know when you have the money!"
                aza[1] "Until next time then."
    
show image "04_pt/slavem/qstart.png" with Dissolve(.3)
show image "04_pt/slavem/onaquest.png" with Dissolve(.3)
show con1 at right
show ctc7 at right
pause 
hide con1
hide ctc7
hide image "04_pt/slavem/qstart.png" with Dissolve(.3)
$ onquest = True
$ storestarted2 = True
$ storestarted = False
$ renpy.play('sounds/door2.mp3')
hide image "04_pt/slavem/bld.png" with Dissolve(.3)
jump mainmenu

label toplesspay:
        if gold >= 200:
            show blkfade with d3
            pause.5
            hide blkfade with d3
            menu:
                aza[1] "Really? You brought the money?"
                "\"Yes.\"":
                    aza[7] "Thank you, sweetie."
                    $ gold -=200
                    $ storestarted2 = False
                    $ storecomplete = True
                    $ quest13complete = True
                    $ onquest = False
                    $ renpy.play('sounds/win2.mp3')                        
                    show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
                    show con1 at right
                    show ctc7 at right
                    pause
                    hide con1
                    hide ctc
                    hide image "04_pt/slavem/onaquest.png" with Dissolve(.3)
                    aza[1] "Your money will be well spent, I promise."
                    hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
                    aza[6] "Our deal? What are you talking about?"
                    aza[3] "I'm just kidding. Next time you visit my shop I will be topless, I promise."
                    aza[3] "Until next time then."
                    $ renpy.play('sounds/door2.mp3')
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
                    jump mainmenu
                "\"Not yet.\"":
                    jump store2
        else:
            aza[3] "Hey, what are you trying to pull? I said 200 gold coins."
            jump store2
            
                

        