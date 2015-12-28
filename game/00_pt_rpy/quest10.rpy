label quest10starts:
    sch5 "Somebody's been stealing from my customers for quite some time now..."
    sch5 "This is very bad for business..."
    sch5 "Would you help me catch the thief?"
    menu:
        "\"Sure.\"":
            if onquest:
                "You need to finish your current quest first, before you can take a new one."
                jump market2
            else:
                if gold >= 200:
                  
                    sch5 "Great! Here is what you will need to do."
                    sch5 "Listen carefully now, because if you miss something important you will most likely fail this quest!"
                    sch5 "Er... I mean you will not be able to help me."
                    sch5 "I want you to come by my fruit stand and pose as a rich customer..."
                    sch5 "You don't have to do much. Just browse through my goods and flash your purse full of gold..."
                    sch5 "This thief is operating in a peculiar manner..."
                    sch5 "He stalks his prey for three days and then makes his move on the forth..."
                    sch5 "We need to throw that bastard off guard!"
                    label repeatbalsam:
                    sch5 "So I want you to come here for three days in a row... Then skip one day and return on the fifth..."
                    sch5 "Did you get it?"
                    menu:
                        "\"Yes, I got it.\"":
                            pass
                        "\"What?\"":
                            jump repeatbalsam

                    sch5 "Oh, and one more thing: make sure you have enough gold on you at all times... 200 gold coins at the very least."
                    sch5 "Alright! I'll see you tomorrow then!"

                    $ quest1000 = False
                    $ quest10start = True
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
                    "It's getting late. You decide to head home."
                    jump dayends 
                else:
                    ">You don't have enough gold."
                    jump market2
        "\"Maybe later.\"":
            sch5 "Oh, I see..."
            jump market2
#####DAY ONE#####
label quest10day1:
    if gold >= 200:
        show blkfade with d3
        pause.7
        hide blkfade with d3
        sch5 "Well, well, well... If it isn't my favorite and most generous customer..."
        sch5 "I hope you brought your purse full of gold with you, like always! *Wink-Wink*"
        ">You spend quite some time on the market square posing as a rich customer..."
        ">You don't know whether or not the thief picked up on you yet..."
        $ quest10fail = False
        ">It's getting late. You decide to head home."
        show blkfade with d3
        pause.7
        hide blkfade with d3
        jump dayends 
    else:
        show blkfade with d3
        pause.7
        hide blkfade with d3
        ">You didn't bring enough gold and thief looses interest in you."
        ">It's getting late. You decide to head home."
        show blkfade with d3
        pause.7
        hide blkfade with d3
        jump dayends 
#####DAY TWO#####
label quest10day2:
    show blkfade with d3
    pause.7
    hide blkfade with d3
    if gold >= 200:
        sch5 "Good day, sir. So nice to see you again..."
        sch5 "Would you like to buy something? I see that you have a lot of money with you again!"
        ">You spend quite some time on the market square posing as a rich customer..."
        ">A few times you felt as if somebody was watching you..."
        ">But it might have just been your imagination..."
        show blkfade with d3
        pause.7
        hide blkfade with d3
        $ quest10fail = False
        ">It's getting late. You decide to head home."
        jump dayends 
    else:
        "You didn't bring enough gold and thief looses interest in you."
        show blkfade with d3
        pause.7
        hide blkfade with d3
        "It's getting late. You decide to head home."
        jump dayends 
#####DAY THREE#####
label quest10day3:
    show blkfade with d3
    pause.7
    hide blkfade with d3
    if gold >= 200:
        sch5 "It's you again... So nice to see you..."
        sch5 "It is also nice to see your purse bulging with gold!"
        ">You spend quite some time on the market square posing as a rich customer..."
        ">Today you definitely felt someone's eyes on you throughout entire time..."
        $ quest10fail = False
        show blkfade with d3
        pause.7
        hide blkfade with d3
        ">It's getting late. You decide to head home."
        jump dayends 
    else:
        "You didn't bring enough gold and thief looses interest in you."
        show blkfade with d3
        pause.7
        hide blkfade with d3
        "It's getting late. You decide to head home."
        jump dayends 
#####DAY FOUR#####
label quest10day4:
    show blkfade with d3
    pause.7
    hide blkfade with d3
    sch5 "Hey! My favorite customer, here again!"
    sch5 "(You weren't supposed to show up today...)"
    sch5 "(You come for four days in a row, flash your gold and don't buy a thing. The thief will get suspicious now...)"
    sch5 "Alright, just act normal, maybe it will still work..."
    ">You spend quite some time on the market square posing as a rich customer..."
    ">The thief is nowhere to be seen...."
    ">You failed the quest."
    show blkfade with d3
    pause.7
    hide blkfade with d3
    $ quest10fail = True
    ">It's getting late. You decide to head home."
    jump dayends 
