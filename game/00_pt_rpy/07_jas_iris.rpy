label jas_iris_sex:
    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1    # Maslab_BG
    show blkfade with d3
    pause.7
    show iris 86 at right behind blkfade
    hide blkfade with d3
    sch1100 "Oh, hey old man. Thank you for choosing me."
    menu: 
        "\"Yes. You and Jasmine.\"":
            hide iris with d3
            show iris 88 at right with d3
            sch1100 "What? Her?!"
            hide iris with d3
            show iris 89 at right with d3
            sch1100 "Why would you even bother with that frigid witch?"
            hide iris with d3
            show iris 86 at right with d3
            sch1100 "Come on, let's just get to it, you and I - scared, huh?"
            menu:
                "\"I said you and Jasmine, girl!\"":
                    m "I said you and Jasmine, girl!"
                    hide iris with d3
                    show iris 82 at right with d3
                    sch1100 "Well, alright alright..."
                    hide iris with d3
                    show iris 83 at right with d3
                    sch1100 "Hm... Come to think of it..."
                    hide iris with d3
                    show iris 84 at right with d3
                    sch1100 "This could actually turn out to be fun after all..."
                    sch1100 "Wait here, I'll go fetch her!"
                    hide iris with d3
                    m "..................."
                    show emo8 at Position(xpos=700, ypos=100, xanchor=0, yanchor=0) 
                    sch1100 "Ja-a-asmine. Ja-a-asmine, my dear..."
                    hide emo8 with d3
                    show emo8 at Position(xpos=700, ypos=100, xanchor=0, yanchor=0) 
                    j "What is it that you want of me this time?"
                    j "Didn't I tell you not to talk to me??"
                    hide emo8 with d3
                    show emo8 at Position(xpos=700, ypos=100, xanchor=0, yanchor=0) 
                    sch1100 "Oh,  but dear, there is a client here to see you..."
                    hide emo8 with d3
                    show emo8 at Position(xpos=700, ypos=100, xanchor=0, yanchor=0) 
                    j "Why didn't you say so right away? You dim wench..."
                    sch1100 "My bad, my bad..."
                    j "Wait a second... Why are you being weird?"
                    hide emo8 with d3
                    show jas 22 at center with d5
                    j "Oh, it's you..."
                    hide jas with d3
                    show jas 24 at center with d3
                    j "Well, alright then. Follow me."
                    hide jas with d3
                    show jas 22 at left with d3
                    show iris 84 at right with d3
                    sch1100 "..................."
                    hide jas with d3
                    show jas 21 at left with d3
                    j "Wait? Where do you think YOU'RE gong, Iris?"
                    hide iris with d3
                    show iris 84 at right with d3
                    sch1100 "Well, upstairs of course... Didn't I tell you? He wants us both."
                    hide jas with d3
                    show jas 22 at left with d3
                    j "He what..?"
                    j "Oh, no, no, no, no, no... NO! You can't do this to me, old man! Not in front of her!"
                    hide iris with d3
                    show iris 84 at right with d3
                    sch1100 "Good! This is fun already!"
                    hide jas with d3
                    show jas 23 at left with d3
                    j "No, old man, please! I'm begging you!"
                    hide iris with d3
                    show iris 83 at right with d3
                    sch1100 "*Giggle!* You poor, spoiled, little thing..."
                    sch1100 "Don't you know by now?"
                    hide jas with d3
                    show jas 23 at left with d3
                    j "Huh??"
                    hide iris with d3
                    show iris 86 at right with d3
                    sch1100 "Under this roof Client's desire is the law!"
                    hide jas with d3
                    show jas 23 at left with d3
                    j "I know... b-but..."
                    hide iris with d3
                    show iris 89 at right with d3
                    sch1100 "Good! Keep walking then!"
                    hide iris with d5
                    j "........................................."
                    show blkfade with Dissolve(1)
                    show ctc7 at right
                    pause
                    hide ctc7
                    jump iris_jasmine_action
                    
                    
                    
                    
                "\"Er... well, alright. Just you and me then.\"":
                    m "Er... well, alright. Just you and me then."
                    hide iris with d3
                    show iris 84 at right with d3
                    sch1100 "Thank you..."
                    jump dont_show_tits
                "\"I changed my mind.\"":
                    show iris 82 at right with d3
                    sch1100 "...................."
                    show blkfade with d3
                    hide iris with d3
                    pause.7
                    hide blkfade with d3
                    play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
                    jump brothelmain
                
        "\"Iris? Sorry, I meant someone else.\"":
            show iris 82 at right with d3
            sch1100 "...................."
            show blkfade with d3
            hide iris with d3
            pause.7
            hide blkfade with d3
            play music "music/Kabul_Flight_Jumpstart.mp3" fadein 1 fadeout 1 #MAIN_THEME
            jump brothelmain
            
            
