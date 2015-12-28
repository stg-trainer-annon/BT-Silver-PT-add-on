label rose_talk: 
    if obedience == 0:
        ros[1] "Today's curriculum includes: \"dancing\", \"cooking\", \"sowing\" and \"history of hateful sex\"."        
    elif obedience == 1:
        ros[1] "You would be pleased to know that our headmaster is no other than The sultan of Agarah, his royal majesty Jafar himself."
        ros[1] "Although, naturally his Majesty the sultan is a very busy man."
        ros[1] "And usually very preoccupied with ruining... *khem*"
        ros[1] "I mean, with ruling the city, so his role as the headmaster is somewhat nominal."
        ros[1] "It would be our honor to have Jasmine, the former princess of Agrabah, as one of our students."
        ros[1] "You will still have to pay the tuition, of course."
    elif obedience == 2:
        ros[1] "\"Men marry women with the hope they will never change\"."
        ros[1] "\"Women marry men with the hope they will change\"."
        ros[1] "\"Invariably they are both disappointed\"." 
        ros[1] "Albert Einstein. An ancient wizard form the old world. I doubt you heard of him." 
    elif obedience == 3:
        ros[1] "The other day I had a dream: I was a singer and I was married to a rabbit..."
        ros[1] "I'm still not sure what to make of it..."
    elif obedience == 4:
        ros[1] "The academy building used to be a brothel..."
        ros[3] "How distasteful..."
        ros[1] "I wish every woman in the world would be trained properly so that men wouldn't have to pay for sex anymore..."
    elif obedience == 5:
        ros[1] "You think our tuition fees are too high?"
        ros[3] "Nonsense. They are not nearly high enough."
    elif obedience == 6:
        ros[1] "Your slave-girl is starting to show some promise..."
        ros[1] "She still has a long way to go of though..."
    elif obedience == 7:
        ros[1] "I'm sorry, I have no time for idle chitchats today."
    elif obedience == 8:
        ros[2] "I find big fat women and little skinny men equally disgusting..."
    elif obedience == 9:
        ros[1] "Every time his majesty, the sultan jafar comes to visit us..."
        ros[1] "Every time I see him in person..."
        ros[1] "I just can't help but feel like a silly fourteen year old girl again."
        ros[4] "Oh, the things I would let that man do to me...{image=textheart.png}"
    elif obedience == 10:
        $ rosa_final_talks = renpy.random.randint(1, 5)
        if rosa_final_talks == 1:
            ros[1] "I know that white and gold colors befit a true sultan..."
            ros[1] "But don't you think that black and burgundy colored attire would suit his majesty better?"
        elif rosa_final_talks == 2:
            ros[1] "My favorite fruit is banana..."
            ros[3] "No, not because of what you think..."
            ros[4] "I like it because it's a cock-shaped fruit..."
            ros[5] "What? That's exactly what you thought?"
            ros[3] "Lucky guess..."
        elif rosa_final_talks == 3:
            ros[1] "My favorite color?"
            ros[1] "Take a wild guess..."
            ros[1] "I'll even give you a hint: it's not green."                
        elif rosa_final_talks == 4:
            ros[1] "I spank them, then I teach them how to please a man..."
            ros[1] "On some days I teach them how to please a men while I spank them..."                
        elif rosa_final_talks == 5:
            ros[1] "What? The \"Royal Goblet\"?"
            ros[1] "Why, yes... It's when a girl dips one of her tits in the man's drink before serving it to him."
            ros[1] "What of it?"
                




jump academy