label balsam_talk: 
    if obedience == 0:
        sch5 "The Market square is a very popular center of commerce here in agrabah."
        sch5 "All sorts of people come and go here every day to restock on goods and food." 
        sch5 "By the way the business is going well so I want to expand my merchandise variety."
        sch5 "I'm looking for someone to look over my fruit stand."          
        sch5 "Doesn't pay much but it's an easy job. Your wench could make a few coins."
        sch5 "Think about it. \n*spit*."
    elif obedience == 1:
        sch5 "On the sunny days like today the business is blooming!"
    elif obedience == 2:
        sch5 "Watch your purse, my friend."
        sch5 "I would hate to see your gold got stolen..."
        sch5 "I would rather see it well spent on my merchandise."
    elif obedience == 3:
        sch5 "\"The Red Phoenix\"?"
        sch5 "Yes, I've heard of it, but I'm afraid I have very little interest in such establishments..."
        sch5 "Oh, don't get me wrong, I love wenches as much as any other man..."
        sch5 "But I don't think it's very smart to spend gold on women."
        sch5 "Eventually I'm gonna get fat and successful, then all the wenches will be mine anyways."
    elif obedience == 4:
        sch5 "Don't you just love daytime?"
        sch5 "I mean how often do you really hear about any crime committed while the sun is shining on us brightly?"
    elif obedience == 5:
        sch5 "Come on, friend, don't be shy. Buy something already..."
    elif obedience == 6:
        sch5 "Gambling? You must be confusing me with my brother."
        sch5 "I have no interest in throwing my money away like that."
        sch5 "Gambling never pays-off."
        sch5 "But hard work does."
    elif obedience == 7:
        sch5 "What is it that you're looking for, my friend?"
        sch5 "Spices, wines, sweets, pastry, precious gems, slave-girls?"
        sch5 "You can find anything here!"
    elif obedience == 8:
        sch5 "They say \"The greatest crime in a desert is to find water and keep silent about it.\""
        sch5 "I couldn't agree more!"
        sch5 "Why keep silent? Let everybody know, and start selling it!"
    elif obedience == 9:
        sch5 "Special deal on apples today: buy two dozen's for double price and get one dozen for free!"
    elif obedience == 10:
        $ rosa_final_talks = renpy.random.randint(1, 5)
        if rosa_final_talks == 1:
            sch5 "Today I'm giving my goods away..."
            sch5 "In exchange for money!"
            sch5 "ha-ha-ha! This one never get's old!"
        elif rosa_final_talks == 2:
            sch5 "You think it's possible to train a monkey to do a man's job?"
            sch5 "I would rather pay my workers with fruits then with gold, you know..."
        elif rosa_final_talks == 3:
            sch5 "If you give me a gold coin, I will turn in into three gold coins..."
            sch5 "Then I will give two coins back to you and keep one for myself."
            sch5 "This is called \"investment\"."
            sch5 "What? I'm not kidding! You have a gold coin?"
        elif rosa_final_talks == 4:
            sch5 "Which is heavier a pound of apples or a pound of gold?"
            sch5 "Oh, you heard this one before? Never mind then..."
        elif rosa_final_talks == 5:
            sch5 "My work is my wife, and this fruit stand right here is my child..."
            sch5 "Don't give me that look, I'm happier then the most man out here."
          

jump market2



                    
             