#########################################################
label iris_jasmine_action:
    hide jas
    ir[1] "Well, here we are..."
    ir[2] "What will you make us do, I'm wondering?"
    jas[43] "................................."
    menu:
        "\"Iris, I will fuck Jasmine. And you get to watch!\"":
            m "Iris, I will fuck Jasmine. And you get to watch the show!"
            jas[56] "No-o-o.... *scowl*"
            ir[2] "With pleasure!"
            jas[46] "I can't believe you're doing this to me... Not in front of her!"
            jas[47] "Twisted old man... Are you purposefully trying to humiliate me?"
            jas[44] "No, don't answer that..."
            m "..........................................."
            jas[44] "ah.......{image=textheart.png}"
            show image "07_jas_iris/ji01.png" behind blkfade
            play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
            show ctc7 at right
            pause
            hide ctc7
            hide blkfade with d5
            show ctc7 at right
            pause
            hide ctc7
            j "ah...{image=textheart.png} ah...{image=textheart.png} "
            sch1100 "And in it goes!"
            hide image "07_jas_iris/ji02.png" 
            show image "07_jas_iris/ji02.png" with d3
            j "Shut up, Iris!"
            sch1100 "Heh! Fuck her good, old man! Show her who's boss!"
            j "Shut it, I said... stop staring... ah...{image=textheart.png} ah...{image=textheart.png}"
            hide image "07_jas_iris/ji01.png" 
            show image "07_jas_iris/ji01.png" with d3
            with hpunch
            j "Ah...{image=textheart.png} ah...{image=textheart.png} no, not like this... ah...{image=textheart.png} ah...{image=textheart.png}"
            sch1100 "You're already enjoying it, don't you?"
            j "ah...{image=textheart.png} n-no...{image=textheart.png}"
            sch1100 "I know you are secretly taking pleasure in being put on display, you perverted whore!"
            hide image "07_jas_iris/ji02.png" 
            show image "07_jas_iris/ji02.png" with d3
            j "Shut your face, Iris! You know nothing about me! Ah...{image=textheart.png} ah...{image=textheart.png}"
            hide image "07_jas_iris/ji01.png" 
            show image "07_jas_iris/ji01.png" with d3
            j "Ah...{image=textheart.png} it's so big...{image=textheart.png} ah...{image=textheart.png}"
            sch1100 "Just admit it. Admit that you're enjoying this!"
            hide image "07_jas_iris/ji03.png" 
            show image "07_jas_iris/ji03.png" with d3
            j "Never! Ah...{image=textheart.png}"
            sch1100 "Oh, don't be like this! Tell me how much you're enjoying getting fucked right now!"
            sch1100 "Describe to me what his dick feels like in your pussy!"
            hide image "07_jas_iris/ji04.png" 
            show image "07_jas_iris/ji04.png" with d3
            j "Ah...{image=textheart.png} ah...{image=textheart.png} Stop it! Stop saying things like this, you vulgar, uneducated slut!"
            sch1100 "Uneducated slut, am I?"
            sch1100 "What does that make you? An educated one?"
            j "Shut up! Ah...{image=textheart.png} ah...{image=textheart.png} Old, man, tell her to be quiet! She is distracting me!"
            g3 "........................."
            sch1100 "Distracting you from what exactly, you whore?"
            hide image "07_jas_iris/ji02.png" 
            show image "07_jas_iris/ji02.png" with d3
            j "Ah...{image=textheart.png} ah? From doing my job properly, of course!"
            sch1100 "This is just your job then, is it? Well, you are pretty good at it, I must say..."
            sch1100 "Very... believable..."
            j "Of course... I'm a princess. There is nothing I couldn't do... you stupid peasant!"
            sch1100 "Is that so?"
            j "Yes! It is! Ah...{image=textheart.png}"
            hide image "07_jas_iris/ji01.png" 
            show image "07_jas_iris/ji01.png" with d3
            j "Yes...{image=textheart.png} yes...{image=textheart.png} ah...{image=textheart.png}"
            sch1100 "I'm sorry, are you still talking to me or are you saying \"yes\" to him now?"
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            j "I'm going to ignore you from now on! Ah...{image=textheart.png} ah...{image=textheart.png}"
            sch1100 "Suits me well! You fuck that insolent whore, old man, you fuck her good!"
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            hide image "07_jas_iris/ji05.png" 
            show image "07_jas_iris/ji05.png" with d3
            sch1100 "Come on, old man! Pick up the pace! Make her scream!"
            g3 "No problem!"
            j "AH!!!?"
            hide image "07_jas_iris/ji06.png" 
            show image "07_jas_iris/ji06.png" with d3
            with hpunch
            j "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} yes...{image=textheart.png}"
            j "Ah...{image=textheart.png} yes...{image=textheart.png} ah..!{image=textheart.png}"
            sch1100 "Yes, she likes it!"
            hide image "07_jas_iris/ji07.png" 
            show image "07_jas_iris/ji07.png" with d3
            sch1100 "Ah...{image=textheart.png} is it getting hot in here?"
            hide image "07_jas_iris/ji06.png" 
            show image "07_jas_iris/ji06.png" with d3
            sch1100 "You mind if I touch myself a little?"
            g3 "Be my guest."
            hide image "07_jas_iris/ji08.png" 
            show image "07_jas_iris/ji08.png" with d5
            sch1100 "Ah... Yes... Yes... Fuck that little bitch!"
            sch1100 "Yes...{image=textheart.png} she's been bad! Punish her!"
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            hide image "07_jas_iris/ji10.png" 
            show image "07_jas_iris/ji10.png" with d3
            sch1100 "Yes...{image=textheart.png} Ah...{image=textheart.png} {size=-5}(Iris's been bad too...{image=textheart.png} She will punish herself...{image=textheart.png}){/size}"
            sch1100 "Yes...{image=textheart.png} {size=-5}(She will punish her own wet little pussy...{image=textheart.png}){/size}"
            hide image "07_jas_iris/ji11.png" 
            show image "07_jas_iris/ji11.png" with d3
            j "Have you no shame, you harlot! Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            hide image "07_jas_iris/ji09.png" 
            show image "07_jas_iris/ji09.png" with d3
            sch1100 "Ah...{image=textheart.png} Old man, could you make her scream for real?"
            sch1100 "She is so annoying, I would love to see you teach her a lesson!"
            g3 "Well, alright then..."
            hide image "07_jas_iris/ji12.png" 
            show image "07_jas_iris/ji12.png" with d3
            with hpunch
            pause.3
            with hpunch
            pause.3
            with hpunch
            pause.3
            j "Ah...{image=textheart.png} Oh, ahh! No, no, not so rough... ah...{image=textheart.png} ah...{image=textheart.png} ah...!{image=textheart.png}"
            j "Yes! Yes! I'm almost there...{image=textheart.png} almost there...{image=textheart.png}"
            sch1100 "Ah!{image=textheart.png} Yes!{image=textheart.png} Yes!{image=textheart.png} Fuck her!{image=textheart.png} Yes, like this!{image=textheart.png} Give it to her!{image=textheart.png}"                                                 
            j "Ah!{image=textheart.png} Ah!{image=textheart.png} No... I... I'm about to cum, I'm serious!"
            hide image "07_jas_iris/ji13.png" 
            show image "07_jas_iris/ji13.png" with d3
            sch1100 "Wait! What did she just say?!"
            hide image "07_jas_iris/ji14.png" 
            show image "07_jas_iris/ji14.png" with d3
            j "I'm about to...{image=textheart.png} I'm...{image=textheart.png}"
            sch1100 "But he just got started with you! Have you no self-control, girl?"
            j "I'm...{image=textheart.png} I'm sorry...{image=textheart.png} I've been so sensitive lately...{image=textheart.png}"      
            j "I'll try to hold it off!"
            sch1100 "You'd better! It's just so embarrassing to lose it so early."
            j "......................................."
            j "Easy for you to say... ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} Today, I've been picked three times already..."
            j "Ah!{image=textheart.png} No, no, I mustn't think about that!" 
            hide image "07_jas_iris/ji15.png" 
            show image "07_jas_iris/ji15.png" with d3
            sch1100 "Now this is just plain unprofessional! Who cares how many men dipped their cocks in your filthy pussy today?!"
            j "No! No, no, don't say things like that! Ah...{image=textheart.png} it will only make me cum sooner!"
            sch1100 "Ah...{image=textheart.png} what a whore...{image=textheart.png}"
            hide image "07_jas_iris/ji16.png" 
            show image "07_jas_iris/ji16.png" with d3
            sch1100 "Ah...{image=textheart.png} {size=-5}(my pussy is so wet...){/size} ah...{image=textheart.png}"
            j "Oh, by the great desert sands, I'm...{image=textheart.png} I'm almost there...{image=textheart.png} I...{image=textheart.png} can't...{image=textheart.png}"
            sch1100 "Don't you dare, woman, or I'm telling Dahlia on you!"
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            g3 "Yes! Yes! You dirty little sluts!"
            hide image "07_jas_iris/ji14.png" 
            show image "07_jas_iris/ji14.png" with d3
            sch1100 "Old man? Is she pleasuring you good? Are you getting close?"
            g3 "Yeah! I'm almost there, you slut!"
            sch1100 "Maybe there is still hope for you left then, you little whore!"
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} so hard!"
            j "No! I can't hold it any longer!"
            show white 
            pause.1
            hide white
            pause.2            
            show white 
            pause .1
            hide white
            hide image "07_jas_iris/ji17.png" 
            show image "07_jas_iris/ji17.png" with d3
            j "I'm cuuuuumming!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            g3 "Argh!"
            hide image "07_jas_iris/ji18.png" 
            show image "07_jas_iris/ji18.png" with d3
            sch1100 "She's cumming, old man, you made her!"
            sch1100 "Come on, then!! Fill her tiny little cunt with your semen!"
            hide image "07_jas_iris/ji17.png" 
            show image "07_jas_iris/ji17.png" with d3
            sch1100 "{size=-5}(Oh...{image=textheart.png} My pussy...{image=textheart.png} so dripping wet...{image=textheart.png} yes...{image=textheart.png}){/size}"
            hide image "07_jas_iris/ji18.png" 
            show image "07_jas_iris/ji18.png" with d3
            sch1100 "Do it! Do it now! Impregnate her! Ah...{image=textheart.png} yes! Yes! That fucking whore! Show her where she belongs!"
            g3 "{size=+7}ARG! Y-yes!{/size}"
            g3 "{size=+5}Yes! Argh, you whore! Here it comes!{/size}"
            show white 
            pause.2
            hide white
            pause.3
            show white 
            pause .1
            hide white
            hide image "07_jas_iris/ji19.png" 
            show image "07_jas_iris/ji19.png" with d3
            with hpunch 
            show ctc7 at right
            pause
            hide ctc7
            g3 "Take it, you slut, take it right up your pussy!"
            hide image "07_jas_iris/ji20.png" 
            show image "07_jas_iris/ji20.png" with d3
            sch1100 "Yes! Fill her up! Fill her up more!"
            j "{size=+5}AAAAAhhhh!{/size}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            g3 "{size=+9}Y-yes! Argh!!!{/size}"
            with hpunch
            hide image "07_jas_iris/ji21.png" 
            show image "07_jas_iris/ji21.png" with d3
            j "ah...{image=textheart.png} I'm cumming...{image=textheart.png} again...{image=textheart.png} You bastard! Ah...{image=textheart.png}"
            sch1100 "What a nasty whore!"
            g3 "{size=+5}Oh... Yes...{/size}"
            j "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} *panting*"
            hide image "07_jas_iris/ji22.png" 
            show image "07_jas_iris/ji22.png" with Dissolve(1)
            show ctc7 at right
            pause
            hide ctc7
            show blkfade with Dissolve(3)
            show ctc7 at right
            pause
            hide ctc7


          



        "\"Now, Iris, you be nice to Jasmine!\"":
            m "Now, Iris, you be nice to Jasmine!"
            ir[5] "What? Really?"
            jas[46] "Client's desire is the law, you harlot!"
            ir[8] "Shut your face, you spoiled--"
            m "Iris!"
            ir[9] "Alright, alright..."
            ir[9] "........................"
            ir[9] "So, Slut-- Khem, er..... Jasmine..."
            ir[9] "Let me help with your clothes..."
            jas[50] "This is not a proper way to address me..."
            ir[8] "Excuse me?"
            jas[50] "You should say \"May I help you with your gowns, my lady?\""
            ir[8] "Why, you little--"
            g4 "Iris!!"
            ir[9] "........................."
            ir[9] "Jasmine, dear... May I help you with your gowns... my lady?"
            jas[59] "You most certainly may... {w}whore."
            ir[8] "............."
            ir[9] "............................"
            jas[59] "Yes, now my pants..."
            ir[9] "..............."
            ">Iris helps jasmine to undress."
            jas[50] "Alright, old man, I am ready, let us begin..."
            play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
            jas[51] "AH!?! Y-yes...{image=textheart.png}"
            ir[9] "......................"
            
            
            hide image "07_jas_iris/ji23.png" 
            show image "07_jas_iris/ji23.png" behind blkfade
            show ctc7 at right
            pause
            hide ctc7
            hide blkfade with Dissolve(2)
            show ctc7 at right
            pause
            hide ctc7
            j "ah...{image=textheart.png} ah...{image=textheart.png} "
            sch1100 "Em... Does it feel... pleasant, my lady?"
            hide image "07_jas_iris/ji24.png" 
            show image "07_jas_iris/ji24.png" with d3
            j "Tsk, what do you think, you dummy?"
            sch1100 "Well, I..."
            j "Shut it, girl. I don't care ah...{image=textheart.png} ah...{image=textheart.png}"
            hide image "07_jas_iris/ji23.png" 
            show image "07_jas_iris/ji23.png" with d3
            j "Ah...{image=textheart.png} ah...{image=textheart.png} yes like this...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            sch1100 "..................................."
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            sch1100 "........................"
            hide image "07_jas_iris/ji24.png" 
            show image "07_jas_iris/ji24.png" with d3
            j "Ah...{image=textheart.png} ah...{image=textheart.png} Why so shy suddenly? Say something nice to me, quick!"
            hide image "07_jas_iris/ji25.png" 
            show image "07_jas_iris/ji25.png" with d3
            sch1100 "Tsk..."
            sch1100 "Em... You have an exquisitely beautiful body... my lady"
            j "ah... {image=textheart.png} yes, that I know... It's only why clients so overwhelmingly choose me over you..."
            sch1100 "..............................."
            j "You scarred mess!"
            $ renpy.play('sounds/spit.mp3') 
            show white 
            pause.4
            hide image "07_jas_iris/ji26.png" 
            show image "07_jas_iris/ji26.png" behind white
            hide white
            show ctc7 at right
            pause
            hide ctc7
            show white with d5
            hide image "07_jas_iris/ji27.png" 
            show image "07_jas_iris/ji27.png" behind white
            pause.2
            hide white with d5
            show ctc7 at right
            pause
            hide ctc7
            sch1100 "..................."
            j "..................................."
            hide image "07_jas_iris/ji28.png" 
            show image "07_jas_iris/ji28.png" with d3
            with hpunch
            j "{size=+5}AH!!!!!! HOW DARE YOU?! Y-YOU B-BITCH!{/size}"
            hide image "07_jas_iris/ji29.png" 
            show image "07_jas_iris/ji29.png" with d3
            j "Old man, did you see what she did there? She spat in my face!"
            g3 "Rightfully so, I must say. You crossed the line, girl..."
            j "I crossed the line? Have you lost your wits completely, old fool?"
            j "The wench spat in my face!!!"
            g3 "{size=+5}I said, you took it too far, woman.{/size}"
            g3 "{size=+5}Apologize, now!{/size}"
            hide image "07_jas_iris/ji30.png" 
            show image "07_jas_iris/ji30.png" with d3
            j "A-apologize?! You can't possibly... ah...{image=textheart.png}"
            sch1100 "..............."
            hide image "07_jas_iris/ji31.png" 
            show image "07_jas_iris/ji31.png" with d3
            sch1100 "Yes, apologize to me, while you are being fucked, my lady."
            hide image "07_jas_iris/ji32.png" 
            show image "07_jas_iris/ji32.png" with d3
            j "This is... this is just unheard of!"
            g3 "Jasmine, you will apologize now, or I'm throwing you out of this room and carry on comforting Iris."
            g3 "Right? You would like that, right, Iris?"
            hide image "07_jas_iris/ji33.png" 
            show image "07_jas_iris/ji33.png" with d3
            sch1100 "Yes...{image=textheart.png} I feel so upset...{image=textheart.png}"
            sch1100 "I need a shoulder to cry on...{image=textheart.png}"
            hide image "07_jas_iris/ji34.png" 
            show image "07_jas_iris/ji34.png" with d3
            sch1100 "And a hard cock to play with...{image=textheart.png}"
            g3 "*chuckle* You little witch..."
            j "Unbelievable..."
            g3 "Well, Jasmine, I'm patiently waiting..."
            sch1100 "Yes, Jasmine, we are waiting! {size=-4}(Ah, my pussy feels so good...{image=textheart.png}){/size}"
            j "I got spit in my face and now I have to apologize? This is simply ludicrous!... Ah...{image=textheart.png}"
            hide image "07_jas_iris/ji35.png" 
            show image "07_jas_iris/ji35.png" with d3
            j "Could you at least stop it with your accursed cock for a moment? ah...{image=textheart.png} ah...{image=textheart.png}"
            g3 "Nope! If anything, I'm pickig up pace!"
            j "W-what?!"
            hide image "07_jas_iris/ji36.png" 
            show image "07_jas_iris/ji36.png" with d3
            with hpunch
            j "No! Ahhhh!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            g3 "Now - apologize!"
            sch1100 "I'm waiting!"
            with hpunch
            pause.3
            with hpunch
            pause.3
            with hpunch
            pause.3
            j "ah....{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            with hpunch
            pause.3
            with hpunch
            pause.3
            with hpunch
            pause.3
            j "ah....{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            with hpunch
            pause.3
            with hpunch
            pause.3
            with hpunch
            pause.3
            j "Ah...{image=textheart.png} Ah...{image=textheart.png} ah...{image=textheart.png}      {size=-5}I'm sorry...{/size}"
            sch1100 "Couldn't hear you!"
            j "I said, I'm sorry! AH!{image=textheart.png} Old, man your cock!"
            sch1100 "Ha-ha-ha. Silly whore! Apology accepted!"
            with hpunch
            pause.3
            with hpunch
            pause.3
            with hpunch
            pause.3
            j "Ah...{image=textheart.png} Oh, ahh!{image=textheart.png} No, no, not so rough... ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}!"
            j "Yes! Yes! I'm almost there...{image=textheart.png} almost there...{image=textheart.png}"
            sch1100 "Ah!{image=textheart.png} Yes! Yes! Fuck her! Yes!{image=textheart.png}"  
            sch1100 "That whore... er... I mean, nice respectable lady..."
            sch1100 "{size=-4}(Look at him go... I wish it was me in her place... ah...{image=textheart.png}){/size}"
            hide image "07_jas_iris/ji37.png" 
            show image "07_jas_iris/ji37.png" with d3
            j "Ah...{image=textheart.png}{image=textheart.png}{image=textheart.png} I think, I'm about to cum...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            hide image "07_jas_iris/ji38.png" 
            show image "07_jas_iris/ji38.png" with d3
            sch1100 "Wait! What did she just say?!"
            j "Ah!{image=textheart.png} Ah!{image=textheart.png} No... I... I'm about to cum, I'm serious!"
            j "I'm about to...{image=textheart.png} I'm...{image=textheart.png}"
            hide image "07_jas_iris/ji39.png" 
            show image "07_jas_iris/ji39.png" with d3
            sch1100 "But he just got started with you! Have you no self-control, woman? {size=-4}(She is coming? Already? Can he really be that good?){/size}"
            j "I'm...{image=textheart.png} I'm sorry...{image=textheart.png} I've been so sensitive lately...{image=textheart.png}"      
            j "I'll try to hold it!"
            sch1100 "You're damn right you'll try to hold it! I mean, please, be so kind and hold your freaking orgasm!{size=-4}(Ah...{image=textheart.png} I want to cum too...){/size}"
            j "......................................."
            j "Easy for you to say... ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} Today, I've been picked three times already..."
            j "Ah! Already?! No, no, I mustn't think about it!{image=textheart.png}" 
            sch1100 "Now, this is just plain unprofessional! Who cares how many times men dipped their cocks in your pussy today?!"
            sch1100 "I mean... er..."
            sch1100 "Nope, there is no way I could sugarcoat this one! You are a nasty whore!"
            j "No! No, no, don't say things like that! Ah...{image=textheart.png} it will only make me cum sooner!"
            j "Oh, by the great desert sands, I'm... I'm almost there...{image=textheart.png} I...{image=textheart.png} can't...{image=textheart.png}"
            sch1100 "Don't you dare, woman! I will tell Dahlia everything!\n{size=-4}(What a whore...{image=textheart.png} I wish I could cum that quick...{image=textheart.png}){/size}"
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            g3 "Yes! Yes! You dirty little sluts! Both of you!"
            sch1100 "Old man? Are you getting close?"
            sch1100 "Maybe there is still hope left for you then, you little slut!"
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} so hard!"
            j "No! I can't hold it any longer!"
            j "{size=+5}I'm cuuuuumming!{/size}"
            show white 
            pause.1
            hide white
            pause.2            
            show white 
            pause .1
            hide white
            hide image "07_jas_iris/ji17.png" 
            show image "07_jas_iris/ji17.png" with d3
            j ".............................."
            g3 "{size=+5}Argh!{/size}"
            sch1100 "She's cumming, old man! Come on! Fill her tiny little cunt with your semen!"
            
            hide image "07_jas_iris/ji18.png" 
            show image "07_jas_iris/ji18.png" with d3
            sch1100 "Do it! Do it now! Impregnate her! Ah...{image=textheart.png} yes!{image=textheart.png} Yes!{image=textheart.png} That fucking whore! Show Jasmine her place!"
            sch1100 "{size=-4}(Oh...{image=textheart.png} My pussy...{image=textheart.png} so dripping wet...{image=textheart.png} yes...{image=textheart.png}){/size}"
            g3 "{size=+7}ARGH! Y-yes!{/size}"
            g3 "{size=+5}Yes! Argh, you whore! Here it comes!{/size}"
            show white 
            pause.2
            hide white
            pause.3
            show white 
            pause .1
            hide white
            hide image "07_jas_iris/ji19.png" 
            show image "07_jas_iris/ji19.png" with d3
            with hpunch 
            show ctc7 at right
            pause
            hide ctc7
            g3 "Take it, you slut! Right up your fucking pussy!"
            hide image "07_jas_iris/ji20.png" 
            show image "07_jas_iris/ji20.png" with d3
            sch1100 "Yes! Fill her up! Fill her up!"
            j "{size=+5}AAAAAhhhh!{image=textheart.png}{image=textheart.png}{image=textheart.png}{/size}"
            g3 "{size=+9}Y-yes! Argh!!!{/size}"
            with hpunch
            hide image "07_jas_iris/ji21.png" 
            show image "07_jas_iris/ji21.png" with d3
            j "ah...{image=textheart.png} I'm cumming...{image=textheart.png} again...{image=textheart.png} You bastard! Ah...{image=textheart.png}"
            sch1100 "Nasty whore!"
            g3 "Oh... Yes..."
            j "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} *panting*"
            hide image "07_jas_iris/ji22.png" 
            show image "07_jas_iris/ji22.png" with Dissolve(1)
            show ctc7 at right
            pause
            hide ctc7
            show blkfade with Dissolve(3)
            show ctc7 at right
            pause
            hide ctc7

        "\"Iris, be mean to Jasmine!\"":
            m "Iris, be mean to Jasmine!"
            ir[4] "My pleasure!"
            jas[46] "What?"
            ir[8] "Shut up, whore!"
            play music "music/TheEasternWindbyroensb.mp3" fadein 1 fadeout 1 #SEX
            ir[8] "Come here!"
            jas[49] "What are you doing! Let go of me!!!"
            ">Iris grabs Jasmine's bosom veil and forcefully rips it off."
            jas[49] "What are you doing, you rabid whore!"
            ir[8] "Now your pants! You are not gonna need them..."
            jas[47] "Don't touch me, you--"
            ir[8] "There! Now, on all fours!"
            jas[57] "Stop this! Stop it!"
            ir[8] "Go down, I said!"
            ir[4] "She is ready, old man!"
            m "Good, job, Iris!"
            jas[57] "No, wait, not--"
            jas[51] "Ah...."
            ir[4] "Heh... let the fun begin!"
            jas[51] "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            hide image "07_jas_iris/ji25.png" 
            show image "07_jas_iris/ji25.png" behind blkfade
            show ctc7 at right
            pause
            hide ctc7
            hide blkfade with Dissolve(2)
            show ctc7 at right
            pause
            hide ctc7
            ir[8] "How do you like it, you little spoiled princess?! Are you enjoying this!"
            j "ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png}"
            sch1100 "Talk to me!"
            j "........................."
            sch1100 "I said - talk to me!"
            show ctc7 at right
            pause
            hide ctc7
            hide image "07_jas_iris/ji40.png" 
            show image "07_jas_iris/ji40.png" with d3
            show ctc7 at right
            pause
            hide ctc7
            j "Ah! Let go of my breasts, you dirty peasant!"
            sch1100 "I asked you a question, you pretentious slut!"
            j "Ouch! It hurts!"
            sch1100 "I'm gonna keep pulling on your nipple until you answer my question, or until I rip it off! Whichever comes first I'll welcome it the same!"
            hide image "07_jas_iris/ji41.png" 
            show image "07_jas_iris/ji41.png" with d3
            j "Ah! No! It hurts! Stop! Ah,{image=textheart.png} no, my pussy... Your dick is so hard! Ah, my nipple!"
            hide image "07_jas_iris/ji42.png" 
            show image "07_jas_iris/ji42.png" with d3
            sch1100 "Answer me!"
            j "!!!!!!!!!!!"
            hide image "07_jas_iris/ji43.png" 
            show image "07_jas_iris/ji43.png" with d3
            j "Curse you, you irritating eyesore! Ah! What was--{w} ...ah, it hurts! What was the question?!"
            hide image "07_jas_iris/ji44.png" 
            show image "07_jas_iris/ji44.png" with d3
            sch1100 "The question was... er..."
            sch1100 "Oh, I don't remember anymore..."
            j "Stop pulling on my breast then, you're going to stretch it out!"
            hide image "07_jas_iris/ji43.png" 
            show image "07_jas_iris/ji43.png" with d3
            sch1100 "Shut up, you whore! I'm gonna keep pulling on it for as long as I want...!"
            j "I hate you, you nasty, vulgar woman!"
            hide image "07_jas_iris/ji42.png" 
            show image "07_jas_iris/ji42.png" with d3
            j "Ah, this feels so good!"
            sch1100 "I knew it! You like it when people hurt you! You masochistic bitch!"
            hide image "07_jas_iris/ji43.png" 
            show image "07_jas_iris/ji43.png" with d3
            j "No, I don't ah...{image=textheart.png}"
            j "I was talking about his dick, you ugly, ugly...{w} ugliness!"
            sch1100 "Was it the best you were able to come up with? Where did your so-called education suddenly go?!"
            hide image "07_jas_iris/ji42.png" 
            show image "07_jas_iris/ji42.png" with d3
            j "Ah, stop it! Stop pulling on my nipple like that, I'm begging you!"
            sch1100 "Say: \"I'm a nasty whore!\". And I'll let go..."
            hide image "07_jas_iris/ji43.png" 
            show image "07_jas_iris/ji43.png" with d3
            j "You're a nasty whore! Now let go!"
            hide image "07_jas_iris/ji44.png" 
            show image "07_jas_iris/ji44.png" with d3
            sch1100 "No, wait... what?"
            hide image "07_jas_iris/ji43.png" 
            show image "07_jas_iris/ji43.png" with d3
            sch1100 "Are you being smart with me??"
            hide image "07_jas_iris/ji42.png" 
            show image "07_jas_iris/ji42.png" with d3
            j "Ah! My nipple! You're going to wreck my breast, you brutish mockery of a woman!"
            sch1100 "You.... you know what? You're really starting to piss me off!"
            show ctc7 at right
            pause
            hide ctc7
            hide image "07_jas_iris/ji45.png" 
            show image "07_jas_iris/ji45.png" with d3
            show ctc7 at right
            pause
            hide ctc7
            j "Ngh!!!!!!!!!!!!!!"
            j "What are you doing?!!!!"
            sch1100 "Are you dumb? What does it look like I'm doing?!"
            j "I...{w} Can't...{w} breathe..."
            hide image "07_jas_iris/ji46.png" 
            show image "07_jas_iris/ji46.png" with d3
            g3 "Iris, careful now..."
            sch1100 "Old man, you just keep doing your thing, alright? Don't worry, I know how to choke people..."
            g3 "Yes. And that's exactly what's bothering me..."
            sch1100 "She will be just fine, trust me..."
            hide image "07_jas_iris/ji47.png" 
            show image "07_jas_iris/ji47.png" with d3
            j "Ah...{image=textheart.png} ah...{image=textheart.png} ah...{image=textheart.png} I'm....{image=textheart.png} about to cum...{image=textheart.png}"
            sch1100 "You see? She is about to cum already..."
            hide image "07_jas_iris/ji48.png" 
            show image "07_jas_iris/ji48.png" with d3
            sch1100 "Wait, what?!"
            hide image "07_jas_iris/ji49.png" 
            show image "07_jas_iris/ji49.png" with d3
            j "I'm...{image=textheart.png} I'm....{image=textheart.png} almost... *gasp!* I can't..."
            sch1100 "Oh, I see... You are one of those..."
            sch1100 "Dahlia told me that some women enjoy being choked!"
            j "I c-can't breathe..."
            sch1100 "So you are one of those weirdos?"
            hide image "07_jas_iris/ji51.png" 
            show image "07_jas_iris/ji51.png" with fade   
            sch1100 "You disgust me, you slut!"
            j "......................"
            show ctc7 at right
            pause
            hide ctc7
            $ renpy.play('sounds/spit.mp3') 
            pause.3
            hide image "07_jas_iris/ji52.png" 
            show image "07_jas_iris/ji52.png" 
            with hpunch
            show ctc7 at right
            pause
            hide ctc7
            show white 
            pause.1
            hide white
            pause.2
            show white 
            pause.1
            hide image "07_jas_iris/ji53.png" 
            show image "07_jas_iris/ji53.png" behind white
            hide white
            show ctc7 at right
            pause
            hide ctc7
            j "I'm cumming...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            sch1100 "Oh, you are just beyond contempt, you perverted, nasty harlot!"
            hide image "07_jas_iris/ji54.png" 
            show image "07_jas_iris/ji54.png" with d3
            with hpunch
            g3 "{size=+7}Argh!{/size}"
            sch1100 "Yeah! You go ahead old man! Cum inside that nasty slut!"
            j "*Gasp!* {w}I *Gasp!*{w} Can't *gasp!*{w} breathe *gasp!*"
            sch1100 "Doesn't stop you from cumming, now does it?!"
            j "*gasp!*{w} I'm cumming...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            with hpunch
            g3 "{size=+5}ARGH! Y-yes! Here it comes!{/size}"
            j "*GASP!*"
            show white 
            pause.2
            hide white
            pause.3
            show white 
            pause .1
            hide white
            hide image "07_jas_iris/ji55.png" 
            show image "07_jas_iris/ji55.png"
            with hpunch 
            show ctc7 at right
            pause
            hide ctc7
            sch1100 "Cum, whore! Keep cumming like crazy, while I'm choking you!"
            j "{size=+9}*GASP!*{/size}"
            g3 "{size=+9}Yes! Yes! Argh!{/size}"
            with hpunch
            sch1100 "{size=+7}Nasty whore!!!{/size}"
            j ".....................*gasp--"
            show ctc7 at right
            pause
            hide ctc7
            show blkfade with Dissolve(1)
            $ renpy.play('sounds/fall.wav') 
            show ctc7 at right
            pause
            hide ctc7
            ">Jasmine loses consciousness and collapses to the floor."
            with hpunch
            g4 "{size=+7}Goddamit! Iris!!!!!!!{/size}"
            ir[2] "Relax, she's breathing, she will be alright..."
            ir[4] "This was quite intense though, huh?"
            m "Yeah..."
            ir[4] "So, are you ready to go another round?"
            ir[7] "With me this time?"
            g4 "Wait, gimme a minute or two to catch my breath, you crazy little witch." 
            ir[6] "Hehe... let me show you a trick I know first..."
            sch1100 "*SLURP!*"
            m "Oh, not bad..."
            ir[6] "Yeah, Dahlia taught me this."
            ir[6] "It should help you recover faster!"
            sch1100 "*Slurp!* *Slurp!* *Gubble!*"
            show ctc7 at right
            pause
            hide ctc7
            

    
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