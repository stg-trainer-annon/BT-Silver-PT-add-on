label questinfo:
    show qbg with d3
    if quest1complete:
        show q1 with d3
    if quest2complete:
        show q2 with d3
    if quest3complete:
        show q3 with d3
    if quest4complete:
        show q4 with d3
    if quest5complete:
        show q5 with d3
    if quest6complete:
        show q6 with d3
    if quest7complete:
        show q7 with d3
    if quest8complete:
        show q8 with d3
    if quest9complete:
        show q9 with d3
    if quest10complete:
        show q10 with d3
    if quest11complete:
        show q11 with d3
    if quest12complete:
        show q12 with d3
    if quest13complete:
        show q13 with d3
    show con1 at right
    show ctc7 at right
    pause 
    hide con1
    hide ctc7
 
        

    
    if quest1start:
        "Current quest: [quest1].\nCurrent task: acquire something eatable."
    if quest1start2:
        "Current quest: [quest1].\nCurrent task: Deliver fruits to the homeless crocus."
    if quest2start:
        "Current quest: [quest2].\nCurrent task: Deliver the box to Maslab."
    if quest2start2:
        "Current quest: [quest2].\nCurrent task: visit the tavern during nighttime."
    if quest2start3:
        "Current quest: [quest2].\nCurrent task: observe the consequences of your actions."
    if quest2start4:
        "Current quest: [quest2].\nCurrent task: meet up with Balsam during nighttime."
    if quest2start5:
        "Current quest: [quest2].\nCurrent task: observe the consequences of your actions."
    if quest3start:
        "Current quest: [quest3].\nCurrent task: Introduce Jasmine to Maslab."
    if quest3start2:
        "Current quest: [quest3].\nCurrent task: Train Jasmine to be a waitress."
    if quest3start3:
        "Current quest: [quest3].\nCurrent task: Train Jasmine to be a waitress."
    if quest3start4:
        "Current quest: [quest3].\nCurrent task: Train Jasmine to be a waitress."
    if quest4start:
        "Current quest: [quest4].\nCurrent task: Find a way to re-open the \"Red Phoenix\"."
    if quest4start2:
        "Current quest: [quest4].\nCurrent task: Acquire the permission papers."
    if quest4start3:
        "Current quest: [quest4].\nCurrent task: Bring the permission papers back to Lily."
    if quest5start:
        "Current quest: [quest5].\nCurrent task: Order the whore's dress from Azalea."
    if quest5start2:
        "Current quest: [quest5].\nCurrent task: Acquire the necessary materials."
    if quest5start3:
        "Current quest: [quest5].\nCurrent task: Acquire the necessary materials."
    if quest5start4:
        "Current quest: [quest5].\nCurrent task: Deliver the materials to Azalea."
    if quest5start5:
        "Current quest: [quest5].\nCurrent task: Pick up the finished dress from Azalea."
    if quest5start7:
        "Current quest: [quest5].\nCurrent task: Bring the dress back to Iris."
    if quest6 ==1:
        "Current quest: \"The Dream Job\".\nCurrent task: No hints this time. You will have to figure this one out on your own."
    if quest6 == 2:
        "Current quest: [quest6].\nCurrent task: Let Iris know that the problem has been solved."
    if quest7start:
        "Current quest: [quest7fix].\nCurrent task: You need to please Lola's mother. Duh!"
    if quest8start:
        "Current quest: [quest8].\nCurrent task: Acquire a whore's dress for Lola."
    if quest8start2:
        "Current quest: [quest8].\nCurrent task: Acquire a whore's dress for Lola."
    if quest8start3:
        "Current quest: [quest8].\nCurrent task: Give Lola the Whore's dress."
    if quest9start:
        "Current quest: [quest9].\nCurrent task: Talk to Crocus in a few days."
    if quest9start2:
        "Current quest: [quest9].\nCurrent task: Acquire a house remodeling permit signed by the owner."
    if quest9start3:
        "Current quest: [quest9].\nCurrent task: Bring the permit back to Crocus."
    if quest10start:
        "Current quest: [quest10].\nCurrent task: Help Balsam capture the thief."
    if quest11start:
        "Current quest: [quest11].\nCurrent task: Figure out a way to change Maslab's mind."
    if quest11start2:
        "Current quest: [quest11].\nCurrent task: Pick up the permit at the palace."
    if quest11start3:
        "Current quest: [quest11].\nCurrent task: Show Maslab the permit."
    if quest11start4:
        "Current quest: [quest11].\nCurrent task: Bring Jasmine to Maslab."
    if quest12start:
        "Current quest: [quest12].\nCurrent task: Acquire the permit."
    if quest12start2:
        "Current quest: [quest12].\nCurrent task: Pick up the permit at the palace."
    if quest12start3:
        "Current quest: [quest12].\nCurrent task: Bring the permit back to Lily."
    if storestarted2:
        "Current quest: [quest13].\nCurrent task: Give Azalea the money."
    else:
        pass
        
        

    show blkfade with d3
    hide qbg
    hide q1
    hide q2
    hide q3
    hide q4
    hide q5
    hide q6
    hide q7
    hide q8
    hide q9
    hide q10
    hide q11
    hide q12
    hide q13
    
    with d3
    pause.3
    hide blkfade with d3
    
if daytime:
    jump house
else: 
    jump dayended