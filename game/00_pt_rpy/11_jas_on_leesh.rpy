label jas_on_a_leesh:
    show image "04_pt/jasmine/outfit/jas12.png" at right with d5
    show ctc7 at right
    pause 
    hide ctc7
    j "................."
    label where_to_go:
    j "So where are we going..... master?"
    menu:
        m "Hm..."
        "-The Market square-":
            j "The market square is full of people at this time of day..."
            j "................."
            j "Everyone will see me in this... outfit..."
            j "Maybe we could go somewhere less crowded, master?"
            menu:
                m "Hm..."
                "\"Well, alright...\"":
                    m "Well, alright, I'll take you somewhere else..."
                    j "Thank you... master."
                    jump where_to_go
                "\"I said, Market Square, let's go!\"":
                    m "I said, Market Square, let's go!"
                    j ".........................."
                    j "Y-yes, master, as you wish..."
                    hide image "04_pt/jasmine/outfit/jas12.png" at right with d5
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                    ">You take Jasmine to the market square."
                    play music "music/Marketplace(short).mp3" fadein 1 fadeout 1 #MARKET
                    hide rest03 with Dissolve(.3)
                    show leash with Dissolve(.3)
                    ".........."
                    #show image im.Alpha("interface/blackfade.png", 0.8) with Dissolve(.9)
                    pause.3
                    ">You take a slow walk through the market square."
                    ">Jasmine is following you on a leash."
                    ">As expected the square is very crowded. People are going about their business in all directions."
                    ">Jasmine's outfit is very revealing, but nobody is paying her much mind."
                    ">People around you seem to be very busy participating in all sort of trade and commerce taking place everywhere the eye can see."
                    ">A slave-girl being lead on a leash to be sold, or after just being bought is nothing new here."
                    ">A group of ragged street urchins are starting to follow you."
                    show image im.Alpha("interface/blackfade.png", 0.8) with Dissolve(.9)
                    ">You double check your purse but it looks like they are here just for entertainment..."
                    ">One of them points at Jasmine and says something to his buddies. The boys start laughing loudly."
                    ">Jasmine gives them a look of indignation."
                    ">One of the boys runs towards you..."
                    urc "Hey, mister! Your slave-girl is pretty!"
                    urc "Can I touch her? Please? Please?"
                    ">Jasmine glances at you in bewilderment."
                    menu:
                        m "Hm..."
                        "\"Out of my way, kid!\"":
                            m "Out of my way, kid!"
                            urc "Tsk! Greedy old man!"
                            g4 "Out of my way I said!"
                            ">You chase away the urchins..."
                            ">Jasmine gives you another glance. She seems to be thankful..."
                            ">You walk the rest of the way to your house without any incidents..."
                        "\"Sure! Jasmine, go on your knees.\"":
                            m "Sure! Jasmine, go on your knees."
                            jas[66] "You... can't be serious..."
                            m "I am. On your knees, girl."
                            ">Jasmine hesitates for a moment but then goes down on one knee."
                            jas[66] "....................."
                            m "Well, go on, kid."
                            urc "Really? Awesome!!!"
                            ">The boy approaches Jasmine gingerly. All his courage is suddenly gone."
                            ">You see his friends watching him with wide eyes from afar."
                            urc "Hello..."
                            jas[66] "Hello, child..."
                            urc "C-can I..."
                            urc "T-touch your tit, lady... p-please?"
                            jas[66] "Have you ever touched a woman before..."
                            urc "No m'am..."
                            jas[66] "................"
                            jas[66] "You seem like a very well mannered boy for a street kid."
                            jas[66] "Well, alright, you can touch me..."
                            ">The boy holds his breath and reaches towards Jasmine's breasts with one hand..."
                            ">He puts his open palm on one of your slave-girl's tits..."
                            urc "Wow... It's so... soft..."
                            ">He jerks the hand away as if expecting to be scolded but Jasmine just keeps looking at him calmly..."
                            urc "Thank you, m'am..."
                            jas[66] "Is this all? Don't you want to try to pull on my nipple as well?"
                            urc "C-can I?"
                            jas[66] "Go ahead, but be gentle..."
                            urc "*GULP!*"
                            ">The kid reaches out with his arm again and grabs one of Jasmine's nipples gingerly..."
                            jas[66] "Ah...{image=textheart.png}"
                            ">He jerks his hand away not sure about Jasmine's reaction..."
                            ">But the princess just keeps looking at him warmly..."
                            urc "T-thank you, lady..."
                            jas[66] "You are welcome."
                            jas[66] "You'll be a real hero among you friends now, won't you?"
                            urc "You bet!"
                            urc "Em... can I ask a question?"
                            jas[66] "Go ahead..."
                            urc "Aren't you embarrassed walking around like this... m'am?"
                            jas[66] "I am very embarrassed, but I must do whatever my master tells me."
                            urc "Awesome! When I grow up I wanna buy myself a slave-girl just like you!"
                            m "Alright, kid, off you go now. Jasmine, get up."
                            jas[66] "Yes, master..."
                            urc "Thank you for letting me touch your slave-girl, mister!"
                            ">The kid runs off gesturing to his friends frantically..."
                            jas[66] "....................."
                            jas[66] "I always felt bad about the underprivileged kids of Agrabah..."
                            jas[66] "*sigh*"
                            jas[66] "Thank you for letting me bring a little joy into this little kid's life..."
                            m "Yeah, sure... Keep walking..."
                            jas[66] "Ah...{image=textheart.png}"
                            ">You walk the rest of the way to your house without any incidents..."
                            play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1  #NIGHT
                            
                    
                    
                    show image "04_pt/slavem/night.jpg" with fade                               
                    hide leash
                    ">It's evening and Princess Jasmine returns from performing your personal request."
                    show image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)                                     
                    ">Jasmine is very tired and feels embarrassed when thinking about her walk through the market square today..."
                    ">Jasmine feels relieved that nobody recognized her today, but she also feels a little disappointed..."
                    $ tired +=2     
                    $ jpslave = False
                    hide image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)
                    return

        "-The Palace vicinity-":
            j "The palace...?"
            j "A lot of nobles and rich merchants live in the houses surrounding the area..."
            j "Some of them know me personally..."
            j "Maybe we could go somewhere else, master?"
            menu:
                m "Hm..."
                "\"Well, alright...\"":
                    m "Well, alright, I'll take you somewhere else..."
                    j "Thank you... master."
                    jump where_to_go
                "\"I said, The Palace district, let's go!\"":
                    m "I said, The Palace district, let's go!"
                    j ".........................."
                    j "Y-yes, master, as you wish..."
                    hide image "04_pt/jasmine/outfit/jas12.png" at right with d5
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                    ">You start walking towards the palace."
                    hide rest03 with Dissolve(.3)
                    show leash with Dissolve(.3)
                    play music "music/JafarsHour.mp3" fadein 1 fadeout 1 #JAFAR
                    ".........."
                    #show image im.Alpha("interface/blackfade.png", 0.8) with Dissolve(.9)
                    pause.3
                    ">The palace district is mostly populated by Agrabah's Upper Class."
                    ">You lead jasmine among clean and well kept houses..."
                    ">A couple of city-guards pass by. Both of them seem to recognize your slave-girl, but they keep their composure."
                    ">Jasmine turns away from them while blushing."
                    ">You take Jasmine to the little square in front of the palace gates."
                    ">A small crowd is starting to gather around you. Mostly local noblemen."
                    ">Some of them try to greet Jasmine properly, others just stare at you in bewilderment..."
                    ">You wait a little longer. Spectators keep arriving..."
                    show image im.Alpha("interface/blackfade.png", 0.8) with Dissolve(.9)
                    m "Alright, girl. Now, address your people..."
                    jas[66] "What? B-but... what am I supposed to say?"
                    m "You will repeat after me..."
                    jas[66] "Em... Ok..."
                    m "(People of agrabah...)"
                    jas[66] "People of agrabah..."
                    m "(Do you now who I am?)"
                    jas[66] "Do you... Know who I am...?"
                    ">A light murmur goes through the crowd..."
                    m "(I'm Princess Jasmine!)"
                    jas[66] "I am...{w}...{w}...princess {size=-5}Jasmine...{/size}"
                    m "(Please, take a better look at my luscious body!)"
                    jas[66] "P-please, take a look at my... body."
                    ">You see some of the men chuckle, others sneer and some give you a stink-eye."
                    m "(If you like what you see, please visit \"The Red Phoenix\" brothel, where I work as a whore now!)"
                    jas[66] "If you like what you see, please visit \"The Red Phoenix\" brothel, where I work..."
                    ">Another, much louder murmur goes through the crowd..."
                    m "(Bring enough gold with you and I will gladly spread my legs for you!)"
                    jas[66] "......................"
                    jas[66] "B-bring enough money and I will... em... do my best to please you."
                    m "(If you want a sample, feel free to approach and touch me.)"
                    jas[66] "If you want a sample feel free to {size=-6}touch me...{/size}"
                    ">You see a dozen or so of men turn around and walk away. But the majority is looking at Jasmine with interest."
                    ">A couple of noblemen approach jasmine..."
                    nob "Princess, is this really you?"
                    jas[66] "Y-yes..."
                    nob "Oh... I used to know you when you were little..."
                    nob "Look at you, all grown up now..."
                    ">The nobleman gives one of Jasmine's tits a good squeeze..."
                    nob "Not bad... Not bad..."
                    nob "So, \"Red Phoenix\" huh?"
                    jas[66] "Y-yes..."
                    jas[66] "P-please... {w}come pay me a visit..."
                    nob "Well, I'll definitely come by..."
                    nob "Little Jasmine turned whore, who would have thought..."
                    jas[66] ".............."
                    ">Another couple of men approache Jasmine..."
                    ">They exchange remarks among themselves and then talk to Jasmine..."
                    ">Most of them seem to know her..."
                    ">A tight circle of men with hungry eyes forms around your slave-girl..."
                    ">Dozens of hands reach out and grab her at random..."
                    ">Some grab her tits, others seem to be more interested in Jasmine's behind."
                    ">The situation escalates quickly... Two different men pull on jasmine's tits in opposite directions, someone gives her butt a loud slap..."
                    jas[66] "Ah...{image=textheart.png}"
                    ">You decide that that's enough for today..."
                    ">You loudly announce that Jasmine has to go now."
                    ">The men look at you with wide eyes... It seems they completely forgot about your presence..."
                    ">You lead Jasmine away from the horny mob..."
                    ">Jasmine is breathing heavily..."
                    ">You walk rest of the way to your house without an incident..."
                    play music "music/Sleep_Walking_by_hektikmusic.mp3" fadein 1 fadeout 1  #NIGHT
  
                    show image "04_pt/slavem/night.jpg" with fade                               
                    hide leash
                    ">It's evening and Princess Jasmine returns from performing your personal request."
                    show image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)                                     
                    ">Jasmine is very tired and feels very embarrassed thinking about today's activities..."
                    ">A few dozen of people saw her today, and most of them not only recognized her but also knew her back when she was still in power..."
                    ">Despite an overwhelming feeling of embarrassment Jasmine feels an odd sort satisfaction..."
                    ">Today Jasmine's reputation suffered a truly devastating blow."
                    $ tired +=2     
                    $ pthink +=12 
                    $ jpslave = False
                    hide image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)
                    return
            
            
            
            
            
         
            
        "-The Cheapside-":
            j "The chapside...?"
            j "The place is full of drunkards and homeless deadbeats..."
            j "Could we go somewhere... cleaner, master?"
            menu:
                m "Hm..."
                "\"Well, alright...\"":
                    m "Well, alright, I'll take you somewhere else..."
                    j "Thank you... master."
                    jump where_to_go
                "\"I said, The Cheapside district, let's go!\"":
                    m "I said, The Cheapside district, let's go!"
                    j ".........................."
                    j "Y-yes, master, as you wish..."
                    hide image "04_pt/jasmine/outfit/jas12.png" at right with d5
                    hide image "04_pt/slavem/bld.png" with Dissolve(.3) 
                    ">You start walking towards the cheapside."
                    hide rest03 with Dissolve(.3)
                    show leash with Dissolve(.3)
                    ".........."
                    #show image im.Alpha("interface/blackfade.png", 0.8) with Dissolve(.9)
                    pause.3
                    ">The Chapside is largely populated by Agrabah's Lower Class."
                    ">You lead jasmine among the dirty streets..."
                    ">The air in this area is stale and filled with all sorts of stmells..."
                    ">Jasmine wrinkles her nose as she jumps over puddles of waste..."
                    show image im.Alpha("interface/blackfade.png", 0.8) with Dissolve(.9)
                    sch7 "Coin for the poor?"
                    sch7 "Oh, but what is this? What a sight for these sore eyes..."
                    jas[66] "..................."
                    m "Hello, old crow."
                    m "I'm here to thank you for your services..."
                    sch8 "Are you really, master? You're too kind..."
                    sch8 "Crocus is unworthy..."
                    m "Yes, yes, I know..."
                    m "Listen, could do me a favor and gather a little crowd for me?"
                    m "My slave-girl prepared a little number for everyone."
                    sch7 "Did she now?"
                    jas[66] "What? What are you talking about?"
                    sch8 "Just give Crocus a minute, kind master."
                    ">With surprising agility crocus shuffles away towards a nearby alley..."
                    jas[66] "What, are you doing? What is this?"
                    m "Relax, I just want you to dance for them, that's all."
                    jas[66] "D-dance? Here? For these dirty peasants and deadbeats?"
                    jas[66] "You must be joking..."
                    m "I am not. You {size=+5}are{/size} gonna dance for them..."
                    jas[66] "............."
                    ">Crocus reappears leading a small group of dirty ragged men of all ages..."
                    ">A couple dozen pour out from another dirty alley nearby..."
                    ">The men surround you and your slave-girl..."
                    ">They don't look dangerous and keep staring at you with caution..."
                    show image im.Alpha("interface/blackfade.png", 0.8) with Dissolve(.9)
                    m "Well, go ahead..."
                    jas[66] "W-what?"
                    m "I said: dance!"
                    jas[66] "..............."
                    ">Jasmine is hesitating..."
                    ">She makes an awkward gesture, then another one..."
                    ">Some of the beggars flinch away from her sudden movements..."
                    ">But then an understanding shows on their faces..."
                    ">Jasmine picks up the pace. She keeps her eyes closed for the most part..."
                    ">She is really dancing now..."
                    ">The ground is covered with mud, but it seems like the slave-girl doesn't care about that anymore..."
                    ">The men are starting to smile and look at her with hunger..."
                    ">You see that Jasmine is dancing with her eyes open now..."
                    ">She does a few awkward movements as always to make sure her tits bounce and jiggle enough..."
                    ">Some of the beggars start to cheer."
                    sch8 "What a feast! What a feast! Shake your tits girl! Shake them!"
                    sch8 "Now bend over! Yes! Yes!"
                    sch8 "Crocus will die a happy man!"
                    ">a Light smile touches Jasmine's lips as she keeps dancing..."
                    ">A minute later she finishes her dance..."
                    ">She gives a light bow to her audience."
                    ">The beggars applause and cheer loudly. Jasmine seems to be flustered."
                    m "Alright, everyone seem to be happy..."
                    m "Now, tell them who you are girl..."
                    ">Jasmine is looking at you with wide eyes..."
                    m "Go ahead..."
                    jas[66] "I..."
                    jas[66] "............."
                    jas[66] "I am princess Jasmine."
                    ">A confused murmur goes through the crowd of beggars."
                    jas[66] "Thank you for watching me dance. I hope you enjoyed my performance..."
                    ">The men surrounding you look bewildered, even scared..."
                    ">Some of them take a couple of steps back..."
                    ">Another few moments and every single one of them is rushing in different directions..."
                    ">The street gets empty in a matter of seconds."
                    jas[66] "D-did I say something wrong?"
                    sch7 "Oh, no, dear, it's not you..."
                    sch8 "Well, I suppose it is..."
                    sch7 "They are afraid, you see..."
                    sch7 "We have a saying around here \"Noblemen bring trouble\"..."
                    jas[66] "Oh..."
                    m "What about you, old crow? Aren't you afraid?"
                    sch8 "Oh, no, crocus is too old to be afraid of anything..."
                    sch7 "Plus, I knew who your slave-girl really was for quite some time now..."
                    sch8 "Princess, your dance was simply magnificent..."
                    jas[66] "Er... thank you..."
                    sch8 "Now, if you don't mind, crocus wants to be alone for a while..."
                    m "Sure, take care old crow..."
                    jas[66] "................"
                    ">You start to walk towards your house..."
                    jas[66] "Old man, I mean, master...?"
                    m "What is it?"
                    jas[66] "You think that crocus man... he will... em..."
                    m "Touch himself thinking about you?"
                    m "I think all of them will..."
                    ">Jasmine smiles timidly..."
                    ">You walk the rest of the way to your house without an incident..."
  
                    show image "04_pt/slavem/night.jpg" with fade                               
                    hide leash
                    ">It's evening and Princess Jasmine returns from performing your personal request."
                    show image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)                                     
                    ">Jasmine is very tired and feels very embarrassed thinking about today's activities..."
                    ">She had to dance in the mud for some unwashed beggars today."
                    ">After the dance was over she introduced herself to them, so now all of them know who she was."
                    ">Despite an overwhelming feeling of embarrassment Jasmine feels an odd sort satisfaction..."
                    ">Today Jasmine's reputation went down."
                    $ tired +=2     
                    $ pthink +=7
                    $ jpslave = False
                    hide image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)
                    return
            
                
            
            
            
            
            
            
            
            
            
            
   














    show image "04_pt/slavem/night.jpg" with fade                               
    hide leash
    "It's evening and Princess Jasmine returns from performing your personal request."
    show image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)                                     
    "Jasmine is very tired and feels embarrassed when she thinks about what you did to her..."
    "Dozens and dozens of people saw her today. Every single one of them knew exactly who she was."
    "Jasmine didn't say anything, but you could see that she was enjoying the attention."
    "A Few people felt sorry for Princess Jasmine but the rest of them hated her for betraying Agrabah like that."
    "You let a few men touch her a little and play with her tits."
    "Jasmine didn't protest, she was just standing there and enjoyed getting groped by strangers."
    "Today Jasmine's reputation suffered a truly devastating blow."
    "Jasmine is very tired."
    $ tired +=2    
    $ pthink +=7  
    $ jpslave = False
    hide image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)
    return
    

#label jas_on_a_leesh2:
#    "......"
#    "..."
#    ".."
#    "You lead Princess Jasmine around the city on a leash like a common slave-girl for everyone to see for the rest of the day."
#    show image "04_pt/slavem/night.jpg" with fade                               
#    hide leash
#    "It's evening and Princess Jasmine returns from performing your personal request."
#    show image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)                                     
#    "Jasmine is very tired and feels embarrassed when she thinks about what you did to her..."
#    "You took her to the market square and made her dance in the middle of it for everyone's enjoyment."
#    "A big crowd gathered up really quick. Some people were shouting out insults."
#    "After the performance was over you announced to everyone that who ever wants to get more intimate with the princess could always visit \"The Red Phoenix Brothel\", where Princess Jasmine now works as a whore."
#    "Today Jasmine's reputation suffered a truly terrible blow."
#    "Jasmine is very tired."
#    $ tired +=2    
#    $ pthink +=7   
#    $ jpslave = False
#    hide image "04_pt/jasmine/outfit/jas12.png" at right with Dissolve(.3)