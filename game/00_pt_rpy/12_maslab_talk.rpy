label maslab_talk: 
    if obedience == 0:
        sch6 "\"The blue bull\" is one of the most popular taverns in Agrabah."
        sch6 "Among thieves and cutthroats that is! \nha-ha-ha!"      
    elif obedience == 1:
        sch6 "My tavern might lack class, some even say the rooms smell like camel stables and the food is crappy..."
        sch6 "But my the wenches are pretty and easy..."           
        sch6 "I mean, they are pretty easy... Ha-ha-ha!"
    elif obedience == 2:
        sch6_6 "Yes, the brothels been outlawed..."
        sch6_6 "Sad times..."
    elif obedience == 3:
        sch6_6 "Sometimes I wish I was born a woman..."
        sch6_6 "Why? Because in this world men do all the heavy lifting..."
        sch6_6 "That's why women live longer, I tell you..."
    elif obedience == 4:
        sch6_6 "Don't you just hate daytime?"
        sch6_6 "All this sunshine makes me nervous..."
    elif obedience == 5:
        sch6 "My eye? Well..."
        sch6 "A tiger took it..."
        sch6 "Yes, I was fighting a tiger! You don't believe me?"
    elif obedience == 6:
        sch6 "You have any kids?"
        sch6 "Good for you..."
        sch6 "I have a daughter..."
        sch6 "She is beautiful but aggressive and spiteful."
        sch6 "A spitting image of her witch of a mother. *Spit!*"
    elif obedience == 7:
        sch6_6 "You ever fantasize about burning down your own tavern to the ground and returning to the life of crime...?"
        sch6 "Yeah, me neither..."
        sch6_6 "..................."
    elif obedience == 8:
        sch6 "My eye? I already told you!"
        sch6 "I lost it in a fight..."
        sch6 "Yes, it was five against one..."
        sch6 "I lost my eye, but they lost their lives!"
        sch6_5 "What? A tiger?"
        sch6_6 "Don't be ridiculous!"
    elif obedience == 9:
        sch6_6 "Fat lily... what a dreadful woman..."
        sch6_4 "But she sure knows her stuff..."
    elif obedience == 10:
        $ rosa_final_talks = renpy.random.randint(1, 5)
        if rosa_final_talks == 1:
            sch6_6 "My tavern is not a place for debauchery!"
            sch6_6 "................................"
            sch6 "Ha-ha-ha! Sorry I can't keep a straight face when I say that!"
        elif rosa_final_talks == 2:
            sch6_6 "What?"
            sch6_6 "No! We don't serve the \"Royal Goblet\" here..."   
        elif rosa_final_talks == 3:
            sch6 "What is my biggest fear?"
            sch6 "To die of an old age."
        elif rosa_final_talks == 4:
            sch6 "Good wine is like a wench..."
            sch6 "It tastes good and..."
            sch6_6 "em... you can't spank her butt... and..."
            sch6 "Ha-ha-ha, I'm not sure where I'm going with this..."
            sch6 "But my love towards both is equally fierce!"  
        elif rosa_final_talks == 5:
            sch6 "On some days I think: \"What did I ever do to deserve such a blessed life!?\""
            sch6_6 "On other days I think: \"Goddamit! Why me?!"
            sch6 "That's just how life is, my friend!"

jump tavern2
















#                        
#                        sch6 "And on occasion they are known to jump on a table and dance."
#                        sch6 "You can order your Jasmine-woman to work as a tavern girl here to serve drinks for my customers."
#                        sch6 "Or you could make her dance on a table for everyone's enjoyment."
#                        sch6 "And don't forget to dress her properly. *spit*"
#                        sch6 "Did I say \"properly\"? I meant {size=+4}inappropriately!{/size} \nHa-ha-ha!"
#                        jump tavern2