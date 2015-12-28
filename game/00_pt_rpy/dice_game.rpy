label playmdice:
    play music "music/dice_game.MP3" fadein 2 fadeout 2  #DICE GAME2
    #play music "music/Bushwick Tarantella Loop.MP3" fadein 2 fadeout 2  #DICE GAME
    $ dicestart = renpy.random.randint(1, 6) #игрок «бросает» первую кость
    if dicestart == 1:
        sch6 "Great, let's play some dice!"
    elif dicestart == 2:
        sch6 "I'm feeling lucky today. I hope you are ready to say \"goodbye\" to your gold, my friend!"
    elif dicestart == 3:
        sch6 "Well I'm ready. What about you?"
        sch6 "Let's play then!"
    elif dicestart == 4:
        sch6 "Finally, a worthy opponent!"
        sch6 "You're still gonna lose your gold though..."
    elif dicestart == 5:
        sch6 "What you call \"luck\", my friend, I call \"skill\"!"
    elif dicestart == 6:
        sch6 "Alright! Let the tournament begin!"
    show blkfade with Dissolve(.3)
    $ dicetris = 0
    show image "dice/dice_m.png" with Dissolve(.3)
    hide blkfade with Dissolve(.3)
label onemoredice:
    sch6 "Your roll."
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
    $ renpy.play('sounds/dice01.mp3')
    pause 1
    $ cube1 = renpy.random.randint(1, 6) #игрок «бросает» первую кость
    if cube1 == 1:
        show image "dice/dice1_01.png" with Dissolve(.3)
    elif cube1 == 2:
        show image "dice/dice1_02.png" with Dissolve(.3)
    elif cube1 == 3:
        show image "dice/dice1_03.png" with Dissolve(.3)
    elif cube1 == 4:
        show image "dice/dice1_04.png" with Dissolve(.3)
    elif cube1 == 5:
        show image "dice/dice1_05.png" with Dissolve(.3)
    elif cube1 == 6:
        show image "dice/dice1_06.png" with Dissolve(.3)
    
    $ cube2 = renpy.random.randint(1, 6) #игрок «бросает» первую кость
    if cube2 == 1:
        show image "dice/dice2_01.png" with Dissolve(.3)
    elif cube2 == 2:
        show image "dice/dice2_02.png" with Dissolve(.3)
    elif cube2 == 3:
        show image "dice/dice2_03.png" with Dissolve(.3)
    elif cube2 == 4:
        show image "dice/dice2_04.png" with Dissolve(.3)
    elif cube2 == 5:
        show image "dice/dice2_05.png" with Dissolve(.3)
    elif cube2 == 6:
        show image "dice/dice2_06.png" with Dissolve(.3)
    
    if cube1 + cube2 >= 1 and cube1 + cube2 <= 4:
        sch6 "Ha-ha-ha! Your gold is as good as already mine!"
    elif cube1 + cube2 >= 4 and cube1 + cube2 <= 6:
        sch6 "I have a good feeling about this one..."
    elif cube1 + cube2 >= 6 and cube1 + cube2 <= 10:
        sch6 "Not bad, not bad... My turn now."
    elif cube1 + cube2 >= 10 and cube1 + cube2 <= 12:
        sch6 "Getting a little worried here..."
    elif cube1 + cube2 == 12:
        sch6_2 "Camel's crap!" 
    $ renpy.play('sounds/dice02.mp3')
    pause.5
    $ cube3 = renpy.random.randint(1, 6) #игрок «бросает» первую кость
    if cube3 == 1:
        show image "dice/dice3_01.png" with Dissolve(.3)
    elif cube3 == 2:
        show image "dice/dice3_02.png" with Dissolve(.3)
    elif cube3 == 3:
        show image "dice/dice3_03.png" with Dissolve(.3)
    elif cube3 == 4:
        show image "dice/dice3_04.png" with Dissolve(.3)
    elif cube3 == 5:
        show image "dice/dice3_05.png" with Dissolve(.3)
    elif cube3 == 6:
        show image "dice/dice3_06.png" with Dissolve(.3)
        
    $ cube4 = renpy.random.randint(1, 6) #игрок «бросает» первую кость
    if cube4 == 1:
        show image "dice/dice4_01.png" with Dissolve(.3)
    elif cube4 == 2:
        show image "dice/dice4_02.png" with Dissolve(.3)
    elif cube4 == 3:
        show image "dice/dice4_03.png" with Dissolve(.3)
    elif cube4 == 4:
        show image "dice/dice4_04.png" with Dissolve(.3)
    elif cube4 == 5:
        show image "dice/dice4_05.png" with Dissolve(.3)
    elif cube4 == 6:
        show image "dice/dice4_06.png" with Dissolve(.3)
    
    if cube1 + cube2 > cube3 + cube4:
        $ renpy.play('sounds/win2.mp3')
        ">You won! You received 20 gold coins!"
        $ youlost = renpy.random.randint(1, 6)
        if youlost == 1:
            sch62 "Dammit... I was so close..."
        elif youlost == 2:
            sch11_3 "Aw... You lost, father."
            sch62 "Thank you, Iris. I can see that."
        elif youlost == 3:
            sch62 "I hope you're not cheating..."
            sch62 "If you do I will have to slice your throat. Nothing personal."
            sch11_2 "Father?"
            sch6 "I'm just kidding. Here is your gold."
        elif youlost == 4:
            sch6 "Another one for me!"
            sch62 "No wait... this plus that... oh, crap..."
            sch62 "Here is your money..."
        elif youlost == 5:
            sch6 "Today is not my day..."
        elif youlost == 6:
            sch62 "If I lose anymore gold I will have to sell this inn and return to my old ways..."
            sch11 "That would be awesome!"
            sch62 "Be quiet girl, I'm not going to lose any more..."
        $ gold +=20
    elif cube1 + cube2 == cube3 + cube4:
        "It's a tie!"
        sch11_2 "Wow! No winners this time..."
        sch62 "How frustrating..."
    else:
        "You lost. You paid 20 gold coins!"
        $ youlost = renpy.random.randint(1, 6)
        if youlost == 1:
            sch11 "Good job, father!"
            sch6 "Of course, I'm a professional."
        if youlost == 2:
            sch6 "He-he. Your gold please!"
        if youlost == 3:
            sch6 "Iris, daddy is gonna buy something nice for you with this money."
            sch11_3 "You always say that..."
        if youlost == 4:
            sch6 "The victory is mine! And your gold as well!"
        if youlost == 5:
            sch6 "Another one for Maslab!"
            sch6 "Drinks for everyone on the house!"
            sch62 "Calm down, you good-for-nothing dirtbags! That was a joke!"
        if youlost == 6:
            sch11 "You won, daddy!"
            sch6 "Pay up, my friend!"
        
        $ gold -=20
        
    $ dicetris += 1
    if dicetris >= 3:
        sch6 "Good game, good game."
        show blkfade with Dissolve(.3)
        hide image "dice/dice1_01.png"
        hide image "dice/dice1_02.png"
        hide image "dice/dice1_03.png"
        hide image "dice/dice1_04.png"
        hide image "dice/dice1_05.png"
        hide image "dice/dice1_06.png"
        hide image "dice/dice2_01.png"
        hide image "dice/dice2_02.png"
        hide image "dice/dice2_03.png"
        hide image "dice/dice2_04.png"
        hide image "dice/dice2_05.png"
        hide image "dice/dice2_06.png"
        hide image "dice/dice3_01.png"
        hide image "dice/dice3_02.png"
        hide image "dice/dice3_03.png"
        hide image "dice/dice3_04.png"
        hide image "dice/dice3_05.png"
        hide image "dice/dice3_06.png"
        hide image "dice/dice4_01.png"
        hide image "dice/dice4_02.png"
        hide image "dice/dice4_03.png"
        hide image "dice/dice4_04.png"
        hide image "dice/dice4_05.png"
        hide image "dice/dice4_06.png"
        hide image "dice/dice_m.png" 
        pause.2
        hide blkfade with Dissolve(.3)
        if awmaslab:
            ">Your relationship with Maslab is at maximum level."
            ">You return home and go to sleep."
            show image "interface/blackfade.png" with Dissolve(.3)
            pause 1
            jump dayone
        else:
            ">Your relationship with Maslab has improved."
            $ maslabfriendship += 1
            ">You return home and go to sleep."
            show image "interface/blackfade.png" with Dissolve(.3)
            pause 1
            jump dayone
        
            
    else:
        show blkfade with Dissolve(.3)
        hide image "dice/dice1_01.png"
        hide image "dice/dice1_02.png"
        hide image "dice/dice1_03.png"
        hide image "dice/dice1_04.png"
        hide image "dice/dice1_05.png"
        hide image "dice/dice1_06.png"
        hide image "dice/dice2_01.png"
        hide image "dice/dice2_02.png"
        hide image "dice/dice2_03.png"
        hide image "dice/dice2_04.png"
        hide image "dice/dice2_05.png"
        hide image "dice/dice2_06.png"
        hide image "dice/dice3_01.png"
        hide image "dice/dice3_02.png"
        hide image "dice/dice3_03.png"
        hide image "dice/dice3_04.png"
        hide image "dice/dice3_05.png"
        hide image "dice/dice3_06.png"
        hide image "dice/dice4_01.png"
        hide image "dice/dice4_02.png"
        hide image "dice/dice4_03.png"
        hide image "dice/dice4_04.png"
        hide image "dice/dice4_05.png"
        hide image "dice/dice4_06.png"
        pause.2
        hide blkfade with Dissolve(.3)
        jump onemoredice
 
        
   
        
        
        
        
        
        
        
        
        