#####DAY FIVE#####
label quest10day5:
    show blkfade with d3
    pause.7
    hide blkfade with d3
    if gold >= 200:
        
        sch5 "My favorite customer here again... With his gold..."
        ">You browse through the goods as usual..."
        ">The thief is most likely to make his move today..."
        ">Time passes by but nothing happens..."
        ">Suddenly you feel a very light pull on your belt..."
        ">You see that your purse is gone!"
        sch5 "This is it! Go after him!!!"
        ">You rush after the thief!"
        $ renpy.play('sounds/iris_run.mp3')
        show blkfade with d3
        pause.7
        hide blkfade with d3
        jump quest10chase
    else:
        "You didn't bring enough gold and thief looses interest in you."
        "It's getting late. You decide to head home."
        jump dayends 
#####QUEST 10 CHASE#####
label quest10chase:
    if strength >= 0 and strength < 4:
        ">You run as fast as you can, but your speed is lacking..."
        ">In a matter of moments you are out of breath and the thief is nowhere to be seen..." 
        ">Which means you also lost your 200 gold coins..."
        $ gold -=200
        ">It's getting late. You decide to head home."
        show image "interface/blackfade.png" with Dissolve(.3)
        jump dayends 
    elif strength >= 4 and strength < 8:
        ">You run as fast as you can..."
        ">You are able to maintain the distance between you and the thief for some time..."
        ">Then you start to feel out of breath... You know that you can't keep this up for much longer."
        ">It's now or never!"
        ">You grab a big rock and throw it aiming for the thief's back..."
        ">The thief notices your throw and avoids the rock but he loses balance and falls to the ground..."
        ">You pin him down..."
        ">You were able to catch the thief, but you took too long to apprehend him and he was able to ditch your purse somewhere..."
        ">You lost 200 gold."
        $ gold -=200
        jump quest10chaseended
    elif strength >= 8:
        ">You sprint after the thief and catch him in a matter of seconds."
        ">Both Balsam and the thief look at you with bewilderment. They had no idea you were in such a great shape..."
        ">You get your purse containing 200 gold coins back." 
        jump quest10chaseended
#####QUEST 10 CHASE ENDED#####
label quest10chaseended:
    ">You hand over the thief to Balsam."
    $ quest10fail = False
    $ quest10start = False
    $ quest10complete = True
    $ quest10days = 0
    $ onquest = False
    $ renpy.play('sounds/win2.mp3')
    hide image "04_pt/slavem/onaquest.png." with Dissolve(.3)
    show image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    show con1 at right
    show ctc7 at right
    pause
    ">You completed the quest."
    ">Come talk to Balsam sometime. He may have a business offer for you."
    hide con1
    hide ctc7
    hide image "04_pt/slavem/qcompleted.png" with Dissolve(.3)
    hide image "04_pt/slavem/bld.png" with Dissolve(.3)
    ">You return home..."
    show image "interface/blackfade.png" with Dissolve(.3)
    pause 1
    jump dayends
#####FRUIT STAND######
label fruitstand:
    show blkfade with d3
    pause.7
    hide blkfade with d3
    sch5 "Thank you for helping me out with that thief problem..."
    sch5 "Business is back to normal now..."
    sch5 "More than that: I'm making even more gold than I used to..."
    sch5 "I'm looking for investors to expand my territory."
    sch5 "What do you say?"
    sch5 "If you were to invest into a new fruit stand I could manage it for you..."
    sch5 "...You would get 40 percent... er... "
    sch5 "25 percent of the profit."
    sch5 "All I need from you is 500 gold coins. Are you interested?"
    menu:
        "You currently have [gold] gold. \nWould you like to invest 500 gold coins?"
        "\"Yes please.\"":
            if gold >= 500: 
                $ gold -=500
                $ standbought = True
                $ fruitstand00 = False
                sch5 "Very good! Leave it to me, I will take care of everything."
                sch5 "All you have to do is show up here every now and then to collect your share..."
                $ renpy.play('sounds/win2.mp3')
                ">You bought a fruit stand. Now you can collect gold from Balsam daily." 
                show blkfade with d3
                pause.7
                hide blkfade with d3
                jump market2
            else:
                sch5 "Not enough gold? That's alright. Come back when you are ready."
                show blkfade with d3
                pause.7
                hide blkfade with d3
                jump market2
        "\"Maybe later.\"":
            sch5 "Come back when you are ready."
            show blkfade with d3
            pause.7
            hide blkfade with d3
            jump market2
        
    
    
    
    
    
    
    
    
    
    
    
    